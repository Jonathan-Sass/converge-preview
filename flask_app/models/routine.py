from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from pprint import pprint
from typing import List

from flask_app.models.user import User
from flask_app.models.user_response import UserResponse
from flask_app.models.routine_template import RoutineTemplate
from flask_app.models.practice import Practice


class Routine:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.routine_type = data["routine_type"]
        self.start_time = data["start_time"] or None
        self.end_time = data["end_time"] or None
        self.is_active = data["is_active"]
        self.notes = data["notes"] or None
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.practices: List[Practice] = []

    def find_routines_by_user_id(user_id):
        query = """
            SELECT 
              r.id AS routine_id,
              r.name AS routine_name,
              r.description AS routine_description,
              r.routine_type,
              r.start_time,
              r.end_time,
              r.is_active,
              r.notes AS routine_notes,
              r.created_at AS routine_created_at,
              r.updated_at AS routine_updated_at,
              rp.routine_id AS practice_routine_id,
              rp.position,
              p.id AS practice_id,
              p.name AS practice_name,
              p.description AS practice_description,
              p.is_common AS practice_is_common,
              p.notes AS practice_notes,
              p.literature_summary,
              p.created_at AS practice_created_at,
              p.updated_at AS practice_updated_at,
              pc.name AS practice_category,
              d.duration_label AS selected_duration,
              ir.impact_rating_description,
              dl.difficulty_label AS practice_difficulty
            FROM
              routines r
            LEFT JOIN 
              routine_practices rp ON r.id = rp.routine_id
            LEFT JOIN 
              practices p ON rp.practice_id = p.id
            LEFT JOIN
              practice_categories pc ON p.practice_category_id = pc.id
            LEFT JOIN
              durations d ON rp.duration_id = d.id
            LEFT JOIN
              impact_ratings ir ON p.impact_rating_id = ir.id
            LEFT JOIN
              difficulty_levels dl ON p.difficulty_level_id = dl.id
            WHERE
              r.user_id = %(user_id)s;
        """

        data = {"user_id": user_id}

        results = Routine.db.query_db(query, data)

        routines = []

        if results:

            for row in results:
                routine = next((r for r in routines if r.id == row["routine_id"]), None)
                if not routine:
                    routine_data = {
                        "id": row["routine_id"],
                        "user_id": user_id,
                        "name": row["routine_name"],
                        "description": row["routine_description"],
                        "routine_type": row["routine_type"],
                        "start_time": row["start_time"],
                        "end_time": row["end_time"],
                        "is_active": row["is_active"],
                        "notes": row["routine_notes"],
                        "created_at": row["routine_created_at"],
                        "updated_at": row["routine_updated_at"],
                        "practices": [],
                    }
                    routine = Routine(routine_data)
                    routines.append(routine)

                practice = None

                practice_id = row["practice_id"]
                if practice_id and row["practice_routine_id"] == routine.id:
                    practice = next(
                        (p for p in routine.practices if p.id == practice_id), None
                    )

                    if not practice:
                        # TODO: Create helper function? map_practice_data(row)
                        practice_data = {
                            "practice_id": row["practice_id"],
                            "routine_id": row["practice_routine_id"],
                            "practice_name": row["practice_name"],
                            "practice_description": row["practice_description"],
                            "practice_category": row["practice_category"],
                            "impact_rating_description": row[
                                "impact_rating_description"
                            ],
                            "practice_difficulty": row["practice_difficulty"],
                            "practice_is_common": row["practice_is_common"],
                            "practice_notes": row["practice_notes"],
                            "literature_summary": row["literature_summary"],
                            "selected_duration": row["selected_duration"],
                            "created_at": row["practice_created_at"],
                            "updated_at": row["practice_updated_at"],
                        }

                        practice = Practice(practice_data)
                        routine.practices.append(practice)

        print("Routines in find_routines:")
        for routine in routines:
            pprint(vars(routine))
            print("Routine's practices:")
            for practice in routine.practices:
                pprint(vars(practice))

        return routines

    @staticmethod
    def select_and_fetch_routine_template(user, survey_topic_slug_string):
        """
        Selects and retrieves a recommended routine template for a given user based on their survey responses.

        This method determines an appropriate routine template for the user by analyzing their responses 
        to survey questions within a specific topic (identified by `survey_topic_slug_string`). If the user 
        has provided responses, the function processes those responses to select the best-matching routine template.
        If no responses are available, it defaults to a "Balanced Start" routine template.

        Args:
            user (User): The user object whose responses are being analyzed.
            survey_topic_slug_string (str): The slug representing the survey topic used to filter user responses.

        Returns:
            RoutineTemplate: The selected routine template, including associated practices.

        Raises:
            AttributeError: If `UserResponse.find_user_responses_by_user_id_and_survey_topic_slug` 
                            or `UserResponse.process_responses_for_routine_template_selection` is not defined.
            ValueError: If no matching routine template is found.

        Example Usage:
            user = User.get_by_id(1)
            routine_template = Routine.select_and_fetch_routine(user, "morning-routine")
            print(routine_template.name)  # Outputs the name of the recommended routine template
        """

        if survey_topic_slug_string:
            # Find the user's responses for the given topic slug
            user_responses = UserResponse.find_user_responses_by_user_id_and_survey_topic_slug(user, survey_topic_slug_string)

            # Process responses to select routine template for the user
            recommended_routine_template_name = UserResponse.process_responses_for_routine_template_selection(user_responses)
        else:
            # Default routine template if no responses determine one
            recommended_routine_template_name = "Balanced Start"

        # Fetch the routine template with associated practices
        recommended_routine_template = RoutineTemplate.fetch_routine_template_with_practices(recommended_routine_template_name)

        return recommended_routine_template


    def create_routine(routine_data):
        print("***routine_data in create_routine***")
        pprint(routine_data)

        query = """
            INSERT INTO
                routines (user_id, name, description, routine_type, start_time, end_time, is_active, notes, created_at, updated_at)
            VALUES
                (%(user_id)s, %(name)s, %(description)s, %(routine_type)s, %(start_time)s, %(end_time)s, %(is_active)s, %(notes)s, NOW(), NOW())
            ON DUPLICATE KEY UPDATE
                description = VALUES(description),
                start_time = VALUES(start_time),
                end_time = VALUES(end_time),
                is_active = VALUES(is_active),
                notes = VALUES(notes), 
                updated_at = NOW();
        """

        data = {
            "user_id": session["user_id"],
            "name": routine_data["name"],
            "description": routine_data["description"],
            "routine_type": routine_data["routineType"],
            "start_time": routine_data["startTime"],
            "end_time": routine_data.get("endTime", None),
            "is_active": True,
            "notes": routine_data.get("notes", None),
        }

        result = Routine.db.query_db(query, data)

        if result:
            print("****result in create_routine****")
            pprint(result)

            routine_id = result
            Routine.create_routine_practices(routine_data, routine_id)
        else:
            raise RuntimeError("Error creating personal routine in database.")

        return

    def create_routine_practices(routine_data, routine_id):
        query = """
            INSERT INTO
                routine_practices (routine_id, practice_id, duration_id, position, created_at, updated_at)
            VALUES
                (%(routine_id)s, %(practice_id)s, %(duration_id)s, %(position)s, NOW(), NOW())
            ON DUPLICATE KEY UPDATE
                duration_id = VALUES(duration_id),
                position = VALUES(position),
                updated_at = NOW();
        """

        success_count = 0

        for practice in routine_data["practices"]:
            routine_practice_data = {
                "routine_id": routine_id,
                "practice_id": practice["practiceId"],
                "duration_id": practice["durationId"],
                "position": practice.get("position", None),
            }

            result = Routine.db.query_db(query, routine_practice_data)
            if result:
                print(
                    f"Insert successful for routine: {routine_data["name"]}, practice id: {practice["practiceId"]}"
                )
                success_count += 1
            else:
                raise RuntimeError(
                    f"Error inserting data for routine: {routine_data["name"]}, practice id: {practice["practice_id"]}"
                )

        print(
            f"Successfully inserted {success_count} practices for routine: {routine_data['name']}"
        )

    # def update_routine():

    # def delete_routine():

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
              ur.id AS routine_id,
              ur.name AS routine_name,
              ur.description AS routine_description,
              ur.routine_type,
              ur.start_time,
              ur.end_time,
              ur.is_active,
              ur.notes AS routine_notes,
              ur.created_at AS routine_created_at,
              ur.updated_at AS routine_updated_at,
              urp.routine_id AS practice_routine_id,
              urp.position,
              p.id AS practice_id,
              p.name AS practice_name,
              p.description AS practice_description,
              p.benefit_synopsis,
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
              user_routines ur
            LEFT JOIN 
              user_routine_practices urp ON ur.id = urp.routine_id
            LEFT JOIN 
              practices p ON urp.practice_id = p.id
            LEFT JOIN
              practice_categories pc ON p.practice_category_id = pc.id
            LEFT JOIN
              durations d ON urp.duration_id = d.id
            LEFT JOIN
              impact_ratings ir ON p.impact_rating_id = ir.id
            LEFT JOIN
              difficulty_levels dl ON p.difficulty_level_id = dl.id
            WHERE
              ur.user_id = %(user_id)s;
        """

        data = {"user_id": user_id}

        results = Routine.db.query_db(query, data)

        routines = []

        if results:

            for row in results:
                routine = next((r for r in routines if r.id == row["routine_id"]), None)
                if not routine:
                    routine = Routine.build_routine_from_row(row, user_id)
                    routines.append(routine)

                practice = None

                practice_id = row["practice_id"]
                if practice_id and row["practice_routine_id"] == routine.id:
                    practice = next((p for p in routine.practices if p.id == practice_id), None)

                    if not practice:
                        practice = Practice.build_practice_from_row(row)
                        routine.practices.append(practice)

        print("Routines in find_routines:")
        for routine in routines:
            pprint(vars(routine))
            print("Routine's practices:")
            for practice in routine.practices:
                pprint(vars(practice))

        return routines
    
    def find_routine_by_user_id_and_routine_type(user_id, routine_type):
        query = """
            SELECT 
              ur.id AS routine_id,
              ur.name AS routine_name,
              ur.description AS routine_description,
              ur.routine_type,
              ur.start_time,
              ur.end_time,
              ur.is_active,
              ur.notes AS routine_notes,
              ur.created_at AS routine_created_at,
              ur.updated_at AS routine_updated_at,
              urp.routine_id AS practice_routine_id,
              urp.position,
              p.id AS practice_id,
              p.name AS practice_name,
              p.description AS practice_description,
              p.benefit_synopsis,
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
              user_routines ur
            LEFT JOIN 
              user_routine_practices urp ON ur.id = urp.routine_id
            LEFT JOIN 
              practices p ON urp.practice_id = p.id
            LEFT JOIN
              practice_categories pc ON p.practice_category_id = pc.id
            LEFT JOIN
              durations d ON urp.duration_id = d.id
            LEFT JOIN
              impact_ratings ir ON p.impact_rating_id = ir.id
            LEFT JOIN
              difficulty_levels dl ON p.difficulty_level_id = dl.id
            WHERE
              ur.user_id = %(user_id)s
            AND
              ur.routine_type = %(routine_type)s;
        """

        data = {
            "user_id": user_id,
            "routine_type": routine_type
            }

        results = Routine.db.query_db(query, data)


        if results:

            for row in results:
                routine = Routine.build_routine_from_row(row, user_id)

                practice = None

                practice_id = row["practice_id"]
                if practice_id and row["practice_routine_id"] == routine.id:
                    practice = next((p for p in routine.practices if p.id == practice_id), None)

                    if not practice:
                        practice = Practice.build_practice_from_row(row)
                        routine.practices.append(practice)

        # print("Routine in find_routines:")
        # pprint(vars(routine))
        # print("Routine's practices:")
        # for practice in routine.practices:
        #     pprint(vars(practice))

        return routine

    @staticmethod
    def build_routine_from_row(row, user_id):
        return Routine(
            {
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
        )

    @staticmethod
    def select_and_fetch_routine_template(user, subcategory_slug):
        """
        Selects and retrieves a recommended routine template for a given user based on their survey responses.

        This method determines an appropriate routine template for the user by analyzing their responses 
        to survey questions within a specific topic (identified by `subcategory_slug_string`). If the user 
        has provided responses, the function processes those responses to select the best-matching routine template.
        If no responses are available, it defaults to a "Balanced Start" routine template.

        Args:
            user (User): The user object whose responses are being analyzed.
            subcategory_slug_string (str): The slug representing the survey topic used to filter user responses.

        Returns:
            RoutineTemplate: The selected routine template, including associated practices.

        Raises:
            AttributeError: If `UserResponse.find_user_responses_by_user_id_and_subcategory_slug` 
                            or `UserResponse.process_responses_for_routine_template_selection` is not defined.
            ValueError: If no matching routine template is found.

        Example Usage:
            user = User.get_by_id(1)
            routine_template = Routine.select_and_fetch_routine(user, "morning-routine")
            print(routine_template.name)  # Outputs the name of the recommended routine template
        """

        if subcategory_slug:
            # Find the user's responses for the given topic slug
            user_responses = UserResponse.find_user_responses_by_user_id_and_subcategory_slug(user, subcategory_slug)

            if user_responses:
            # Process responses to select routine template for the user
              recommended_routine_template_name = UserResponse.map_user_response_to_routine_template(user_responses, subcategory_slug)

        else:
            # Default routine template if no responses determine one
            recommended_routine_template_name = "Balanced Start"

        # Fetch the routine template with associated practices
        recommended_routine_template = RoutineTemplate.find_routine_template_by_name_with_practices(recommended_routine_template_name)
        print("*****recommended_routine_template in select_and_fetch_routine_template******")
        pprint(recommended_routine_template)
        return recommended_routine_template
    

    def create_routine(routine_data):
        print("***routine_data in create_routine***")
        pprint(routine_data)

        query = """
            INSERT INTO
                user_routines (user_id, name, description, routine_type, start_time, end_time, is_active, notes, created_at, updated_at)
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
                user_routine_practices (routine_id, practice_id, duration_id, position, created_at, updated_at)
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
                    f"Error inserting data for routine: {routine_data["name"]}, practice id: {practice["practiceId"]}"
                )

        print(
            f"Successfully inserted {success_count} practices for routine: {routine_data['name']}"
        )

    # def update_routine():

    # def delete_routine():

    def get_intro_am_routine():
        
        recommended_routine_template_name = "The Grounded Start"

        RoutineTemplate.find_routine_template_by_name_with_practices(recommended_routine_template_name)


    def update_routine_practices():
        # Retrieve routine_practices for user

        # for routine_practice in routine_practices
            # if new routine_practice not in new practices
              # delete routine_practice
        
        # for practice in new_practices
          # if practice not in routine_practices
              #   insert into routine_practices
          # if practice in routine_practices
            # update practice


        return
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, jsonify, redirect
from flask_app.models.practice import Practice
from flask_app.models.duration import Duration
from flask_app.models.user_response import UserResponse
from flask_app.models.user import User


class RoutineTemplate:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["routine_template_id"]
        self.frequency = data["routine_template_frequency"]
        self.name = data["routine_template_name"]
        self.description = data["routine_template_description"]
        self.category = data["routine_template_category"]
        self.notes = data.get("routine_template_notes", None)
        self.practices = []

    def am_routine_template_selector(user, survey_topic_slug_string):

        user_with_responses = User.fetch_user_responses_by_survey_topic_slug(
            user, survey_topic_slug_string
        )
        UserResponse.process_user_responses(user_with_responses)
        return

    def find_routine_template_by_name_with_practices(routine_template_name):
        query = """
            SELECT
                routine_templates.id AS routine_template_id,
                routine_templates.name AS routine_template_name,
                routine_templates.description AS routine_template_description,
                routine_templates.routine_type,
                routine_templates.category AS routine_template_category,
                routine_templates.notes AS routine_template_notes,
                frequencies.frequency_label AS routine_template_frequency,
                practices.id AS practice_id,
                practices.name AS practice_name,
                practices.description AS practice_description,
                practices.is_common AS practice_is_common,
                practices.notes AS practice_notes,
                practices.literature_summary,
                practices.created_at,
                practices.updated_at,
                practice_categories.name AS practice_category,
                impact_ratings.impact_rating_description,
                difficulty_levels.difficulty_label AS practice_difficulty,
                durations.id AS duration_id,
                durations.duration_label,
                durations.duration_seconds,
                engagement_levels.level AS engagement_level
            FROM
                routine_templates
            JOIN
                frequencies ON routine_templates.frequency_id = frequencies.id
            JOIN
                routine_template_practices ON routine_templates.id = routine_template_practices.routine_template_id
            JOIN
                practices ON routine_template_practices.practice_id = practices.id
            JOIN
                practice_categories ON practices.practice_category_id = practice_categories.id
            JOIN
                impact_ratings ON practices.impact_rating_id = impact_ratings.id
            JOIN
                difficulty_levels ON practices.difficulty_level_id = difficulty_levels.id
            LEFT JOIN
              recommended_durations ON practices.id = recommended_durations.practice_id
            LEFT JOIN
              durations ON recommended_durations.duration_id = durations.id
            LEFT JOIN
              engagement_levels ON recommended_durations.engagement_level_id = engagement_levels.id
            WHERE
                routine_templates.name = %(routine_template_name)s
            ORDER BY
                routine_template_practices.position;
        """

        data = {"routine_template_name": routine_template_name}

        try:
            results = RoutineTemplate.db.query_db(query, data)

            if not results:
                return None

            routine_template = RoutineTemplate(results[0])
            
            practice_map = {}

            for result in results:
                practice_id = result["practice_id"]

                if practice_id not in practice_map:
                    practice = Practice(result)
                    practice_map[practice_id] = practice
                    routine_template.practices.append(practice)
                
                if result["duration_id"]:
                    duration = Duration(result)
                    practice_map[practice_id].durations.append(duration)

            return routine_template
        
        except Exception as e:
            raise RuntimeError(f"Error retrieving routine template: {e}")

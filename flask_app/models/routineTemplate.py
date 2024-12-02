from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, jsonify, redirect
from flask_app.models.practice import Practice
from flask_app.models.userResponse import UserResponse
from flask_app.models.user import User

class RoutineTemplate:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.frequency = data["routine_template_frequency"]
        self.name = data["routine_template_name"]
        self.description = data["routine_template_description"]
        self.category = data["routine_template_category"]
        self.notes = data["routine_template_notes"] or None
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def am_routine_template_selector(user, survey_topic_slug_string):
        
        user_with_responses = User.fetch_user_responses_by_survey_topic_slug(user, survey_topic_slug_string)
        UserResponse.process_user_responses(user_with_responses)
   

    def fetch_routine_templates(routine_template_name):
        query = """
            SELECT
                routine_templates.name AS routine_template_name,
                routine_templates.description AS routine_template_description,
                routine_templates.routine_type,
                routine_templates.category AS routine_template_category,
                routine_templates.notes AS routine_template_notes,
                frequencies.frequency_label AS routine_template_frequency,
                practices.name AS practice_name,
                practices.description AS practice_description,
                practices.is_common AS practice_is_common,
                practices.notes AS practice_notes,
                practices.literature_summary,
                practice_categories.name AS practice_category,
                impact_ratings.impact_rating_value,
                difficulty_levels.difficulty_label AS practice_difficulty
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
            WHERE
                routine_templates.name = %(routine_template_name)s
            ORDER BY
                routine_template_practices.position;
        """

        result = RoutineTemplate.db.query_db(query, routine_template_name)

        if result:
            routine_template = result
        
        return routine_template
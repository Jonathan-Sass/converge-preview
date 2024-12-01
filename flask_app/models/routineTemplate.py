from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, jsonify, redirect
from flask_app.models.practice import Practice

class RoutineTemplate:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.frequency_id = data["frequency_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.category = data["category"]
        self.notes = data["notes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def fetch_routine_templates():
        query = """
            SELECT
                routine_templates.frequency_id AS routine_template_frequency_id,
                routine_template.name AS routine_template_name,
                routine_template.description AS routine_template_description,
                routine_template.routine_type,
                routine_template.category AS routine_template_category,
                routine_template.notes AS routine_template_notes,
                frequency.frequency_label AS routine_template_frequency,
                practices.name AS practice_name,
                practices.description AS practice_description,
                practices.is_common AS practice_is_common,
                practices.notes AS practice_notes,
                practices.literature_summary,
                practice_categories.name AS practice_category,
                impact_ratings.impact_rating_value,
                difficulty_levels.difficulty_label AS practice_difficulty,

            FROM
                routine_templates 
            JOIN
                frequencies ON routine_templates.frequency_id = frequencies.id
            JOIN
                routine_template_practices ON routine_templates.id = routine_template_practices.routine_template.id
            JOIN
                practices ON routine_template_practices.practice_id = practices.id
            JOIN
                practice_categories ON practices.practice_category_id = practice_categories.id
            JOIN
                impact_ratings ON practices.impact_rating_id = impact_ratings.id
            JOIN
                difficulty_levels ON practices.difficulty_level_id = difficulty_levels.id
            WHERE
                routine_template.id = routine_template_id
            ORDERBY
                routine_template_practices.position
        """
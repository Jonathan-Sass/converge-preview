from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, jsonify, redirect
from pprint import pprint

from flask_app.models.practice import Practice
from flask_app.models.duration import Duration
from flask_app.models.user_response import UserResponse
from flask_app.models.user import User


class RoutineTemplate:
    """Model representing a reusable routine template with a collection of practices."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a RoutineTemplate object.

        Args:
            data (dict): Dictionary containing routine template fields.
        """
        self.id = data["routine_template_id"]
        self.frequency = data["routine_template_frequency"]
        self.name = data["routine_template_name"]
        self.description = data["routine_template_description"]
        self.category = data["routine_template_category"]
        self.notes = data.get("routine_template_notes", None)
        self.practices = []

    @staticmethod
    def am_routine_template_selector(user, subcategory_slug_string):
        """
        Retrieves user responses for a given subcategory and processes them.

        Args:
            user (User): The current logged-in user.
            subcategory_slug_string (str): Slug for the subcategory related to the routine.
        """
        user_with_responses = UserResponse.fetch_user_responses_by_user_id_and_subcategory_slug(
            user, subcategory_slug_string
        )
        UserResponse.process_user_responses(user_with_responses)
        return

    @staticmethod
    def find_routine_template_by_name_with_practices(routine_template_name):
        """
        Fetches a routine template by name along with its associated practices and durations.

        Args:
            routine_template_name (str): The name of the routine template to fetch.

        Returns:
            RoutineTemplate: A populated RoutineTemplate object or None if not found.
        """
        query = """
            SELECT
                routine_templates.id AS routine_template_id,
                routine_templates.name AS routine_template_name,
                routine_templates.description AS routine_template_description,
                routine_templates.routine_type,
                routine_templates.category AS routine_template_category,
                routine_templates.notes AS routine_template_notes,
                practices.id AS practice_id,
                practices.name AS practice_name,
                practices.description AS practice_description,
                practices.benefit_synopsis,
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

        print(f"****Searching for: {routine_template_name}")

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

            print("*****routine_template in find_by_name_with_practices")
            pprint(vars(routine_template))
            return routine_template

        except Exception as e:
            raise RuntimeError(f"Error retrieving routine template: {e}")

    
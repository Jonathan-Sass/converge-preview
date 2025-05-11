from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, jsonify, redirect
from pprint import pprint
import logging

from flask_app.models.practice import Practice
from flask_app.models.routine_block import RoutineBlock
from flask_app.models.duration import Duration
# from flask_app.models.user_response import UserResponse
from flask_app.models.user import User


class RoutineBlockTemplate:
    """Model representing a reusable routine block template and its associated practices."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a RoutineBlockTemplate object.

        Args:
            data (dict): Dictionary containing routine template fields.
        """
        self.id = data["routine_block_template_id"]
        self.routine_block_id = data["routine_block_template_routine_block_id"]
        self.name = data["routine_block_template_name"]
        self.slug = data["routine_block_template_slug"]
        self.description = data["routine_block_template_description"]
        self.notes = data.get("routine_block_template_notes", None)
        self.practices = []

    # @staticmethod
    # def am_routine_block_template_selector(user, subcategory_slug_string):
    #     """
    #     Retrieves user responses for a given subcategory and processes them.

    #     Args:
    #         user (User): The current logged-in user.
    #         subcategory_slug_string (str): Slug for the subcategory related to the routine.
    #     """
    #     user_with_responses = UserResponse.fetch_user_responses_by_user_id_and_subcategory_slug(
    #         user, subcategory_slug_string
    #     )
    #     UserResponse.process_user_responses(user_with_responses)
    #     return

    @staticmethod
    def find_routine_block_template_by_name_with_practices(routine_block_template_name):
        """
        Fetches a routine template by name along with its associated practices and durations.

        Args:
            routine_block_template_name (str): The name of the routine template to fetch.

        Returns:
            RoutineBlockTemplate: A populated RoutineBlockTemplate object or None if not found.
        """
        query = """
            SELECT
                rbt.id AS routine_block_template_id,
                rbt.routine_block_id AS routine_block_template_routine_block_id,
                rbt.name AS routine_block_template_name,
                rbt.slug AS routine_block_template_slug,
                rbt.description AS routine_block_template_description,
                rbt.notes AS routine_block_template_notes,
                p.id AS practice_id,
                p.name AS practice_name,
                p.description AS practice_description,
                p.benefit_synopsis,
                p.is_common AS practice_is_common,
                p.notes AS practice_notes,
                p.literature_summary,
                p.created_at,
                p.updated_at,
                practice_categories.name AS practice_category,
                impact_ratings.impact_rating_description,
                difficulty_levels.difficulty_label AS practice_difficulty,
                durations.id AS duration_id,
                durations.duration_label,
                durations.duration_seconds,
                engagement_levels.level AS engagement_level
            FROM
                routine_block_templates rbt
            JOIN
                routine_block_template_practice rbtp ON rbt.id = rbtp.routine_block_template_id
            JOIN
                practice p ON rbtp.practice_id = p.id
            JOIN
                practice_categories ON p.practice_category_id = practice_categories.id
            JOIN
                impact_ratings ON p.impact_rating_id = impact_ratings.id
            JOIN
                difficulty_levels ON p.difficulty_level_id = difficulty_levels.id
            LEFT JOIN
                recommended_durations ON p.id = recommended_durations.practice_id
            LEFT JOIN
                durations ON recommended_durations.duration_id = durations.id
            LEFT JOIN
                engagement_levels ON recommended_durations.engagement_level_id = engagement_levels.id
            WHERE
                rbt.name = %(routine_block_template_name)s
            ORDER BY
                rbtp.position;
        """

        print(f"****Searching for: {routine_block_template_name}")

        data = {"routine_block_template_name": routine_block_template_name}

        try:
            results = RoutineBlockTemplate.db.query_db(query, data)

            if not results:
                return None

            return RoutineBlockTemplate.build_routine_block_template_with_practices(results)
            # routine_block_template = RoutineBlockTemplate(results[0])
            # practice_map = {}

            # for result in results:
            #     practice_id = result["practice_id"]

            #     if practice_id not in practice_map:
            #         practice = Practice(result)
            #         practice_map[practice_id] = practice
            #         routine_block_template.practices.append(practice)

            #     if result["duration_id"]:
            #         duration = Duration(result)
            #         practice_map[practice_id].durations.append(duration)

            # print("*****routine_block_template in find_by_name_with_practices")
            # pprint(vars(routine_block_template))
            # return routine_block_template

        except Exception as e:
            raise RuntimeError(f"Error retrieving routine template: {e}")
        
    @classmethod
    def find_routine_block_template_by_slug(cls, block_template_slug):
        """
        Fetches a routine block template by slug along with its associated practices and durations.

        Args:
            routine_block_template_slug (str): The slug of the routine template to fetch.

        Returns:
            RoutineBlockTemplate: A populated RoutineBlockTemplate object or None if not found.
        """
        query = """
            SELECT
                routine_block_templates.id AS routine_block_template_id,
                routine_block_templates.routine_block_id AS routine_block_template_routine_block_id,
                routine_block_templates.slug AS routine_block_template_slug,
                routine_block_templates.name AS routine_block_template_name,
                routine_block_templates.description AS routine_block_template_description,
                routine_block_templates.notes AS routine_block_template_notes,
                practices.id AS practice_id,
                practices.slug AS practice_slug,
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
                routine_block_templates
            JOIN
                routine_block_template_practices ON routine_block_templates.id = routine_block_template_practices.routine_block_template_id
            JOIN
                practices ON routine_block_template_practices.practice_id = practices.id
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
                routine_block_templates.slug = %(slug)s
            ORDER BY
                routine_block_template_practices.position;
        """

        print(f"****Searching for: {block_template_slug}")

        data = {"slug": block_template_slug}

        try:
            results = RoutineBlockTemplate.db.query_db(query, data)

            if not results:
                return None
            
            template = RoutineBlockTemplate.build_routine_block_template_with_practices(results)
            print("*****ROUTINE BLOCK TEMPLATE WITH PRACTICES IN find_rbt_by_slug")
            pprint(template)

            return template
        
        except Exception as e:
          logging.error(f"[find_routine_block_template_by_slug] Failed for slug={block_template_slug}: {e}")
          return []
    
    def build_routine_block_template_with_practices(template_data):
        routine_block_template = RoutineBlockTemplate(template_data[0])
        practice_map = {}

        for practice in template_data:
            practice_id = practice["practice_id"]

            if practice_id not in practice_map:
                practice = Practice(practice)
                practice_map[practice_id] = practice
                routine_block_template.practices.append(practice)

            # if practice.selected_duration:
            #     duration = Duration(practice)
            #     practice_map[practice_id].durations.append(duration)

        print("*****routine_block_template in find_by_name_with_practices")
        pprint(vars(routine_block_template))
        return routine_block_template

    

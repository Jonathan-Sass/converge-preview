from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.duration import Duration


class Practice:
    db = connectToMySQL("converge_schema")

    # TODO: Need to update routine/routine_template retrieving logic to account for changes to Practice class
    def __init__(self, data):
        self.id = data["practice_id"]
        self.routine_id = data.get("routine_id", None)
        self.name = data["practice_name"]
        self.description = data["practice_description"]
        self.practice_category = data["practice_category"]
        self.impact_rating_description = data["impact_rating_description"]
        # TODO: Condense difficulties and impact_ratings column names for consistency
        self.difficulty = data["practice_difficulty"]
        self.is_common = data["practice_is_common"]
        self.notes = data["practice_notes"]
        self.literature_summary = data["literature_summary"]
        self.selected_duration = data.get("selected_duration", None)
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.durations = []
        # DO WE NEED A self.frequency?

    def to_dict(self):
        """Converts a Practice object to a dictionary"""
        return {
        "id": self.id,
        "routine_id": self.routine_id,
        "name": self.name,
        "description": self.description,
        "practice_category": self.practice_category,
        "impact_rating_description": self.impact_rating_description,
        "difficulty": self.difficulty,
        "is_common": self.is_common,
        "literature_summary": self.literature_summary,
        "selected_duration": self.selected_duration,
        "created_at": self.created_at.isoformat() if self.created_at else None,
        "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        "durations": self.durations,
        }

    @staticmethod
    def dict_from_query_result(result):
        """Converts raw query result to a dictionary with instantiating an object"""
        return {
            "id": result["practice_id"],
            "routine_id": result.get("routine_id", None),
            "name": result["practice_name"],
            "description": result["practice_description"],
            "practice_category": result["practice_category"],
            "impact_rating_description": result["impact_rating_description"],
            # TODO: Condense difficulties and impact_ratings column names for consistency
            "difficulty": result["practice_difficulty"],
            "is_common": result["practice_is_common"],
            "notes": result["practice_notes"],
            "literature_summary": result["literature_summary"],
            "selected_duration": result.get("selected_duration", None),
            "created_at": result["created_at"].isoformat() if result["created_at"] else None,
            "updated_at": result["updated_at"].isoformat() if result["updated_at"] else None,
            "durations": []
        }


    def create_practice_with_durations(routine_template_and_practice_data):
        practice = Practice(routine_template_and_practice_data)

        durations = Duration.find_durations_by_practice_id(practice)
        for duration in durations:
            practice.durations.append(duration)

        return practice

    def get_all_practices():
        query = """
          SELECT
            p.id AS practice_id,
            p.name AS practice_name,
            p.description AS practice_description,
            p.is_common AS practice_is_common,
            p.notes AS practice_notes,
            p.literature_summary,
            p.created_at,
            p.updated_at,
            pc.name AS practice_category,
            ir.impact_rating_description,
            dl.difficulty_label AS practice_difficulty
          FROM
            practices p
          LEFT JOIN
            practice_categories pc ON pc.id = p.practice_category_id
          LEFT JOIN
            impact_ratings ir ON ir.id = p.impact_rating_id
          LEFT JOIN
            difficulty_levels dl ON dl.id = p.difficulty_level_id
          ORDER BY
            p.id;
        """

        try:
            results = Practice.db.query_db(query)

            if not results:
                return []
            
            practices = []
            seen_ids = set()

            for result in results:
              practice_id = result["practice_id"]
              if practice_id not in seen_ids:
                  seen_ids.add(practice_id)
                  practices.append(Practice.dict_from_query_result(result))
            return practices
        except Exception as e:
            raise RuntimeError(f"Error retrieving all practices: {e}")
        
  
    def get_all_practices_grouped_by_category():
        all_practices = Practice.get_all_practices()

        grouped_practices = {}

        for practice in all_practices:
            practice_category = practice["practice_category"]

            if practice_category not in grouped_practices:
                grouped_practices[practice_category] = []
            
            practice.pop("practice_category")
            grouped_practices[practice_category].append(practice)

        return grouped_practices
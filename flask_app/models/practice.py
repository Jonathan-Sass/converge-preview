from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from pprint import pprint

from flask_app.models.duration import Duration


class Practice:
    """Model representing a self-care or personal development practice."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a Practice object.

        Args:
            data (dict): Dictionary containing practice attributes.
        """
        self.id = data["practice_id"]
        self.routine_id = data.get("routine_id", None)
        self.name = data["practice_name"]
        self.description = data["practice_description"]
        self.benefit_synopsis = data["benefit_synopsis"]
        self.practice_category = data["practice_category"]
        self.impact_rating_description = data["impact_rating_description"]
        self.difficulty = data["practice_difficulty"]
        self.is_common = data["practice_is_common"]
        self.notes = data["practice_notes"]
        self.literature_summary = data["literature_summary"]
        self.selected_duration = data.get("selected_duration", None)
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.durations = []

    def to_dict(self):
        """
        Converts the Practice object to a dictionary.

        Returns:
            dict: Serialized version of the Practice instance.
        """
        return {
            "id": self.id,
            "routine_id": self.routine_id,
            "name": self.name,
            "description": self.description,
            "benefit_synopsis": self.benefit_synopsis,
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
        """
        Converts a raw query result into a dictionary without instantiating the class.

        Args:
            result (dict): Raw result from the database.

        Returns:
            dict: Dictionary representation of the practice.
        """
        return {
            "id": result["practice_id"],
            "routine_id": result.get("routine_id", None),
            "name": result["practice_name"],
            "description": result["practice_description"],
            "benefit_synopsis": result["benefit_synopsis"],
            "practice_category": result["practice_category"],
            "impact_rating_description": result["impact_rating_description"],
            "difficulty": result["practice_difficulty"],
            "is_common": result["practice_is_common"],
            "notes": result["practice_notes"],
            "literature_summary": result["literature_summary"],
            "selected_duration": result.get("selected_duration", None),
            "created_at": result["created_at"].isoformat() if result["created_at"] else None,
            "updated_at": result["updated_at"].isoformat() if result["updated_at"] else None,
            "durations": []
        }

    @staticmethod
    def get_all_practices():
        """
        Retrieves all practices from the database, including joined category, rating, and durations.

        Returns:
            dict: A dictionary of practices indexed by ID.
        """
        query = """
          SELECT
            p.id AS practice_id,
            p.name AS practice_name,
            p.description AS practice_description,
            p.benefit_synopsis,
            p.is_common AS practice_is_common,
            p.notes AS practice_notes,
            p.literature_summary,
            p.created_at,
            p.updated_at,
            pc.name AS practice_category,
            ir.impact_rating_description,
            dl.difficulty_label AS practice_difficulty,
            d.id AS duration_id,
            d.duration_label,
            d.duration_seconds,
            el.level AS engagement_level
          FROM
            practices p
          LEFT JOIN
            practice_categories pc ON pc.id = p.practice_category_id
          LEFT JOIN
            impact_ratings ir ON ir.id = p.impact_rating_id
          LEFT JOIN
            difficulty_levels dl ON dl.id = p.difficulty_level_id
          LEFT JOIN
            recommended_durations rd ON p.id = rd.practice_id
          LEFT JOIN
            durations d ON rd.duration_id = d.id
          LEFT JOIN
            engagement_levels el ON rd.engagement_level_id = el.id
          ORDER BY
            p.id;
        """

        try:
            results = Practice.db.query_db(query)

            if not results:
                return {}

            practice_map = {}

            for result in results:
                practice_id = result["practice_id"]

                if practice_id not in practice_map:
                    practice_map[practice_id] = Practice.dict_from_query_result(result)

                if result["duration_id"]:
                    duration = Duration.dict_from_query_result(result)
                    practice_map[practice_id]["durations"].append(duration)

            return practice_map
        except Exception as e:
            raise RuntimeError(f"Error retrieving all practices: {e}")

    @staticmethod
    def get_all_practices_grouped_by_category():
        """
        Returns all practices grouped by their category name.

        Returns:
            dict: A dictionary where keys are category names and values are lists of practices.
        """
        all_practices = Practice.get_all_practices()
        grouped_practices = {}

        for practice in all_practices.values():
            category = practice["practice_category"]

            if category not in grouped_practices:
                grouped_practices[category] = []

            practice.pop("practice_category")
            grouped_practices[category].append(practice)

        return grouped_practices

    @staticmethod
    def build_practice_from_row(row):
        """
        Builds a Practice object from a raw row returned by a joined query.

        Args:
            row (dict): A row from a SQL query with aliased fields.

        Returns:
            Practice: An instantiated Practice object.
        """
        return Practice(
            {
                "practice_id": row["practice_id"],
                "routine_id": row["practice_routine_id"],
                "practice_name": row["practice_name"],
                "practice_description": row["practice_description"],
                "benefit_synopsis": row["benefit_synopsis"],
                "practice_category": row["practice_category"],
                "impact_rating_description": row["impact_rating_description"],
                "practice_difficulty": row["practice_difficulty"],
                "practice_is_common": row["practice_is_common"],
                "practice_notes": row["practice_notes"],
                "literature_summary": row["literature_summary"],
                "selected_duration": row["selected_duration"],
                "created_at": row["practice_created_at"],
                "updated_at": row["practice_updated_at"],
            }
        )

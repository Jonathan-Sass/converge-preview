from flask_app.config.mysqlconnection import connectToMySQL


class Duration:
    """
    Model representing a time duration for practice engagement.
    Includes associated methods for fetching durations and engagement levels.
    """
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a Duration object.

        Args:
            data (dict): Dictionary containing duration data.
        """
        self.id = data["duration_id"]
        self.duration_label = data["duration_label"]
        self.duration_seconds = data["duration_seconds"]
        self.engagement_level = data["engagement_level"] or None

    @staticmethod
    def find_durations_by_practice_id(practice_id):
        """
        Retrieve recommended durations for a given practice, including engagement levels.

        Args:
            practice_id (int): ID of the practice.

        Returns:
            list[Duration]: A list of Duration objects for the specified practice.
        """
        query = """
            SELECT
                durations.id AS duration_id,
                durations.duration_label,
                durations.duration_seconds,
                engagement_levels.level AS engagement_level
            FROM 
                recommended_durations
            JOIN
                durations ON recommended_durations.duration_id = durations.id
            LEFT JOIN
                engagement_levels ON recommended_durations.engagement_level_id = engagement_levels.id
            WHERE
                recommended_durations.practice_id = %(practice_id)s;
        """
        data = {"practice_id": practice_id}
        results = Duration.db.query_db(query, data)

        return [Duration(result) for result in results]

    @staticmethod
    def dict_from_query_result(result):
        """
        Converts a raw query result into a dictionary.

        Args:
            result (dict): A single row from a database query.

        Returns:
            dict: Dictionary with keys: id, duration_label, duration_seconds, engagement_level.
        """
        return {
            "id": result["duration_id"],
            "duration_label": result["duration_label"],
            "duration_seconds": result["duration_seconds"],
            "engagement_level": result["engagement_level"]
        }

    @staticmethod
    def fetch_all_durations():
        """
        Retrieve all durations from the database.

        Returns:
            list[dict]: List of duration records.

        Raises:
            RuntimeError: If no durations are found.
        """
        query = "SELECT * FROM durations;"
        results = Duration.db.query_db(query)

        if results:
            return results
        else:
            raise RuntimeError("No durations found in database.")

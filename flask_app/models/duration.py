from flask_app.config.mysqlconnection import connectToMySQL


class Duration:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.duration_label = data["duration_label"]
        self.duration_seconds = data["duration_seconds"]
        self.engagement_level = data["engagement_level"] or None
        

    def fetch_durations_by_practice_id(practice):
        query = """
            SELECT
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

        data = {"practice_id": practice.id}

        results = Duration.db.query_db(query, data)

        practice_durations = []

        for result in results:
            practice_durations.append(Duration(result))

        return practice_durations
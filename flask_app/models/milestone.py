from flask_app.config.mysqlconnection import connectToMySQL


class Milestone:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.goal_id = data["goal_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.projected_completion = data["projected_completion"]
        self.is_complete = data["is_complete"]
        self.completed_at = data["completed_at"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def save_milestone(data):
        query = """
          INSERT INTO
            milestones (goal_id, name, description, projected_completion, is_complete, created_at, updated_at)
          VALUES
            (%(goal_id)s, %(name)s, %(description)s, %(projected_completion)s, %(is_complete)s, NOW(), NOW())
          ON DUPLICATE KEY UPDATE
            updated_at = NOW();
        """

        result = Milestone.db.query_db(query, data)

        if result:
            return result
        else:
            raise RuntimeError("Could not insert milestone: " + data["name"])

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

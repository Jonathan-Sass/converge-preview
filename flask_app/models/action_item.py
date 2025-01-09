from flask_app.config.mysqlconnection import connectToMySQL


class ActionItem:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.goal_id = data["goal_id"]
        self.milestone_id = data["milestone_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.action_item_order = data["action_item_order"]
        self.estimated_time_value = data["estimated_time_value"]
        self.estimated_time_unit = data["estimated_time_unit"]
        self.is_complete = data["is_complete"]
        self.completed_at = data["completed_at"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def save_action_item(data):
        query = """

    """
        return

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


    def build_action_item_from_row(row, action_item_id):
        return ActionItem(action_item_data = {
            "id": action_item_id,
            "goal_id": row["action_item_goal_id"],
            "milestone_id": row["action_item_milestone_id"],
            "name": row["action_item_name"],
            "description": row["action_item_description"],
            "action_item_order": row["action_item_order"],
            "estimated_time_value": row["estimated_time_value"],
            "estimated_time_unit": row["estimated_time_unit"],
            "is_complete": row["action_item_is_complete"],
            "completed_at": row["action_item_completed_at"],
            "created_at": row["action_item_created_at"],
            "updated_at": row["action_item_updated_at"],
        })

    def save_action_item(data):
        query = """
          INSERT INTO
            action_items (goal_id, milestone_id, name, description, action_item_order, estimated_time_value, estimated_time_unit, is_complete, created_at, updated_at)
          VALUES
            (%(goal_id)s, %(milestone_id)s, %(name)s, %(description)s, %(action_item_order)s, %(estimated_time_value)s, %(estimated_time_unit)s, %(is_complete)s, NOW(), NOW())
          ON DUPLICATE KEY UPDATE
            updated_at = NOW();
        """

        result = ActionItem.db.query_db(query, data)

        if result:
            return result
        else:
            raise RuntimeError("Could not insert action item: " + data["name"])

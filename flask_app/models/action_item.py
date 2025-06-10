from flask_app.config.mysqlconnection import connectToMySQL


class ActionItem:
    """
    Represents an action item within a milestone and goal.
    Provides methods to build and persist action item instances.
    """

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """Initializes an ActionItem instance with data from the database."""
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

    @staticmethod
    def build_action_item_from_row(row, action_item_id):
        """
        Builds an ActionItem object from a row of joined SQL data.

        Args:
            row (dict): Row data from a SQL JOIN query.
            action_item_id (int): The ID of the action item.

        Returns:
            ActionItem: An instance of ActionItem.
        """
        return ActionItem({
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

    @staticmethod
    def save_action_item(data):
        """
        Saves or updates an action item in the database.

        Args:
            data (dict): Action item data to be inserted or updated.

        Returns:
            int: The ID of the inserted or updated action item.

        Raises:
            RuntimeError: If the action item could not be saved.
        """
        query = """
          INSERT INTO
            action_items (goal_id, milestone_id, name, description, action_item_order, estimated_time_value, estimated_time_unit, is_complete, created_at, updated_at)
          VALUES
            (%(goal_id)s, %(milestone_id)s, %(name)s, %(description)s, %(action_item_order)s, %(estimated_time_value)s, %(estimated_time_unit)s, %(is_complete)s, NOW(), NOW())
          ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            description = VALUES(description),
            action_item_order = VALUES(action_item_order),
            estimated_time_value = VALUES(estimated_time_value),
            estimated_time_unit = VALUES(estimated_time_unit),
            is_complete = VALUES(is_complete),
            updated_at = NOW();
        """

        try:
          result = ActionItem.db.query_db(query, data)
          return result
        except Exception as e:
            print(f"Error inserting action item: {e}")
        # if result:
        #     return result
        # else:
        #     raise RuntimeError("Could not insert action item: " + data["name"])

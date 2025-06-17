from flask_app.config.mysqlconnection import connectToMySQL


class ExampleActionItem:
    """
    Represents an action item within a milestone and goal.
    Provides methods to build and persist action item instances.
    """

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """Initializes an ActionItem instance with data from the database."""
        self.id = data["id"]
        self.example_goal_id = data["example_goal_id"]
        self.example_milestone_id = data["example_milestone_id"]
        self.slug = data["slug"]
        self.name = data["name"]
        self.description = data["description"]
        self.action_item_order = data["action_item_order"]
        self.estimated_time_value = data["estimated_time_value"]
        self.estimated_time_unit = data["estimated_time_unit"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def build_example_action_item_from_row(row, action_item_id):
        """
        Builds an ActionItem object from a row of joined SQL data.

        Args:
            row (dict): Row data from a SQL JOIN query.
            action_item_id (int): The ID of the action item.

        Returns:
            ActionItem: An instance of ActionItem.
        """
        return ExampleActionItem({
            "id": action_item_id,
            "example_goal_id": row["example_action_item_example_goal_id"],
            "example_milestone_id": row["example_action_item_example_milestone_id"],
            "slug": row["example_action_item_slug"],
            "name": row["example_action_item_name"],
            "description": row["example_action_item_description"],
            "action_item_order": row["action_item_order"],
            "estimated_time_value": row["example_action_item_estimated_time_value"],
            "estimated_time_unit": row["example_action_item_estimated_time_unit"],
            "created_at": row["example_action_item_created_at"],
            "updated_at": row["example_action_item_updated_at"],
        })
from flask_app.config.mysqlconnection import connectToMySQL
from typing import List

from flask_app.models.example_action_item import ExampleActionItem


class ExampleMilestone:
    """Model representing an ExampleMilestone within a Goal, including associated Action Items."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a ExampleMilestone object.

        Args:
            data (dict): Dictionary containing milestone attributes.
        """
        self.id = data["id"]
        self.example_goal_id = data["example_goal_id"]
        self.slug = data["slug"]
        self.name = data["name"]
        self.description = data["description"]
        self.estimated_time_value = data["estimated_time_value"]
        self.estimated_time_unit = data["estimated_time_unit"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.example_action_items: List[ExampleActionItem] = []

    @staticmethod
    def build_example_milestone_from_row(row, milestone_id):
        """
        Construct a ExampleMilestone object from a SQL query result row.

        Args:
            row (dict): A row of SQL query results with aliased milestone fields.
            milestone_id (int): The ID of the milestone being built.

        Returns:
            Milestone: A Milestone object with an empty action_items list.
        """
        return ExampleMilestone(
            {
                "id": milestone_id,
                "example_goal_id": row["example_milestone_example_goal_id"],
                "name": row["example_milestone_name"],
                "description": row["example_milestone_description"],
                "estimated_time_value": row["example_milestone_estimated_time_value"],
                "estimated_time_unit": row["example_milestone_estimated_time_unit"],
                "created_at": row["example_milestone_created_at"],
                "updated_at": row["example_milestone_updated_at"],
                "action_items": [],
            }
        )

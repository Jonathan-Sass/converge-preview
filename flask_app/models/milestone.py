from flask_app.config.mysqlconnection import connectToMySQL
from typing import List

from flask_app.models.action_item import ActionItem


class Milestone:
    """Model representing a Milestone within a Goal, including associated Action Items."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a Milestone object.

        Args:
            data (dict): Dictionary containing milestone attributes.
        """
        self.id = data["id"]
        self.goal_id = data["goal_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.projected_completion = data["projected_completion"]
        self.is_complete = data["is_complete"]
        self.completed_at = data.get("completed_at", None)
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.action_items: List[ActionItem] = []

    @staticmethod
    def build_milestone_from_row(row, milestone_id):
        """
        Construct a Milestone object from a SQL query result row.

        Args:
            row (dict): A row of SQL query results with aliased milestone fields.
            milestone_id (int): The ID of the milestone being built.

        Returns:
            Milestone: A Milestone object with an empty action_items list.
        """
        return Milestone(
            {
                "id": milestone_id,
                "goal_id": row["milestone_goal_id"],
                "name": row["milestone_name"],
                "description": row["milestone_description"],
                "projected_completion": row["milestone_projected_completion"],
                "is_complete": row["milestone_is_complete"],
                "completed_at": row["milestone_completed_at"],
                "action_items": [],
                "created_at": row["milestone_created_at"],
                "updated_at": row["milestone_updated_at"],
            }
        )

    @staticmethod
    def save_milestone(data):
        """
        Save a new milestone to the database or update its `updated_at` timestamp if it exists.

        Args:
            data (dict): A dictionary of milestone values to insert.

        Returns:
            int: The ID of the inserted or updated milestone.

        Raises:
            RuntimeError: If the insert fails.
        """
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

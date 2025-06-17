from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.goals.goal import Goal


class FlexTask:
    """Handles database interactions for user Flex Tasks."""

    db = connectToMySQL("converge_schema")

    @staticmethod
    def find_flex_tasks_goal_ids_by_user_id(user_id):
        """
        Retrieve goal IDs of all flex tasks assigned to a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list[int]: A list of goal IDs linked to the user's flex tasks.
        """
        query = "SELECT * FROM user_flex_tasks WHERE user_id = %(user_id)s;"
        data = {"user_id": user_id}

        try:
            results = FlexTask.db.query_db(query, data)
            if not results:
                return []

            flex_tasks = [row["goal_id"] for row in results]
            return flex_tasks

        except Exception as e:
            raise RuntimeError(f"Error finding flex_tasks: {e}")

    @staticmethod
    def find_flex_tasks_objects_by_user_id(user_id):
        """
        Retrieve full goal objects (with milestones and action items) for a user's flex tasks.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list[Goal]: A list of Goal objects representing the user's flex tasks.
        """
        query = "SELECT * FROM user_flex_tasks WHERE user_id = %(user_id)s;"
        data = {"user_id": user_id}

        try:
            results = FlexTask.db.query_db(query, data)
            if not results:
                return []

            goal_ids = [row["goal_id"] for row in results]
            flex_tasks = Goal.find_goals_with_milestones_and_action_items_by_goal_ids(goal_ids, user_id)
            return flex_tasks

        except Exception as e:
            raise RuntimeError(f"Error finding flex_tasks: {e}")

    @staticmethod
    def assemble_flex_task_data_by_goal_id(flex_task_goal_ids, goal_data):
        """
        Assemble goal objects from a list of goal IDs and pre-fetched goal data.

        Args:
            flex_task_goal_ids (list[int]): List of goal IDs from flex tasks.
            goal_data (list[Goal]): Full list of goal objects.

        Returns:
            list[Goal]: A filtered list of goal objects that match the given flex task goal IDs.
        """
        goal_lookup = {goal.id: goal for goal in goal_data}
        flex_tasks = [goal_lookup[goal_id] for goal_id in flex_task_goal_ids if goal_id in goal_lookup]

        pprint(flex_tasks)
        return flex_tasks

    @staticmethod
    def save_flex_task(user_id, goal_id):
        """
        Save or update a flex task for a user.

        If the task already exists, its `updated_at` timestamp is refreshed.

        Args:
            user_id (int): The ID of the user.
            goal_id (int): The ID of the goal to add to flex tasks.

        Returns:
            Any: The result of the database query.
        """
        query = """
            INSERT INTO 
                user_flex_tasks (user_id, goal_id, created_at, updated_at)
            VALUES
                (%(user_id)s, %(goal_id)s, NOW(), NOW())
            ON DUPLICATE KEY UPDATE
                updated_at = NOW();
        """
        data = {
            "user_id": user_id,
            "goal_id": goal_id
        }

        try:
            result = FlexTask.db.query_db(query, data)
            return result
        except Exception as e:
            raise RuntimeError(f"Error saving goal to Flex Tasks: {e}")

    @staticmethod
    def delete_flex_task(goal_id, user_id):
        """
        Delete a flex task entry from the database for a given user and goal.

        Args:
            goal_id (int): The ID of the goal to remove.
            user_id (int): The ID of the user who owns the flex task.

        Returns:
            None
        """
        query = "DELETE FROM user_flex_tasks WHERE goal_id = %(goal_id)s AND user_id = %(user_id)s"
        data = {
            "goal_id": goal_id,
            "user_id": user_id
        }

        FlexTask.db.query_db(query, data)

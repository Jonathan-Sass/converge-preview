from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.user import User
from flask_app.models.milestone import Milestone
from flask_app.models.action_item import ActionItem
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory


class Goal:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = (data["id"],)
        self.category_id = (data["category_id"],)
        self.subcategory_id = (data["subcategory_id"],)
        self.name = (data["name"],)
        self.description = (data["description"],)
        self.goal_type = (data["goal_type"],)
        self.projected_completion = (data["projected_completion"],)
        self.is_complete = (data["is_complete"],)
        self.priority = (data["priority"],)
        self.created_at = (data["created_at"],)
        self.updated_at = (data["updated_at"],)

    # CRUD methods
    @staticmethod
    def process_and_save_subcategory_goals_data(subcategory_goal_data):
        user = User.get_logged_in_user()
        user_id = user.id
        subcategory = Subcategory.find_subcategory_by_slug(
            subcategory_goal_data["subcategorySlug"]
        )
        subcategory_id = subcategory.id
        category_id = subcategory.category_id

        for goal in subcategory_goal_data["goals"]:
            goal_data = {
                "user_id": user_id,
                "category_id": category_id,
                "subcategory_id": subcategory_id,
                "name": goal["name"],
                "description": goal["description"],
                "goal_type": goal["goalType"],
                "projected_completion": goal["projectedCompletion"],
                "is_complete": goal["isComplete"],
                "priority": goal["priority"],
            }

            goal_id = Goal.save_subcategory_goals(goal_data)

            for milestone in goal["milestones"]:
                milestone_data = {
                    "goal_id": goal_id,
                    "name": milestone["name"],
                    "description": milestone["description"],
                    "projected_completion": milestone["projectedCompletion"],
                    "is_complete": milestone["isComplete"],
                }

                result = Milestone.save_milestone(milestone_data)
                if result:
                    milestone_id = result

                print("Let's look at the data...")
                pprint(milestone["actionItems"])

                for action_item in milestone["actionItems"]:
                    print("action_item loop achieved!")
                    action_item_data = {
                        "goal_id": goal_id,
                        "milestone_id": milestone_id,
                        "name": action_item["name"],
                        "description": action_item["description"],
                        "action_item_order": action_item["actionItemOrder"],
                        "estimated_time_value": action_item["estimatedTimeValue"],
                        "estimated_time_unit": action_item["estimatedTimeUnit"],
                        "is_complete": action_item["isComplete"],
                    }

                    ActionItem.save_action_item(action_item_data)

        return

    def save_subcategory_goals(data):
        query = """
      INSERT INTO
        goals (user_id, category_id, subcategory_id, name, description, goal_type, projected_completion, is_complete, priority, created_at, updated_at)
      VALUES 
        (%(user_id)s, %(category_id)s, %(subcategory_id)s, %(name)s, %(description)s, %(goal_type)s, %(projected_completion)s, %(is_complete)s, %(priority)s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        updated_at = NOW();
    """

        result = Goal.db.query_db(query, data)
        if result:
            return result

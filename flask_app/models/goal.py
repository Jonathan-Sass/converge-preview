from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
import logging
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
        self.milestones = []
        self.created_at = (data["created_at"],)
        self.updated_at = (data["updated_at"],)

    # CRUD methods
    def find_goals_with_milestones_and_action_items_by_user_id(user_id):
        query = """
          SELECT
            g.id AS goal_id,
            g.category_id,
            g.subcategory_id,
            g.name AS goal_name,
            g.description AS goal_description,
            g.goal_type,
            g.projected_completion AS goal_projected_completion,
            g.is_complete AS goal_is_complete,
            g.completed_at AS goal_completed_at,
            g.priority AS goal_priority,
            m.id AS milestone_id,
            m.goal_id,
            m.name AS milestone_name,
            m.projected_completion AS milestone_projected_completion,
            m.is_complete AS milestone_is_complete,
            m.completed_at AS milestone_completed_at,
            a.id AS action_item_id,
            a.name AS action_item_name,
            a.action_item_order,
            a.estimated_time_value,
            a.estimated_time_unit,
            a.is_complete AS action_item_is_complete
          FROM
            goals g
          LEFT JOIN
            milestones m ON g.id = m.goal_id
          LEFT JOIN
            action_items a ON m.id = a.milestone_id
          WHERE 
            user_id = %(user_id)s;
        """

        data = {"user_id": user_id}

        results = Goal.db.query_db(query, data)

        goals = {}
        for row in results:
            goal_id = row["goal_id"]
            if goal_id not in goals:
                goals[goal_id] = Goal(
                    id=row["goal_id"],
                    category_id=row["category_id"],
                    subcategory_id=row["subcategory_id"],
                    name=row["goal_name"],
                    description=row["goal_description"],
                    goal_type=row["goal_type"],
                    projected_completion=row["goal_projected_completion"],
                    is_complete=row["goal_is_complete"],
                    completed_at=row["goal_completed_at"],
                    priority=row["priority"],
                    milestones=[],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )

            milestone_id = row["milestone_id"]
            if milestone_id not in goals[goal_id]["milestones"]:
                goals[goal_id]["milestones"][milestone_id] = Milestone(
                    id=row["milestone_id"],
                    goal_id=row["goal_id"],
                    name=row["milestone_name"],
                    description=row["milestone_description"],
                    projected_completion=row["milestone_projected_completion"],
                    is_complete=row["milestone_is_complete"],
                    completed_at=row["milestone_completed_at"],
                    created_at=row["milestone_created_at"],
                    updated_at=row["milestone_updated_at"],
                )
            
            action_item_id = row["action_item_id"]
            if action_item_id not in 

        return goals

    @staticmethod
    def process_and_save_subcategory_goals_data(subcategory_goal_data):
        try:
            # Get user information
            user = User.get_logged_in_user()
            if not user:
                raise ValueError("User is not logged in.")
            user_id = user.id

            # Find subcategory and associated IDs
            subcategory = Subcategory.find_subcategory_by_slug(
                subcategory_goal_data.get("subcategorySlug")
            )
            if not subcategory:
                raise ValueError(
                    f"Subcategory not found for slug: {subcategory_goal_data.get('subcategorySlug')}"
                )
            subcategory_id = subcategory.id
            category_id = subcategory.category_id

            # Process each goal in the subcategory
            for goal in subcategory_goal_data.get("goals", []):
                try:
                    # Save goal data
                    goal_data = {
                        "user_id": user_id,
                        "category_id": category_id,
                        "subcategory_id": subcategory_id,
                        "name": goal.get("name", "").strip(),
                        "description": goal.get("description", "").strip(),
                        "goal_type": goal.get("goalType"),
                        "projected_completion": goal.get("projectedCompletion"),
                        "is_complete": goal.get("isComplete", False),
                        "priority": goal.get("priority"),
                    }
                    goal_id = Goal.save_subcategory_goals(goal_data)

                    # Process milestones
                    for milestone in goal.get("milestones", []):
                        try:
                            milestone_data = {
                                "goal_id": goal_id,
                                "name": milestone.get("name", "").strip(),
                                "description": milestone.get("description", "").strip(),
                                "projected_completion": milestone.get(
                                    "projectedCompletion"
                                ),
                                "is_complete": milestone.get("isComplete", False),
                            }
                            result = Milestone.save_milestone(milestone_data)
                            milestone_id = result if result else None

                            if not milestone_id:
                                logging.warning(
                                    f"Failed to save milestone for goal ID {goal_id}. Skipping related action items."
                                )
                                continue

                            # Process action items
                            for action_item in milestone.get("actionItems", []):
                                try:
                                    action_item_data = {
                                        "goal_id": goal_id,
                                        "milestone_id": milestone_id,
                                        "name": action_item.get("name", "").strip(),
                                        "description": action_item.get(
                                            "description", ""
                                        ).strip(),
                                        "action_item_order": action_item.get(
                                            "actionItemOrder"
                                        ),
                                        "estimated_time_value": action_item.get(
                                            "estimatedTimeValue"
                                        ),
                                        "estimated_time_unit": action_item.get(
                                            "estimatedTimeUnit"
                                        ),
                                        "is_complete": action_item.get(
                                            "isComplete", False
                                        ),
                                    }
                                    ActionItem.save_action_item(action_item_data)
                                except Exception as e:
                                    logging.error(
                                        f"Error saving action item: {action_item}, Error: {e}"
                                    )
                        except Exception as e:
                            logging.error(
                                f"Error processing milestone: {milestone}, Error: {e}"
                            )
                except Exception as e:
                    logging.error(f"Error processing goal: {goal}, Error: {e}")

        except Exception as e:
            logging.critical(
                f"Critical error in process_and_save_subcategory_goals_data: {e}"
            )
            raise  # Optionally re-raise the exception for higher-level handling

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

    # @staticmethod
    # def process_and_save_subcategory_goals_data_can_haz_more_error_handling(
    #     subcategory_goal_data,
    # ):
    #     user = User.get_logged_in_user()
    #     user_id = user.id
    #     subcategory = Subcategory.find_subcategory_by_slug(
    #         subcategory_goal_data["subcategorySlug"]
    #     )
    #     subcategory_id = subcategory.id
    #     category_id = subcategory.category_id

    #     for goal in subcategory_goal_data["goals"]:
    #         goal_data = {
    #             "user_id": user_id,
    #             "category_id": category_id,
    #             "subcategory_id": subcategory_id,
    #             "name": goal["name"],
    #             "description": goal["description"],
    #             "goal_type": goal["goalType"],
    #             "projected_completion": goal["projectedCompletion"],
    #             "is_complete": goal["isComplete"],
    #             "priority": goal["priority"],
    #         }

    #         goal_id = Goal.save_subcategory_goals(goal_data)

    #         for milestone in goal["milestones"]:
    #             milestone_data = {
    #                 "goal_id": goal_id,
    #                 "name": milestone["name"],
    #                 "description": milestone["description"],
    #                 "projected_completion": milestone["projectedCompletion"],
    #                 "is_complete": milestone["isComplete"],
    #             }

    #             result = Milestone.save_milestone(milestone_data)
    #             if result:
    #                 milestone_id = result

    #             print("Let's look at the data...")
    #             pprint(milestone["actionItems"])

    #             for action_item in milestone["actionItems"]:
    #                 print("action_item loop achieved!")
    #                 action_item_data = {
    #                     "goal_id": goal_id,
    #                     "milestone_id": milestone_id,
    #                     "name": action_item["name"],
    #                     "description": action_item["description"],
    #                     "action_item_order": action_item["actionItemOrder"],
    #                     "estimated_time_value": action_item["estimatedTimeValue"],
    #                     "estimated_time_unit": action_item["estimatedTimeUnit"],
    #                     "is_complete": action_item["isComplete"],
    #                 }

    #                 ActionItem.save_action_item(action_item_data)

    #     return

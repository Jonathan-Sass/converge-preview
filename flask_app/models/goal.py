from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from typing import List
import logging
from flask_app.models.user import User
from flask_app.models.milestone import Milestone
from flask_app.models.action_item import ActionItem
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory


class Goal:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.category_id = data["category_id"]
        self.subcategory_id = data["subcategory_id"]
        self.name = data["name"]
        self.description = data["goal_description"]
        self.goal_type = data["goal_type"]
        self.is_active = data["goal_is_active"]
        self.projected_completion = data["projected_completion"]
        self.is_complete = data["is_complete"]
        self.priority = data["priority"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.milestones: List[Milestone] = []

    # CRUD methods
    
    def find_goals_with_milestones_and_action_items_by_user_id(user_id):
        query = """
          SELECT
              g.id AS goal_id,
              g.user_id,
              g.category_id,
              g.subcategory_id,
              g.name AS goal_name,
              g.description AS goal_description,
              g.goal_type,
              g.projected_completion AS goal_projected_completion,
              g.is_complete AS goal_is_complete,
              g.priority AS goal_priority,
              g.is_active AS goal_is_active,
              g.created_at AS goal_created_at,
              g.updated_at AS goal_updated_at,
              m.id AS milestone_id,
              m.goal_id AS milestone_goal_id,
              m.name AS milestone_name,
              m.description AS milestone_description,
              m.projected_completion AS milestone_projected_completion,
              m.is_complete AS milestone_is_complete,
              m.completed_at AS milestone_completed_at,
              m.created_at AS milestone_created_at,
              m.updated_at AS milestone_updated_at,
              a.id AS action_item_id,
              a.goal_id AS action_item_goal_id,
              a.milestone_id AS action_item_milestone_id,
              a.name AS action_item_name,
              a.description AS action_item_description,
              a.action_item_order,
              a.estimated_time_value,
              a.estimated_time_unit,
              a.is_complete AS action_item_is_complete,
              a.completed_at AS action_item_completed_at,
              a.created_at AS action_item_created_at,
              a.updated_at AS action_item_updated_at
          FROM
              goals g
          LEFT JOIN
              milestones m ON g.id = m.goal_id
          LEFT JOIN
              action_items a ON m.id = a.milestone_id
          WHERE 
              g.user_id = %(user_id)s
          ORDER BY
              g.priority;
      """

        data = {"user_id": user_id}
        results = Goal.db.query_db(query, data)

        return Goal.build_goals_with_milestones_and_action_items(results, user_id)
    

    def find_goals_with_milestones_and_action_items_by_goal_ids(goal_ids, user_id):
        query = """
          SELECT
              g.id AS goal_id,
              g.user_id,
              g.category_id,
              g.subcategory_id,
              g.name AS goal_name,
              g.description AS goal_description,
              g.goal_type,
              g.projected_completion AS goal_projected_completion,
              g.is_complete AS goal_is_complete,
              g.priority AS goal_priority,
              g.is_active AS goal_is_active,
              g.created_at AS goal_created_at,
              g.updated_at AS goal_updated_at,
              m.id AS milestone_id,
              m.goal_id AS milestone_goal_id,
              m.name AS milestone_name,
              m.description AS milestone_description,
              m.projected_completion AS milestone_projected_completion,
              m.is_complete AS milestone_is_complete,
              m.completed_at AS milestone_completed_at,
              m.created_at AS milestone_created_at,
              m.updated_at AS milestone_updated_at,
              a.id AS action_item_id,
              a.goal_id AS action_item_goal_id,
              a.milestone_id AS action_item_milestone_id,
              a.name AS action_item_name,
              a.description AS action_item_description,
              a.action_item_order,
              a.estimated_time_value,
              a.estimated_time_unit,
              a.is_complete AS action_item_is_complete,
              a.completed_at AS action_item_completed_at,
              a.created_at AS action_item_created_at,
              a.updated_at AS action_item_updated_at
          FROM
              goals g
          LEFT JOIN
              milestones m ON g.id = m.goal_id
          LEFT JOIN
              action_items a ON m.id = a.milestone_id
          WHERE 
              g.id IN %(goal_ids)s
          ORDER BY
              g.priority;
        """
          
        data = {"goal_ids": tuple(goal_ids)}
        results = Goal.db.query_db(query, data)

        return Goal.build_goals_with_milestones_and_action_items(results, user_id)


    def build_goals_with_milestones_and_action_items(results, user_id):
        goals = []

        if results:

            for row in results:
                # Add goal if not already present
                goal = next((g for g in goals if g.id == row["goal_id"]), None)
                if not goal:
                    goal = Goal.build_goal_from_row(row, user_id)
                    goals.append(goal)
                    # pprint(vars(goals[goal_id]))

                milestone = None

                # Add milestone if not already present
                milestone_id = row["milestone_id"]
                if milestone_id and row["milestone_goal_id"] == goal.id:
                    milestone = next((m for m in goal.milestones if m.id == milestone_id), None)
                    if not milestone:
                        milestone = Milestone.build_milestone_from_row(row, milestone_id)
                        goal.milestones.append(milestone)

                # Add action item if not already present
                action_item_id = row["action_item_id"]

                if (milestone and action_item_id and row["action_item_milestone_id"] == milestone.id):
                    action_item = next((ai for ai in milestone.action_items if ai.id == action_item_id), None)
                    
                    if not action_item:
                        action_item = ActionItem.build_action_item_from_row(row, action_item_id)
                        milestone.action_items.append(action_item)

        # print("goals in find_goals_with_m_a_i:")
        # for goal in goals:
        #     pprint(vars(goal))
        #     if goal.milestones:
        #         for milestone in goal.milestones:
        #             print("Milestone in goal")
        #             pprint(vars(milestone))
        return goals

    def build_goal_from_row(row, user_id):
        return Goal({
            "id": row["goal_id"],
            "user_id": user_id,
            "category_id": row["category_id"],
            "subcategory_id": row["subcategory_id"],
            "name": row["goal_name"],
            "goal_description": row["goal_description"],
            "goal_type": row["goal_type"],
            "goal_is_active": row["goal_is_active"],
            "projected_completion": row["goal_projected_completion"],
            "is_complete": row["goal_is_complete"],
            "priority": row["goal_priority"],
            "goal_is_active": row["goal_is_active"],
            "milestones": [],
            "created_at": row["goal_created_at"],
            "updated_at": row["goal_updated_at"],
        })
    

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
                        "is_active": goal.get("isActive") if goal.get("isActive") is not None else True,
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
        goals (user_id, category_id, subcategory_id, name, description, goal_type, projected_completion, is_complete, priority, is_active, created_at, updated_at)
      VALUES 
        (%(user_id)s, %(category_id)s, %(subcategory_id)s, %(name)s, %(description)s, %(goal_type)s, %(projected_completion)s, %(is_complete)s, %(priority)s, %(is_active)s, NOW(), NOW())
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

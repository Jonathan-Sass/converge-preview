from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from typing import List
import logging
from flask_app.models.user import User
from flask_app.models.goals.milestone import Milestone
from flask_app.models.goals.action_item import ActionItem
from flask_app.models.goals.goal_category import GoalCategory
from flask_app.models.goals.category_component import CategoryComponent


class Goal:
    """
    Represents a user-defined goal within the Converge application.
    A goal can have milestones and action items nested within it.
    """

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.goal_category_id = data["goal_category_id"]
        self.category_component_id = data["category_component_id"]
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

    # CRUD methodsg
    
    def find_goals_with_milestones_and_action_items_by_user_id(user_id):
        """Retrieve all goals for a user along with their milestones and action items."""
        query = """
          SELECT
              g.id AS goal_id,
              g.user_id,
              g.goal_category_id,
              g.category_component_id,
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
        """Retrieve selected goals (by IDs) with their milestones and action items."""
        query = """
          SELECT
              g.id AS goal_id,
              g.user_id,
              g.goal_category_id,
              g.category_component_id,
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
      """Builds a list of Goal objects from raw SQL results, nesting milestones and action items."""

      goals = []
      goal_map = {}

      if results:
          for row in results:
              goal_id = row.get("goal_id")
              if goal_id is None:
                  continue

              # -- GOAL --
              if goal_id not in goal_map:
                  goal = Goal.build_goal_from_row(row, user_id)
                  goal.milestones = []
                  goal_map[goal_id] = goal
                  goals.append(goal)
              else:
                  goal = goal_map[goal_id]

              # -- MILESTONE --
              milestone_id = row.get("milestone_id")
              if milestone_id:
                  milestone_map = getattr(goal, "_milestone_map", {})
                  if milestone_id not in milestone_map:
                      milestone = Milestone.build_milestone_from_row(row, milestone_id)
                      milestone.action_items = []
                      goal.milestones.append(milestone)
                      milestone_map[milestone_id] = milestone
                      goal._milestone_map = milestone_map
                  else:
                      milestone = milestone_map[milestone_id]
              else:
                  milestone = None

              # -- ACTION ITEM --
              action_item_id = row.get("action_item_id")
              if milestone and action_item_id:
                  action_item_map = getattr(milestone, "_action_item_map", {})
                  if action_item_id not in action_item_map:
                      action_item = ActionItem.build_action_item_from_row(row, action_item_id)
                      milestone.action_items.append(action_item)
                      action_item_map[action_item_id] = action_item
                      milestone._action_item_map = action_item_map

      return goals


    def build_goal_from_row(row, user_id):
        """Converts a single SQL row into a Goal object."""
        return Goal({
            "id": row["goal_id"],
            "user_id": user_id,
            "goal_category_id": row["goal_category_id"],
            "category_component_id": row["category_component_id"],
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
    def filter_flex_task_goals_from_goal_data(goal_data, flex_task_goal_ids):
        """Filters a user's goals in their flex tasks from the goal_data rendered in actionable items on the dashboard"""
        filtered_goal_data = [goal for goal in goal_data if goal.id not in flex_task_goal_ids]
        return filtered_goal_data


    @staticmethod
    def process_and_save_category_component_goals_data(category_component_goal_data):
        """Processes and saves a set of user-submitted goals, milestones, and action items."""
        try:
            # Get user information
            user = User.get_logged_in_user()
            if not user:
                raise ValueError("User is not logged in.")
            user_id = user.id

            component_slug = category_component_goal_data["goals"][0].get("categoryComponentSlug")

            # print(f"Component slug in Goal.process_and_save: {component_slug}")

            # Find category_component and associated IDs
            if component_slug:
              category_component = CategoryComponent.find_category_component_by_slug(component_slug)
            if not category_component:
                raise ValueError(
                    f"CategoryComponent not found for slug: {component_slug}"
                )
            category_component_id = category_component.id
            goal_category_id = category_component.goal_category_id

            # Process each goal in the category_component
            for goal in category_component_goal_data.get("goals", []):
                try:
                    # Save goal data
                    goal_data = {
                        "user_id": user_id,
                        "goal_category_id": goal_category_id,
                        "category_component_id": category_component_id,
                        "name": goal.get("name", "").strip(),
                        "description": goal.get("description", "").strip(),
                        "goal_type": goal.get("goalType"),
                        "priority": goal.get("priority"),
                        "is_active": goal.get("isActive") if goal.get("isActive") is not None else True,
                        "projected_completion": goal.get("projectedCompletion"),
                        "is_complete": goal.get("isComplete", False)
                    }
                    goal_id = Goal.save_goal(goal_data)

                    # Process milestones
                    for milestone in goal.get("milestones", []):
                        try:
                            milestone_data = {
                                "goal_id": goal_id,
                                "name": milestone.get("name", "").strip(),
                                "description": milestone.get("description", "").strip(),
                                "projected_completion": milestone.get("projectedCompletion"),
                                "is_complete": milestone.get("isComplete", False),
                            }
                            result = Milestone.save_milestone(milestone_data)
                            milestone_id = result if result else None
                            
                            print(f"Milestone saved: {milestone_id}")

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
                                        "description": action_item.get("description", "").strip(),
                                        "action_item_order": action_item.get("actionItemOrder"),
                                        "estimated_time_value": action_item.get("estimatedTimeValue"),
                                        "estimated_time_unit": action_item.get("estimatedTimeUnit"),
                                        "is_complete": action_item.get("isComplete", False),
                                    }
                                    print(f"Saving action item: {action_item_data["name"]}")
                                    ActionItem.save_action_item(action_item_data)
                                except Exception as e:
                                    logging.error(f"Error saving action item: {action_item}, Error: {e}")
                        except Exception as e:
                            logging.error(f"Error processing milestone: {milestone}, Error: {e}")
                except Exception as e:
                    logging.error(f"Error processing goal: {goal}, Error: {e}")

        except Exception as e:
            logging.critical(f"Critical error in process_and_save_category_component_goals_data: {e}")
            raise  # Optionally re-raise the exception for higher-level handling

    def save_goal(data):
        """Saves a goal to the database."""

        query = """
          INSERT INTO
            goals (user_id, goal_category_id, category_component_id, name, description, goal_type, projected_completion, is_complete, priority, is_active, created_at, updated_at)
          VALUES 
            (%(user_id)s, %(goal_category_id)s, %(category_component_id)s, %(name)s, %(description)s, %(goal_type)s, %(projected_completion)s, %(is_complete)s, %(priority)s, %(is_active)s, NOW(), NOW())
          ON DUPLICATE KEY UPDATE
            updated_at = NOW();
        """

        result = Goal.db.query_db(query, data)
        if result:
            return result

    # @staticmethod
    # def process_and_save_category_component_goals_data_can_haz_more_error_handling(
    #     category_component_goal_data,
    # ):
    #     user = User.get_logged_in_user()
    #     user_id = user.id
    #     category_component = CategoryComponent.find_category_component_by_slug(
    #         category_component_goal_data["category_componentSlug"]
    #     )
    #     category_component_id = category_component.id
    #     goal_category_id = category_component.goal_category_id

    #     for goal in category_component_goal_data["goals"]:
    #         goal_data = {
    #             "user_id": user_id,
    #             "goal_category_id": goal_category_id,
    #             "category_component_id": category_component_id,
    #             "name": goal["name"],
    #             "description": goal["description"],
    #             "goal_type": goal["goalType"],
    #             "projected_completion": goal["projectedCompletion"],
    #             "is_complete": goal["isComplete"],
    #             "priority": goal["priority"],
    #         }

    #         goal_id = Goal.save_category_component_goals(goal_data)

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

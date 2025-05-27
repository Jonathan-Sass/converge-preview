from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from typing import List
import logging
from flask_app.models.user import User
from flask_app.models.example_milestone import ExampleMilestone
from flask_app.models.example_action_item import ExampleActionItem
from flask_app.models.goal_category import GoalCategory
from flask_app.models.category_component import CategoryComponent


class ExampleGoal:
    """
    Represents a user-defined goal within the Converge application.
    A goal can have milestones and action items nested within it.
    """

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.goal_category_id = data["goal_category_id"]
        self.category_component_id = data["category_component_id"]
        self.slug = data["slug"]
        self.name = data["name"]
        self.description = data["goal_description"]
        self.goal_type = data["goal_type"]
        self.priority = data["priority"]
        self.estimated_time_value = data["estimated_time_value"]
        self.estimated_time_unit = data["estimated_time_unit"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.example_milestones: List[ExampleMilestone] = []


    def build_goal_from_row(row):
      """Converts a single SQL row into an ExampleGoal object."""
      return ExampleGoal({
        "id": row["example_goal_id"],
        "goal_category_id": row["goal_category_id"],
        "category_component_id": row["category_component_id"],
        "slug": row["example_goal_slug"],
        "name": row["example_goal_name"],
        "description": row["example_goal_description"],
        "goal_type": row["goal_type"],
        "priority": row["example_goal_priority"],
        "estimated_time_value": row["example_goal_estimated_time_value"],
        "estimated_time_unit": row["example_goal_estimated_time_unit"],
        "created_at": row["example_goal_created_at"],
        "updated_at": row["example_goal_updated_at"],
        "example_milestones": [],
      })

    # CRUD methods
    
    def find_example_goals_with_milestones_and_action_items_by_user_id(user_id):
      """Retrieve all example goals for a user along with their milestones and action items."""
      query = """
        SELECT
          eg.id AS example_goal_id,
          eg.user_id,
          eg.goal_category_id,
          eg.category_component_id,
          eg.slug AS example_goal_slug,
          eg.name AS example_goal_name,
          eg.description AS example_goal_description,
          eg.goal_type,
          eg.priority AS example_goal_priority,
          eg.estimated_time_value AS example_goal_estimated_time_value,
          eg.estimated_time_unit AS example_goal_estimated_time_unit,
          eg.created_at AS example_goal_created_at,
          eg.updated_at AS example_goal_updated_at,
          em.id AS example_milestone_id,
          em.goal_id AS example_milestone_goal_id,
          em.name AS example_milestone_name,
          em.description AS example_milestone_description,
          em.estimated_time_value AS example_milestone_estimated_time_value,
          em.estimated_time_unit AS example_milestone_estimated_time_unit,
          em.completed_at AS example_milestone_completed_at,
          em.created_at AS example_milestone_created_at,
          em.updated_at AS example_milestone_updated_at,
          ea.id AS example_action_item_id,
          ea.goal_id AS example_action_item_goal_id,
          ea.milestone_id AS example_action_item_milestone_id,
          ea.slug AS example_action_item_slug,
          ea.name AS example_action_item_name,
          ea.description AS example_action_item_description,
          ea.action_item_order,
          ea.estimated_time_value AS example_action_item_estimated_time_value,
          ea.estimated_time_unit AS example_action_item_estimated_time_unit,
          ea.created_at AS example_action_item_created_at,
          ea.updated_at AS example_action_item_updated_at
        FROM
          example_goals eg
        LEFT JOIN
          example_milestones em ON eg.id = em.goal_id
        LEFT JOIN
          example_action_items a ON em.id = ea.milestone_id
        WHERE 
          eg.user_id = %(user_id)s
        ORDER BY
          eg.priority;
    """

      data = {"user_id": user_id}
      results = ExampleGoal.db.query_db(query, data)

      return ExampleGoal.build_goals_with_milestones_and_action_items(results, user_id)
    

    def find_goals_with_milestones_and_action_items_by_goal_ids(goal_ids, user_id):
      """Retrieve selected example goals (by IDs) with their milestones and action items."""
      query = """
        SELECT
          eg.id AS example_goal_id,
          eg.user_id,
          eg.goal_category_id,
          eg.category_component_id,
          eg.slug AS example_goal_slug,
          eg.name AS example_goal_name,
          eg.description AS example_goal_description,
          eg.goal_type,
          eg.priority AS example_goal_priority,
          eg.estimated_time_value AS example_goal_estimated_time_value,
          eg.estimated_time_unit AS example_goal_estimated_time_unit,
          eg.created_at AS example_goal_created_at,
          eg.updated_at AS example_goal_updated_at,
          em.id AS example_milestone_id,
          em.goal_id AS example_milestone_goal_id,
          em.name AS example_milestone_name,
          em.description AS example_milestone_description,
          em.estimated_time_value AS example_milestone_estimated_time_value,
          em.estimated_time_unit AS example_milestone_estimated_time_unit,
          em.completed_at AS example_milestone_completed_at,
          em.created_at AS example_milestone_created_at,
          em.updated_at AS example_milestone_updated_at,
          ea.id AS example_action_item_id,
          ea.goal_id AS example_action_item_goal_id,
          ea.milestone_id AS example_action_item_milestone_id,
          ea.slug AS example_action_item_slug,
          ea.name AS example_action_item_name,
          ea.description AS example_action_item_description,
          ea.action_item_order,
          ea.estimated_time_value AS example_action_item_estimated_time_value,
          ea.estimated_time_unit AS example_action_item_estimated_time_unit,
          ea.created_at AS example_action_item_created_at,
          ea.updated_at AS example_action_item_updated_at
        FROM
          example_goals eg
        LEFT JOIN
          example_milestones em ON eg.id = em.goal_id
        LEFT JOIN
          example_action_items a ON em.id = ea.milestone_id
        WHERE 
            eg.id IN %(goal_ids)s
        ORDER BY
            eg.priority;
      """
          
      data = {"goal_ids": tuple(goal_ids)}
      results = ExampleGoal.db.query_db(query, data)

      return ExampleGoal.build_goals_with_milestones_and_action_items(results, user_id)


    def build_goals_with_milestones_and_action_items(results, user_id):
      """Builds a list of ExampleGoal objects from raw SQL results, nesting milestones and action items."""

      goals = []
      goal_map = {}

      if results:
          for row in results:
              goal_id = row.get("goal_id")
              if goal_id is None:
                  continue

              # -- GOAL --
              if goal_id not in goal_map:
                  goal = ExampleGoal.build_goal_from_row(row, user_id)
                  goal.example_milestones = []
                  goal_map[goal_id] = goal
                  goals.append(goal)
              else:
                  goal = goal_map[goal_id]

              # -- MILESTONE --
              milestone_id = row.get("milestone_id")
              if milestone_id:
                  milestone_map = getattr(goal, "_milestone_map", {})
                  if milestone_id not in milestone_map:
                      milestone = ExampleMilestone.build_milestone_from_row(row, milestone_id)
                      milestone.example_action_items = []
                      goal.example_milestones.append(milestone)
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
                      action_item = ExampleActionItem.build_action_item_from_row(row, action_item_id)
                      milestone.example_action_items.append(action_item)
                      action_item_map[action_item_id] = action_item
                      milestone._action_item_map = action_item_map

      return goals

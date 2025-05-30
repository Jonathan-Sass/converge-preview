from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from typing import List
import logging
from flask_app.models.user import User
from flask_app.models.example_goal import ExampleGoal
from flask_app.models.example_milestone import ExampleMilestone
from flask_app.models.example_action_item import ExampleActionItem
from flask_app.models.goal_category import GoalCategory
from flask_app.models.category_component import CategoryComponent


class CategoryArchetype:
  db = connectToMySQL("converge_schema")

  def __init__(self, data):
    """Initiate a CategoryArchetype object from database row data"""

    self.id = data["id"]
    self.goal_category_id = data["goal_category_id"]
    self.slug = data["slug"]
    self.name = data["name"]
    self.description = data["description"]
    self.is_default = data["is_default"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]
    self.example_goals = []

  def build_archetype_from_row(row):
    """Converts a single SQL row into an CategoryArchetype object."""
    return CategoryArchetype({
      "id": row["category_archetype_id"],
      "goal_category_id": row["goal_category_id"],
      "slug": row["category_archetype_slug"],
      "name": row["category_archetype_name"],
      "description": row["category_archetype_description"],
      "is_default": row["category_archetype_is_default"],
      "created_at": row["category_archetype_created_at"],
      "updated_at": row["category_archetype_updated_at"],
      "example_milestones": [],
    })

  def find_archetype_with_goals_milestones_and_action_items_by_archetype_slug(archetype_slug):
        """Retrieve a category archetype from its slug, with example goals, milestones and action items."""
        query = """
          SELECT
            ca.id AS category_archetype_id,
            ca.goal_category_id,
            ca.slug AS category_archetype_slug,
            ca.name AS category_archetype_name,
            ca.description AS category_archetype_description,
            ca.is_default AS category_archetype_is_default,
            ca.created_at AS category_archetype_created_at,
            ca.updated_at AS category_archetype_updated_at,
            eg.id AS example_goal_id,
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
            em.example_goal_id AS example_milestone_example_goal_id,
            em.name AS example_milestone_name,
            em.description AS example_milestone_description,
            em.estimated_time_value AS example_milestone_estimated_time_value,
            em.estimated_time_unit AS example_milestone_estimated_time_unit,
            em.completed_at AS example_milestone_completed_at,
            em.created_at AS example_milestone_created_at,
            em.updated_at AS example_milestone_updated_at,
            ea.id AS example_action_item_id,
            ea.example_goal_id AS example_action_item_example_goal_id,
            ea.example_milestone_id AS example_action_item_example_milestone_id,
            ea.slug AS example_action_item_slug,
            ea.name AS example_action_item_name,
            ea.description AS example_action_item_description,
            ea.action_item_order,
            ea.estimated_time_value AS example_action_item_estimated_time_value,
            ea.estimated_time_unit AS example_action_item_estimated_time_unit,
            ea.created_at AS example_action_item_created_at,
            ea.updated_at AS example_action_item_updated_at
          FROM
            category_archetypes ca
          LEFT JOIN
            category_archetypes_has_example_goals caheg ON ca.id = caheg.category_archetype_id
          LEFT JOIN
            example_goals eg ON caheg.example_goal_id = eg.id
          LEFT JOIN
            example_milestones em ON eg.id = em.example_goal_id
          LEFT JOIN
            example_action_items ea ON em.id = ea.example_milestone_id
          WHERE 
            ca.slug = %(slug)s
          ORDER BY
            eg.priority;
      """

        data = {"slug": archetype_slug}
        results = CategoryArchetype.db.query_db(query, data)
        if not results:
            raise RuntimeError(f"No category archetype found for slug: {archetype_slug}")
        
        return results
  
  @classmethod
  def build_enriched_archetype_with_category_and_components(cls, category_archetype_data):
      """Builds an archetype complete with goals, milestones and action items as well as the associated category and category components"""
      archetype = cls.build_archetype_with_goals_milestones_and_action_items(category_archetype_data)

      enriched_archetype = cls.add_category_and_components_to_archetype(archetype)
      return enriched_archetype
  
  def add_category_and_components_to_archetype(archetype):
      category_id = archetype.goal_category_id
      category = GoalCategory.find_category_by_id(category_id)

      category_components = CategoryComponent.get_all_as_dict()

      archetype.category = category
      for goal in archetype.example_goals:
          component_id = goal["category_component_id"]
          goal.category_component = category_components[component_id]

      return archetype
  
  def build_archetype_with_goals_milestones_and_action_items(results):
      """Builds a list of ExampleGoal objects from raw SQL results, nesting milestones and action items."""
      archetype = CategoryArchetype.build_archetype_from_row(results[0])

      goals = []
      goal_map = {}

      if results:
          for row in results:
              goal_id = row.get("goal_id")
              if goal_id is None:
                  continue

              # -- GOAL --
              if goal_id not in goal_map:
                  goal = ExampleGoal.build_goal_from_row(row)
                  goal.example_milestones = []
                  goal_map[goal_id] = goal
                  archetype.example_goals.append(goal)
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

      return archetype
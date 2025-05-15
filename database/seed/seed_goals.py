from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import redirect
import re

from flask_app.models.user import User
from database.seed_data.category_component_data import category_components
from database.seed_data.goal_archetype_data import category_archetypes

def goal_seed():
  user = User.get_logged_in_user()
  if not user:
      return redirect("/")
  
  goal_category_seed()
  category_component_seed()
  category_archetype_seed(category_archetypes)

  return

def goal_category_seed():
    query = """
    INSERT INTO goal_categories (slug, name, created_at, updated_at)
    VALUES
      ('health-wellness', 'Health and Wellness', NOW(), NOW()),
      ('social-community', 'Social and Community Engagement', NOW(), NOW()),
      ('recreation-travel', 'Recreation and Travel', NOW(), NOW()),
      ('spirituality-life-purpose', 'Spirituality and Life Purpose', NOW(), NOW()),
      ('career-professional-development', 'Career and Professional Development', NOW(), NOW()),
      ('creative-expression-hobbies', 'Creative Expression and Hobbies', NOW(), NOW()),
      ('wealth-finance', 'Wealth Building and Financial Health', NOW(), NOW()),
      ('environment-success', 'Environment and Success', NOW(), NOW())
    ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    updated_at = NOW();
      """
    User.db.query_db(query)

    return

def category_component_seed():
    batch_data = {}

    # Organize subcategories into batches by category (key)
    for category_slug, subcategories in category_components.items():
        for subcategory in subcategories:
            if category_slug not in batch_data:
                batch_data[category_slug] = []
            batch_data[category_slug].append(
                {
                    "slug": subcategory["slug"], 
                    "name": subcategory["name"],
                    "description": subcategory["description"],
                    "role": subcategory["role"],}
            )

    # Retrieve the mapping of category slugs to category IDs
    category_id_lookup = (
        get_goal_category_id_lookup()
    )  # Should return a dictionary like {'health-wellness': 1, 'social-community': 2, ...}

    # Prepare and execute batch insert queries for each category
    for category_slug, subcategory_batch in batch_data.items():
        # Check if the category slug exists in the retrieved category IDs
        if category_slug in category_id_lookup:
            category_id = category_id_lookup[category_slug]
        else:
            print(f"Category slug '{category_slug}' not found in the database.")
            continue  # Skip this category if the ID is not found

        # Create the base query
        query = """
        INSERT INTO category_components
          (goal_category_id, slug, name, description, role, created_at, updated_at)
        VALUES
          (%s, %s, %s, %s, %s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
          goal_category_id = VALUES(goal_category_id),
          name = VALUES(name),
          description = VALUES(description),
          role = VALUES(role),
          updated_at = NOW();
        """

        values = [(category_id, sc["slug"], sc["name"], sc["description"], sc["role"]) for sc in subcategory_batch]

        User.db.query_db(query, values, many=True)

    return

def category_archetype_seed(category_archetypes):
    category_id_lookup = get_goal_category_id_lookup()
    goal_id_lookup = get_example_goal_id_lookup()
    print("↪ goal_id_lookup keys:", list(goal_id_lookup.keys()))

    batched_milestones = []
    batched_action_items = []
    
    batched_archetypes = batch_category_archetype_data(category_archetypes, category_id_lookup)
    execute_category_archetype_seed(batched_archetypes)

    batched_goals = batch_example_goal_data(category_archetypes, category_id_lookup)
    execute_example_goal_seed(batched_goals)
    
    batched_milestones = batch_example_milestone_data(category_archetypes, category_id_lookup, goal_id_lookup)
    execute_example_milestone_seed(batched_milestones)

    batched_action_items = batch_example_action_item_data(category_archetypes, category_id_lookup, goal_id_lookup)
    execute_example_action_item_seed(batched_action_items)

    batched_archetypes_has_example_goals = batch_archetypes_has_example_goals(category_archetypes, goal_id_lookup)
    execute_category_archetypes_has_example_goals_seed(batched_archetypes_has_example_goals)
    # Package archetypes_has_example_goal_data - category_archetype_id, example_goal_id, goal_subcategory_id      
    return

def batch_category_archetype_data(category_archetypes, category_id_lookup):
    batched_archetypes = []

    for archetype in category_archetypes:
      category_id = category_id_lookup.get(archetype["goal_category_slug"])
      if category_id is None:
            raise KeyError(f"Unknown 'category_slug' {archetype["category_slug"]} used in category_id lookup")
    
      batched_archetypes.append(
          {
              "goal_category_id": category_id,
              "slug": archetype["slug"],
              "name": archetype["name"],
              "description": archetype["description"],
              "is_default": archetype["is_default"],
          }
      )
    return batched_archetypes

def batch_example_goal_data(category_archetypes, category_id_lookup):
    category_component_id_lookup = get_category_component_id_lookup()

    batched_goals = []
    
    for archetype in category_archetypes:
      category_id = category_id_lookup.get(archetype["goal_category_slug"])

      for goal in archetype["example_goals"]:

          category_component_id = category_component_id_lookup.get(goal["category_component_slug"])
          if category_component_id is None:
            raise KeyError(f"Unknown 'category_component_slug' {goal["category_component_slug"]} used in category_component_id lookup")
          
          batched_goals.append(
              {
                  "goal_category_id": category_id,
                  "category_component_id": category_component_id,
                  "slug": goal["slug"],
                  "name": goal["name"],
                  "description": goal["description"],
                  "goal_type": goal["goal_type"],
                  "priority": goal["priority"],
                  "estimated_time_value": goal["estimated_time_value"],
                  "estimated_time_unit": goal["estimated_time_unit"],
              }
          )

    return batched_goals

def batch_example_milestone_data(category_archetypes, category_id_lookup, goal_id_lookup):
    batched_milestones = []
    
    for archetype in category_archetypes:
      category_id = category_id_lookup.get(archetype["goal_category_slug"])

      for goal in archetype["example_goals"]:          
          goal_id = goal_id_lookup.get(goal["slug"])
          if goal_id is None:
            raise KeyError(f"Unknown 'goal_slug' {goal["slug"]} used in goal_id lookup")
          
          for milestone in goal["milestones"]:
    
              batched_milestones.append(
              {
                  "example_goal_id": goal_id,
                  "slug": milestone["slug"],
                  "name": milestone["name"],
                  "description": milestone["description"],
                  "estimated_time_value": milestone["estimated_time_value"],
                  "estimated_time_unit": milestone["estimated_time_unit"]
              }
          )

    return batched_milestones

def batch_example_action_item_data(category_archetypes, category_id_lookup, goal_id_lookup):
    milestone_id_lookup = get_milestone_id_lookup()
    
    batched_action_items = []
    
    for archetype in category_archetypes:

      for goal in archetype["example_goals"]:
          goal_id = goal_id_lookup.get(goal["slug"])
          if goal_id is None:
            raise KeyError(f"Unknown 'goal_slug' {goal["slug"]} used in goal_id lookup")
          
          for milestone in goal["milestones"]:

              milestone_id = milestone_id_lookup.get(milestone["slug"])
              if milestone_id is None:
                  raise KeyError(f"Unknown 'milestone_slug' {milestone["slug"]} used in milestone_id lookup")
              
              for action_item in milestone["action_items"]:
                  batched_action_items.append(
                  {
                      "example_milestone_id": milestone_id,
                      "example_goal_id": goal_id,
                      "slug": action_item["slug"],
                      "name": action_item["name"],
                      "description": action_item["description"],
                      "action_item_order": action_item.get("action_item_order", 1),
                      "estimated_time_value": action_item["estimated_time_value"],
                      "estimated_time_unit": action_item["estimated_time_unit"]
                  }
          )

    return batched_action_items

def batch_archetypes_has_example_goals(category_archetypes, goal_id_lookup):
    category_archetype_id_lookup = get_category_archetype_id_lookup()
    category_component_id_lookup = get_category_component_id_lookup()

    batched_archetypes_has_example_goals = []

    for archetype in category_archetypes:
        category_archetype_id = category_archetype_id_lookup.get(archetype["slug"])

        if category_archetype_id is None:
            raise KeyError(f"Unknown 'category_archetype_slug' {archetype["category_archetype_slug"]} used in category_archetype_id lookup")
   
        for goal in archetype["example_goals"]:
            example_goal_id = goal_id_lookup.get(goal["slug"])

            if example_goal_id is None:
                raise KeyError(f"Unknown 'goal_slug' {goal["goal_slug"]} used in goal_id lookup")

            category_component_id = category_component_id_lookup.get(goal["category_component_slug"])
  
  
            batched_archetypes_has_example_goals.append({
                "category_archetype_id": category_archetype_id,
                "example_goal_id": example_goal_id,
                "category_component_id": category_component_id,
                "priority": goal["priority"]
            })
    
    return batched_archetypes_has_example_goals

def execute_category_archetype_seed(batched_category_archetypes):
    query = """
      INSERT INTO category_archetypes
        (goal_category_id, slug, name, description, is_default, created_at, updated_at)
      VALUES
        (%s, %s, %s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        goal_category_id = VALUES(goal_category_id),
        name = VALUES(name),
        description = VALUES(description),
        is_default = VALUES(is_default),
        updated_at = NOW();
    """

    values = [(row["goal_category_id"], row["slug"], row["name"], row["description"], row["is_default"]) for row in batched_category_archetypes]
    
    return User.db.query_db(query, values, many=True)

def execute_category_archetypes_has_example_goals_seed(batched_category_archetypes_has_example_goals):
    query = """
      INSERT INTO category_archetypes_has_example_goals
        (category_archetype_id, example_goal_id, category_component_id, priority)
      VALUES
        (%s, %s, %s, %s)
      ON DUPLICATE KEY UPDATE
        category_component_id = VALUES(category_component_id),
        priority = VALUES(priority);
    """

    values = [(row["category_archetype_id"], row["example_goal_id"], row["category_component_id"], row["priority"]) for row in batched_category_archetypes_has_example_goals]
    
    return User.db.query_db(query, values, many=True)

def execute_example_goal_seed(batched_example_goals):
    query = """
      INSERT INTO example_goals
        (goal_category_id, category_component_id, slug, name, description, goal_type, priority, estimated_time_value, estimated_time_unit, created_at, updated_at)
      VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        category_component_id = VALUES(category_component_id),
        name = VALUES(name),
        description = VALUES(description),
        goal_type = VALUES(goal_type),
        priority = VALUES(priority),
        estimated_time_value = VALUES(estimated_time_value),
        estimated_time_unit = VALUES(estimated_time_unit),
        updated_at = NOW();
    """

    values = [(row["goal_category_id"], row["category_component_id"], row["slug"], row["name"], row["description"], row["goal_type"], row["priority"], row["estimated_time_value"], row["estimated_time_unit"]) for row in batched_example_goals]
    
    return User.db.query_db(query, values, many=True)


def execute_example_milestone_seed(batched_example_milestones):
    query = """
      INSERT INTO example_milestones
        (example_goal_id, slug, name, description, estimated_time_value, estimated_time_unit, created_at, updated_at)
      VALUES
        (%s, %s, %s, %s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        description = VALUES(description),
        estimated_time_value = VALUES(estimated_time_value),
        estimated_time_unit = VALUES(estimated_time_unit),
        updated_at = NOW();
    """

    values = [(row["example_goal_id"], row["slug"], row["name"], row["description"], row["estimated_time_value"], row["estimated_time_unit"]) for row in batched_example_milestones]
    
    return User.db.query_db(query, values, many=True)

def execute_example_action_item_seed(batched_example_action_items):
    query = """
      INSERT INTO example_action_items
        (example_goal_id, example_milestone_id, slug, name, description, action_item_order, estimated_time_value, estimated_time_unit, created_at, updated_at)
      VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        description = VALUES(description),
        action_item_order = VALUES(action_item_order),
        estimated_time_value = VALUES(estimated_time_value),
        estimated_time_unit = VALUES(estimated_time_unit),
        updated_at = NOW();
    """

    values = [(row["example_goal_id"], row["example_milestone_id"],  row["slug"], row["name"], row["description"], row["action_item_order"], row["estimated_time_value"], row["estimated_time_unit"]) for row in batched_example_action_items]
    
    return User.db.query_db(query, values, many=True)

def get_goal_category_id_lookup():
    query = "SELECT id, slug FROM goal_categories;"

    # Fetch all category ids and names
    results = User.db.query_db(query)

    if not results:  # Handle case where no results are found
        return {}
    # Create a dictionary mapping category names to their IDs
    category_ids = {row["slug"]: row["id"] for row in results}

    return category_ids

def get_category_component_id_lookup():
    query = "SELECT id, slug FROM category_components;"

    results = User.db.query_db(query)

    if not results:
        return {}
    
    category_component_ids = {row["slug"]: row["id"] for row in results}

    return category_component_ids

def get_example_goal_id_lookup():
    query = "SELECT id, slug FROM example_goals;"

    results = User.db.query_db(query)

    if not results:
        return {}
    
    goal_ids = {row["slug"]: row["id"] for row in results}

    return goal_ids

def get_milestone_id_lookup():
    query = "SELECT id, slug FROM example_milestones;"

    results = User.db.query_db(query)

    if not results:
        return {}
    
    goal_ids = {row["slug"]: row["id"] for row in results}

    return goal_ids

def get_category_archetype_id_lookup():
    query = "SELECT id, slug FROM category_archetypes;"

    results = User.db.query_db(query)

    if not results:
        return {}
    
    goal_ids = {row["slug"]: row["id"] for row in results}

    return goal_ids
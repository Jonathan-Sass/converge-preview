from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import redirect
import re

from flask_app.models.user import User
from database.seed_data.goal_subcategory_data import goal_subcategory_data

def goal_seed():
  user = User.get_logged_in_user()
  if not user:
      return redirect("/")
  
  goal_category_seed()
  # goal_subcategory_seed()




def goal_category_seed():
    query = """
    INSERT INTO goal_categories (category_slug, name, created_at, updated_at)
    VALUES
      ('health-wellness', 'Health and Wellness', NOW(), NOW()),
      ('social-community', 'Social and Community Engagement', NOW(), NOW()),
      ('recreation-travel', 'Recreation and Travel', NOW(), NOW()),
      ('spirituality-life-purpose', 'Spirituality and Life Purpose', NOW(), NOW()),
      ('career-professional-development', 'Career and Professional Development', NOW(), NOW()),
      ('creative-expression-hobbies', 'Creative Expression and Hobbies', NOW(), NOW()),
      ('wealth-finance', 'Wealth Building and Financial Health', NOW(), NOW()),
      ('environment-success', 'Environment and Success', NOW(), NOW())
    ON DUPLICATE KEY UPDATE updated_at = NOW();
      """
    User.db.query_db(query)

    return

def goal_subcategory_seed():
    batch_data = {}

    # Organize subcategories into batches by category (key)
    for category_slug, subcategories in goal_subcategory_data.items():
        for subcategory in subcategories:
            if category_slug not in batch_data:
                batch_data[category_slug] = []
            batch_data[category_slug].append(
                {"subcategory_slug": subcategory["subcategory_slug"], "subcategory_name": subcategory["name"]}
            )

    # Retrieve the mapping of category slugs to category IDs
    category_ids = (
        get_all_goal_category_ids()
    )  # Should return a dictionary like {'health-wellness': 1, 'social-community': 2, ...}

    # Prepare and execute batch insert queries for each category
    for category_slug, subcategory_batch in batch_data.items():
        # Check if the category slug exists in the retrieved category IDs
        if category_slug in category_ids:
            category_id = category_ids[category_slug]
        else:
            print(f"Category slug '{category_slug}' not found in the database.")
            continue  # Skip this category if the ID is not found

        # Create the base query
        query = "INSERT INTO goal_subcategories (category_id, subcategory_slug, name, created_at, updated_at) VALUES "
        query_values = []

        # Temporary secondary seed to subcategories, merge pending

        # Add the subcategory values to the query
        for subcategory in subcategory_batch:
            values = f"({category_id}, '{subcategory['subcategory_slug']}', '{subcategory['subcategory_name']}', NOW(), NOW())"
            query_values.append(values)

        # Combine the query and execute it
        query += ", ".join(query_values)
        query += " ON DUPLICATE KEY UPDATE updated_at = NOW();"

        # Execute the query using your database method
        User.db.query_db(query)

    return

def get_all_goal_category_ids():
    query = "SELECT id, category_slug FROM goal_categories"

    # Fetch all category ids and names
    results = User.db.query_db(query)

    if not results:  # Handle case where no results are found
        return {}
    # Create a dictionary mapping category names to their IDs
    category_ids = {row["category_slug"]: row["id"] for row in results}

    return category_ids
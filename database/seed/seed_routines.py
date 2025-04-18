from flask_app.config.mysqlconnection import connectToMySQL

from database.seed_data.routine_data import routine_blocks
import pymysql
from pprint import pprint

db = connectToMySQL("converge_schema")

def seed_routine_data():

  # seed_routine_templates()

  seed_routine_blocks()
  return

def seed_routine_blocks():
    query = """
      INSERT INTO routine_blocks
        (name, slug, description, tier_level, created_at, updated_at)
      VALUES 
        (%s, %s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        description = VALUES(description),
        tier_level = VALUES(tier_level),
        updated_at = NOW();
    """

    params = [(rb["name"], rb["slug"], rb["description"], rb["tier_level"]) for rb in routine_blocks]
    
    try:
      db.query_db(query, params, many=True)
    except Exception as e:
       print(f"Seeding routine blocks failed: {e}")
    else:
       print("Seeded routine blocks.")
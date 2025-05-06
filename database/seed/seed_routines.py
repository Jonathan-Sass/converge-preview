from flask_app.config.mysqlconnection import connectToMySQL
import pymysql
from pprint import pprint

from database.seed_data.routine_data import routine_blocks
from database.seed.seed_routine_template import seed_routine_block_templates

db = connectToMySQL("converge_schema")

def seed_routine_data():

  seed_routine_blocks()
  seed_routine_block_templates()
  return

def seed_routine_blocks():
    query = """
      INSERT INTO routine_blocks
        (name, slug, description, type, created_at, updated_at)
      VALUES 
        (%s, %s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        slug = slug,
        description = VALUES(description),
        type = VALUES(type),
        updated_at = NOW();
    """

    params = [(rb["name"], rb["slug"], rb["description"], rb["type"]) for rb in routine_blocks]
    
    try:
      db.query_db(query, params, many=True)
    except Exception as e:
       print(f"Seeding routine blocks failed: {e}")
    else:
       print("Seeded routine blocks.")
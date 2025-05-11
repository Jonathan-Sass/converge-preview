from flask_app.config.mysqlconnection import connectToMySQL
from typing import List

from flask_app.models.practice import Practice

class RoutineBlock:
  """Model representing a Routine Block, an organization structure for Routines."""

  db = connectToMySQL("converge_schema")

  def __init__(self, data):
    """Initialize a Routine Block object"""
    self.id = data["id"],
    self.slug = data["slug"],
    self.name = data["name"],
    self.description = data["description"],
    self.icon_slug =  data["icon_slug"],
    self.created_at = data["created_at"],
    self.updated_at = data["updated_at"],
    self.practices: List[Practice] = []


  def build_routine_block_from_row(row):
    return RoutineBlock(
      {
        "id": row["routine_block_id"],
        "slug": row["routine_block_slug"],
        "name": row["routine_block_name"],
        "description": row["routine_block_description"],
        "icon_slug": row.get("routine_block_icon_slug", None),
        "created_at": row["routine_block_created_at"],
        "updated_at": row["routine_block_updated_at"]
      }
    )
  
  def find_routine_blocks_by_user_id(user_id):
    """
    Retrieve all routines for a given user and their associated practices.

    Args:
        user_id (int): The user's ID.

    Returns:
        list: List of Routine instances.
    """
    query = """
        SELECT 
          ur.id AS routine_id,
          ur.name AS routine_name,
          ur.description AS routine_description,
          ur.routine_type,
          ur.start_time,
          ur.end_time,
          ur.is_active,
          ur.notes AS routine_notes,
          ur.created_at AS routine_created_at,
          ur.updated_at AS routine_updated_at,
          urbp.routine_block_id AS user_routine_block_practice_routine_block_id,
          urbp.position,
          rb.id AS routine_block_id,
          rb.name AS routine_block_name,
          rb.slug AS routine_block_slug,
          rb.description AS routine_block_description,
          rb.created_at AS routine_block_created_at,
          rb.updated_at AS routine_block_updated_at,
          p.id AS practice_id,
          p.name AS practice_name,
          p.description AS practice_description,
          p.benefit_synopsis,
          p.is_common AS practice_is_common,
          p.notes AS practice_notes,
          p.literature_summary,
          p.created_at AS practice_created_at,
          p.updated_at AS practice_updated_at,
          pc.name AS practice_category,
          d.duration_label AS selected_duration,
          ir.impact_rating_description,
          dl.difficulty_label AS practice_difficulty
        FROM
          user_routines ur
        LEFT JOIN 
          user_routine_block_practices urbp ON ur.id = urbp.routine_block_id
        LEFT JOIN
          routine_blocks rb ON urbp.routine_block_id = rb.id
        LEFT JOIN 
          practices p ON urbp.practice_id = p.id
        LEFT JOIN
          practice_categories pc ON p.practice_category_id = pc.id
        LEFT JOIN
          durations d ON urbp.duration_id = d.id
        LEFT JOIN
          impact_ratings ir ON p.impact_rating_id = ir.id
        LEFT JOIN
          difficulty_levels dl ON p.difficulty_level_id = dl.id
        WHERE
          ur.user_id = %(user_id)s;
    """

    data = {"user_id": user_id}

    results = RoutineBlock.db.query_db(query, data)

    if results:
        return RoutineBlock.build_complete_user_routine_blocks(results, user_id)

  def build_complete_routine_blocks():
     return

  def save_user_routine_block_from_template(user, block_template_slug):
      """
        
      """
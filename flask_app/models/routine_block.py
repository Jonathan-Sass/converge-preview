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
  
  
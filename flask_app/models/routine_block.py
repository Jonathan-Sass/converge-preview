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
    self.tier_level = data["tier_level"],
    self.icon_slug =  data.get("icon_slug", None)
    self.created_at = data["created_at"],
    self.updated_at = data["updated_at"],
    self.practices: List[Practice] = []


  def build_routine_block_from_row(row):
    RoutineBlock(
      {
        "id": row["id"],
        "slug": row["slug"],
        "name": row["name"],
        "description": row["description"],
        "tier_level": row["tier_level"],
        "icon_slug": row.get("icon_slug", None),
        "created_at": row["created_at"],
        "updated_at": row["updated_at"]
      }
    )
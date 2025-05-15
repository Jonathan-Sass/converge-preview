from flask_app.config.mysqlconnection import connectToMySQL


class CategoryComponent:
  """
  
  """
  db = connectToMySQL("converge_schema")

  def __init__ (self, data):
    ""
    self.id = data["category_component_id"]
    self.goal_category_id = data["goal_category_id"]
    self.slug = data["category_component_slug"]
    self.name = data["category_component_name"]
    self.description = data["category_component_description"], None
    self.role = data["category_component_role"]
    self.created_at = data["category_component_created_at"]
    self.updated_at = data["category_component_updated_at"]
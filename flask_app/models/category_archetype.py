from flask_app.config.mysqlconnection import connectToMySQL


class CategoryArchetype:
  db = connectToMySQL("converge_schema")

  def __init__(self, data):
    """Initiate a CategoryArchetype object from database row data"""

    self.id = data["id"]
    self.goal_category_id = data["goal_category_id"]
    self.slug = data["slug"]
    self.name = data["survey_name"]
    self.description = data["question_description"]
    self.is_default = data["is_default"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]
    self.example_goals = []

from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.user import User
from flask_app.models.milestone import Milestone
from flask_app.models.action_item import ActionItem
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory


class Goal:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = (data["id"],)
        self.category_id = (data["category_id"],)
        self.subcategory_id = (data["subcategory_id"],)
        self.name = (data["name"],)
        self.description = (data["description"],)
        self.goal_type = (data["goal_type"],)
        self.projected_completion = (data["projected_completion"],)
        self.is_complete = (data["is_complete"],)
        self.priority = (data["priority"],)
        self.created_at = (data["created_at"],)
        self.updated_at = (data["updated_at"],)

    def process_and_save_subcategory_goals_data(subcategory_goal_data):
      user_id = User.get_logged_in_user()
      subcategory_id = Subcategory

      goal_data = []

      for goal in subcategory_goal_data:
        user_id: 
      
      
      Goal.save_goals(goal_data)
      milestone_data = []
      Milestone.save_milestones(milestone_data)
      action_item_data = []
      ActionItem.save_action_item(action_item_data)

    def save_subcategory_goals(data):
            query = """
      INSERT INTO
        goals (id, user_id, category_id, subcategory_id, name, description, goal_type, projected_completion, is_complete, priority, created_at, updated_at)
      VALUES 
        (%(id)s, %(user_id)s, %(category_id)s, %(subcategory_id)s, %(name)s, %(description)s, %(goal_type)s, %(projected_completion)s, %(is_complete)s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        updated_at = NOW();
    """

            result = Goal.db.query_db(query, data)


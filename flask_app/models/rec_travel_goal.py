from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.user import User


class Goal:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = (data["id"],)
        self.category_id = (data["category_id"],)
        self.subcategory_id = (data["subcategory_id"],)
        self.column = (data["column"],)

        self.name = (data["name"],)
        self.description = (data["description"],)
        self.goal_type = (data["goal_type"],)
        self.projected_completion = (data["projected_completion"],)
        self.is_complete = (data["is_complete"],)
        self.priority = (data["priority"],)
        self.created_at = (data["created_at"],)
        self.updated_at = (data["updated_at"],)

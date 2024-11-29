from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from flask_app.models.user import User

class Practice:
    db = connectToMySQL('converge_schema')

    def __init__ (self, data):
        self.id = data["id"]
        self.practice_category_id = data["practice_category_id"]
        self.impact_rating_id = data["impact_rating_id"]
        self.difficulty_id = data["difficulty_id"]
        self.frequency_id = data["frequency_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.is_common = data["is_common"]
        self.notes = data["notes"]
        self.literature_summary = data["literature_summary"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]




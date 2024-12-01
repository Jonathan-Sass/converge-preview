from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from flask_app.models.user import User

class PersonalRoutine:
    db = connectToMySQL("converge_schema")

    def __init__ (self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.routine_type = data["routine_type"]
        self.start_time = data["start_time"]
        self.end_time = data["end_time"]
        self.is_active = data["is_active"]
        self.notes = data["notes"] or None
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.practices = []


    def fetch_personal_routines():
        query = """
            SELECT 
        """



    # def save_personal_routine():

    # def update_personal_routine():

    # def delete_personal_routine()
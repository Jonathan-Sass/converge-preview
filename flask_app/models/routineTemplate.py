from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, jsonify, redirect
from flask_app.models.practice import Practice

class RoutineTemplate:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.frequency_id = data["frequency_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.category = data["category"]
        self.notes = data["notes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
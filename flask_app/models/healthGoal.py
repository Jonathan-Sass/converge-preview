from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session
from flask_app.models import user
from flask_app.models import userHealthGoal
from flask_app.models.timeDomain import TimeDomain

class HealthGoal: 
    _db = "dreamweaver_schema"

    def __init__ (self, data):
        self.id = data['id']
        self.category = data["category"]
        self.name = data["name"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.time_domains = None

    @classmethod
    def find_by_id(cls, health_goal_id):
        query = "SELECT * FROM health_goals WHERE id = %(id)s;"

        data = {"id": health_goal_id}

        results = connectToMySQL(HealthGoal._db).query_db(query, data)

        health_goal = HealthGoal(results[0])

        return health_goal

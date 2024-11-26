from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash
from flask_app.models import userHealthGoal

class TimeDomain: 
    _db = "converge_schema"

    def __init__ (self, data):
        self.id = data['id']
        self.action_item = data["action_item"]
        self.time_domain_10_year = data["time_domain_10_year"]
        self.time_domain_5_year = data["time_domain_5_year"]
        self.time_domain_3_year = data["time_domain_3_year"]
        self.time_domain_2_year = data["time_domain_2_year"]
        self.time_domain_1_year = data["time_domain_1_year"]
        self.time_domain_6_month = data["time_domain_6_month"]
        self.time_domain_3_month = data["time_domain_3_month"]
        self.time_domain_1_month = data["time_domain_1_month"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# This is a classmethod to Create a database entry.
    @classmethod
    def create_time_domain(cls):
        query = """
            INSERT INTO time_domains
            (action_item, time_domain_10_year, time_domain_5_year, time_domain_3_year, time_domain_2_year, time_domain_1_year, time_domain_6_month, time_domain_3_month, time_domain_1_month, created_at, updated_at)
            VALUES (" ", " ", " ", " ", " ", " ", " ", " ", " ", NOW(), NOW());
                """

        return connectToMySQL(TimeDomain._db).query_db(query)
  
    @classmethod
    def update_time_domain(cls, form_data):
        query = """
                UPDATE time_domains SET 
                action_item = %(action_item)s, 
                time_domain_5_year = %(time_domain_5_year)s, 
                time_domain_3_year = %(time_domain_3_year)s, 
                time_domain_2_year = %(time_domain_2_year)s, 
                time_domain_1_year = %(time_domain_1_year)s, 
                time_domain_6_month = %(time_domain_6_month)s, 
                time_domain_3_month = %(time_domain_3_month)s, 
                time_domain_1_month = %(time_domain_1_month)s
                WHERE id = %(id)s;
                """
        
        data = {
            "id": form_data["time_domain_id"],
            "action_item": form_data["action_item"], 
            "time_domain_5_year": form_data["time_domain_5_year"], 
            "time_domain_3_year": form_data["time_domain_3_year"], 
            "time_domain_2_year": form_data["time_domain_2_year"], 
            "time_domain_1_year": form_data["time_domain_1_year"], 
            "time_domain_6_month": form_data["time_domain_6_month"], 
            "time_domain_3_month": form_data["time_domain_3_month"], 
            "time_domain_1_month": form_data["time_domain_1_month"]

        }

        connectToMySQL(TimeDomain._db).query_db(query, data)
        return
    
    @classmethod
    def find_by_id(cls, time_domain_id):
        """Find a time_domain by its ID"""
        
        query = "SELECT * FROM time_domains WHERE id = %(id)s;"
        data = {"id": time_domain_id}
        result = connectToMySQL(TimeDomain._db).query_db(query, data)
        
        if len(result) == 0:
            return None
        time_domain = TimeDomain(result[0])
        return time_domain

    @classmethod
    def find_by_user_and_goal_id(user_id, health_goal_id):
        query = """
                SELECT *
                FROM users_health_goals_has_time_domains
                JOIN time_domains
                ON users_health_goals_has_time_domains.time_domain_id = time_domains.id
                WHERE user_id = %(user_id)s
                AND goal_id = %(health_goal_id)s;
                """

        data= {
            "user_id": user_id, 
            "health_goal_id": health_goal_id
        }

        results = connectToMySQL(TimeDomain._db).query_db(query, data)

        time_domain = results[0]
        time_domain_id = time_domain[id]

        return time_domain_id

    
    @classmethod
    def delete_time_domain(cls, time_domain_id):
        query = "DELETE FROM time_domains WHERE id = %(id)s;"
        data = {"id": time_domain_id}
        connectToMySQL(TimeDomain._db).query_db(query, data)
        return

from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session
from flask_app.models import timeDomain

class UserHealthGoal: 
    _db = "converge_schema"

    def __init__ (self, data):
        self.user_id = data['user_id']
        self.health_goal_id = data["health_goal_id"]
        self.time_domain_id = data["time_domain_id"]
        self.details = data["details"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.time_domains = None
        self.health_goal = None

# NOT FINISHED, STILL NEEDS WORK
  
    @classmethod
    def create_health_goals(cls, form_data):
        query = """
            INSERT INTO users_health_goals_has_time_domains
         (user_id, health_goal_id, details, time_domain_id, created_at, updated_at)
            VALUES (%(user_id)s, %(health_goal_id)s, %(details)s, %(time_domain_id)s, NOW(), NOW());
                """

        user_id = session["user_id"]
        for goal_selection in form_data:
            health_goal_id = int(form_data[goal_selection])

            existing_check_results = UserHealthGoal.check_for_existing(user_id, health_goal_id)
            print("****existing check***********")
            print(existing_check_results)
            print("***********")

            if existing_check_results == False:
                time_domain_id = timeDomain.TimeDomain.create_time_domain()
                print("******time_domain_id*****")
                print(time_domain_id)

                goal = {
                    "user_id": user_id, 
                    "health_goal_id": health_goal_id, 
                    "time_domain_id": time_domain_id,
                    "details": " "
                }
                connectToMySQL(UserHealthGoal._db).query_db(query, goal)

        return

    @classmethod
    def check_for_existing(cls, user_id, health_goal_id):
        query = """
                SELECT * FROM users_health_goals_has_time_domains
                WHERE user_id = %(user_id)s
                AND health_goal_id = %(health_goal_id)s;
                """
        
        goal_data = {
            "user_id": user_id, 
            "health_goal_id": health_goal_id
        }

        results = connectToMySQL(UserHealthGoal._db).query_db(query, goal_data)
        print("******results check*****")
        print(results)
        print("*************")
        if len(results) > 0:
            return True
        else: 
            return False

    @classmethod
    def find_one_user_health_goal_with_time_domains(cls, health_health_goal_id):
        
        user_id = session["user_id"]
        user_health_goal = UserHealthGoal.find_by_user_id_and_health_goal_id(user_id, health_health_goal_id)
        time_domain_id = user_health_goal.time_domain_id

        time_domain = timeDomain.TimeDomain.find_by_id(time_domain_id)
        health_goal = healthGoalDeprecated.HealthGoal.find_by_id(user_health_goal.health_goal_id)
        
        user_health_goal.time_domains = time_domain
        user_health_goal.health_goal = health_goal

        return user_health_goal
  
    @classmethod
    def find_by_user_id_and_health_goal_id(cls, user_id, health_health_goal_id):
        """Find a goal by user_id and health_goal_id"""
        
        query = """
                SELECT * 
                FROM users_health_goals_has_time_domains
                WHERE health_goal_id = %(health_goal_id)s
                AND user_id = %(user_id)s;
                """
        
        data = {
            "user_id": user_id, 
            "health_goal_id": health_health_goal_id
                }
        results = connectToMySQL(UserHealthGoal._db).query_db(query, data)
       
        if len(results) == 0:
            return None
        user_health_goal = UserHealthGoal(results[0])
        
        return user_health_goal
    
    @classmethod
    def update_user_health_goals(cls, form_data):
        # user_id = session["user_id"]
        
        timeDomain.TimeDomain.update_time_domain(form_data)

        # user_health_goal = UserHealthGoal.find_by_user_id_and_time_domain_id(user_id, time_domain_id)
        # UserHealthGoal.update_user_health_goals(user_health_goal)

        return

    @classmethod
    def find_by_user_id_and_time_domain_id(cls, user_id, time_domain_id):
        query = """
                SELECT * 
                FROM users_health_goals_has_time_domains
                WHERE user_id = %(user_id)s
                AND time_domain_id = %(time_domain_id)s;
                """
        
        data = {
            "user_id": user_id, 
            "time_domain_id": time_domain_id
        }

        results = connectToMySQL(UserHealthGoal._db).query_db(query, data)
        user_health_goal = UserHealthGoal(results[0])

        return user_health_goal
    
    @classmethod
    def find_all_user_health_goals_with_time_domains(cls, user_id):
        query = """
                SELECT * FROM users
                LEFT JOIN users_health_goals_has_time_domains ON users_health_goals_has_time_domains.user_id = user_id
                JOIN time_domains ON users_health_goals_has_time_domains.time_domain_id = time_domains.id
                WHERE user_id = %(user_id)s;
                """
        data = {"user_id": user_id}
        results = connectToMySQL(UserHealthGoal._db).query_db(query, data)
        
        for result in results:
            health_goal = UserHealthGoal.find_by_id(result["health_goal_id"])

    
    @classmethod
    def delete_user_health_goal_and_time_domain(cls, health_health_goal_id):
        query = """
                DELETE FROM users_health_goals_has_time_domains
                WHERE health_goal_id = %(health_goal_id)s
                AND user_id = %(user_id)s;
                """
        
        user_id = session["user_id"]
        user_health_goal = UserHealthGoal.find_by_user_id_and_health_goal_id(user_id, health_health_goal_id)
        time_domain_id = user_health_goal.time_domain_id

        data = {
            "user_id": user_id, 
            "health_goal_id": health_health_goal_id
            }

        connectToMySQL(UserHealthGoal._db).query_db(query, data)
        timeDomain.TimeDomain.delete_time_domain(time_domain_id)
        return


from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session
import re

from flask_app.models.healthGoal import HealthGoal
from flask_app.models.userHealthGoal import UserHealthGoal
from flask_app.models.userResponse import UserResponse


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PASSWORD_REGEX = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')

class User: 
    db = connectToMySQL("converge_schema")

    def __init__ (self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.health_quiz_id = data["health_quiz_id"]
        self.responses = []
        self.health_goals = []
        self.user_health_goals = []
        self.personal_routines = []
        self.day_flex_items = []
    
    
    @classmethod
    def find_all(cls):
        query = "SELECT * FROM users"
        users = User.db.query_db(query)
        return users

    @classmethod
    def find_by_email(cls, form_data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {"email": form_data["email"]}
        result = User.db.query_db(query, data)
        
        if len(result) == 0:
            return None
        return User(result[0])
    
    @classmethod
    def get_logged_in_user(cls):
        user_id = session.get("user_id")
        if not user_id:
            flash("Please log in.", "login")
            return None
        
        user = User.find_by_id(user_id)
        if not user:
            flash("Invalid user. Please log in again.", "login")
            return None
        
        return user

    @classmethod
    def find_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        result = User.db.query_db(query, data)
        if len(result) == 0:
            return None
        user = User(result[0])
        return user
    
    # WILL LIKELY NEED TWEAKING DEPENDING ON USER ATTRIBUTES
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users
                (first_name, last_name, email, password, created_at, updated_at)
                VALUES
                (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
                """
        return User.db.query_db(query, data)

    # METHODS FOR USER RESPONSES
    def fetch_user_responses_by_survey_topic_slug(self, survey_topic_slug_string):
        query = """
            SELECT 
                user_responses.user_id,
                survey_topics.topic_slug,
                user_responses.survey_question_id,
                survey_questions.question_text AS survey_question_text,
                user_responses.survey_answer_id,
                survey_answers.answer_text AS survey_answer_text,
                survey_answers.answer_value AS survey_answer_value
            FROM
                user_responses
            JOIN
                survey_questions ON user_responses.survey_question_id = survey_questions.id
            JOIN
                survey_answers ON user_responses.survey_answer_id = survey_answers.id
            JOIN
                survey_topics ON survey_questions.survey_topic_id = survey_topics.id
            WHERE
                user_responses.user_id = %(user_id)s
            AND
                survey_topics.topic_slug = %(survey_topic_slug)s
            ORDER BY
                user_responses.survey_question_id;
        """

        data = {
            "user_id": self.id,
            "survey_topic_slug": survey_topic_slug_string
        }

        results = User.db.query_db(query, data)

        # user_responses = []
        if results:
            for result in results:
                self.responses.append(UserResponse(result))
                print("*****user_response result*****")
                pprint(result)
        else:
            print(f"No responses found for user: {self.id} and survey_topic: {survey_topic_slug_string}")
        
        return self

    @staticmethod
    def validate_registration(user):
        is_valid = True
        if len(user["first_name"].strip()) == 0 or len(user["first_name"].strip()) < 2:
            flash("Please enter your first name.", "registration")
            is_valid = False
        elif not str.isalpha(user["first_name"]):
            flash("Your first name may only contain alphanumeric characters.")
            is_valid = False

        if len(user["last_name"].strip()) == 0 or len(user["last_name"].strip()) < 2:
            flash("Please enter your last name.", "registration")
            is_valid = False
        elif not str.isalpha(user["last_name"]):
            flash("Your last name may only contain alphanumeric characters.", "registration")
            is_valid = False

        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address!", "registration")
            is_valid = False

        if "password" not in user:
            flash("Please enter a password", "registration")
            is_valid = False
        elif len(user["password"].strip()) < 8:
            flash("Your password must contain at least 8 characters.", "registration")
            is_valid = False

        if not PASSWORD_REGEX.match(user["password"].strip()):
            flash("Your password must contain at least 1 capital letter, 1 number and 1 special character.", "registration")
            is_valid = False
        elif not user["password"] == user["confirm_password"]:
            flash("Your passwords must match.", "registration")
            is_valid = False
            
        return is_valid
    
    @staticmethod
    def login_is_valid(form_data):
        is_valid = True

        if len(form_data["email"].strip()) == 0:
            flash("Please enter your email address.", "login")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data["email"]):
            flash("Please enter a valid email address.", "login")
            is_valid = False

        if len(form_data["password"].strip()) == 0:
            flash("Please enter a password.")
            is_valid = False
        elif len(form_data["password"].strip()) < 8:
            flash("Your password must contain at least 8 characters.")
            is_valid = False

        return is_valid

    

    @classmethod
    def find_by_id_with_health_goals(cls, user_id):
        query = """
                SELECT * FROM health_goals
                JOIN  users_health_goals_has_time_domains ON users_health_goals_has_time_domains.health_goal_id = health_goals.id
                JOIN users ON users_health_goals_has_time_domains.user_id = users.id
                WHERE users.id = %(id)s;
                """

        data = {"id": user_id}
        results = User.db.query_db(query, data)
        if len(results) == 0:
            return None
        user = User(User.find_by_id(session["user_id"]))

        for result in results:
            health_goal_data = {
                "id": result["id"], 
                "category": result["category"], 
                "name": result["name"], 
                "details": result["details"],
                "created_at": result["users_health_goals_has_time_domains.created_at"], 
                "updated_at": result["users_health_goals_has_time_domains.updated_at"]
            }
            user.health_goals.append(health_goal_data)

        print("**********************")
        print(user.health_goals)
        print("**********************")
        # print(user.health_goals[name])

        return user
    
    @classmethod
    def find_all_user_health_goals_with_time_domains(cls, user_id):
        query = """
                SELECT * 
                FROM users
                JOIN users_health_goals_has_time_domains 
                ON users_health_goals_has_time_domains.user_id = users.id
                JOIN time_domains 
                ON users_health_goals_has_time_domains.time_domain_id = time_domains.id
                JOIN health_goals
                ON users_health_goals_has_time_domains.health_goal_id = health_goals.id
                WHERE users.id = %(user_id)s;
                """
        data = {"user_id": user_id}
        results = User.db.query_db(query, data)
        print("*****users health goals with time domains results*****")
        for result in results:
            pprint(result)
            print("")
        print("**************************")
        
        user = User.find_by_id(user_id)
        for result in results:
            health_goal_data = {
                "id": result["health_goals.id"], 
                "category": result["category"], 
                "name": result["name"], 
                "created_at": result["health_goals.created_at"], 
                "updated_at": result["health_goals.updated_at"], 
            }
            health_goal = HealthGoal(health_goal_data)
            time_domain_data = {
                "id": result["time_domains.id"], 
                "action_item": result["action_item"], 
                "time_domain_10_year": result["time_domain_10_year"], 
                "time_domain_5_year": result["time_domain_5_year"], 
                "time_domain_3_year": result["time_domain_3_year"], 
                "time_domain_2_year": result["time_domain_2_year"], 
                "time_domain_1_year": result["time_domain_1_year"], 
                "time_domain_6_month": result["time_domain_6_month"], 
                "time_domain_3_month": result["time_domain_3_month"], 
                "time_domain_1_month": result["time_domain_1_month"], 
                "created_at": result["time_domains.created_at"], 
                "updated_at": result["time_domains.updated_at"]
            }
            health_goal.time_domains = time_domain_data
            user.health_goals.append(health_goal)
            print("*********USER HEALTH GOALS*******")
            pprint(user.health_goals)
            print("**************")
        return user
    
    @classmethod
    def save_health_quiz_id(cls):
        data = {
            "user_id": session["user_id"], 
            "health_quiz_id": session["health_quiz_id"]
        }

        query = "UPDATE users SET health_quiz_id = %(health_quiz_id)s WHERE id = %(user_id)s"
        print("******HEALTH QUIZ ID SAVING...*****")
        return User.db.query_db(query, data)
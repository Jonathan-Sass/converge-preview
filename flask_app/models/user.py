from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session
import re

# Regular expressions for validating email and password formats
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASSWORD_REGEX = re.compile(
    r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
)


class User:
    """Represents a user in the Converge application."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """Initialize a User instance from a dictionary of user data."""
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.responses = []
        self.goals = []
        self.personal_routines = []
        self.day_flex_items = []

    @classmethod
    def get_logged_in_user(cls):
        """
        Retrieve the logged-in user from the session.

        Returns:
            User or None: The logged-in User object, or None if not found.
        """
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
        """
        Find a user by their ID.

        Args:
            user_id (int): The user's ID.

        Returns:
            User or None: User instance if found, else None.
        """
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        result = User.db.query_db(query, data)
        if len(result) == 0:
            return None
        return User(result[0])

    @classmethod
    def find_all(cls):
        """
        Retrieve all users from the database.

        Returns:
            list[dict]: List of user records.
        """
        query = "SELECT * FROM users"
        return User.db.query_db(query)

    @classmethod
    def find_by_email(cls, form_data):
        """
        Find a user by their email address.

        Args:
            form_data (dict): Form data containing 'email'.

        Returns:
            User or None: User instance if found, else None.
        """
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {"email": form_data["email"]}
        result = User.db.query_db(query, data)

        if len(result) == 0:
            return None
        return User(result[0])

    @classmethod
    def save(cls, data):
        """
        Save a new user to the database.

        Args:
            data (dict): User data to insert.

        Returns:
            int: The ID of the inserted user.
        """
        query = """
            INSERT INTO users
            (first_name, last_name, email, password, created_at, updated_at)
            VALUES
            (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
        """
        return User.db.query_db(query, data)

    # ---------------- LOGIN/REGISTRATION METHODS ---------------- #

    @staticmethod
    def validate_registration(user):
        """
        Validate user registration input.

        Args:
            user (dict): Form input data.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        is_valid = True

        if len(user["first_name"].strip()) < 2:
            flash("Please enter your first name.", "first_name")
            is_valid = False
        elif not str.isalpha(user["first_name"]):
            flash("Your first name may only contain letters.", "first_name")
            is_valid = False

        if len(user["last_name"].strip()) < 2:
            flash("Please enter your last name.", "last_name")
            is_valid = False
        elif not str.isalpha(user["last_name"]):
            flash("Your last name may only contain letters.", "last_name")
            is_valid = False

        if not EMAIL_REGEX.match(user["email"]):
            flash("Please enter a valid email address.", "email")
            is_valid = False

        if "password" not in user or len(user["password"].strip()) < 8:
            flash("Your password must contain at least 8 characters.", "password")
            is_valid = False
        elif not PASSWORD_REGEX.match(user["password"].strip()):
            flash(
                "Your password must contain at least 1 capital letter, 1 number and 1 special character.",
                "password",
            )
            is_valid = False
        elif user["password"] != user["confirm_password"]:
            flash("Your passwords must match.", "confirm_password")
            is_valid = False

        return is_valid

    @staticmethod
    def login_is_valid(form_data):
        """
        Validate login form input.

        Args:
            form_data (dict): Contains 'email' and 'password'.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        is_valid = True

        if len(form_data["email"].strip()) == 0:
            flash("Please enter your email address.", "login")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data["email"]):
            flash("Please enter a valid email address.", "login")
            is_valid = False

        if len(form_data["password"].strip()) == 0:
            flash("Please enter a password.", "login")
            is_valid = False
        elif len(form_data["password"].strip()) < 8:
            flash("Your password must contain at least 8 characters.", "login")
            is_valid = False

        return is_valid



    # ---------------- DEPRECATED METHODS ---------------- #
    # Health goal and quiz methods were used in early prototypes and may be removed.
    # They are retained here for review/stability verification before permanent deletion.



# ALL HEALTH GOAL AND HEALTH QUIZ METHODS ARE DEPRECATED, VERIFYING STABILITY BEFORE REMOVAL
    # @classmethod
    # def find_by_id_with_health_goals(cls, user_id):
    #     query = """
    #             SELECT * FROM health_goals
    #             JOIN  users_health_goals_has_time_domains ON users_health_goals_has_time_domains.health_goal_id = health_goals.id
    #             JOIN users ON users_health_goals_has_time_domains.user_id = users.id
    #             WHERE users.id = %(id)s;
    #             """

    #     data = {"id": user_id}
    #     results = User.db.query_db(query, data)
    #     if len(results) == 0:
    #         return None
    #     user = User(User.find_by_id(session["user_id"]))

    #     for result in results:
    #         health_goal_data = {
    #             "id": result["id"],
    #             "category": result["category"],
    #             "name": result["name"],
    #             "details": result["details"],
    #             "created_at": result["users_health_goals_has_time_domains.created_at"],
    #             "updated_at": result["users_health_goals_has_time_domains.updated_at"],
    #         }
    #         user.health_goals.append(health_goal_data)

    #     print("**********************")
    #     print(user.health_goals)
    #     print("**********************")
    #     # print(user.health_goals[name])

    #     return user

    # @classmethod
    # def find_all_user_health_goals_with_time_domains(cls, user_id):
    #     query = """
    #             SELECT * 
    #             FROM users
    #             JOIN users_health_goals_has_time_domains 
    #             ON users_health_goals_has_time_domains.user_id = users.id
    #             JOIN time_domains 
    #             ON users_health_goals_has_time_domains.time_domain_id = time_domains.id
    #             JOIN health_goals
    #             ON users_health_goals_has_time_domains.health_goal_id = health_goals.id
    #             WHERE users.id = %(user_id)s;
    #             """
    #     data = {"user_id": user_id}
    #     results = User.db.query_db(query, data)
    #     print("*****users health goals with time domains results*****")
    #     for result in results:
    #         pprint(result)
    #         print("")
    #     print("**************************")

    #     user = User.find_by_id(user_id)
    #     for result in results:
    #         health_goal_data = {
    #             "id": result["health_goals.id"],
    #             "category": result["category"],
    #             "name": result["name"],
    #             "created_at": result["health_goals.created_at"],
    #             "updated_at": result["health_goals.updated_at"],
    #         }
    #         health_goal = HealthGoal(health_goal_data)
    #         time_domain_data = {
    #             "id": result["time_domains.id"],
    #             "action_item": result["action_item"],
    #             "time_domain_10_year": result["time_domain_10_year"],
    #             "time_domain_5_year": result["time_domain_5_year"],
    #             "time_domain_3_year": result["time_domain_3_year"],
    #             "time_domain_2_year": result["time_domain_2_year"],
    #             "time_domain_1_year": result["time_domain_1_year"],
    #             "time_domain_6_month": result["time_domain_6_month"],
    #             "time_domain_3_month": result["time_domain_3_month"],
    #             "time_domain_1_month": result["time_domain_1_month"],
    #             "created_at": result["time_domains.created_at"],
    #             "updated_at": result["time_domains.updated_at"],
    #         }
    #         health_goal.time_domains = time_domain_data
    #         user.health_goals.append(health_goal)
    #         print("*********USER HEALTH GOALS*******")
    #         pprint(user.health_goals)
    #         print("**************")
    #     return user

    # @classmethod
    # def save_health_quiz_id(cls):
    #     data = {
    #         "user_id": session["user_id"],
    #         "health_quiz_id": session["health_quiz_id"],
    #     }

    #     query = "UPDATE users SET health_quiz_id = %(health_quiz_id)s WHERE id = %(user_id)s"
    #     print("******HEALTH QUIZ ID SAVING...*****")
    #     return User.db.query_db(query, data)

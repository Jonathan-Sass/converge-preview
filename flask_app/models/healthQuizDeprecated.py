from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session, jsonify, flash, redirect
from flask_app.models.user import User
from flask_app.models import healthQuizDeprecated
import pymysql

class HealthQuiz: 
    db = connectToMySQL("converge_schema")
    _db = "converge_schema"

    def __init__ (self, data):
        self.id = data['id']
        self.health_rating = data["health_rating"]
        self.fitness_rating = data["fitness_rating"]
        self.activity_rating = data["activity_rating"]
        self.is_open_to_movement = data["is_open_to_movement"]
        self.is_open_to_practices = data["is_open_to_practices"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.health_quiz = None

    # Create a health_quiz entry.
    @classmethod
    def create_health_quiz(cls):
        user_id = session["user_id"]
        if not user_id:
            flash("Please log in.", "login")
            return redirect("/")

        user = User.find_by_id(user_id)
        if not user:
            flash("Please log in.", "login")
            return redirect("/")
        
        if user.health_quiz_id is None:
            try:
                query = """
                    INSERT INTO health_quizzes
                    (health_rating, health_interest, fitness_rating, activity_rating, is_open_to_movement, is_open_to_practices, created_at, updated_at)
                    VALUES (%(health_rating)s, %(health_interest)s, %(fitness_rating)s, %(activity_rating)s, %(is_open_to_movement)s, %(is_open_to_practices)s, NOW(), NOW());
                        """
                data = {
                    "health_rating": 0, 
                    "health_interest": 0, 
                    "fitness_rating": 0, 
                    "activity_rating": 0, 
                    "is_open_to_movement": 0, 
                    "is_open_to_practices": 0
                }

                health_quiz_id = HealthQuiz.db.query_db(query, data)
                if health_quiz_id:
                    session["health_quiz_id"] = health_quiz_id
                    user.health_quiz_id = health_quiz_id
                    User.save_health_quiz_id()
                    return jsonify({'message': 'Quiz submitted successfully!'}), 200
                else:
                    return jsonify({'message': 'Failed to create quiz'}), 500
            except pymysql.MySQLError as e:
                return jsonify({"message": f"Database error: {str(e)}"}), 500
        else:
            return jsonify({'message': 'Quiz already exists for this user'}), 400
        #     result = HealthQuiz.db.query_db(query)
            
        #     if result:
        #         health_quiz_id = HealthQuiz.db.lastrowid
        #         session["health_quiz_id"] = result
        #         user.health_quiz_id = health_quiz_id
        #         User.save_health_quiz_id()
        # return jsonify({'message': 'Quiz submitted successfully!'}), 200
  
#   Update a health_quiz entry
    @classmethod
    def update_health_quiz_single_column(cls, form_data):
        # Ensure that user_id is in the session and user is valid
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"message": "User not logged in"}), 401

        user = User.find_by_id(user_id)
     
        if not user:
            return jsonify({"message": "User not found"}), 404

        health_quiz_id = user.health_quiz_id
        if not health_quiz_id:
            return jsonify({"message": "Health quiz ID not found for user"}), 400

        valid_columns = [
            "health_rating", "health_interest", "fitness_rating", 
            "activity_rating", "is_open_to_movement", "is_open_to_practices"
        ]
        columns_updated = False

        print("****ENTERING form_data LOOPS*****")

        for key, value in form_data.items():
            ("*****FOR LOOP ACHIEVED*****")
            if key in valid_columns:
                print("*************FORM-DATA IN LOOP**********")
                pprint(form_data)

                try:
                    query = f"""
                            UPDATE health_quizzes 
                            SET {key} = %(value)s 
                            WHERE id = %(id)s;
                    """
                    # data = (value, health_quiz_id)
                    data = {
                        "value": int(value), 
                        "id":  health_quiz_id
                    }
                    print("****DATA***")
                    print(data)
                    result = HealthQuiz.db.query_db(query, data)
                    print("*****QUERY RESULT*****")
                    pprint(result)
                    columns_updated = True
                except pymysql.IntegrityError as e:
                    return jsonify({"message": f"Integrity error: {str(e)}"}), 400
                except pymysql.MySQLError as e:
                    print("Database error: ", e)
                    return jsonify({"message": f"Database error: {str(e)}"}), 500
        if columns_updated:
            return jsonify({'message': 'Quiz column(s) updated successfully!'}), 200
        else:
            return jsonify({'message': 'No valid columns found in form data'}), 400

    @classmethod
    def find_by_id(cls, health_quiz_id):
        query = "SELECT * FROM health_quizzes WHERE id = %(id)s;"

        data = {"id": health_quiz_id}

        results = connectToMySQL(HealthQuiz._db).query_db(query, data)

        health_quiz = HealthQuiz(results[0])

        return health_quiz

from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session, jsonify, redirect
import asyncio, aiomysql, logging
import pymysql

from flask_app.models.user import User
from flask_app.models.user_response import UserResponse

class UserSurvey: 
    db = connectToMySQL("converge_schema")
    _db = "converge_schema"

    def __init__ (self, data):
        self.id = data["id"]
        self.category = data["category"]
        self.subcategory = data["subcategory"]
        self.questions = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_survey = None

    # Find a User Survey Category and User ID
    @classmethod
    def find_questions_by_category_and_subcategory(cls, user_category_subcategory_data):
        query = """
            SELECT 
                categories.name AS category,
                subcategories.name AS subcategory,
                survey_questions.id AS question_id,
                survey_questions.question_slug,
                survey_questions.question_text,
                survey_questions.type,
                survey_answers.id AS answer_id,
                survey_answers.answer_text, 
                survey_answers.answer_value,
                survey_branching.next_question_id,
                sq_next.question_slug AS next_question_slug
            FROM 
                survey_questions
            JOIN
              subcategories ON survey_questions.subcategory_id  = subcategories.id
            JOIN
              categories ON subcategories.category_id = categories.id
            LEFT JOIN
                survey_question_answer_map ON survey_question_answer_map.survey_question_id = survey_questions.id
            LEFT JOIN
                survey_answers ON survey_answers.id = survey_question_answer_map.survey_answer_id
            LEFT JOIN 
                survey_branching ON survey_questions.id = survey_branching.survey_question_id
            LEFT JOIN
                survey_questions sq_next ON survey_branching.next_question_id = sq_next.id
            WHERE 
                categories.category_slug = %(category)s
            AND
                subcategories.subcategory_slug = %(subcategory)s
            ORDER BY
                survey_questions.id, survey_answers.id;
          """
        
        data = {
            'category': user_category_subcategory_data['category'], 
            'subcategory': user_category_subcategory_data['subcategory']
        }


        result = UserSurvey.db.query_db(query, data)

        question_set = UserSurvey.process_question_data_for_frontend(result)
        survey_branches = UserSurvey.process_survey_branch_data(result)

        # print("*****question_set in find questions by survey category and subcategory*****")
        # pprint(question_set)

        return question_set, survey_branches

    
    def process_survey_branch_data(questions):

        survey_branches = []

        for question in questions:
            if question["next_question_id"]:
                branch_data = {
                    "questionId": question["question_id"],
                    "surveyQuestionSlug": question["question_slug"],
                    "answerText": question["answer_text"],
                    "nextQuestionSlug": question["next_question_slug"]
                }

                survey_branches.append(branch_data)

        # print("survey_branches in process_survey_branch_data")
        # pprint(survey_branches)

        return survey_branches
    

    @staticmethod
    def process_question_data_for_frontend(question_data):
        question_set = {}
        for question in question_data:
            question_id = question['question_id']

            if question_id not in question_set:
                question_set[question_id] = {
                    'question': question['question_text'], 
                    'questionId': question_id, 
                    'questionSlug': question['question_slug'],
                    'type': question['type'], 
                    'answers': []
                }
            
            # .get?
            if question['answer_text']:
                if not any (answer['answerText'] == question['answer_text'] for answer in question_set[question_id]['answers']):
                  question_set[question_id]['answers'].append({
                      'answerId': question['answer_id'],
                      'answerText': question['answer_text'], 
                      'answerValue': question.get('answer_value', None)
                  })

        return list(question_set.values())

    @classmethod
    def find_user_response_by_user_id_and_question_id(cls, survey_question_id):
        query = """
                SELECT 
                    user_id, 
                    survey_question_id
                FROM
                    user_responses
                WHERE 
                    user_id= %(user_id)s
                AND
                    survey_question_id = %(survey_question_id)s;
                """
        user_response_data = {
            'user_id': session['user_id'], 
            'survey_question_id': survey_question_id
        }
        
        return UserSurvey.db(query, user_response_data)


#   Update a user_survey entry
    @classmethod
    def update_user_survey_single_column(cls, form_data):
        # Ensure that user_id is in the session and user is valid
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"message": "User not logged in"}), 401

        user = User.find_by_id(user_id)
     
        if not user:
            return jsonify({"message": "User not found"}), 404

        user_survey_id = user['user_survey_id']
        if not user_survey_id:
            return jsonify({"message": "Health survey ID not found for user"}), 400

        valid_columns = [
            "health_rating", "health_interest", "fitness_rating", 
            "activity_rating", "is_open_to_movement", "is_open_to_practices"
        ]
        columns_updated = False

        for key, value in form_data.items():
            if key in valid_columns:

                try:
                    query = f"""
                            UPDATE user_surveys 
                            SET {key} = %(value)s 
                            WHERE id = %(id)s;
                    """
                    # data = (value, user_survey_id)
                    data = {
                        "value": int(value), 
                        "id":  user_survey_id
                    }
                    print(data)
                    result = UserSurvey.db.query_db(query, data)
                    print("*****QUERY RESULT*****")
                    pprint(result)
                    columns_updated = True
                except pymysql.IntegrityError as e:
                    return jsonify({"message": f"Integrity error: {str(e)}"}), 400
                except pymysql.MySQLError as e:
                    print("Database error: ", e)
                    return jsonify({"message": f"Database error: {str(e)}"}), 500
        if columns_updated:
            return jsonify({'message': 'Survey column(s) updated successfully!'}), 200
        else:
            return jsonify({'message': 'No valid columns found in form data'}), 400

    @classmethod
    def find_by_id(cls, user_survey_id):
        query = "SELECT * FROM user_surveys WHERE user_id = %(id)s;"

        data = {"id": user_survey_id}

        results = connectToMySQL(UserSurvey._db).query_db(query, data)

        user_survey = UserSurvey(results[0])

        return user_survey

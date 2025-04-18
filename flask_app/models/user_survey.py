from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session, jsonify
# import asyncio, aiomysql, logging
import pymysql

from flask_app.models.user import User
from flask_app.models.user_response import UserResponse

class UserSurvey: 
    """
    A class to manage survey logic for users within the Converge app.

    Responsibilities include:
    - Fetching and processing questions and answers based on category/subcategory
    - Handling branching logic for survey flows
    - Saving and updating user-specific responses and survey metadata
    """
    db = connectToMySQL("converge_schema")

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
        """
        Retrieves all questions and potential answers for a given category/subcategory pair.
        
        Also includes survey branching logic when applicable.

        Args:
            user_category_subcategory_data (dict): Dictionary with 'category' and 'subcategory' keys.

        Returns:
            tuple: A list of structured question data for the frontend, and a list of branching rules.
        """
        query = """
            SELECT 
                c.name AS category,
                sc.id AS subcategory_id,
                sc.name AS subcategory,
                sc.subcategory_slug,
                sq.id AS question_id,
                sq.question_slug,
                sq.question_text,
                sq.type,
                sa.id AS answer_id,
                sa.answer_text, 
                sa.answer_value,
                sb.answer_value AS branch_answer_value,
                sb.next_question_id,
                sq_next.question_slug AS next_question_slug
            FROM 
                survey_questions sq
            JOIN
              survey_subcategories sc ON sq.survey_subcategory_id  = sc.id
            JOIN
              survey_categories c ON sc.survey_category_id = c.id
            LEFT JOIN
                survey_question_answer_map sqam ON sqam.survey_question_id = sq.id
            LEFT JOIN
                survey_answers sa ON sa.id = sqam.survey_answer_id
            LEFT JOIN 
                survey_branching sb ON sq.id = sb.survey_question_id
            LEFT JOIN
                survey_questions sq_next ON sb.next_question_id = sq_next.id
            WHERE 
                sc.subcategory_slug = %(subcategory)s
            ORDER BY
                subcategory_id, sq.id, sa.id;
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

    def find_questions_by_id_range(start_id, end_id):
        query = """
          SELECT 
                c.name AS category,
                sc.id AS subcategory_id,
                sc.name AS subcategory,
                sc.subcategory_slug,
                sq.id AS question_id,
                sq.question_slug,
                sq.question_text,
                sq.type,
                sa.id AS answer_id,
                sa.answer_text, 
                sa.answer_value,
                sb.answer_value AS branch_answer_value,
                sb.next_question_id,
                sq_next.question_slug AS next_question_slug
            FROM 
                survey_questions sq
            JOIN
              survey_subcategories sc ON sq.survey_subcategory_id  = sc.id
            JOIN
              categories c ON sc.category_id = c.id
            LEFT JOIN
                survey_question_answer_map sqam ON sqam.survey_question_id = sq.id
            LEFT JOIN
                survey_answers sa ON sa.id = sqam.survey_answer_id
            LEFT JOIN 
                survey_branching sb ON sq.id = sb.survey_question_id
            LEFT JOIN
                survey_questions sq_next ON sb.next_question_id = sq_next.id
            WHERE 
                question_id BETWEEN %(start_id)s AND %(end_id)s
            ORDER BY
                subcategory_id, sq.id, sa.id;
        """

        data = {
            "start_id": start_id,
            "end_id": end_id
        }

        result = UserSurvey.db.query_db(query, data)
        
        question_set = UserSurvey.process_question_data_for_frontend(result)
        survey_branches = UserSurvey.process_survey_branch_data(result)

        return question_set, survey_branches
    
    def process_survey_branch_data(questions):
        """
        Extracts and structures survey branching logic from a raw result set.

        Args:
            questions (list[dict]): Raw joined query results including branching info.

        Returns:
            list[dict]: A list of branch mappings used by the frontend to control flow.
        """
        survey_branches = []

        for question in questions:
            if question["branch_answer_value"] is not None and question["answer_value"] == question["branch_answer_value"]:
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
        """
        Groups and organizes question and answer data for clean frontend rendering.

        Args:
            question_data (list[dict]): Raw joined query results for questions and answers.

        Returns:
            list[dict]: Structured list of questions with associated answers.
        """
        question_set = {}

        for question in question_data:
            question_id = question['question_id']

            if question_id not in question_set:
                if question['type'] == 'prompt':
                    question_set[question_id] = {
                        'question': question['question_text'],
                        'questionId': question_id,
                        'questionSlug': question['question_slug'],
                        'type': question['type']
                    }
                
                question_set[question_id] = {
                    'question': question['question_text'], 
                    'questionId': question_id, 
                    'questionSlug': question['question_slug'],
                    'type': question['type'], 
                    'answers': []
                }
            
            if question.get('answer_text'):  # Use .get() to prevent KeyError
                if not any(answer['answerText'] == question['answer_text'] for answer in question_set[question_id]['answers']):
                    question_set[question_id]['answers'].append({
                        'answerId': question['answer_id'],
                        'answerText': question['answer_text'], 
                        'answerValue': question.get('answer_value', None)
                    })

        return list(question_set.values())


# LIKELY DEPRECATED, NEED TO COMMENT AND TEST AFTER SUFFICIENT TESTING OF RECENT PERVASIVE DOCSTRING ADDITIONS
#   Update a user_survey entry
    @classmethod
    def update_user_survey_single_column(cls, form_data):
        """
        Updates one column in a user's survey metadata (e.g. ratings or interest flags).

        Args:
            form_data (dict): Key-value pairs representing fields to update.

        Returns:
            Response: Flask `jsonify` response indicating success or failure.
        """
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
    def find_user_survey_by_id(cls, user_survey_id):
        """
        Retrieves a user_survey entry by its ID.

        Args:
            user_survey_id (int): ID of the user_survey entry.

        Returns:
            UserSurvey: A populated UserSurvey object.
        """
        query = "SELECT * FROM user_surveys WHERE user_id = %(id)s;"

        data = {"id": user_survey_id}

        results = UserSurvey.db.query_db(query, data)

        user_survey = UserSurvey(results[0])

        return user_survey

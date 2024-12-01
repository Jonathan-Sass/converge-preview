from flask_app.config.mysqlconnection import connectToMySQL


class UserResponse:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.user_id = data["user_id"]
        self.question_id = data["survey_question_id"]
        self.question_text = data["survey_question_text"]
        self.answer_id = data["survey_answer_id"]
        self.answer_text = data["survey_answer_text"]
        self.answer_value = data["survey_answer_value"]

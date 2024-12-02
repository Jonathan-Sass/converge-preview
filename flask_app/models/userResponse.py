from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class UserResponse:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.user_id = data["user_id"]
        self.survey_topic_slug = data["topic_slug"]
        self.question_id = data["survey_question_id"]
        self.question_text = data["survey_question_text"]
        self.answer_id = data["survey_answer_id"]
        self.answer_text = data["survey_answer_text"]
        self.answer_value = data["survey_answer_value"]


    # def fetch_user_and_responses_by_survey_topic_slug(user, survey_topic_slug_string):
    #     query = """
    #         SELECT 
    #             user_responses.user_id,
    #             survey_topics.topic_slug AS survey_topic_slug,
    #             user_responses.survey_question_id,
    #             survey_questions.question_text AS survey_question_text,
    #             user_responses.survey_answer_id,
    #             survey_answers.answer_text AS survey_answer_text,
    #             survey_answers.answer_value AS survey_answer_value
    #         FROM
    #             user_responses
    #         JOIN
    #             survey_questions ON user_responses.survey_question_id = survey_questions.id
    #         JOIN
    #             survey_answers ON user_responses.survey_answer_id = survey_answers.id
    #         JOIN
    #             survey_topics ON survey_questions.survey_topic_id = survey_topics.id
    #         WHERE
    #             user_responses.user_id = %(user_id)s
    #         AND
    #             survey_topics.topic_slug = %(survey_topic_slug)s
    #         ORDER BY
    #             user_responses.survey_question_id;
    #     """

    #     data = {
    #         "user_id": user["id"],
    #         "survey_topic_slug": survey_topic_slug_string
    #     }

    #     results = UserResponse.db.query_db(query, data)

    #     # user_responses = []
    #     if results:
    #         for result in results:
    #             user["responses"].append(UserResponse(result))
    #     else:
    #         print("No responses found for user or survey_topic_id")
        
    #     return user


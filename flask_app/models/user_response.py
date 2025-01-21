from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from pprint import pprint


class UserResponse:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.user_id = data["user_id"]
        self.topic_slug = data["topic_slug"]
        self.question_slug = data["question_slug"]
        self.question_id = data["survey_question_id"]
        self.question_text = data["survey_question_text"]
        self.answer_id = data["survey_answer_id"]
        self.answer_text = data["survey_answer_text"]
        self.answer_value = data["survey_answer_value"]

    @staticmethod
    def process_user_responses(responses):
        # CURRENT LOGIC FOR TESTING ONLY - ALL SUBSEQUENT FUNCTIONS WILL UNDERGO SIGNIFICANT REWORK FOR A MORE MEANINGFUL FILTERING PROCESS

        if not responses:
            print("No responses to process")
            return None

        for response in responses:
            pprint(response)

        topic_slug = responses[0].topic_slug

        if topic_slug == "getting-to-know-you":
            return UserResponse.process_getting_to_know_you_responses(responses)

    @staticmethod
    def process_getting_to_know_you_responses(responses):
        recommended_routine_template = "Balanced Start"

        response_values = {
            response.question_slug: response.answer_value for response in responses
        }

        # TODO: Change to match-case syntax.
        if response_values.get("adhd-self-assessment") >= 2:
            if response_values.get("current-fitness-level") == 4:
                recommended_routine_template = "Momentum Builder"
                return recommended_routine_template
            elif response_values.get("satisfaction-relationships") < 2:
                recommended_routine_template = "Connected Start"
                return recommended_routine_template
            else:
                recommended_routine_template = "Energized Focus"
                return recommended_routine_template

        if response_values.get("current-fitness-level"):
            recommended_routine_template = "Peak Performance Start"
            return recommended_routine_template

        # for i, response in enumerate(responses):
        #     print(f"*****Index: {i}")
        #     print(vars(response))
        #     print("*****")

        #     if response.question_slug == "current-fitness-level":
        #         if response.answer_value == 4:
        #             recommended_routine_template = "Peak Performance Start"
        #     if response.question_slug == "adhd-self-assessment":
        #         if response.answer_value >= 2:
        #             recommended_routine_template = "Energized Focus"
        #     if response.question_slug == "satisfaction-relationships":
        #         if response.answer_value < 2:
        #             recommended_routine_template = "Connected Start"

        return recommended_routine_template

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

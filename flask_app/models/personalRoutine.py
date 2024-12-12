from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.userResponse import UserResponse
from flask_app.models.routineTemplate import RoutineTemplate

class PersonalRoutine:
    db = connectToMySQL("converge_schema")

    def __init__ (self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.routine_type = data["routine_type"]
        self.start_time = data["start_time"]
        self.end_time = data["end_time"]
        self.is_active = data["is_active"]
        self.notes = data["notes"] or None
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.practices = []

    @classmethod
    def fetch_personal_routines():
        query = """
            SELECT 
        """
        return

    @staticmethod
    def select_and_fetch_initial_am_routine(user, survey_topic_slug_string):
        user.fetch_user_responses_by_survey_topic_slug(survey_topic_slug_string)

        recommended_routine_template_name = UserResponse.process_user_responses(user.responses)
        # template_name = PersonalRoutine.am_routine_template_selector(user.responses)
        recommended_routine_template = RoutineTemplate.fetch_routine_template_with_practices(recommended_routine_template_name)

        # print("****RECOMMENDED ROUTINE TEMPLATE!!!!...?****")
        # print(vars(recommended_routine_template))

        return recommended_routine_template
    
    # @classmethod
    # def select_am_routine_template(self, user_responses):
    #     if user_responses.survey_topic_slug == "getting-to-know-you":

        
    #     return

    def create_personal_routine(routine_data):
        print("***routine_data in create_personal_routine***")
        pprint(vars(routine_data))

        query = """
            INSERT INTO
                personal_routines (user_id, name, desription, routine_type, start_time, end_time, is_active, notes, created_at, updated_at)
            VALUES
                (%(user_id)s, %(description)s, %(routine_type)s, %(start_time)s, %(end_time)s, %(is_active)s, %(notes)s, NOW(), NOW())
            ON DUPLICATE KEY UPDATE
                description = VALUE(description),
                start_time = VALUE(start_time),
                end_time = VALUE(end_time),
                is_active = VALUE(is_active),
                notes = VALUE(notes), 
                updated_at = NOW)();
        """

        result = PersonalRoutine.db.query_db(query, routine_data)

        if result:
            print("****result in create_personal_routine****")
            pprint(result)
            
            personal_routine_id = result
            PersonalRoutine.create_personal_routine_practices(routine_data, personal_routine_id)
        else:
            raise RuntimeError("Error creating personal routine in database.")

        return


    def create_personal_routine_practices(routine_data, personal_routine_id):
        return

    # def update_personal_routine():

    # def delete_personal_routine():
        # return
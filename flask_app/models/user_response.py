from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from pprint import pprint
from flask import session, logging


class UserResponse:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.user_id = data["user_id"]
        self.subcategory_slug = data["subcategory_slug"]
        self.question_slug = data["question_slug"]
        self.question_id = data["survey_question_id"]
        self.question_text = data["question_text"]
        self.answer_id = data["survey_answer_id"]
        self.answer_text = data["answer_text"]
        self.answer_value = data["answer_value"]


    def find_user_responses_by_user_id_and_subcategory_slug(user, subcategory_slug):
        query = """
          SELECT
            ur.user_id,
            sc.subcategory_slug,
            ur.survey_question_id,
            sq.question_slug,
            sq.question_text,
            ur.survey_answer_id,
            sa.answer_text,
            sa.answer_value
          FROM
            subcategories sc
          JOIN
            survey_questions sq ON sc.id = sq.subcategory_id
          JOIN
            user_responses ur on sq.id = ur.survey_question_id
          JOIN
            survey_answers sa on sa.id = ur.survey_answer_id
          WHERE
            ur.user_id = %(user_id)s
          AND
            sc.subcategory_slug = %(subcategory_slug)s
          ORDER BY
            ur.survey_question_id;
        """

        data = {
            "user_id": user.id,
            "subcategory_slug": subcategory_slug
        }

        results = UserResponse.db.query_db(query, data)

        responses = []
        if results:
            for result in results:
                pprint(result)
                responses.append(UserResponse(result))

        return responses


    def map_user_response_to_routine_template(user_responses, subcategory_slug):
      print("***map_user_response_to_routine_template***")
      
      subcategory_processors = {
        "user-orientation": UserResponse.process_user_orientation,
        # Note: Day map also returns a variable for route selection and thus is called separately/omitted from this list.
        # "day-map": UserResponse.process_day_map,
        "discipline-motivation-focus map": UserResponse.process_discipline_motivation_focus,
        "value-map": UserResponse.process_value_map,
      }

      processor_function = subcategory_processors.get(subcategory_slug)

      if processor_function:
        return processor_function(user_responses)
      else:
        raise ValueError(f"Unkown subcategory: {subcategory_slug}")
      
    def process_day_map(user_responses):
      print("***process_day_map***")
      
      recommended_routine_template_name = "The Grounded Start"
      existing_routine_status = False
      
      response_values = {
            response.question_slug: response.answer_value for response in user_responses
        }
      
      existing_routines_check = response_values.get("existing-routines-check")
      existing_am_routines_satisfaction = response_values.get("existing-am-routines-satisfaction")
      am_routine_time_availability = response_values.get("am-routine-availability")
      daily_movement_check = response_values.get("daily-movement-check")
      exercise_frequency = response_values.get("exercise-frequency")
      exercise_timing = response_values.get("exercise-timing")
      am_focus_block_check = response_values.get("am-focus-block-check")
      hobbies_check = response_values.get("hobbies-check")
      hobbies_types = response_values.get("hobbies-types")
      work_schedule_flexibility = response_values.get("work-schedule-flexibility")
      evening_routine_check = response_values.get("evening-routine-check")
      existing_pm_routines_satisfaction = response_values.get("existing-pm-routines-satisfaction")
      pm_routine_time_availability = response_values.get("pm-routine-time-availability")
      social_wellness_check = response_values.get("social-wellness-check")


          # TODO: Outsource routine Template selection to another function?

      # ADD TIME CONSTRAINT TO AUTO SELECT STARTER ROUTINES FOR USERS WITH LESS THAN 10 MINUTES FOR AM HABITS

      if existing_routines_check is not None and existing_am_routines_satisfaction is not None:
        
        #  User has a morning routine but is not satisfied with it
        if existing_routines_check != 0 and existing_am_routines_satisfaction < 2:
          
          if daily_movement_check is not None and exercise_timing is not None and am_focus_block_check is not None:
            
            # User exercises in the morning, and has a morning focus block
            if exercise_timing == 1 and am_focus_block_check > 0:
              #  User is at least moderately active
              if daily_movement_check >=3:
                recommended_routine_template_name = "Peak Performance Start"
            
              # User is lightly active
              if daily_movement_check < 3:
                recommended_routine_template_name = "Energized Focus"

        existing_routine_status = True
         

      if existing_routines_check:
        
        # User does not have an existing morning routine
        if existing_routines_check == 0:

          if daily_movement_check is not None and am_focus_block_check is not None:
          
            # User moves daily and has a morning focus block
            if daily_movement_check == 1 and am_focus_block_check >= 1:
              recommended_routine_template_name = "Active Focus Start"
           
          existing_routine_status = False

      # TODO: Ready for business logic to filter based on responses.

      return recommended_routine_template_name, existing_routine_status



    def process_discipline_motivation_focus(user_response):
          
      return

    def process_value_map(user_response):
          
      return

    def process_user_orientation(user_response):
          
      return

    #TODO: REMOVE - DEPRECATED FOR SCALABLE/FLEXIBLE map_user_responses_to_routine_template and process_map methods
    @staticmethod
    def process_responses_for_routine_template_selection(responses):
        # CURRENT LOGIC FOR TESTING ONLY - ALL SUBSEQUENT FUNCTIONS WILL UNDERGO SIGNIFICANT REWORK FOR A MORE MEANINGFUL FILTERING PROCESS

        if not responses:
            print("No responses to process")
            return None

        for response in responses:
            pprint(response)

        subcategory_slug = responses[0].subcategory_slug

        if subcategory_slug == "getting-to-know-you":
            routine_template_name = UserResponse.select_routine_template_from_getting_to_know_you_responses(responses)
            return routine_template_name

        return

    @staticmethod
    def select_routine_template_from_getting_to_know_you_responses(responses):
        # Set default template
        recommended_routine_template = "Balanced Start"

        response_values = {
            response.question_slug: response.answer_value for response in responses
        }

        # TODO: Change to match-case syntax.
        if response_values.get("adhd-self-assessment") >= 2:
            if response_values.get("current-activity-level") == 4:
                recommended_routine_template = "Momentum Builder"
                return recommended_routine_template
            elif response_values.get("satisfaction-relationships") < 2:
                recommended_routine_template = "Connected Start"
                return recommended_routine_template
            else:
                recommended_routine_template = "Energized Focus"
                return recommended_routine_template

        if response_values.get("current-activity-level") == 4:
            recommended_routine_template = "Peak Performance Start"
            return recommended_routine_template

        return recommended_routine_template

    @classmethod
    def process_user_responses_to_save(cls, collected_answers):
        
        batched_responses = []

        print("*****collected_answers in process_user_responses()*****")
        pprint(collected_answers)

        for answer in collected_answers:
            # FOR OPEN ANSWERS? 
            # if 'answer_text' in answer:
            # answer_data ... 'answer_text': answer['answer_text']

            answer_data = {
                'user_id': session['user_id'],
                'survey_question_id': answer['question_id'], 
                'survey_answer_id': answer['answer_id']
            }
            batched_responses.append(answer_data)
                
        # print("*****batched_responses in process_user_responses*****")
        # pprint(batched_responses)

        return UserResponse.save_user_responses(batched_responses)

    @classmethod
    def save_user_responses(cls, batched_responses):
        # The following question types may contain 
        # flagged_question_types
        
        query = """
            INSERT INTO
                user_responses (user_id, survey_question_id, survey_answer_id, created_at, updated_at)
            VALUES
                (%(user_id)s, %(survey_question_id)s, %(survey_answer_id)s, NOW(), NOW())
            ON DUPLICATE KEY UPDATE
                survey_answer_id = VALUES(survey_answer_id),
                updated_at = NOW();
        """

        try:
            print("Attempting to insert batched responses...")
            pprint(batched_responses) 

            # Execute batch insert
            UserResponse.db.query_db(query, batched_responses, many=True)

            print("Batch insert completed successfully.")
            return True 
        except Exception as e:
            logging.error("Error in save_user_responses: Failed to insert batched responses.")
            logging.error("Exception details:", exc_info=True)  # Log full traceback
            return False



    # def fetch_user_and_responses_by_subcategory_slug(user, subcategory_slug_string):
    #     query = """
    #         SELECT
    #             user_responses.user_id,
    #             subcategorys.subcategory_slug AS subcategory_slug,
    #             user_responses.survey_question_id,
    #             survey_questions.question_text AS survey_question_text,
    #             user_responses.survey_answer_id,
    #             survey_answers.answer_text AS answer_text,
    #             survey_answers.answer_value AS answer_value
    #         FROM
    #             user_responses
    #         JOIN
    #             survey_questions ON user_responses.survey_question_id = survey_questions.id
    #         JOIN
    #             survey_answers ON user_responses.survey_answer_id = survey_answers.id
    #         JOIN
    #             subcategorys ON survey_questions.subcategory_id = subcategorys.id
    #         WHERE
    #             user_responses.user_id = %(user_id)s
    #         AND
    #             subcategories.subcategory_slug = %(subcategory_slug)s
    #         ORDER BY
    #             user_responses.survey_question_id;
    #     """

    #     data = {
    #         "user_id": user["id"],
    #         "subcategory_slug": subcategory_slug_string
    #     }

    #     results = UserResponse.db.query_db(query, data)

    #     # user_responses = []
    #     if results:
    #         for result in results:
    #             user["responses"].append(UserResponse(result))
    #     else:
    #         print("No responses found for user or subcategory_id")

    #     return user

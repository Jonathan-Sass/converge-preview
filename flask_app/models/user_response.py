from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, logging
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.routine_block_template import RoutineBlockTemplate

class UserResponse:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """Initialize a UserResponse object from database row data."""

        self.user_id = data["user_id"]
        self.subcategory_slug = data["subcategory_slug"]
        self.question_slug = data["question_slug"]
        self.question_id = data["survey_question_id"]
        self.question_text = data["question_text"]
        self.type = data["question_type"]
        self.answer_id = data["survey_answer_id"]
        self.answer_text = data["answer_text"]
        self.answer_value = data["answer_value"]


    def find_user_responses_by_user_id_and_subcategory_slug(user, subcategory_slug):
        """
        Retrieve all responses for a given user and subcategory.

        Args:
            user (User): The current logged-in user.
            subcategory_slug (str): The slug representing the subcategory of the survey.

        Returns:
            List[UserResponse]: A list of UserResponse objects with survey question and answer data.
        """
        query = """
          SELECT
            ur.user_id,
            sc.subcategory_slug,
            ur.survey_question_id,
            sq.question_slug,
            sq.question_text,
            sq.type AS question_type,
            ur.survey_answer_id,
            sa.answer_text,
            sa.answer_value
          FROM
            survey_subcategories sc
          JOIN
            survey_questions sq ON sc.id = sq.survey_subcategory_id
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
                responses.append(UserResponse(result))

        return responses

    def hyphen_to_snake(hyphen_slug):
        return

# METHODS FOR MAPPING USER RESPONSES TO ROUTINE BLOCK TEMPLATES
    
    # def map_user_responses(user_responses):
    #   """
    #     Converts a list of UserResponse objects into a snake_case dict of {question_slug: answer_value}.
    #     Handles both single-value and multi-select answers.
    #   """
    #   mapped = {}
    #   for response in user_responses:
    #       slug = hyphen_to_snake(response.question_slug)
    #       value = response.answer_value
    #       if slug in mapped:
    #           # assume it's a multi-select and append
    #           if isinstance(mapped[slug], list):
    #               mapped[slug].append(value)
    #           else:
    #               mapped[slug] = [mapped[slug], value]
    #       else:
    #           mapped[slug] = value
    #   return mapped
    
    def score_trait(user_value, template_value, trait_meta):
      if trait_meta["type"] == "proximity":
        return trait_meta["max_score"] - abs(user_value - template_value)
      elif trait_meta["type"] == "exact":
        return int(user_value == template_value)
      elif trait_meta["type"] == "boolean":
         return 1 if user_value == template_value else 0
      else:
        return 0

    def extract_response_values(user_responses):
      """
        Converts a list of UserResponse objects into a dict mapping question_slug → answer_value(s).
        Handles both single and multi-response questions.
      """
      response_map = {}

      for response in user_responses:
          slug = response.question_slug
          val = response.answer_value

          if slug in response_map:
              # Promote to list if not already
              if not isinstance(response_map[slug], list):
                  response_map[slug] = [response_map[slug]]
              response_map[slug].append(val)
          else:
              response_map[slug] = val

      return response_map
    
    @staticmethod
    def select_goal_category_from_goal_starter_map(user_responses):
      """
      Determines the best goal category slug based on responses to the current-focus-area questions.
      Uses prioritization: top-1 > top-3 > full list.
      """

      mapped = UserResponse.extract_response_values(user_responses)

      top_1 = mapped.get("current-focus-area-top-1", None)
      top_3 = mapped.get("current-focus-area-top-3", [])
      all_selected = mapped.get("current-focus-area", [])

      if not isinstance(top_3, list):
          top_3 = [top_3]
      if not isinstance(all_selected, list):
          all_selected = [all_selected]

      # Mapping from answer_value to goal category slug
      value_to_slug = {
          0: "career-professional-development",
          1: "health-wellness",
          2: "spirituality-life-purpose",  # Personal growth proxy
          3: "social-community",           # Family & relationships proxy
          4: "spirituality-life-purpose",
          5: "recreation-travel",
          6: "creative-expression-hobbies",
          7: "wealth-finance",
          8: "social-community",
          9: "environment-success",        # Productivity
          10: "environment-success",       # Self-discipline proxy
          # 11 is 'Not sure' — skip
      }

      def match_from(values):
          for val in values:
              slug = value_to_slug.get(val)
              if slug:
                  return slug
          return None

      # Priority: top-1 → top-3 → all
      return match_from([top_1]) or match_from(top_3) or match_from(all_selected)
    
    def select_archetype_from_map(user,map_slug):
      responses = UserResponse.find_user_responses_by_user_id_and_subcategory_slug(user, map_slug)

      if not responses:
        raise ValueError(f"No responses found for user {user.id} and map '{map_slug}'")

      subcategory_slug = responses[0].get("subcategory_slug")
      if not subcategory_slug:
        raise ValueError("Response is missing 'subcategory_slug'")

      # Dispatch table: maps subcategory slugs to the appropriate selector function
      archetype_selector = {
        "career-professional-development-map": select_career_archetype,
        # Add additional subcategory → function mappings here
        # "fitness-training-map": select_fitness_archetype,
      }

      selector_fn = archetype_selector.get(subcategory_slug)
      if not selector_fn:
          raise ValueError(f"No archetype selection logic defined for '{subcategory_slug}'")

      return selector_fn(responses)

    def select_career_archetype(responses):
      values = UserResponse.extract_response_values(responses)

      situation = values.get("career-current-situation")
      motivation = values.get("career-motivation")
      indie = values.get("independent-experience")

      if situation == 0 and motivation == 0:
          return "career-leadership-growth"
      elif motivation == 1:
          return "career-skills-credentials"
      elif motivation == 2:
          return "career-discovery"
      elif motivation == 3 or situation == 3:
          return "career-pivot"
      elif motivation == 4 or (indie == 0 and situation == 4):
          return "aspiring-independent-creator"
      elif motivation == 5 or indie == 1:
          return "experienced-independent-creator"
      elif motivation == 6 or situation == 6:
          return "creative-professional-growth"
      else:
        return "career-skills-credentials"  # fallback


    def select_digital_disconnect_template(user_responses):
      mapped_responses = UserResponse.extract_response_values(user_responses)

      relationship = mapped_responses.get("tech-use-and-attitude", 0)
      phone_checks = mapped_responses.get("impulsive-phone-checks", 0)
      screen_fatigue = mapped_responses.get("screen-fatigue-awareness", 0)
      top_pain_points = mapped_responses.get("pain-point-top-2", [])
      is_boundary_curious = mapped_responses.get("digital-boundary-check", None)
      pain_points = mapped_responses.get("pain-point-identification", [])
      if not isinstance(top_pain_points, list):
         top_pain_points = [top_pain_points]
        

      # Strong doomscrolling + desire to change
      if 0 in top_pain_points and relationship <= 2:
          return "social-scroll-reset"

      # Phone anxiety or compulsive behavior
      if 4 in top_pain_points or (1 in top_pain_points and phone_checks >= 2):
          return "micro-break-reset"

      # Deep fatigue, overwhelm, or trouble sleeping
      if 3 in top_pain_points or screen_fatigue == 3:
          return "digital-detox-lite"

      # News-specific frustration
      if 4 == is_boundary_curious:
          return "news-limits"
      if 0 in top_pain_points and 4 not in pain_points and 3 <= relationship <= 4:
          return "news-light-boundaries"

      # Seeking structured, productive breaks
      if is_boundary_curious in [0, 2, 5] and phone_checks >= 2:
          return "focus-block-boundaries"

      # Moderate use and wants to try limits (not deep distress)
      if is_boundary_curious in [1, 3] or relationship == 2:
          return "keepin-it-real"

      # Not ready to commit
      if is_boundary_curious == 6:
          return "micro-break-reset"

      # Fallback for cautious or minimal-response users
      return "keepin-it-real"


    def select_core_primer_template(user_responses):
      mapped_responses = UserResponse.extract_response_values(user_responses)

      cold = mapped_responses.get("core-primer-cold-readiness", "basic")      # values: "basic", "intermediate", "advanced"
      style = mapped_responses.get("core-primer-light-movement-style", "beverage")  # values: "beverage", "walk", "run"

      # Build slug dynamically
      slug = f"{cold}-primer"

      if style == "walk":
          slug += "-walk"
      elif style == "run":
          slug += "-sun-run"

      return slug

    
    def select_core_builder_template(user_responses):
      # Map user responses to extracted values
      mapped_responses = UserResponse.extract_response_values(user_responses)

      # Extract relevant response values
      meditation_style = mapped_responses.get("meditation-preference", None)
      movement_type = mapped_responses.get("movement-preference", None)
      calm_or_energy = mapped_responses.get("calm-or-energy", None)
      strength_vs_mobility = mapped_responses.get("strength-vs-mobility", None)
      desired_intensity = mapped_responses.get("desired-intensity", None)
      reflection_preference = mapped_responses.get("reflection-practice", None)
      routine_focus = mapped_responses.get("routine-focus", None)

      # Handle cases where response values may be missing or in an unexpected format
      if meditation_style is None or movement_type is None or calm_or_energy is None:
          return "reset-and-rise"  # Fallback template if responses are incomplete or invalid

      # Default case for low-intensity, balanced routines
      if calm_or_energy == "Calming and Grounding" and desired_intensity == "Low-Intensity, Grounding":
          return "reset-and-rise"  # For those who prefer a calming start and low effort

      # User preferring high-energy movement with meditation:
      if calm_or_energy == "Energy-Boosting Movement" and meditation_style == "Breath-Based Calm":
          if desired_intensity == "High-Intensity, Full Body Workout":
              return "hiit-and-sit"  # High-energy and quick workouts with meditation integration

      # Balance of strength and mobility for resilience and strength training
      if strength_vs_mobility == "Balance of Strength and Mobility" and routine_focus == "Strength and Resilience":
          return "resilience-stack"  # Balanced, mixed focus on physical resilience and mobility

      # Focusing on mindful, flowing movement and clarity
      if meditation_style == "Mindfulness Meditation" and movement_type == "Mindful Movement with Focus":
          return "mindful-movement"  # Mindful movement with deep presence and focus

      # Seeking high energy and full-body challenge
      if desired_intensity == "High-Intensity, Full Body Workout" and routine_focus == "High-Energy, Full-Body Challenge":
          return "hiit-and-sit"  # High-intensity focus for full-body workout and energy boost

      # Prioritizing mobility work for flexibility and joint health
      if strength_vs_mobility == "Prioritize Mobility and Flexibility" and routine_focus == "Focused, Mindful Movement":
          return "reset-and-rise"  # Gentle, grounding mobility with mindfulness and reflective practice

      # Prioritizing strength with an integrated energy boost
      if strength_vs_mobility == "Prioritize Strength Training" and desired_intensity == "High-Intensity, Full Body Workout":
          return "strong-start"  # Full-body strength workout with grounding meditation

      # General routine for balanced strength and mindfulness
      if strength_vs_mobility == "Equal Focus on Both Strength and Mobility" and routine_focus == "Reset and Restore":
          return "reset-and-rise"  # Calm, restorative routine with balanced body strength and mobility focus

      # Reflection preference integration
      if reflection_preference == "Yes, a Gratitude Practice":
          return "mindful-movement"  # Reflective gratitude practice included in the mindful movement routine

      # Fallback for moderate responses (don't fully commit but want a balanced experience)
      if meditation_style == "Breath-Based Calm" or desired_intensity == "Balanced, with Movement and Stillness":
          return "reset-and-rise"  # General balanced routine that integrates movement and calming practices

      # Fallback to a mindful practice if no clear preference
      return "mindful-movement"  # Default to mindful movement if no clear decision


    def process_responses_for_routine_block_template_selection(user_id, block_slug):
       responses = UserResponse.find_user_responses_by_user_id_and_subcategory_slug(user_id, block_slug)

       logic_map = {
          "digital-disconnect-map": UserResponse.select_digital_disconnect_template,
          "core-primer": UserResponse.select_core_primer_template,
          "core-builder": UserResponse.select_core_builder_template
       }

       if block_slug in logic_map:
          # Returns slug string of routine_block_template, due to differences in downstream
          return logic_map[block_slug](responses)
       else:
          raise ValueError(f"No template selector registered for block: {block_slug}")


    def process_discipline_motivation_focus(user_response):
      """
      Placeholder: Future logic for processing Discipline/Motivation/Focus map.

      Args:
          user_response (List[UserResponse]): User responses to this map.
      """
      return

    def process_value_map(user_response):
      """
      Placeholder: Future logic for processing Value Map.

      Args:
          user_response (List[UserResponse]): User responses to this map.
      """
      return

    def process_user_orientation(user_response):
      """
      Placeholder: Future logic for processing User Orientation Map.

      Args:
          user_response (List[UserResponse]): User responses to this map.
      """
      return


    # ALSO DEPRECATED? CAN'T FIND REFERENCE TO IT ELSEWHERE IN CODE BASE, WAS LOCATED IN user_survey.py
   

    @classmethod
    def process_user_responses_to_save(cls, collected_answers):
        """
        Parse JSON-formatted answers from frontend and prepare for batch insert.

        Args:
            collected_answers (List[Dict]): Dictionary entries containing question_id and answer_id.

        Returns:
            bool: Success status of the batch save operation.
        """
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
        """
        Insert or update user responses in the database.

        Args:
            batched_responses (List[Dict]): Cleaned data entries for insert.

        Returns:
            bool: True if successful, False if there was an error.
        """
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

#  @classmethod
#     def find_user_response_by_user_id_and_question_id(cls, survey_question_id):
#         """
#         Checks if the current user has already submitted a response to a specific question.

#         Args:
#             survey_question_id (int): ID of the survey question to check.

#         Returns:
#             list[dict] | None: The user response if found, otherwise None.
#         """
#         query = """
#                 SELECT 
#                     user_id, 
#                     survey_question_id
#                 FROM
#                     user_responses
#                 WHERE 
#                     user_id= %(user_id)s
#                 AND
#                     survey_question_id = %(survey_question_id)s;
#                 """
#         user_response_data = {
#             'user_id': session['user_id'], 
#             'survey_question_id': survey_question_id
#         }
        
#         return UserResponse.db(query, user_response_data)


# def map_user_response_to_routine_block_templates(user_responses, subcategory_slug):
    #   """
    #     Determine which routine template to recommend based on user responses.

    #     Args:
    #       user_responses (List[UserResponse]): User responses for a specific subcategory.
    #       subcategory_slug (str): Slug identifying which mapping logic to apply.

    #     Returns:
    #       str or Tuple[str, bool]: Name of the recommended routine template or a tuple including the name and a flag (e.g., for day-map).
    #     """
      
    #   print("***map_user_response_to_routine_template***")
      
    #   subcategory_processors = {
    #     "user-orientation": UserResponse.process_user_orientation,
    #     # Note: Day map also returns a variable for route selection and thus is called separately/omitted from this list.
    #     # "day-map": UserResponse.process_am_routine_map,
    #     "discipline-motivation-focus map": UserResponse.process_discipline_motivation_focus,
    #     "value-map": UserResponse.process_value_map,
    #   }

    #   processor_function = subcategory_processors.get(subcategory_slug)

    #   if processor_function:
    #     return processor_function(user_responses)
    #   else:
    #     raise ValueError(f"Unkown subcategory: {subcategory_slug}")


    # @staticmethod
    # def select_routine_template_from_getting_to_know_you_responses(responses):
    #     """
    #     Legacy routine selector based on getting-to-know-you responses.

    #     Args:
    #         responses (List[UserResponse]): A list of user responses.

    #     Returns:
    #         str: Name of the recommended routine template.
    #     """
    #     # Set default template
    #     recommended_routine_template = "Balanced Start"

    #     response_values = {
    #         response.question_slug: response.answer_value for response in responses
    #     }

    #     # TODO: Change to match-case syntax.
    #     if response_values.get("adhd-self-assessment") >= 2:
    #         if response_values.get("current-activity-level") == 4:
    #             recommended_routine_template = "Momentum Builder"
    #             return recommended_routine_template
    #         elif response_values.get("satisfaction-relationships") < 2:
    #             recommended_routine_template = "Connected Start"
    #             return recommended_routine_template
    #         else:
    #             recommended_routine_template = "Energized Focus"
    #             return recommended_routine_template

    #     if response_values.get("current-activity-level") == 4:
    #         recommended_routine_template = "Peak Performance Start"
    #         return recommended_routine_template

    #     return recommended_routine_template

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

# def map_user_traits(user_responses):
    #   user_traits = {}

    #   for question in user_responses:
    #     slug = question.question_slug
    #     question_type = question.type

    #     if not slug or not question_type:
    #       continue
         
    #     if question_type in ["yes-no", "boolean"]:
    #       user_traits[slug] = {"type": "exact"}
        
    #     # TODO: Add relevant question types to list below to ensure adequate representation of proximity-based answers
    #     elif question_type in ["guided_choice", "satisfaction", "scale"]:
    #       max_score = max(
    #          (a.get("answer_value", 0) for a in question.get("answers", [])),
    #          default = 1
    #       )
    #       user_traits[slug] = {"type": "proximity", "max_score": max_score}
        
    #      # Optional: add custom scoring types
    #     # elif q_type == "select-any":
    #     #     user_traits[slug] = {"type": "multi-match", "max_score": 1}

    #     return user_traits
      
    # def map_template_traits(user_responses):
        
    #   return

     # def process_am_routine_map(user_responses):
    #   """
    #     Analyze responses from the Day Map to recommend a morning routine.

    #     Args:
    #         user_responses (List[UserResponse]): The responses collected from the day map.

    #     Returns:
    #         Tuple[str, bool]: Recommended routine template name and a flag indicating whether
    #                           the user already has a morning routine.
    #   """ 
    #   print("***process_am_routine_map***")
      
    #   response_values = extract_response_values(user_responses)
    #   user_traits = UserResponse.map_user_traits(user_responses)
    #   template_traits = UserResponse.map_template_traits(user_responses)
    #   existing_routine_status = UserResponse.has_existing_morning_routine(response_values)
      
      
    #   # Set default values until seeding and scoring logic is complete
    #   recommended_digital_disconnect_template = "keeping-it-real"
    #   recommended_core_system_primer_template = "basic-primer-walk"
    #   recommended_core_system_builder_template = "resilience-circuit"
    #   recommended_auxiliary_templates = []
    #   recommended_routine_template_name = "The Grounded Start"
    #   recommended_routine_template_slug = None
    #   existing_routine_status = False
    #   score = 0;
      
      

    #   # Prototype for proximity-based scoring system using User Trait Profile
    #   # TODO: FINISH IT!
    #   user_traits = {
    #      "am_routine_check": response_values.get("am-routine-check", 0),
    #      "habit_implementation_history": response_values.get("habit-implementation-history", 3),
    #      "digital_hygiene": response_values.get("digital-hygiene", 0),
    #      "fuel_and_hydration": response_values.get("fuel-and-hydration"),
    #      "midday_recovery": response_values.get("midday-recovery"),
    #      "digital_detox_willingness": response_values.get("digital-detox-willingness"),
    #      "exercise_style_preferences": response_values.get("exercise-style-preferences"),
    #      "gaming_practice_interest": response_values.get("gaming-practice-interest"),
    #      "social_life_satisfaction": response_values.get("social-life-satisfaction"),
    #      "social_connection_priority": response_values.get("social-connection-priority"),
    #      "am_spiritual_practices": response_values.get("am-spiritual-practices"),
    #      "creative_activity_frequency": response_values.get("creative-activity-frequency"),
    #      "productivity_block_preferences": response_values.get("productivity-block-preference"),
    #      "mindset_primer_usage": response_values.get("mindset-primer-usage")
    #   }
    #   am_routine_status = response_values.get("am_routine_check")

    #   if am_routine_status:
    #     if am_routine_status <= 1:
    #       recommended_routine_template_slug = "core-reset"
    #     else:
    #       for trait, trait_meta in user_traits.items():
    #         user_value = user_traits.get(trait)
    #         template_value = template_traits.get(trait)

    #         if user_value is None or template_value is None:
    #           continue
            
    #         score += UserResponse.score_trait(user_value, template_value, trait_meta)


    #   existing_routines_check = response_values.get("existing-routines-check")
    #   existing_am_routines_satisfaction = response_values.get("existing-am-routines-satisfaction")
    #   am_routine_time_availability = response_values.get("am-routine-availability")
    #   daily_movement_check = response_values.get("daily-movement-check")
    #   exercise_frequency = response_values.get("exercise-frequency")
    #   exercise_timing = response_values.get("exercise-timing")
    #   am_focus_block_check = response_values.get("am-focus-block-check")
    #   hobbies_check = response_values.get("hobbies-check")
    #   hobbies_types = response_values.get("hobbies-types")
    #   work_schedule_flexibility = response_values.get("work-schedule-flexibility")
    #   evening_routine_check = response_values.get("evening-routine-check")
    #   existing_pm_routines_satisfaction = response_values.get("existing-pm-routines-satisfaction")
    #   pm_routine_time_availability = response_values.get("pm-routine-time-availability")
    #   social_wellness_check = response_values.get("social-wellness-check")


    # # 
    #       # TODO: Outsource routine Template selection to another function?

    #   # ADD TIME CONSTRAINT TO AUTO SELECT STARTER ROUTINES FOR USERS WITH LESS THAN 10 MINUTES FOR AM HABITS?

    #   if existing_routines_check is not None and existing_am_routines_satisfaction is not None:
        
    #     #  User has a morning routine but is not satisfied with it
    #     if existing_routines_check != 0 and existing_am_routines_satisfaction < 2:
          
    #       if daily_movement_check is not None and exercise_timing is not None and am_focus_block_check is not None:
            
    #         # User exercises in the morning, and has a morning focus block
    #         if exercise_timing == 1 and am_focus_block_check > 0:
    #           #  User is at least moderately active
    #           if daily_movement_check >=3:
    #             recommended_routine_template_name = "Peak Performance Start"
            
    #           # User is lightly active
    #           if daily_movement_check < 3:
    #             recommended_routine_template_name = "Energized Focus"

    #       existing_routine_status = True
         

    #   if existing_routines_check:
        
    #     # User does not have an existing morning routine
    #     if existing_routines_check == 0:

    #       if daily_movement_check is not None and am_focus_block_check is not None:
          
    #         # User moves daily and has a morning focus block
    #         if daily_movement_check == 1 and am_focus_block_check >= 1:
    #           recommended_routine_template_name = "Active Focus Start"
           
    #       existing_routine_status = False

    #   # TODO: Ready for business logic to filter based on responses.

    #   return recommended_routine_template_name, existing_routine_status
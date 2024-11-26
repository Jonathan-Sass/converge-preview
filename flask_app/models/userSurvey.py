from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session, jsonify, flash, redirect
import asyncio, aiomysql, logging
from flask_app.models.user import User
from flask_app.models import healthQuiz
import pymysql

class UserSurvey: 
    db = connectToMySQL("converge_schema")
    _db = "converge_schema"

    def __init__ (self, data):
        self.id = data["id"]
        self.survey_category = data["survey_category"]
        self.survey_topic = data["survey_topic"]
        self.questions = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_survey = None

    # Find a User Survey Category and User ID
    @classmethod
    def find_questions_by_survey_category_and_topic(cls, user_category_topic_data):
        query = """
            SELECT 
                
                survey_categories.name AS survey_category,
                survey_topics.name AS survey_topic,
                survey_questions.id AS question_id,
                survey_questions.question_text,
                survey_questions.type,
                survey_answers.id AS answer_id,
                survey_answers.answer_text, 
                survey_answers.answer_value

            FROM 
                survey_questions
			JOIN
				survey_topics ON survey_questions.survey_topic_id  = survey_topics.id
			JOIN
				survey_categories ON survey_topics.survey_category_id = survey_categories.id
			LEFT JOIN
                survey_question_answer_map ON survey_question_answer_map.survey_question_id = survey_questions.id
            LEFT JOIN
				survey_answers ON survey_answers.id = survey_question_answer_map.survey_answer_id
            WHERE 
                survey_categories.category_slug = %(survey_category)s
            AND
                survey_topics.topic_slug = %(survey_topic)s
            ORDER BY
                survey_questions.id, survey_answers.id;
        """
        
        data = {
            'survey_category': user_category_topic_data['survey_category'], 
            'survey_topic': user_category_topic_data['survey_topic']
        }


        result = UserSurvey.db.query_db(query, data)
        question_set = UserSurvey.process_question_data(result)

        # print("*****question_set in find questions by survey category and topic*****")
        # pprint(question_set)

        return question_set
    
    @staticmethod
    def process_question_data(question_data):
        question_set = {}
        for question in question_data:
            question_id = question['question_id']

            if question_id not in question_set:
                question_set[question_id] = {
                    'question': question['question_text'], 
                    'questionId': question_id, 
                    'type': question['type'], 
                    'answers': []
                }
            
            # .get?
            if question['answer_text']:
                question_set[question_id]['answers'].append({
                    'answerId': question['answer_id'],
                    'answerText': question['answer_text'], 
                    'answerValue': question.get('answer_value', None)
                })

        return list(question_set.values())

    @classmethod
    def process_user_responses(cls, collected_answers):
        user = User.get_logged_in_user()
        if not user:
            # jsonify({"error": "Please log in"}), 401
            return redirect("/")
        
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

        return UserSurvey.save_user_responses(batched_responses)


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
            pprint(batched_responses)  # Log the batched data for visibility

            # Execute the batch insert
            UserSurvey.db.query_db(query, batched_responses, many=True)

            print("Batch insert completed successfully.")
            return True  # Return success
        except Exception as e:
            logging.error("Error in save_user_responses: Failed to insert batched responses.")
            logging.error("Exception details:", exc_info=True)  # Log full traceback
            return False  # Return failure

        # UserSurvey.db.query_db(query, batched_responses, many=True)

  
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

    # FUNCTIONS TO CHECK FOR USER SURVEY DATA IN DB
    # User Surveys are organized in the following way:

#     # LOOKS FOR AND SEEDS SURVEY DATA IN DB
#     @classmethod
#     def user_survey_seed(cls):
#         user = User.get_logged_in_user()
#         if not user:
#             return redirect("/")
        
#         # REVISIT VALIDATION FOR ENTIRETY OF SEEDING FUNCTIONS
#         UserSurvey.survey_category_seed()
#         UserSurvey.survey_topic_seed()
#         prepared_question_data = UserSurvey.prepare_survey_question_data()
#         UserSurvey.survey_question_seed(prepared_question_data)
#         UserSurvey.survey_generic_answer_seed()
#         UserSurvey.process_survey_question_and_map_data(prepared_question_data)
#         # survey_answer_seed and survey_example_seed in prepare_survey_question_data

#         return

#     @classmethod
#     def survey_category_seed(cls):
#         query = """
#             INSERT INTO survey_categories (category_slug, name, created_at, updated_at)
#             VALUES
#                 ('foundations', 'Foundations', NOW(), NOW()),
#                 ('your-why', 'Defining Your Why', NOW(), NOW()),
#                 ('health-wellness', 'Health and Wellness', NOW(), NOW()),
#                 ('social-community', 'Social and Community Engagement', NOW(), NOW()),
#                 ('recreation-travel', 'Recreation and Travel', NOW(), NOW()),
#                 ('spirituality-life-purpose', 'Spirituality and Life Purpose', NOW(), NOW()),
#                 ('career-professional-development', 'Career and Professional Development', NOW(), NOW()),
#                 ('creative-expression-hobbies', 'Creative Expression and Hobbies', NOW(), NOW()),
#                 ('wealth-finance', 'Wealth Building and Financial Health', NOW(), NOW()),
#                 ('environment-success', 'Environment and Success', NOW(), NOW())
#             ON DUPLICATE KEY UPDATE updated_at = NOW();
#                 """
#         UserSurvey.db.query_db(query)

#     @classmethod
#     def survey_topic_seed(cls):
#         # Fetch all survey_topic_id and topic_name pairs once
#         survey_topics = {
#             # Key is survey_category.slug
#             'foundations': [
#                 {'topic_slug': 'getting-to-know-you', 'name': "Getting to Know You"}, 
#                 {'topic_slug': 'current-habits-patterns', 'name': "Exploring Your Current Habits and Daily Patterns"}, 
#                 {'topic_slug': 'social-support-accountability', 'name': "Understanding Your Social Support and Accountability"}, 
#                 {'topic_slug': 'reflecting-purpose-motivation', 'name': "Reflecting on Your Purpose and Motivation"}, 

#             ],
#             "your-why": [
#                 {"topic_slug": "define-your-purpose", "name": "Define Your Purpose"},
#                 {"topic_slug": "define-your-values", "name": "Define Your Values"},
#                 {"topic_slug": "growth-drivers", "name": "Drivers of Growth"},
#                 {"topic_slug": "long-term-vision", "name": "Long-Term Vision"}
#             ],
#             "health-wellness": [
#                 {"topic_slug": "mental-health", "name": "Mental Health"},
#                 {"topic_slug": "physical-fitness", "name": "Physical Fitness"},
#                 {"topic_slug": "stress-relaxation", "name": "Stress and Relaxation"},
#                 {"topic_slug": "sleep-hygiene", "name": "Sleep Hygiene"},
#                 {"topic_slug": "nutrition-diet", "name": "Nutrition and Diet"},
#                 {"topic_slug": "preventative-checkups", "name": "Preventative Health and Checkups"},
#                 {"topic_slug": "body-image-self-acceptance", "name": "Body Image and Self Acceptance"},
#                 {"topic_slug": "reproductive-sexual-health", "name": "Reproductive and Sexual Health"},
#                 {"topic_slug": "healthy-habits", "name": "Healthy Habits"},
#                 {"topic_slug": "health-education-awareness", "name": "Health Education and Awareness"},
#                 {"topic_slug": "chronic-disease-management", "name": "Chronic Disease Management"},
#                 {"topic_slug": "holistic-health", "name": "Holistic Health"},
#                 {"topic_slug": "health-accountability-tracking", "name": "Health Accountability and Tracking"}
#             ],
#             "social-community": [
#                 {"topic_slug": "family-relationships", "name": "Family Relationships"},
#                 {"topic_slug": "friendships", "name": "Friendships"},
#                 {"topic_slug": "romantic-relationships", "name": "Romantic Relationships"},
#                 {"topic_slug": "workplace-relationships", "name": "Workplace Relationships"},
#                 {"topic_slug": "community-involvement", "name": "Community Involvement"},
#                 {"topic_slug": "social-skills-development", "name": "Social Skills Development"},
#                 {"topic_slug": "healthy-boundaries", "name": "Healthy Boundaries"},
#                 {"topic_slug": "relationship-growth-maintenance", "name": "Relationship Growth & Maintenance"},
#                 {"topic_slug": "networking-building-connections", "name": "Networking and Building New Connections"},
#                 {"topic_slug": "conflict-resolution", "name": "Conflict Resolution"}
#             ],
#             "recreation-travel": [
#                 {"topic_slug": "frequent-hobbies-activities", "name": "Frequent Hobbies and Activities"},
#                 {"topic_slug": "adventure-travel", "name": "Adventure and Travel"},
#                 {"topic_slug": "family-group-events", "name": "Family and Group Events"},
#                 {"topic_slug": "cultural-exploration", "name": "Cultural Exploration"},
#                 {"topic_slug": "special-events", "name": "Special Events"},
#                 {"topic_slug": "competitive-events", "name": "Competitive Events"},
#                 {"topic_slug": "bucket-list", "name": "Bucket List"},
#             ],
#             "spirituality-life-purpose": [
#                 {"topic_slug": "personal-values-beliefs-purpose", "name": "Personal Values, Beliefs and Purpose"},
#                 {"topic_slug": "spiritual-practices-mindfulness", "name": "Spiritual Practices and Mindfulness"},
#                 {"topic_slug": "emotional-balance", "name": "Emotional Balance and Inner Peace"},
#                 {"topic_slug": "higher-power-connection", "name": "Connection to a Higher Power"},
#                 {"topic_slug": "community-service", "name": "Service to Others and Community"},
#                 {"topic_slug": "self-discovery-growth", "name": "Self-Discovery and Growth"},
#                 {"topic_slug": "mind-body-spirit-connection", "name": "Mind-Body-Spirit Connection"},
#                 {"topic_slug": "gratitude-positive-mindset", "name": "Gratitude and Positive Mindset"},
#                 {"topic_slug": "healing-forgiveness-letting-go", "name": "Healing, Forgiveness and Letting Go"},
#                 {"topic_slug": "spiritual-exploration", "name": "Spiritual Exploration and Curiosity"},
#                 {"topic_slug": "environmental-connection-stewardship", "name": "Environmental Connection and Stewardship"},
                
#             ],
#             "career-professional-development": [
#                 {"topic_slug": "professional-skills-continuous-learning", "name": "Professional Skill Development and Continuous Learning"},
#                 {"topic_slug": "career-planning-goal-setting", "name": "Career Planning and Goal Setting"},
#                 {"topic_slug": "leadership-management-skills", "name": "Leadership and Management Skills Development"},
#                 {"topic_slug": "productivity-time-management", "name": "Productivity and Time Management"},
#                 {"topic_slug": "professional-relationships-networking", "name": "Professional Relationships and Networking"},
#                 {"topic_slug": "career-transition-adaptability", "name": "Career Transition and Adaptability"},
#                 {"topic_slug": "financial-growth-compensation", "name": "Financial Growth and Compensation"},
#                 {"topic_slug": "work-life-balance", "name": "Work-Life Balance and Well-being"},
#                 {"topic_slug": "job-satisfaction-fulfillment", "name": "Job Satisfaction and Personal Fulfillment"},
#                 {"topic_slug": "problem-solving-decision-making", "name": "Problem-Solving and Decision-Making"},
#                 {"topic_slug": "adaptation-work-environment", "name": "Adaptation to Remote Work or New Work Environments"},
#                 {"topic_slug": "workplace-ethics-integrity", "name": "Workplace Ethics and Integrity"}
#             ],
#             "creative-expression-hobbies": [
#                 {"topic_slug": "exploring-hobbies-interests", "name": "Exploring New Hobbies and Interests"},
#                 {"topic_slug": "hobby-creative-skills", "name": "Hobby and Creative Skill Improvement"},
#                 {"topic_slug": "creative-projects", "name": "Personal Creative Projects"},
#                 {"topic_slug": "artistic-growth", "name": "Artistic Growth and Self-Improvement"},
#                 {"topic_slug": "creative-problem-solving", "name": "Creative Problem-Solving"},
#                 {"topic_slug": "social-collaborative-hobbies", "name": "Social and Collaborative Hobbies"},
#                 {"topic_slug": "creative-expression-flow", "name": "Creative Expression and Flow"},
#                 {"topic_slug": "long-term-creative-goals", "name": "Long-Term Creative Goals"},
                
#             ],
#             "wealth-finance": [
#                 {"topic_slug": "budgeting-expense-management", "name": "Budgeting and Expense Management"},
#                 {"topic_slug": "saving-emergency-funds", "name": "Saving and Emergency Funds"},
#                 {"topic_slug": "debt-management", "name": "Debt Management"},
#                 {"topic_slug": "investing-build-wealth", "name": "Investing and Building Wealth"},
#                 {"topic_slug": "retirement-planning", "name": "Retirement Planning"},
#                 {"topic_slug": "income-growth-career-advancement", "name": "Income Growth and Career Advancement"},
#                 {"topic_slug": "tax-planning-optimization", "name": "Tax Planning and Optimization"},
#                 {"topic_slug": "wealth-protection-insurance", "name": "Wealth Protection and Insurance"},
#                 {"topic_slug": "financial-literacy", "name": "Financial Literacy and Education"},
#                 {"topic_slug": "goal-oriented-finance-planning", "name": "Goal-Oriented Finance Planning"},
#                 {"topic_slug": "philanthropy-charitable-giving", "name": "Philanthropy and Charitable Giving"},
#                 {"topic_slug": "financial-independence", "name": "Financial Independence and Freedom"},
#                 {"topic_slug": "large-purchase-travel-savings", "name": "Large Purchase and Travel Savings Goals"},
#             ],
#             "environment-success": [
#                 {"topic_slug": "physical-environment-optimization", "name": "Physical Environment Optimization"},
#                 {"topic_slug": "time-task-management", "name": "Time and Task Management"},
#                 {"topic_slug": "social-environment-relationships", "name": "Social Environment and Relationships"},
#                 {"topic_slug": "mindset-mental-environment", "name": "Mindset and Mental Environment"},
#                 {"topic_slug": "success-planning-goal-setting", "name": "Success Planning and Goal Setting"},
#                 {"topic_slug": "leveraging-tools-resources", "name": "Leveraging Tools and Resources for Success"},
#                 {"topic_slug": "continuous-learning-", "name": "Continuous Learning and Improvement"},
#                 {"topic_slug": "workplace-career-success", "name": "Workplace and Career Success"}
#             ]
#         }

#         batch_data = {}

#         # Organize topics into batches by category (key)
#         for category_slug, topics in survey_topics.items():
#             for topic in topics:
#                 if category_slug not in batch_data:
#                     batch_data[category_slug] = []
#                 batch_data[category_slug].append({
#                     'topic_slug': topic['topic_slug'],
#                     'topic_name': topic['name']
#                 })

#         # Retrieve the mapping of category slugs to category IDs
#         survey_category_ids = UserSurvey.get_all_survey_category_ids()  # Should return a dictionary like {'health-wellness': 1, 'social-community': 2, ...}

#         # Prepare and execute batch insert queries for each category
#         for category_slug, topic_batch in batch_data.items():
#             # Check if the category slug exists in the retrieved category IDs
#             if category_slug in survey_category_ids:
#                 survey_category_id = survey_category_ids[category_slug]
#             else:
#                 print(f"Category slug '{category_slug}' not found in the database.")
#                 continue  # Skip this category if the ID is not found

#             # Create the base query
#             query = "INSERT INTO survey_topics (survey_category_id, topic_slug, name, created_at, updated_at) VALUES "
#             query_values = []
            
#             # Add the topic values to the query
#             for topic in topic_batch:
#                 values = f"({survey_category_id}, '{topic['topic_slug']}', '{topic['topic_name']}', NOW(), NOW())"
#                 query_values.append(values)

#             # Combine the query and execute it
#             query += ", ".join(query_values)
#             query += " ON DUPLICATE KEY UPDATE updated_at = NOW();"
            
#             # Execute the query using your database method
#             UserSurvey.db.query_db(query)

#         print(f"{sum(len(v) for v in survey_topics.values())} survey topics have been seeded.")

#     @classmethod
#     def prepare_survey_question_data(cls):
# # ADD QUESTIONS ABOUT SCREEN TIME AND DOPAMINE RELATED DESIRES/DRIVERS/RESPONSES
#         survey_question_data = [
#             {
#                 'topic_slug': 'getting-to-know-you', 
#                 'questions': [
#                     {
#                         'question_slug': 'am-self-care-time-current', 
#                         'question_text': "How much personal or self-care time do you typically make for yourself/have available when you first wake up", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "None", 'answer_value': 0}, 
#                             {'answer_text': "Less than 10 minutes", 'answer_value': 1}, 
#                             {'answer_text': "10-30 minutes", 'answer_value': 2}, 
#                             {'answer_text': "30-60 minutes", 'answer_value': 3}, 
#                             {'answer_text': "1-2 hours", 'answer_value': 4}, 
#                             {'answer_text': "More than 2 hours", 'answer_value': 5}, 
#                         ]
#                     },
#                     {
#                         'question_slug': 'am-self-care-desire-more', 
#                         'question_text': "Do you wish you had more of this time in your morning?", 
#                         'type': 'yes-no'
#                     }, 
#                     {
#                         'question_slug': 'am-self-care-barriers', 
#                         'question_text': "What are your barriers to having more morning self-care time?", 
#                         'type': 'guided-choice',
#                         'examples': [
#                             {'answer_text': "Inconsistent Bedtime/Difficulty Falling Asleep", 'answer_value': None}, 
#                             {'answer_text': "Poor Sleep Quality", 'answer_value': None},
#                             {'answer_text': "Late-Night Responsibilities", 'answer_value': None},
#                             {'answer_text': "Difficulty Waking Up", 'answer_value': None},
#                             {'answer_text': "Early Work/Obligations", 'answer_value': None},
#                             {'answer_text': "Overcommitted Schedule", 'answer_value': None},
#                             {'answer_text': "Stress or Anxiety", 'answer_value': None},
#                             {'answer_text': "Lack of Motivation in the Morning", 'answer_value': None},
#                             {'answer_text': "Evening Screen Time", 'answer_value': None},
#                             {'answer_text': "Household Responsibilities", 'answer_value': None},
#                             {'answer_text': "Busy or Unpredictable Work Schedule", 'answer_value': None},
#                             {'answer_text': "Long Commute", 'answer_value': None},
#                             {'answer_text': "Difficulty Prioritizing Self-Care", 'answer_value': None},
#                             {'answer_text': "Unpredictable Sleep Schedule", 'answer_value': None},
#                             {'answer_text': "Need More Quiet or Private Space", 'answer_value': None},
#                             {'answer_text': "Fatigue or Health Issues", 'answer_value': None},
#                             {'answer_text': "Family Disruptions", 'answer_value': None}
#                         ]
#                     }, 
#                     {
#                         'question_slug': 'am-self-care-routines-dialed', 
#                         'question_text': "If your evening routines or sleep habits were more dialed in, would you have extra time in the morning?", 
#                         'type': 'guided-choice',
#                         'examples': [
#                             {'answer_text': "Yes, I could have a lot more time", 'answer_value': 2},
#                             {'answer_text': "Yes, maybe a bit more", 'answer_value': 1},
#                             {'answer_text': "No, it probably wouldn't change much", 'answer_value': 0}
#                         ]
#                     },
#                     {
#                         'question_slug': 'am-self-care-ideal-morning', 
#                         'question_text': "In your ideal world, how much time would you have for morning self-care or practices?", 
#                         'type': 'guided-choice',
#                         'examples': [
#                             {'answer_text': "I am not interested in morning self-care", 'answer_value': 0},
#                             {'answer_text': "10-15 minutes", 'answer_value': 1},
#                             {'answer_text': "15-30 minutes", 'answer_value': 2},
#                             {'answer_text': "30-60 minutes", 'answer_value': 3},
#                             {'answer_text': "1-2 hours", 'answer_value': 4},
#                             {'answer_text': "More than 2 hours", 'answer_value': 5}
#                         ]
#                     }, 
#                     {
#                         'question_slug': 'sleep-wake-rested', 
#                         'question_text': "Do you usually wake up feeling rested and refreshed?", 
#                         'type': 'frequency'
#                     }, 
#                     {
#                         'question_slug': 'energy-through-day', 
#                         'question_text': "How would you describe your energy levels throughout the day?", 
#                         'type': 'guided-choice',
#                         'examples': [
#                             {'answer_text': "Consistent energy throughout the day", 'answer_value': 5},
#                             {'answer_text': "High energy in the morning, dips in the afternoon", 'answer_value': 4},
#                             {'answer_text': "Low energy in the morning, improves later in the day", 'answer_value': 3},
#                             {'answer_text': "I have energy, but it feels buzzy or hyperactive", 'answer_value': 2},
#                             {'answer_text': "High at night with trouble going to sleep before 10", 'answer_value': 1},
#                             {'answer_text': "Frequently low energy all day", 'answer_value': 0}

#                         ]
#                     },
#                     {
#                         'question_slug': 'energy-type', 
#                         'question_text': "How would you describe your energy patterns?", 
#                         'type': 'guided-choice',
#                         'examples': [
#                             {'answer_text': "I have the energy I need most times, most days.", 'answer_value': 0},
#                             {'answer_text': "I have energy when I am active, but am tired when sedentary.", 'answer_value': 1},
#                             {'answer_text': "I feel like I have mental energy, but my body can't keep up.", 'answer_value': 2},
#                             {'answer_text': "I am mentally fatigued, but my body want to move.", 'answer_value': 3},
#                             {'answer_text': "Both my mind and my body are fatigued.", 'answer_value': 4},
#                             {'answer_text': "I can feel fatigued in the situations where I am overwhelmed or stressed.", 'answer_value': 5},
#                             {'answer_text': "I am tired unless I am engaged in something of interest.", 'answer_value': 6},
#                             {'answer_text': "None of the above.", 'answer_value': 7}
#                         ]
#                     },
#                     {
#                         'question_slug': 'sleep-average-nightly', 
#                         'question_text': "On average, how many hours of sleep do you get each night?", 
#                         'type': 'range-hours-sleep',
#                     }
#                 ]
#             },
#             {
#                 'topic_slug': 'current-habits-patterns', 
#                 'questions': [
#                     {
#                         'question_slug': 'daily-habits-aspirations', 
#                         'question_text': "Are there any positive daily habits you would like to implement into your day? (Select all that apply)", 
#                         'type': 'select-any-add', 
#                         'examples': [
#                             {'answer_text': "Healthier food choices", 'answer_value': None},
#                             {'answer_text': "Improved sleep schedule/hygiene", 'answer_value': None},
#                             {'answer_text': "Building an exercise regimen", 'answer_value': None},
#                             {'answer_text': "Spending more time outdoors", 'answer_value': None},
#                             {'answer_text': "Practicing mindfulness, meditation or something similar", 'answer_value': None},
#                             {'answer_text': "Daily prayer, journaling, and/or reflection", 'answer_value': None},
#                             {'answer_text': "Staying more hydrated", 'answer_value': None},
#                             {'answer_text': "Creating a space to set clear intentions for the day", 'answer_value': None},
#                             {'answer_text': "Practicing gratitude", 'answer_value': None},
#                             {'answer_text': "Spending more time reading or learning", 'answer_value': None},
#                             {'answer_text': "Being more present with family or friends", 'answer_value': None},
#                             {'answer_text': "Spending more quality time with family or friends", 'answer_value': None},
#                             {'answer_text': "Decluttering or organizing my space", 'answer_value': None},
#                             {'answer_text': "Positive self-talk and affirmations", 'answer_value': None},
#                             {'answer_text': "Learning new skills or hobbies", 'answer_value': None},
#                             {'answer_text': "Creating a budget or tracking finances", 'answer_value': None},
#                             {'answer_text': "Volunteering or giving back", 'answer_value': None},
#                             {'answer_text': "None of the above", 'answer_value': None},
#                         ]
#                     },
#                     {
#                         'question_slug': 'daily-habits-vices-to-change', 
#                         'question_text': "Are there any daily habits(vices) you'd like to improve upon or change? (Select all that apply)", 
#                         'type': 'select-any-add', 
#                         'examples': [
#                             {'answer_text': "Less screen time", 'answer_value': None},
#                             {'answer_text': "Less social media", 'answer_value': None},
#                             {'answer_text': "Healthier food choices", 'answer_value': None},
#                             {'answer_text': "Improving regulation of procrastination", 'answer_value': None},
#                             {'answer_text': "Cutting back on drinking, smoking or other substances", 'answer_value': None},
#                             {'answer_text': "Reduce caffeine intake", 'answer_value': None},
#                             {'answer_text': "Reduce impulse spending", 'answer_value': None},
#                             {'answer_text': "Negative self-talk or self-criticism", 'answer_value': None},
#                             {'answer_text': "Skip fewer meals", 'answer_value': None},
#                             {'answer_text': "Multitask less or finish tasks before starting new ones", 'answer_value': None},
#                             {'answer_text': "None of the above", 'answer_value': None}
#                         ]
#                     },
#                     {
#                         'question_slug': 'daily-habits-biggest-change', 
#                         'question_text': "What is the one change that you feel would make the biggest positive impact in your life right now?", 
#                         'type': 'select-any-add', 
#                         'examples': [
#                             {'answer_text': "To be populated from selected habits", 'answer_value': None}
#                         ]
#                     },
#                     {
#                         'question_slug': 'headspace-presence', 
#                         'question_text': "How often do you find yourself thinking about the past and/or future?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "Very little, I tend to stay present in the moment", 'answer_value': 4},
#                             {'answer_text': "I am often dwelling in the past", 'answer_value': 3},
#                             {'answer_text': "I often find myself daydreaming about the future", 'answer_value': 2},
#                             {'answer_text': "It varies day-to-day", 'answer_value': 1},
#                             {'answer_text': "I am very often lost in thought/daydreaming in general", 'answer_value': 0},
#                         ]
#                     },
#                     {
#                         'question_slug': 'headspace-focus', 
#                         'question_text': "How would you describe your ability to stay focused and free from distractions?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "I have rock solid focus", 'answer_value': 5},
#                             {'answer_text': "I am not easily distracted but it does happen", 'answer_value': 4},
#                             {'answer_text': "My focus is decent, but I sometimes experience inertia in getting started", 'answer_value': 3},
#                             {'answer_text': "I can find myself hyperfocused on something I really enjoy", 'answer_value': 2},
#                             {'answer_text': "I am easily distracted", 'answer_value': 1},
#                             {'answer_text': "I have a difficult time motivating to do things I need or want to do", 'answer_value': 0}
#                         ]
#                     },
#                     {
#                         'question_slug': 'headspace-responsibility-burden', 
#                         'question_text': "How often do you feel overburdened by your to-dos and responsibilities?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "I am always/almost always overwhelmed", 'answer_value': 5},
#                             {'answer_text': "I am busy and frequently stressed by my obligations", 'answer_value': 4},
#                             {'answer_text': "I am busy and am sometimes stressed by the load", 'answer_value': 3},
#                             {'answer_text': "I am busy or moderately busy and I usually manage the load well", 'answer_value': 2},
#                             {'answer_text': "I don't have many obligations but am easily stressed by those I have", 'answer_value': 1},
#                             {'answer_text': "I have minimal obligations and live a relaxed life", 'answer_value': 0}
#                         ]
#                     },
#                     {
#                         'question_slug': 'headspace-responsibility-upkeep', 
#                         'question_text': "Do you feel that you are able to keep up with your day-to-day responsibilities?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "Yes, I get what I need done with little or no problem", 'answer_value': 4},
#                             {'answer_text': "Yes, but keeping up can be a challenge", 'answer_value': 3},
#                             {'answer_text': "I mostly keep up, but sometimes it becomes too much", 'answer_value': 2},
#                             {'answer_text': "I am often unable to follow through with responsibilities", 'answer_value': 1},
#                             {'answer_text': "Sometimes I don't even know how much I overlook", 'answer_value': 0}
#                         ]
#                     },
#                     {
#                         'question_slug': 'headspace-responsibility-sources', 
#                         'question_text': "How many of your responsibilities are optional?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "My schedule is set in stone, non-negotiable", 'answer_value': 0},
#                             {'answer_text': "I have some wiggle room in my day", 'answer_value': 1},
#                             {'answer_text': "My schedule is fairly flexible", 'answer_value': 2},
#                             {'answer_text': "I can move just about anything I want in my day", 'answer_value': 3}
#                         ]
#                     },
#                     {
#                         'question_slug': 'satisfaction-current-fitness', 
#                         'question_text': "How satisfied are you with your current fitness level?", 
#                         'type': 'satisfaction'
#                     },
#                     {
#                         'question_slug': 'satisfaction-current-energy', 
#                         'question_text': "How satisfied are you with your typical energy level?", 
#                         'type': 'satisfaction'
#                     },
#                     {
#                         'question_slug': 'satisfaction-current-stress', 
#                         'question_text': "How satisfied are you with your current level of stress?", 
#                         'type': 'satisfaction'
#                     },
#                     {
#                         'question_slug': 'satisfaction-current-stress-resilience', 
#                         'question_text': "How satisfied are you with your level of resilience to stress?", 
#                         'type': 'satisfaction'
#                     },
#                 ]
#             },
#                         {
#                 'topic_slug': 'social-support-accountability', 
#                 'questions': [
#                     {
#                         'question_slug': 'support-system-status', 
#                         'question_text': "How would you describe your support system?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "I have a very strong network of multiple people I can rely on unconditionally for support", 'answer_value': 4},
#                             {'answer_text': "I have a few close individuals or groups who are there for me in most situations", 'answer_value': 3},
#                             {'answer_text': "I have a mix of friends, family or acquaintanaces who can lend a hand or ear in specific circumstances and/or may not be consistently available", 'answer_value': 2},
#                             {'answer_text': "I have one or two people I can turn to occasionally, and they may have limited availability or resources", 'answer_value': 1},
#                             {'answer_text': "I currently have no one I feel comfortable relying on for support or assistance", 'answer_value': 0}
#                         ]
#                     },
#                     {
#                         'question_slug': 'support-system-desired-expansion', 
#                         'question_text': "Are you content with your support system in its current state, or are you interested in expanding you social network/support system?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "I am content with the level of connections and support in my life and am not currently looking to expand", 'answer_value': 5},
#                             {'answer_text': "I am mostly content with my current support system but would welcome new connections if they align with my interests", 'answer_value': 4},
#                             {'answer_text': "I am actively looking to meet new people with aligned interests and values who I can integrate into my social circle", 'answer_value': 3},
#                             {'answer_text': "I am open to meeting new people, but am not quite sure where to start", 'answer_value': 2},
#                             {'answer_text': "I feel that I could use more of a support system but meeting new people can be daunting, uncomfortable or otherwise challenging", 'answer_value': 1}
#                         ]
#                     },
#                     {
#                         'question_slug': 'support-system-growth-strats', 
#                         'question_text': "Identify individuals or groups in your current support network. If you’d like to broaden your support, select any of the listed potential avenues for support-seeking that most interest you", 
#                         'type': 'select-any-add', 
#                         'examples': [
#                             {'answer_text': "Immediate or extended family members", 'answer_value': None},
#                             {'answer_text': "Friends you trust and who will show up for you", 'answer_value': None},
#                             {'answer_text': "Respected coworkers or professional contacts", 'answer_value': None},
#                             {'answer_text': "Online or local community and social groups, hobby groups, sport and activity-based clubs", 'answer_value': None},
#                             {'answer_text': "Friends from real life or video games", 'answer_value': None},
#                             {'answer_text': "A mentor or coach", 'answer_value': None},
#                             {'answer_text': "Classes or skill-building groups", 'answer_value': None},
#                             {'answer_text': "A mental health professional, therapist or counselor, or support group", 'answer_value': None},
#                             {'answer_text': "Groups within a temple, church, mosque, meditation center, or other spiritual gathering space", 'answer_value': None},
#                             {'answer_text': "Pet groups or animal-related communities", 'answer_value': None},
#                             {'answer_text': "Interest-based online communities", 'answer_value': None},
#                             {'answer_text': "I'm not sure at the moment", 'answer_value': None},
#                             {'answer_text': "I prefer to keep to myself", 'answer_value': None}
                            
#                         ]
#                     },
#                     {
#                         'question_slug': 'support-system-preferred-type', 
#                         'question_text': "What type of support do you find most helpful?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "Emotional support (listening, empathy, encouragement)", 'answer_value': 0},
#                             {'answer_text': "Practical support (help with tasks, planning, logistics)", 'answer_value': 1},
#                             {'answer_text': "Accountability (checking in, helping me stay on track)", 'answer_value': 2},
#                             {'answer_text': "Social engagement (companionship, spending time together)", 'answer_value': 3},
#                             {'answer_text': "Advice or mentorship (guidance, problem-solving, feedback)", 'answer_value': 4},
#                         ]
#                     },
#                     {
#                         'question_slug': 'support-system-comfort-asking', 
#                         'question_text': "How comfortable do you feel reaching out to others for help?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "I am very comfortable reaching out for help when I need it", 'answer_value': 3},
#                             {'answer_text': "I am comfortable, though I don't do it often", 'answer_value': 2},
#                             {'answer_text': "Somewhat uncomfortable but open to it if necessary", 'answer_value': 1},
#                             {'answer_text': "Very uncomfortable, I rarely ask for help", 'answer_value': 0}
                            
#                         ]
#                     },
#                     {
#                         'question_slug': 'support-system-goal-understanding', 
#                         'question_text': "Do you feel that your support system understands your personal goals and challenges?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "Yes, they fully understand my goals and challenges", 'answer_value': 5},
#                             {'answer_text': "The understand some of my goals, but not all", 'answer_value': 4},
#                             {'answer_text': "They know my goals but don't fully grasp my challenges", 'answer_value': 3},
#                             {'answer_text': "They know my challenges but don't know about my goals/vision", 'answer_value': 2},
#                             {'answer_text': "No, I don't feel they understand my goals or challenges", 'answer_value': 1},
#                             {'answer_text': "I haven't discussed my goals and challenges with my network", 'answer_value': 0},
#                         ]
#                     }
#                 ]
#             },
#             {
#                 'topic_slug': 'reflecting-purpose-motivation', 
#                 'questions': [
#                     {
#                         'question_slug': 'personal-landscape-purpose', 
#                         'question_text': "The following are things that inspire and motivate me, or otherwise bring joy or purpose into my life. (Select all that apply)", 
#                         'type': 'select-all-add', 
#                         'examples': [
#                             {'answer_text': "Building a sense of community, both locally and online, gives me motivation and belonging", 'answer_value': None},
#                             {'answer_text': "My relationships with family and close friends give meaning and motivation to my life", 'answer_value': None},
#                             {'answer_text': "My spiritual or religious beliefs provide me with guidance, purpose, and motivation", 'answer_value': None},
#                             {'answer_text': "Finding peace, contentment, and balance in daily life is important to me", 'answer_value': None},
#                             {'answer_text': "The process of growth and learning in life brings me joy, regardless of specific outcomes", 'answer_value': None},
#                             {'answer_text': "I am motivated by self-improvement, learning new skills, or gaining knowledge", 'answer_value': None},
#                             {'answer_text': "Self-discovery and growing through adversity give me purpose", 'answer_value': None},
#                             {'answer_text': "Exploring philosophy, existential questions, or life perspectives gives me purpose", 'answer_value': None},
#                             {'answer_text': "Mindfulness, emotional resilience, or mental clarity help me stay centered and focused", 'answer_value': None},
#                             {'answer_text': "Helping others or making a positive impact, whether through work, volunteering, or kindness, is important to me", 'answer_value': None},
#                             {'answer_text': "Being a positive role model for my family or community motivates me", 'answer_value': None},
#                             {'answer_text': "Professional growth, career development, or achieving my goals motivates me", 'answer_value': None},
#                             {'answer_text': "Achieving financial stability and working toward financial goals gives me direction", 'answer_value': None},
#                             {'answer_text': "Problem-solving, innovation, and finding creative solutions energize me", 'answer_value': None},
#                             {'answer_text': "Creative activities like art, music, writing, or crafting bring me a sense of purpose", 'answer_value': None},
#                             {'answer_text': "Expressing my personality through fashion, makeup, or personal style builds my confidence", 'answer_value': None},
#                             {'answer_text': "Engaging in sports, dance, or physical activities keeps me energized", 'answer_value': None},
#                             {'answer_text': "I’m inspired by new experiences, exploration, or connecting with different cultures and ideas", 'answer_value': None},
#                             {'answer_text': "Spending time in nature, whether through outdoor activities or quiet reflection, inspires me", 'answer_value': None},
#                             {'answer_text': "Video games, online communities, or esports give me a sense of connection and accomplishment", 'answer_value': None},
#                             {'answer_text': "Connecting with my cultural heritage or traditions brings me joy and a sense of identity", 'answer_value': None},
#                             {'answer_text': "Advocating for social identities or social justice (e.g., LGBTQIA+, indigenous rights) is meaningful to me", 'answer_value': None},
#                             {'answer_text': "Advocating for causes like social justice, environmental sustainability, or animal welfare gives me purpose", 'answer_value': None},
#                             {'answer_text': "Environmental connection and stewardship bring me purpose", 'answer_value': None},
#                             {'answer_text': "Discovering and understanding my purpose brings me meaning", 'answer_value': None},
#                         ]
#                     },
#                     {
#                         'question_slug': 'personal-landscape-current-strengths', 
#                         'question_text': "What are some personal strengths or qualities that you feel help you succeed through challenges?", 
#                         'type': 'select-all-add', 
#                         'examples': [
#                             {'answer_text': "Patience", 'answer_value': None},
#                             {'answer_text': "Discipline", 'answer_value': None},
#                             {'answer_text': "Creativity", 'answer_value': None},
#                             {'answer_text': "Focus", 'answer_value': None},
#                             {'answer_text': "Positivity", 'answer_value': None},
#                             {'answer_text': "Resilience", 'answer_value': None},
#                             {'answer_text': "Confidence", 'answer_value': None},
#                             {'answer_text': "Empathy", 'answer_value': None},
#                             {'answer_text': "Adaptability", 'answer_value': None},
#                             {'answer_text': "Emotional Intelligence", 'answer_value': None},
#                             {'answer_text': "Mindfulness", 'answer_value': None},
#                             {'answer_text': "Gratitude", 'answer_value': None},
#                             {'answer_text': "Problem-Solving", 'answer_value': None},
#                             {'answer_text': "Optimism", 'answer_value': None},
#                             {'answer_text': "Assertiveness", 'answer_value': None},
#                             {'answer_text': "Self-Compassion", 'answer_value': None}
#                         ]
#                     },
#                     {
#                         'question_slug': 'personal-landscape-desired-strengths', 
#                         'question_text': "What are personal strengths or qualities that you would like to cultivate in yourself?", 
#                         'type': 'select-all-add', 
#                         'examples': [
#                             {'answer_text': "Patience", 'answer_value': None},
#                             {'answer_text': "Discipline", 'answer_value': None},
#                             {'answer_text': "Creativity", 'answer_value': None},
#                             {'answer_text': "Focus", 'answer_value': None},
#                             {'answer_text': "Positivity", 'answer_value': None},
#                             {'answer_text': "Resilience", 'answer_value': None},
#                             {'answer_text': "Confidence", 'answer_value': None},
#                             {'answer_text': "Empathy", 'answer_value': None},
#                             {'answer_text': "Adaptability", 'answer_value': None},
#                             {'answer_text': "Emotional Intelligence", 'answer_value': None},
#                             {'answer_text': "Mindfulness", 'answer_value': None},
#                             {'answer_text': "Gratitude", 'answer_value': None},
#                             {'answer_text': "Problem-Solving", 'answer_value': None},
#                             {'answer_text': "Optimism", 'answer_value': None},
#                             {'answer_text': "Assertiveness", 'answer_value': None},
#                             {'answer_text': "Self-Compassion", 'answer_value': None}

#                         ]
#                     },
#                     {
#                         'question_slug': 'personal-landscape-barriers', 
#                         'question_text': "Are there potential barriers that might make reaching your goals challenging?", 
#                         'type': 'select-all-add', 
#                         'examples': [
#                             {'answer_text': "Limited time", 'answer_value': None},
#                             {'answer_text': "Financial limitations", 'answer_value': None},
#                             {'answer_text': "Health challenges", 'answer_value': None},
#                             {'answer_text': "Limited support system", 'answer_value': None},
#                             {'answer_text': "Difficulty staying motivated", 'answer_value': None},
#                             {'answer_text': "Unclear goals or vision", 'answer_value': None}
#                         ]
#                     },
#                     {
#                         'question_slug': 'personal-landscape-adhd', 
#                         'question_text': "Have you been diagnosed with ADHD, or do you feel you might exhibit ADHD-related behaviors? Examples can include, but are not limited to: difficulty maintaining focus, easily distracted, procrastination, difficulty with organization and time management, forgetfulness, impulsive behavior, restlessness or fidgeting, difficulty completing tasks, hyperfocus on certain activities, low frustration tolerance, emotional sensitivity and mood swings, poor working memory, interrupting or speaking out of turn, struggling to listen fully, zoning out easily, forgetting social commitements or details, challenges in group dynamics, difficulty with emotional regulation, low self-esteem or social anxiety, avoidance of social situations, difficulty building or maintaining friendships", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "Yes, I have been diagnosed.", 'answer_value': 3},
#                             {'answer_text': "I think ADHD might be a factor in some of the issues I experience", 'answer_value': 2},
#                             {'answer_text': "I'm not sure/haven't explored this", 'answer_value': 1},
#                             {'answer_text': "I don't think I exhibit symptoms of ADHD", 'answer_value': 0},
#                         ]
#                     },
#                     {
#                         'question_slug': 'personal-landscape-adhd-type', 
#                         'question_text': "If you think you might have ADHD symptoms, which of the following patterns best describes your typcial experiences with attention, activitiy levels, and focus?", 
#                         'type': 'guided-choice', 
#                         'examples': [
#                             {'answer_text': "Inattentive - I often struggle with focus, organization, and following through on tasks.  I may get easily distracted, lose track of details, or feel overwhelmed by organizing information", 'answer_value': 5},
#                             {'answer_text': "Hyperactive-Impulsive - I tend to feel restless or fidgey, often acting without thinking things through.  I may talk frequently, interrupt others, or find it difficult to stay still for long", 'answer_value': 4},
#                             {'answer_text': "Combined Inattentive and Hyperactive-Impulsive - I experience a mix of attention issues and hyperactivity-impulsivity.  I find it challenging to stay organized and focused and often feel a need to be active or act on impulse", 'answer_value': 3},
#                             {'answer_text': "Situational or Contextual Challenges - My attention, focus, or impulse control varies significantly depending on the situation (e.g., work, social gatherings, or high-interest activities). I may hyperfocus in some areas while struffling with others", 'answer_value': 2},
#                             {'answer_text': "Emotional Dysregulation - I experience intense emotions or mood swings that affect my realtionships and focus. I may struggle with frustration, motivation, or self-esteem, especially in social or high-pressure situations", 'answer_value': 1},
#                             {'answer_text': "None of these patterns resonate with me", 'answer_value': 0}
#                         ]
#                     }
#                 ]
#             },
#             # DEFINING YOUR WHY
#             {

#                 # TODO: CHANGE QUESTION TYPES TO MATCH NEW TYPES
#                 'topic_slug': 'define-your-purpose',
#                 'questions': [
#                     {
#                         'question_text': "What gets you up in the morning? What keeps you motivated?",
#                         'type': 'select-any-add', 
#                         'question_slug': 'what-motivates-you',
#                         'examples': [
#                             {'answer_text': "I want to provide a better life for my family.", 'answer_value': None},
#                             {'answer_text': "I feel motivated by helping others and making a positive impact in my community.", 'answer_value': None},
#                             {'answer_text': "I want to leave a lasting legacy for future generations, something meaningful that will outlive me.", 'answer_value': None},
#                             {'answer_text': "My faith gives me purpose and guides the decisions I make everyday.", 'answer_value': None},
#                             {'answer_text': "I'm committed to staying healthy so I can enjoy a long, active life with the people I love.", 'answer_value': None},
#                             {'answer_text': "I am driven by a desire to constantly improve myself and grow into the best version of me.", 'answer_value': None},
#                             {'answer_text': "My passion for work drives me, especially when I'm making a difference in people's lives.", 'answer_value': None},
#                             {'answer_text': "I feel most alive when I'm exploring the world, experiencing new cultures, and seeking adventure.", 'answer_value': None},
#                             {'answer_text': "Overcoming challenges in my life has shaped me, and now I feel driven to use my experiences to help others do the same.", 'answer_value': None},
#                             {'answer_text': "I'm in survival mode, I get up because I have to.", 'answer_value': None},

#                         ]
#                     },
#                     {
#                         'question_text': "Who or what do you feel deeply connected to?",
#                         'type': 'select-any-add', 
#                         'question_slug': 'deep-connections',
#                         'examples': [
#                             {'answer_text': "My community - helping others brings me a sense of purpose and fulfillment.", 'answer_value': None},
#                             {'answer_text': "I feel a profound connection to nature and find peace in protecting the environment.", 'answer_value': None},
#                             {'answer_text': "My creative work feels like a unique contribution to the world, expressing who I am.", 'answer_value': None},
#                             {'answer_text': "Mentoring others gives me a sense of legacy, knowing I'm making a lasting impact.", 'answer_value': None},
#                             {'answer_text': "I'm driven by my family connections — they are my foundation and a source of deep pride.", 'answer_value': None},
#                             {'answer_text': "I feel at my best when connecting with friends, sharing life’s journey together.", 'answer_value': None},
#                             {'answer_text': "Learning something new invigorates me; it keeps my mind sharp and curiosity alive.", 'answer_value': None},
#                             {'answer_text': "My faith or spiritual beliefs provide a sense of purpose and connection to something greater.", 'answer_value': None},
#                             {'answer_text': "Being in a team setting, working toward a common goal, makes me feel a strong sense of unity.", 'answer_value': None},
#                         ]
#                     },
#                     {
#                         'question_text': "Do you feel like you have uncovered your purpose in life, or are you still searching?",
#                         'type': 'guided-choice', 
#                         'question_slug': 'have-you-uncovered-purpose',
#                         'examples': [
#                             {'answer_text': "I know one or more of my purposes in life.", 'answer_value': None},
#                             {'answer_text': "I think I have identified my purpose.", 'answer_value': None},
#                             {'answer_text': "I think I am starting to uncover it, but I have more exploring to do.", 'answer_value': None},
#                             {'answer_text': "I am still searching.", 'answer_value': None},
#                         ]
#                     },
#                     {
#                         'question_text': "When do you feel most like yourself? What activities bring you the greatest sense of authenticity?",
#                         'type': 'guided-choice', 
#                         'question_slug': 'activities-greatest-authenticity',
#                         'examples': [
#                             {'answer_text': "When I'm creating or building something that excites me.", 'answer_value': None},
#                             {'answer_text': "When I’m working out, I feel like I’m building both my body and my mental resilience.", 'answer_value': None},
#                             {'answer_text': "When I'm spending quality time with the people I care about.", 'answer_value': None},
#                             {'answer_text': "I’m at my best when I’m mentoring others, passing on my knowledge feels like I'm creating a legacy.", 'answer_value': None},
#                             {'answer_text': "I’m most energized when I’m learning something new because it keeps me curious and engaged.", 'answer_value': None},
#                         ]
#                     },
#                     {
#                         'question_text': "What current activities in your life give you a sense of purpose and fulfillment?",
#                         'type': 'guided-choice', 
#                         'question_slug': 'current-activities-purpose-fulfillment',
#                         'examples': [
#                             {'answer_text': "When I am spending quality time with my loved ones, I feel like I am truly myself", 'answer_value': None},
#                             {'answer_text': "When I am working on something creative, like painting, writing, or designing.", 'answer_value': None},
#                             {'answer_text': "I feel most fulfilled when I am helping others, whether through volunteering or supporting a friend.", 'answer_value': None},
#                             {'answer_text': "When I'm immersed in nature, hiking or just being outside, I feel grounded and at peace.", 'answer_value': None},
#                             {'answer_text': "When I'm pursuing personal growth - learning new skills or challenging myself.", 'answer_value': None},
#                             {'answer_text': "When I am engaging in deep conversations with people I care about.", 'answer_value': None},
#                             {'answer_text': "When I am fully present in the moment, like during meditation or mindfulness exercises.", 'answer_value': None},
#                             {'answer_text': "When I am exercising, especially in activities like yoga, running or strength training.", 'answer_value': None},
#                             {'answer_text': "When I am working on a project that aligns with my values and passions.", 'answer_value': None},
#                             {'answer_text': "When I'm exploring new places or experiencing different cultures.", 'answer_value': None},
#                         ]
#                     },
#                     {
#                         'question_text': "Are there things you haven't yet explored that you think might be part of your vision of a fulfilled life?",
#                         'type': 'guided-choice', 
#                         'question_slug': 'unexplored-activities-fulfillment',
#                         'examples': [
#                             {'answer_text': "Yes, I can think of one or more.", 'answer_value': None},
#                             {'answer_text': "I'm not sure, I need to think more.", 'answer_value': None},
#                             {'answer_text': "Perhaps, but I currently have many activities I enjoy that are fulfilling to me.", 'answer_value': None},
#                             {'answer_text': "I'm all set, if anything I could take on less in my day.", 'answer_value': None},
#                         ]
#                     },
#                     {
#                         'question_text': "What small steps could you take today to start exploring your sense of purpose?", 
#                         'type': 'guided-choice', 
#                         'question_slug': 'small-steps-toward-purpose',
#                         'examples': [
#                             {'answer_text': "I could reflect on what truly makes me happy and aligned with my values.", 'answer_value': None},
#                             {'answer_text': "I could start writing or journaling about the things I'm passionate and energetic about to see what comes up.", 'answer_value': None},
#                             {'answer_text': "I could try a new activity or hobby to see if it clicks with me.", 'answer_value': None},
#                             {'answer_text': "I am not sure I can take on any new activities at the moment.", 'answer_value': None}
#                         ]
#                     },
#                     {
#                         'question_text': "What personal strengths or traits help you navigate difficulties?",
#                         'type': 'guided-choice', 
#                         'question_slug': 'personal-strengths-navigate-difficulties',
#                         'examples': [
#                             {'answer_text': "I am resilient and always find a way through challenges.", 'answer_value': None},
#                             {'answer_text': "I am adaptable.", 'answer_value': None},
#                             {'answer_text': "My creativity helps me think outside the box in difficult situations.", 'answer_value': None},
#                             {'answer_text': "My resourcefulness helps me think outside the box in difficult tuations.", 'answer_value': None},
#                             {'answer_text': "I am good at letting go of the little things and focusing on the big picture.", 'answer_value': None},
#                         ]
#                     },
#                 ]
#             },
#             {
#                 'topic_slug': 'define-your-values',
#                 'questions': [
#                     {
#                         'question_text': "What values do you hold most dear in life?",
#                         'type': 'guided-choice', 
#                         'question_slug': 'values-most-dear',
#                         'examples': [
#                             {'answer_text': "Integrity and honesty are my highest values.", 'answer_value': None},
#                             {'answer_text': "Treating others with respect, kindness and compassion.", 'answer_value': None},
#                             {'answer_text': "Family - prioritizing family connections, care and support.", 'answer_value': None},
#                             {'answer_text': "Personal growth or professional development.", 'answer_value': None},
#                             {'answer_text': "Autonomy, independence, personal freedom.", 'answer_value': None},
#                             {'answer_text': "Accountability for my actions", 'answer_value': None},
#                             {'answer_text': "Courage - having the strength to face my fears, adversity, uncertainty.", 'answer_value': None},
#                             {'answer_text': "Maintaining balance between work, family, and personal life.", 'answer_value': None},
#                             {'answer_text': "Creativity.", 'answer_value': None},
#                             {'answer_text': "Health - prioritizing physical and mental well-being.", 'answer_value': None},
#                             {'answer_text': "Justice - fairness, equality, a desire to do what is morally right.", 'answer_value': None},
#                             {'answer_text': "Perseverance - commitment to pursuing goals and dreams despite challenges or setbacks.", 'answer_value': None},
#                             {'answer_text': "Adventure - seeking new experiences.", 'answer_value': None},
#                             {'answer_text': "Service - helping others, contributing to the well-being of the community.", 'answer_value': None}
#                         ]
#                     }
#                 ]
#             },
            
#     # TODO: POSSIBLE DATA STRUCTURE UPDATE TO UTILIZE MANY-TO-MANY TABLE, POSSIBLY ATTAINABLE WITH ONLY CHANGES TO survey_custom_answer_seed()

#             # RECREATION AND TRAVEL
#             {
#                 'topic_slug': 'frequent-hobbies-activities',
#                 'questions': [
#                     {
#                         'question_text': "How often do you think about engaging in new hobbies or activities?",
#                         'question_slug': 'new-hobby-activity-interest',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "How much time do you spend considering your personal interests, such as traveling or exploring new hobbies?",
#                         'question_slug': 'time-exploring-new-interests',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "What is your interest level in local or international travel?",
#                         'question_slug': 'interest-local-international-travel',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "How interested are you in pursuing hobbies like crafting or DIY projects on a daily basis?",
#                         'question_slug': 'interest-crafts-projects',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "How interested are you in participating in events, competitions, or skill-based activities?",
#                         'question_slug': 'interest-competitive-skill-based',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "How spontaneous are you when it comes to trying random new activities or experiences?",
#                         'question_slug': 'spontaneity-new-experiences',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "How often do you currently engage in hobbies or activities that bring you joy?",
#                         'question_slug': 'frequency-joyful-activities',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "How much time per week do you currently dedicate to activities like traveling, crafting, sports, or other personal hobbies?",
#                         'question_slug': 'time-dedicated-various-activities',
#                         'type': 'range-hours-0-10'
#                     },
#                     {
#                         "question_text": "Are you interested in setting specific goals to prioritize hobbies or activities?",
#                         'question_slug': 'interest-goals-prioritizing-hobbies',
#                         'type': 'yes-no'
#                     },
#                     {
#                         "question_text": "Do you feel motivated to make time for hobbies or activities that you haven’t yet explored?",
#                         'question_slug': 'interest-make-time-new-activities',
#                         'type': 'yes-no'
#                     },
#                     # {
#                     #     "question_text": "Describe an activity or hobby you’ve always wanted to explore but haven’t yet started.",
#                     #     'slug': 'describe-unexplored-activity',
#                     #     'type': 'open-ended'
#                     # },
#                     # {
#                     #     "question_text": "What barriers, if any, prevent you from engaging in your preferred hobbies or activities?",
#                     #     'slug': 'barriers-to-hobbies',
#                     #     'type': 'open-ended'
#                     # }
#                 ]
#             },
#             {
#                 'topic_slug': 'adventure-travel',
#                 'questions': [
#                     {
#                         "question_text": "How interested are you in traveling to remote or adventurous locations?",
#                         'question_slug': 'interest-remote-travel',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "How often do you participate in outdoor adventure activities like hiking, camping, or mountain climbing?",
#                         'question_slug': 'frequency-adventure-activities',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "Are you interested in trying extreme sports or adventure travel?",
#                         'question_slug': 'interest-extreme-sports',
#                         'type': 'yes-no'
#                     }
#                 ]
#             },
#             {
#                 'topic_slug': 'family-group-events',
#                 'questions': [
#                     {
#                         "question_text": "How often do you plan events or activities with family or friends?",
#                         'question_slug': 'frequency-family-friend-events',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "What is your interest level in organizing group activities such as reunions or community events?",
#                         'question_slug': 'interest-group-activities-community-events',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "Do you enjoy being part of group activities or social gatherings?",
#                         'question_slug': 'enjoyment-group-social-activities',
#                         'type': 'yes-no'
#                     }
#                 ]
#             },
#             {
#                 'topic_slug': 'cultural-exploration',
#                 'questions': [
#                     {
#                         "question_text": "How often do you seek out new cultural experiences (e.g., art exhibits, music, cuisine)?",
#                         'question_slug': 'frequency-new-cultural-experiences',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "How interested are you in learning about different cultures or traditions?",
#                         'question_slug': 'interest-cultures-traditions',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "Are you open to trying new foods, art forms, or cultural events?",
#                         'question_slug': 'interest-new-foods-events',
#                         'type': 'yes-no'
#                     }
#                 ]
#             },
#             {
#                 'topic_slug': 'special-events',
#                 'questions': [
#                     {
#                         "question_text": "How often do you plan or attend special events (e.g., weddings, concerts, parties)?",
#                         'question_slug': 'frequency-plan-attend-special-events',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "How much do you enjoy organizing or hosting special events?",
#                         'question_slug': 'enjoyment-organizing-hosting-special-events',
#                         'type': 'scale-1-5'
#                     }
#                 ]
#             },
#             {
#                 'topic_slug': 'competitive-events',
#                 'questions': [
#                     {
#                         "question_text": "How often do you participate in competitive events such as races or tournaments?",
#                         'question_slug': 'frequency-competitions',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "How interested are you in training for or competing in an event?",
#                         'question_slug': 'interest-training-competitive-events',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "Do you have specific competitive goals you would like to achieve?",
#                         'question_slug': 'specific-competitive-goals',
#                         'type': 'yes-no'
#                     }
#                 ]
#             },
#             {
#                 'topic_slug': 'bucket-list',
#                 'questions': [
#                     {
#                         "question_text": "How often do you think about your bucket list goals or dreams?",
#                         'question_slug': 'frequency-thinking-goals-dreams',
#                         'type': 'frequency'
#                     },
#                     {
#                         "question_text": "How interested are you in working towards checking off items from your bucket list?",
#                         'question_slug': 'interest-checking-off-bucket-list',
#                         'type': 'scale-1-5'
#                     },
#                     {
#                         "question_text": "Do you feel motivated to take steps towards achieving your bucket list dreams?",
#                         'question_slug': 'motivation-bucket-list-dreams',
#                         'type': 'yes-no'
#                     }
#                 ]
#             }
#         ]

#         # Prepare the batched queries for each survey_topic_id
#         batched_data = {}

#         # Iterate over each topic and its questions
#         for topic in survey_question_data:
#             survey_topic_data = {
#                 'topic_slug': topic['topic_slug']
#             }
#             query = "SELECT id FROM survey_topics WHERE topic_slug = %(topic_slug)s"
            
#             result = UserSurvey.db.query_db(query, survey_topic_data)

#             if result:
#                 survey_topic_id = result[0]['id']
#             else:
#                 print(f"No survey_topic found for slug: {survey_topic_data['topic_slug']}")

#             for question in topic['questions']:
#                 answer_data = []
#                 answer_type = question['type']
                
#                 if 'examples' in question:
#                     for answer in question['examples']:
#                         answer_data.append({
#                             'answer_type': answer_type,
#                             'answer_text': answer.get('answer_text', ''), 
#                             'answer_value': answer.get('answer_value')
#                         })

#                 question_data = {
#                     'survey_topic_id': survey_topic_id,
#                     'question_slug': question['question_slug'], 
#                     'question_text': question['question_text'],
#                     'type': question['type'],
#                     'answers': answer_data
#                 }

#                 # Batch questions by topic_id
#                 if survey_topic_id not in batched_data:
#                     batched_data[survey_topic_id] = []

#                 batched_data[survey_topic_id].append(question_data)

#         # print("*****BATCHED DATA*****")
#         # pprint(batched_data)

#         return batched_data
        

#     @classmethod
#     def survey_question_seed(cls, batched_data):

#         for survey_topic_id, questions in batched_data.items():
#             query = """
#                 INSERT INTO survey_questions (survey_topic_id, question_slug, question_text, type, created_at, updated_at)
#                 VALUES %s
#                 ON DUPLICATE KEY UPDATE updated_at = NOW();
#             """
#             # Prepare values for each question
#             query_values = [
#                 (question['survey_topic_id'], question['question_slug'], question['question_text'], question['type']) for question in questions
#             ]

#             # Build the placeholders for each question (MySQL-style batch insert)
#             query_values_placeholder = ', '.join(['(%s, %s, %s, %s, NOW(), NOW())' for _ in query_values])

#             # Format the final query
#             final_query = query % query_values_placeholder

#             # Flatten the parameters list for the batch execution
#             parameters = [item for sublist in query_values for item in sublist]

#             try:
#                 # Execute the query using the database connection
#                 UserSurvey.db.query_db(final_query, parameters)
#                 print("Survey questions seeded successfully!")
#             except Exception as e:
#                 print(f"Error while inserting questions for topic {survey_topic_id}: {e}")

# # TODO: ADDRESS GENERIC ANSWER FORMATS, NEW FUNCTION FOR THESE QUESTION TYPES?
# # QUERY FOR ANSWERS MATCHING ANSWER_TYPE
# # FOR ANSWER IN ANSWERS:
# # SEED MANY-TO-MANY TABLE WITH IDS
#     @classmethod
#     def process_survey_question_and_map_data(cls, batched_data):
#         # These lists will hold mappings for different types of answers
#         custom_survey_question_answer_map_data = []
#         generic_survey_question_answer_map_data = []

#         # Process each question and separate them based on answer type
#         for survey_topic_id, questions in batched_data.items():
#             for question in questions:
#                 survey_question_id = UserSurvey._get_survey_question_id(survey_topic_id, question['question_slug'])
#                 if not survey_question_id:
#                     print(f"Could not retrieve survey question ID for topic {survey_topic_id}, question {question['question_slug']}")
#                     continue
                
#                 answers = question.get('answers', [])
#                 if answers:
#                     UserSurvey.prepare_answer_data(
#                         answers, survey_question_id, 
#                         custom_survey_question_answer_map_data
#                     )
#                 else:
#                     UserSurvey._categorize_generic_question(
#                         question, survey_question_id, generic_survey_question_answer_map_data
#                     )

#         # Seed custom answers
#         UserSurvey.seed_custom_question_answer_map(custom_survey_question_answer_map_data)
        
#         # Seed generic answers
#         UserSurvey.seed_generic_question_answer_map(generic_survey_question_answer_map_data)


#     @classmethod
#     def _get_survey_question_id(cls, survey_topic_id, question_slug):
#         query = """
#             SELECT id FROM survey_questions
#             WHERE survey_topic_id = %(survey_topic_id)s AND question_slug = %(question_slug)s;
#         """
#         try:
#             result = UserSurvey.db.query_db(query, {
#                 'survey_topic_id': survey_topic_id, 
#                 'question_slug': question_slug
#             })
#             return result[0]['id'] if result else None
#         except Exception as e:
#             print(f"Error retrieving survey question ID for topic {survey_topic_id}: {e}")
#             return None


#     @classmethod
#     def prepare_answer_data(cls, answers, survey_question_id, custom_answer_map_data):
#         """
#         Prepare custom answer data to be seeded in the database. 
#         This function both inserts new answers and maps them to survey questions.
#         """
#         answer_query = """
#             INSERT INTO survey_answers (answer_type, answer_text, answer_value, created_at, updated_at)
#             VALUES (%(answer_type)s, %(answer_text)s, %(answer_value)s, NOW(), NOW())
#             ON DUPLICATE KEY UPDATE updated_at = NOW();
#         """
        
#         for answer in answers:
#             answer_id = cls._insert_answer(answer, answer_query)
#             if answer_id:
#                 custom_answer_map_data.append({
#                     'survey_question_id': survey_question_id,
#                     'survey_answer_id': answer_id
#                 })


#     @classmethod
#     def _insert_answer(cls, answer, answer_query):
#         """
#         Insert an individual answer and return its ID if successful.
#         """
#         try:
#             result = UserSurvey.db.query_db(answer_query, {
#                 'answer_type': answer['answer_type'],
#                 'answer_text': answer['answer_text'],
#                 'answer_value': answer['answer_value']
#             })
#             return result if result else None
#         except Exception as e:
#             print(f"Error inserting answer: {e}")
#             return None


#     @classmethod
#     def _categorize_generic_question(cls, question, survey_question_id, generic_answer_map_data):
#         """
#         Add generic questions to a separate list for processing later.
#         """
#         custom_answer_types = ['open-answer', 'guided-choice', 'select-any', 'select-any-add']
#         if question['type'] not in custom_answer_types:
#             query = """
#                 SELECT id FROM survey_answers WHERE survey_answers.answer_type = %(answer_type)s;
#             """

#             data = {'answer_type': question['type']}

#             results = UserSurvey.db.query_db(query, data)
#             if results:
#                 for result in results:
#                     survey_answer_id = result['id']
            
#                     generic_answer_map_data.append({
#                         'survey_question_id': survey_question_id,
#                         'survey_answer_id': survey_answer_id  # To be filled in later if applicable
#                     })


#     @classmethod
#     def seed_custom_question_answer_map(cls, custom_answer_map_data):
#         """
#         Seed the database with mappings for custom answers.
#         """
#         map_query = """
#             INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
#             VALUES (%(survey_question_id)s, %(survey_answer_id)s)
#             ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
#         """
#         try:
#             for params in custom_answer_map_data:
#                 UserSurvey.db.query_db(map_query, params)
#         except Exception as e:
#             print(f"Error inserting custom mappings: {e}")


#     @classmethod
#     def seed_generic_question_answer_map(cls, generic_answer_map_data):
#         """
#         Seed the database with mappings for generic answers.
#         """
#         map_query = """
#             INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
#             VALUES (%(survey_question_id)s, %(survey_answer_id)s)
#             ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
#         """
#         try:
#             for params in generic_answer_map_data:
#                 UserSurvey.db.query_db(map_query, params)
#         except Exception as e:
#             print(f"Error inserting generic mappings: {e}")


#     # @classmethod
#     # def survey_custom_answer_seed(cls, batched_data):
#     #     custom_answer_types = ['open-answer', 'guided-choice', 'select-any', 'select-any-add']

#     #     for survey_topic_id, questions in batched_data.items():
#     #         for question in questions:
#     #             # print("*****Question in survey_custom_answer_seed****")
#     #             # pprint(question)
                
#     #             query = """
#     #                 SELECT id FROM survey_questions
#     #                 WHERE survey_topic_id = %(survey_topic_id)s AND question_slug = %(question_slug)s;
#     #             """
#     #             survey_question_data = {
#     #                 'survey_topic_id': survey_topic_id, 
#     #                 'question_slug': question['question_slug']
#     #             }
#     #             try:
#     #                 question_results = UserSurvey.db.query_db(query, survey_question_data)[0]['id']
#     #                 if question_results:
#     #                     survey_question_id = question_results
#     #                 else:
#     #                     print("No survey question ID found. Please check the query and data.")

#     #             except Exception as e:
#     #                 print(f"Error retrieving survey_question_id: {e}")
#     #                 continue  # Skip this iteration if there's an issue

#     #             answers = question.get('answers', [])
#     #             if answers:
#     #                 answer_query = """
#     #                     INSERT INTO survey_answers (answer_type, answer_text, answer_value, created_at, updated_at)
#     #                     VALUES (%(answer_type)s, %(answer_text)s, %(answer_value)s, NOW(), NOW())
#     #                     ON DUPLICATE KEY UPDATE updated_at = NOW();
#     #                 """

#     #                 query_values = [
#     #                     {
#     #                         'answer_type': answer['answer_type'], 
#     #                         'answer_text': answer['answer_text'],
#     #                         'answer_value': answer['answer_value']
#     #                     } 
#     #                     for answer in answers]
#     #                 # print("*****query_values: *****")
#     #                 # pprint(query_values)

#     #                 custom_survey_question_answer_map_data = []
#     #                 generic_survey_question_answer_map_data = []

#     #                 try:
#     #                     for params in query_values:
#     #                         # print("*****survey_answer_id*****")
#     #                         # print(UserSurvey.db.query_db(answer_query, params))
#     #                         answer_results = UserSurvey.db.query_db(answer_query, params)
#     #                         if answer_results:
#     #                             survey_answer_id = answer_results
#     #                         else:
#     #                             print("No survey answer ID found. Please check the query and data.")
                            
#     #                         survey_question_answer_ids = {
#     #                             'survey_question_id': survey_question_id, 
#     #                             'survey_answer_id': survey_answer_id
#     #                         }
#     #                         custom_survey_question_answer_map_data.append(survey_question_answer_ids)
#     #                     print(f"Examples for question {survey_question_id} seeded successfully!")
#     #                 except Exception as e:
#     #                     print(f"Error while inserting answers for question {survey_question_id}: {e}")
            
#     #                 map_query = """
#     #                     INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
#     #                     VALUES (%(survey_question_id)s, %(survey_answer_id)s)
#     #                     ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
#     #                 """

#     #                 try:
#     #                     for params in custom_survey_question_answer_map_data:
#     #                         UserSurvey.db.query_db(map_query, params)
#     #                 except Exception as e:
#     #                     print(f"Error while inserting answers for question {survey_question_id}: {e}")
#     #             else:
#     #                 if question['type'] not in custom_answer_types:
#     #                     generic_survey_question_answer_map_data.append(question)
#     #     UserSurvey.question_answer_map_seed_generic_answers(generic_survey_question_answer_map_data)
    
#     # @classmethod
#     # def question_answer_map_seed_generic_answers(cls, question_answer_map_data):
#     #     # survey_question_answer_ids = {
#     #     #                     'survey_question_id': question_answer_map_data['survey_question_id'], 
#     #     #                     'survey_answer_id': question_answer_map_data['survey_answer_id']
#     #     #                 }
        
#     #     map_query = """
#     #                 INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
#     #                 VALUES (%(survey_question_id)s, %(survey_answer_id)s)
#     #                 ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
#     #             """
#     #     try:
#     #         for params in question_answer_map_data:
#     #             UserSurvey.db.query_db(map_query, params)
#     #     except Exception as e:
#     #         print(f"Error while inserting answers for question {question_answer_map_data['survey_question_id']}: {e}")

#     @classmethod
#     def survey_generic_answer_seed(cls):
#         # Answers data with dynamic mappings for questions
#         survey_answers_data = [
#             # SELECT ANY/ALL, OPEN ANSWER, and GUIDED CHOICE ANSWERS
#             # {
#             #     'answer_type': 'open-answer', 
#             #     'answers': [
#             #         {'answer_text': None, "answer_value": 0}
#             #     ]
#             # },
#             {
#                 'answer_type': 'select-any', 
#                 'answers': [
#                     {'answer_text': None, "answer_value": 0}
#                 ]
#             },
#             {
#                 'answer_type': 'select-any-add', 
#                 'answers': [
#                     {'answer_text': None, "answer_value": 0}
#                 ]
#             },
#             {
#                 'answer_type': 'guided-choice', 
#                 'answers': [
#                     {'answer_text': None, "answer_value": 0}
#                 ]
#             },
#             # YES/NO and ANSWERS
#             {
#                 'answer_type': 'yes-no',
#                 'answers': [
#                     {"answer_text": "Yes", "answer_value": 1},
#                     {"answer_text": "No", "answer_value": 0}
#                 ]
#             },
#             {
#                 'answer_type': 'true-false',
#                 'answers': [
#                     {"answer_text": "True", "answer_value": 1},
#                     {"answer_text": "False", "answer_value": 0}
#                 ]
#             },

#             #  SCALE ANSWER SETS

#             # Scale 1-5 Answers
#             {
#                 'answer_type': 'scale-1-5',
#                 'answers': [
#                     {"answer_text": "1 - Strongly Disagree", "answer_value": 1},
#                     {"answer_text": "2 - Disagree", "answer_value": 2},
#                     {"answer_text": "3 - Neutral", "answer_value": 3},
#                     {"answer_text": "4 - Agree", "answer_value": 4},
#                     {"answer_text": "5 - Strongly Agree", "answer_value": 5}
#                 ]
#             },
#             # FREQUENCY ANSWER SETS

#             {
#                 'answer_type': 'frequency',
#                 'answers': [
#                     {"answer_text": "Never/Almost Never", "answer_value": 0},
#                     {"answer_text": "Rarely", "answer_value": 1},
#                     {"answer_text": "Occasionally", "answer_value": 2},
#                     {"answer_text": "Often", "answer_value": 3},
#                     {"answer_text": "Always/Almost Always", "answer_value": 4}
#                 ]
#             },
#             # Opinion-Importance Scale
#             {
#                 'answer_type': 'opinion-importance-scale',
#                 'answers': [
#                     {"answer_text": "Not at all important", "answer_value": 0},
#                     {"answer_text": "Slightly important", "answer_value": 1},
#                     {"answer_text": "Moderately important", "answer_value": 2},
#                     {"answer_text": "Very important", "answer_value": 3},
#                     {"answer_text": "Extremely important", "answer_value": 4}
#                 ]
#             },
#             # RANGE ANSWER SETS
            
#             # Range 0-10
#             {
#                 'answer_type': 'range-hours-0-10',
#                 'answers': [
#                     {"answer_text": "0-1 hour", "answer_value": 0},
#                     {"answer_text": "1-5 hours", "answer_value": 1},
#                     {"answer_text": "5-10 hours", "answer_value": 2},
#                     {"answer_text": "10+ hours", "answer_value": 3}
#                 ]
#             }, 
#             # Range Less 5, Greater 8 Hours
#             {
#                 "survey_question_id": 6,
#                 "answer_type": "range-hours-L5-G8",
#                 "answers": [
#                     {"answer_text": "Less than 5 hours", "answer_value": 1},
#                     {"answer_text": "5-6 hours", "answer_value": 2},
#                     {"answer_text": "7-8 hours", "answer_value": 3},
#                     {"answer_text": "More than 8 hours", "answer_value": 4}
#                 ]
#             }, 
#             {
#                 'answer_type': 'range-hours-sleep',
#                 'answers': [
#                     {"answer_text": "Less than 4 hours", "answer_value": 1},
#                     {"answer_text": "4-6 hours", "answer_value": 2},
#                     {"answer_text": "6-8 hours", "answer_value": 3},
#                     {"answer_text": "8-10 hours", "answer_value": 4},
#                     {"answer_text": "More than 10 hours", "answer_value": 5}

#                 ]
#             }, 

#             # SATISFACTION ANSWERS
            
#             # 
#             {
#                 "survey_question_id": 6,
#                 "answer_type": "satisfaction",
#                 "answers": [
#                     {"answer_text": "Dissatisfied", "answer_value": 0}, 
#                     {"answer_text": "Not very satisfied", "answer_value": 1}, 
#                     {"answer_text": "Neutral", "answer_value": 2},
#                     {"answer_text": "Mostly satisfied", "answer_value": 3},
#                     {"answer_text": "Very satisfied", "answer_value": 4}

#                 ]
#             },

#             # SUPPORT SYSTEM

#             # MULTIPLE CHOICE

#             # Multiple Choice
#             {
#                 "survey_question_id": 5,
#                 "answer_type": "multiple-choice-travel-cat",
#                 "answers": [
#                     {"answer_text": "Adventure Travel", "answer_value": 1},
#                     {"answer_text": "Relaxation and Leisure", "answer_value": 2},
#                     {"answer_text": "Cultural Exploration", "answer_value": 3},
#                     {"answer_text": "Family-Friendly", "answer_value": 4},
#                     {"answer_text": "Luxury Travel", "answer_value": 5}
#                 ]
#             }
#         ]

#         batched_queries = {}
#         question_answer_map = []

#         # Prepare data for batch insertion
#         for answer_set in survey_answers_data:
#             answer_type = answer_set['answer_type']
#             for answer in answer_set['answers']:
#                 # Create answer data structure
#                 answer_data = {
#                     'answer_type': answer_type,
#                     'answer_text': answer['answer_text'],
#                     'answer_value': answer['answer_value'],
#                 }

#                 # Batch answers by slug
#                 if answer_type not in batched_queries:
#                     batched_queries[answer_type] = []

#                 batched_queries[answer_type].append(answer_data)

#         # Build and execute the batch insert queries for survey_answers
#         for answer_type, answers in batched_queries.items():
#             query = """
#                 INSERT INTO survey_answers (answer_type, answer_text, answer_value, created_at, updated_at)
#                 VALUES %s
#                 ON DUPLICATE KEY UPDATE updated_at = NOW();
#             """
#             # Convert the list of tuples into a format MySQL can handle
#             query_values = [
#                 (a['answer_type'], a['answer_text'], a['answer_value']) for a in answers
#             ]
            
#             # Placeholder for each answer row
#             query_values_placeholder = ', '.join(['(%s, %s, %s, NOW(), NOW())' for _ in query_values])
            
#             final_query = query % query_values_placeholder
#             parameters = [item for sublist in query_values for item in sublist]
            
#             UserSurvey.db.query_db(final_query, parameters)

#         # Insert the mappings into the intermediate table
#         if question_answer_map:
#             map_query = """
#                 INSERT INTO question_answer_map (survey_question_id, survey_answer_id, created_at, updated_at)
#                 VALUES %s
#             """
#             map_query_values = [
#                 (mapping['survey_question_id'], mapping['answer_id']) for mapping in question_answer_map
#             ]
            
#             map_query_placeholder = ', '.join(['(%s, %s, NOW(), NOW())' for _ in map_query_values])
            
#             final_map_query = map_query % map_query_placeholder
#             map_parameters = [item for sublist in map_query_values for item in sublist]
            
#             UserSurvey.db.query_db(final_map_query, map_parameters)

#         print("Survey answers and mappings seeded successfully!")



#     @classmethod
#     def get_all_survey_category_ids(cls):
#         query = "SELECT id, category_slug FROM survey_categories"
        
#         # Fetch all category ids and names
#         results = UserSurvey.db.query_db(query)

#         if not results:  # Handle case where no results are found
#             return {}
#         # Create a dictionary mapping category names to their IDs
#         category_ids = {row['category_slug']: row['id'] for row in results}

#         return category_ids

#     @classmethod
#     def get_all_survey_topic_ids(cls):
#         """
#         Fetch all survey_topic_id and topic_name pairs.
#         Returns a dictionary mapping topic names to topic IDs.
#         """
#         query = "SELECT id, topic_slug FROM survey_topics"
#         results = UserSurvey.db.query_db(query)
        
#         if not results:  # Handle case where no results are found
#             return {}
    
#         return {row['topic_slug']: row['id'] for row in results}
    
#     @classmethod
#     def get_all_survey_question_ids(cls):
#         """
#         Fetch all survey_question_id and survey_answer pairs.
#         Returns a dictionary mapping topic names to topic IDs.
#         """
#         query = "SELECT id, question_text FROM survey_questions"
#         results = UserSurvey.db.query_db(query)
        
#         if not results:  # Handle case where no results are found
#             return {}
    
#         return {row['question_text']: row['id'] for row in results}
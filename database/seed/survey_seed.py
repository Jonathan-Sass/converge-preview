from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session, jsonify, flash, redirect
# import asyncio, aiomysql, logging

from flask_app.models.user import User
from flask_app.models.userSurvey import UserSurvey
# import pymysql
from database.seed.survey_topic_data import survey_topic_data
from database.seed.survey_question_data import survey_question_data

# LOOKS FOR AND SEEDS SURVEY DATA IN DB
def user_survey_seed():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    # REVISIT VALIDATION FOR ENTIRETY OF SEEDING FUNCTIONS
    survey_category_seed()
    survey_topic_seed()
    prepared_question_data = prepare_survey_question_data()
    survey_question_seed(prepared_question_data)
    # Seed generic answers first, custom answers second
    survey_generic_answer_seed()
    process_survey_question_and_map_data(prepared_question_data)
    # survey_answer_seed and survey_example_seed in prepare_survey_question_data

    return


def survey_category_seed():
    query = """
        INSERT INTO survey_categories (category_slug, name, created_at, updated_at)
        VALUES
            ('foundations', 'Foundations', NOW(), NOW()),
            ('your-why', 'Defining Your Why', NOW(), NOW()),
            ('health-wellness', 'Health and Wellness', NOW(), NOW()),
            ('social-community', 'Social and Community Engagement', NOW(), NOW()),
            ('recreation-travel', 'Recreation and Travel', NOW(), NOW()),
            ('spirituality-life-purpose', 'Spirituality and Life Purpose', NOW(), NOW()),
            ('career-professional-development', 'Career and Professional Development', NOW(), NOW()),
            ('creative-expression-hobbies', 'Creative Expression and Hobbies', NOW(), NOW()),
            ('wealth-finance', 'Wealth Building and Financial Health', NOW(), NOW()),
            ('environment-success', 'Environment and Success', NOW(), NOW())
        ON DUPLICATE KEY UPDATE updated_at = NOW();
            """
    UserSurvey.db.query_db(query)

    # Temporary secondary query to seed goal related categories, merge pending
    query_2 = """
        INSERT INTO categories (category_slug, name, created_at, updated_at)
        VALUES
            ('foundations', 'Foundations', NOW(), NOW()),
            ('your-why', 'Defining Your Why', NOW(), NOW()),
            ('health-wellness', 'Health and Wellness', NOW(), NOW()),
            ('social-community', 'Social and Community Engagement', NOW(), NOW()),
            ('recreation-travel', 'Recreation and Travel', NOW(), NOW()),
            ('spirituality-life-purpose', 'Spirituality and Life Purpose', NOW(), NOW()),
            ('career-professional-development', 'Career and Professional Development', NOW(), NOW()),
            ('creative-expression-hobbies', 'Creative Expression and Hobbies', NOW(), NOW()),
            ('wealth-finance', 'Wealth Building and Financial Health', NOW(), NOW()),
            ('environment-success', 'Environment and Success', NOW(), NOW())
        ON DUPLICATE KEY UPDATE updated_at = NOW();
            """
    UserSurvey.db.query_db(query_2)

def survey_topic_seed():
    # Fetch all survey_topic_id and topic_name pairs once

    batch_data = {}

    # Organize topics into batches by category (key)
    for category_slug, topics in survey_topic_data.items():
        for topic in topics:
            if category_slug not in batch_data:
                batch_data[category_slug] = []
            batch_data[category_slug].append({
                'topic_slug': topic['topic_slug'],
                'topic_name': topic['name']
            })

    # Retrieve the mapping of category slugs to category IDs
    survey_category_ids = get_all_survey_category_ids()  # Should return a dictionary like {'health-wellness': 1, 'social-community': 2, ...}

    # Prepare and execute batch insert queries for each category
    for category_slug, topic_batch in batch_data.items():
        # Check if the category slug exists in the retrieved category IDs
        if category_slug in survey_category_ids:
            survey_category_id = survey_category_ids[category_slug]
        else:
            print(f"Category slug '{category_slug}' not found in the database.")
            continue  # Skip this category if the ID is not found

        # Create the base query
        query = "INSERT INTO survey_topics (survey_category_id, topic_slug, name, created_at, updated_at) VALUES "
        query_values = []

        # Temporary secondary seed to subcategories, merge pending
        query_2 = "INSERT INTO subcategories (category_id, subcategory_slug, name, created_at, updated_at) VALUES "
        query_values_2 = []

        # Add the topic values to the query
        for topic in topic_batch:
            values = f"({survey_category_id}, '{topic['topic_slug']}', '{topic['topic_name']}', NOW(), NOW())"
            query_values.append(values)

            # # Temporary secondary snippet, merge pending, OOPS, REDUNDANT?
            # values_2 = f"({survey_category_id}, '{topic['topic_slug']}', '{topic['topic_name']}', NOW(), NOW())"
            # query_values_2.append(values_2)

        # Combine the query and execute it
        query += ", ".join(query_values)
        query += " ON DUPLICATE KEY UPDATE updated_at = NOW();"
        
        # TEMPORARY SECONDARY SNIPPET, MERGE PENDING
        query_2 += ", ".join(query_values)
        query_2 += " ON DUPLICATE KEY UPDATE updated_at = NOW();"

        # Execute the query using your database method
        UserSurvey.db.query_db(query)

        # TEMPORARY SECONDARY QUERY, MERGE PENDING
        UserSurvey.db.query_db(query_2)

    print(f"{sum(len(v) for v in survey_topic_data.values())} survey topics have been seeded.")


def prepare_survey_question_data():
# ADD QUESTIONS ABOUT SCREEN TIME AND DOPAMINE RELATED DESIRES/DRIVERS/RESPONSES
    

    # Prepare the batched queries for each survey_topic_id
    batched_data = {}

    # Iterate over each topic and its questions
    for topic in survey_question_data:
        survey_topic_data = {
            'topic_slug': topic['topic_slug']
        }
        query = "SELECT id FROM survey_topics WHERE topic_slug = %(topic_slug)s"
        
        result = UserSurvey.db.query_db(query, survey_topic_data)

        if result:
            survey_topic_id = result[0]['id']
        else:
            print(f"No survey_topic found for slug: {survey_topic_data['topic_slug']}")

        for question in topic['questions']:
            answer_data = []
            answer_type = question['type']
            
            if 'answers' in question:
                for answer in question['answers']:
                    answer_data.append({
                        'answer_type': answer_type,
                        'answer_text': answer.get('answer_text', ''), 
                        'answer_value': answer.get('answer_value')
                    })

            question_data = {
                'survey_topic_id': survey_topic_id,
                'question_slug': question['question_slug'], 
                'question_text': question['question_text'],
                'type': question['type'],
                'answers': answer_data
            }

            # Batch questions by topic_id
            if survey_topic_id not in batched_data:
                batched_data[survey_topic_id] = []

            batched_data[survey_topic_id].append(question_data)

    # print("*****BATCHED DATA*****")
    # pprint(batched_data)

    return batched_data
    


def survey_question_seed(batched_data):

    for survey_topic_id, questions in batched_data.items():
        query = """
            INSERT INTO survey_questions (survey_topic_id, question_slug, question_text, type, created_at, updated_at)
            VALUES %s
            ON DUPLICATE KEY UPDATE 
                survey_topic_id = VALUES(survey_topic_id),
                question_slug = question_slug,
                question_text = question_text,
                type = VALUES(type),
                updated_at = NOW();
        """
        # Prepare values for each question
        query_values = [
            (question['survey_topic_id'], question['question_slug'], question['question_text'], question['type']) for question in questions
        ]

        # Build the placeholders for each question (MySQL-style batch insert)
        query_values_placeholder = ', '.join(['(%s, %s, %s, %s, NOW(), NOW())' for _ in query_values])

        # Format the final query
        final_query = query % query_values_placeholder

        # Flatten the parameters list for the batch execution
        parameters = [item for sublist in query_values for item in sublist]

        try:
            # Execute the query using the database connection
            UserSurvey.db.query_db(final_query, parameters)
            print("Survey questions seeded successfully!")
        except Exception as e:
            print(f"Error while inserting questions for topic {survey_topic_id}: {e}")

# TODO: ADDRESS GENERIC ANSWER FORMATS, NEW FUNCTION FOR THESE QUESTION TYPES?
# QUERY FOR ANSWERS MATCHING ANSWER_TYPE
# FOR ANSWER IN ANSWERS:
# SEED MANY-TO-MANY TABLE WITH IDS

def process_survey_question_and_map_data(batched_data):
    # These lists will hold mappings for different types of answers
    custom_survey_question_answer_map_data = []
    generic_survey_question_answer_map_data = []

    # Process each question and separate them based on answer type
    for survey_topic_id, questions in batched_data.items():
        for question in questions:
            survey_question_id = _get_survey_question_id(survey_topic_id, question['question_slug'])
            if not survey_question_id:
                print(f"Could not retrieve survey question ID for topic {survey_topic_id}, question {question['question_slug']}")
                continue
            
            answers = question.get('answers', [])
            if answers:
                prepare_answer_data(
                    answers, survey_question_id, 
                    custom_survey_question_answer_map_data
                )
            else:
                _categorize_generic_question(
                    question, survey_question_id, generic_survey_question_answer_map_data
                )

    # Seed custom answers
    seed_custom_question_answer_map(custom_survey_question_answer_map_data)
    
    # Seed generic answers
    seed_generic_question_answer_map(generic_survey_question_answer_map_data)



def _get_survey_question_id(survey_topic_id, question_slug):
    query = """
        SELECT id FROM survey_questions
        WHERE survey_topic_id = %(survey_topic_id)s AND question_slug = %(question_slug)s;
    """
    try:
        result = UserSurvey.db.query_db(query, {
            'survey_topic_id': survey_topic_id, 
            'question_slug': question_slug
        })
        return result[0]['id'] if result else None
    except Exception as e:
        print(f"Error retrieving survey question ID for topic {survey_topic_id}: {e}")
        return None



def prepare_answer_data(answers, survey_question_id, custom_answer_map_data):
    """
    Prepare custom answer data to be seeded in the database. 
    This function both inserts new answers and maps them to survey questions.
    """
    answer_query = """
        INSERT INTO survey_answers (answer_type, answer_text, answer_value, created_at, updated_at)
        VALUES (%(answer_type)s, %(answer_text)s, %(answer_value)s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE updated_at = NOW();
    """
    
    for answer in answers:
        answer_id = _insert_answer(answer, answer_query)
        if answer_id:
            custom_answer_map_data.append({
                'survey_question_id': survey_question_id,
                'survey_answer_id': answer_id
            })



def _insert_answer(answer, answer_query):
    """
    Insert an individual answer and return its ID if successful.
    """
    try:
        result = UserSurvey.db.query_db(answer_query, {
            'answer_type': answer['answer_type'],
            'answer_text': answer['answer_text'],
            'answer_value': answer['answer_value']
        })
        return result if result else None
    except Exception as e:
        print(f"Error inserting answer: {e}")
        return None



def _categorize_generic_question(question, survey_question_id, generic_answer_map_data):
    """
    Add generic questions to a separate list for processing later.
    """
    custom_answer_types = ['open-answer', 'guided-choice', 'select-any', 'select-any-add']
    if question['type'] not in custom_answer_types:
        query = """
            SELECT id FROM survey_answers WHERE survey_answers.answer_type = %(answer_type)s;
        """

        data = {'answer_type': question['type']}

        results = UserSurvey.db.query_db(query, data)
        if results:
            for result in results:
                survey_answer_id = result['id']
        
                generic_answer_map_data.append({
                    'survey_question_id': survey_question_id,
                    'survey_answer_id': survey_answer_id  # To be filled in later if applicable
                })



def seed_custom_question_answer_map(custom_answer_map_data):
    """
    Seed the database with mappings for custom answers.
    """
    map_query = """
        INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
        VALUES (%(survey_question_id)s, %(survey_answer_id)s)
        ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
    """
    try:
        for params in custom_answer_map_data:
            UserSurvey.db.query_db(map_query, params)
    except Exception as e:
        print(f"Error inserting custom mappings: {e}")



def seed_generic_question_answer_map(generic_answer_map_data):
    """
    Seed the database with mappings for generic answers.
    """
    map_query = """
        INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
        VALUES (%(survey_question_id)s, %(survey_answer_id)s)
        ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
    """
    try:
        for params in generic_answer_map_data:
            UserSurvey.db.query_db(map_query, params)
    except Exception as e:
        print(f"Error inserting generic mappings: {e}")


# 
# def survey_custom_answer_seed(batched_data):
#     custom_answer_types = ['open-answer', 'guided-choice', 'select-any', 'select-any-add']

#     for survey_topic_id, questions in batched_data.items():
#         for question in questions:
#             # print("*****Question in survey_custom_answer_seed****")
#             # pprint(question)
            
#             query = """
#                 SELECT id FROM survey_questions
#                 WHERE survey_topic_id = %(survey_topic_id)s AND question_slug = %(question_slug)s;
#             """
#             survey_question_data = {
#                 'survey_topic_id': survey_topic_id, 
#                 'question_slug': question['question_slug']
#             }
#             try:
#                 question_results = UserSurvey.db.query_db(query, survey_question_data)[0]['id']
#                 if question_results:
#                     survey_question_id = question_results
#                 else:
#                     print("No survey question ID found. Please check the query and data.")

#             except Exception as e:
#                 print(f"Error retrieving survey_question_id: {e}")
#                 continue  # Skip this iteration if there's an issue

#             answers = question.get('answers', [])
#             if answers:
#                 answer_query = """
#                     INSERT INTO survey_answers (answer_type, answer_text, answer_value, created_at, updated_at)
#                     VALUES (%(answer_type)s, %(answer_text)s, %(answer_value)s, NOW(), NOW())
#                     ON DUPLICATE KEY UPDATE updated_at = NOW();
#                 """

#                 query_values = [
#                     {
#                         'answer_type': answer['answer_type'], 
#                         'answer_text': answer['answer_text'],
#                         'answer_value': answer['answer_value']
#                     } 
#                     for answer in answers]
#                 # print("*****query_values: *****")
#                 # pprint(query_values)

#                 custom_survey_question_answer_map_data = []
#                 generic_survey_question_answer_map_data = []

#                 try:
#                     for params in query_values:
#                         # print("*****survey_answer_id*****")
#                         # print(UserSurvey.db.query_db(answer_query, params))
#                         answer_results = UserSurvey.db.query_db(answer_query, params)
#                         if answer_results:
#                             survey_answer_id = answer_results
#                         else:
#                             print("No survey answer ID found. Please check the query and data.")
                        
#                         survey_question_answer_ids = {
#                             'survey_question_id': survey_question_id, 
#                             'survey_answer_id': survey_answer_id
#                         }
#                         custom_survey_question_answer_map_data.append(survey_question_answer_ids)
#                     print(f"Examples for question {survey_question_id} seeded successfully!")
#                 except Exception as e:
#                     print(f"Error while inserting answers for question {survey_question_id}: {e}")
        
#                 map_query = """
#                     INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
#                     VALUES (%(survey_question_id)s, %(survey_answer_id)s)
#                     ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
#                 """

#                 try:
#                     for params in custom_survey_question_answer_map_data:
#                         UserSurvey.db.query_db(map_query, params)
#                 except Exception as e:
#                     print(f"Error while inserting answers for question {survey_question_id}: {e}")
#             else:
#                 if question['type'] not in custom_answer_types:
#                     generic_survey_question_answer_map_data.append(question)
#     question_answer_map_seed_generic_answers(generic_survey_question_answer_map_data)

# 
# def question_answer_map_seed_generic_answers(question_answer_map_data):
#     # survey_question_answer_ids = {
#     #                     'survey_question_id': question_answer_map_data['survey_question_id'], 
#     #                     'survey_answer_id': question_answer_map_data['survey_answer_id']
#     #                 }
    
#     map_query = """
#                 INSERT INTO survey_question_answer_map (survey_question_id, survey_answer_id)
#                 VALUES (%(survey_question_id)s, %(survey_answer_id)s)
#                 ON DUPLICATE KEY UPDATE survey_question_id = survey_question_id;
#             """
#     try:
#         for params in question_answer_map_data:
#             UserSurvey.db.query_db(map_query, params)
#     except Exception as e:
#         print(f"Error while inserting answers for question {question_answer_map_data['survey_question_id']}: {e}")


def survey_generic_answer_seed():
    # Answers data with dynamic mappings for questions
    survey_answers_data = [
        # SELECT ANY/ALL, OPEN ANSWER, and GUIDED CHOICE ANSWERS - DEPRECATED?
        # {
        #     'answer_type': 'open-answer', 
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # {
        #     'answer_type': 'select-any', 
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # {
        #     'answer_type': 'select-any-add', 
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # {
        #     'answer_type': 'guided-choice', 
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # YES/NO and ANSWERS
        {
            'answer_type': 'yes-no',
            'answers': [
                {"answer_text": "Yes", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'yes-no-sometimes',
            'answers': [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "Sometimes", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'yes-no-unsure',
            'answers': [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "I am not sure", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'yes-no-alittle',
            'answers': [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "Maybe a little", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'yes-no-inconsistent',
            'answers': [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "Yes, but it's inconsistent", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'true-false',
            'answers': [
                {"answer_text": "True", "answer_value": 1},
                {"answer_text": "False", "answer_value": 0}
            ]
        },

        #  SCALE ANSWER SETS

        # Scale 1-5 Answers
        {
            'answer_type': 'scale-agree-disagree',
            'answers': [
                {"answer_text": "Strongly Agree", "answer_value": 4},
                {"answer_text": "Agree", "answer_value": 3},
                {"answer_text": "Neutral", "answer_value": 2},
                {"answer_text": "Disagree", "answer_value": 1},
                {"answer_text": "Strongly Disagree", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'scale-interest',
            'answers': [
                {"answer_text": "Very Interested", "answer_value": 4},
                {"answer_text": "Interested", "answer_value": 3},
                {"answer_text": "Neutral", "answer_value": 2},
                {"answer_text": "Not Interested", "answer_value": 1},
                {"answer_text": "Not at All Interested", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'scale-stress-resilience',
            'answers': [
                {"answer_text": "Yes, very resilient, I can handle just about anything.", "answer_value": 4},
                {"answer_text": "Mostly resilient, I have a relatively high tolerance to stress", "answer_value": 3},
                {"answer_text": "Moderate, sometimes it is difficult to roll with the punches.", "answer_value": 2},
                {"answer_text": "Not very resilient", "answer_value": 1},
                {"answer_text": "I am easily be overwhelmed by stress", "answer_value": 0}
            ]
        },
        
        
        # FREQUENCY ANSWER SETS
        {
            'answer_type': 'frequency',
            'answers': [
                {"answer_text": "Always/Almost Always", "answer_value": 4},
                {"answer_text": "Frequently", "answer_value": 3},
                {"answer_text": "Sometimes", "answer_value": 2},
                {"answer_text": "Rarely", "answer_value": 1},
                {"answer_text": "Never/Almost Never", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'frequency-often',
            'answers': [
                {"answer_text": "Very Often", "answer_value": 4},
                {"answer_text": "Often", "answer_value": 3},
                {"answer_text": "Sometimes", "answer_value": 2},
                {"answer_text": "Rarely", "answer_value": 1},
                {"answer_text": "Never", "answer_value": 0}
            ]
        },
        {
            'answer_type': 'frequency-day',
            'answers': [
                {"answer_text": "Almost every day", "answer_value": 4},
                {"answer_text": "Most days", "answer_value": 3},
                {"answer_text": "Sometimes", "answer_value": 2},
                {"answer_text": "Rarely", "answer_value": 1},
                {"answer_text": "Never/Almost Never", "answer_value": 0}
            ]
        },

        # Opinion-Importance Scale
        {
            'answer_type': 'opinion-importance-scale',
            'answers': [
                {"answer_text": "Extremely important", "answer_value": 4},
                {"answer_text": "Very important", "answer_value": 3},
                {"answer_text": "Moderately important", "answer_value": 2},
                {"answer_text": "Slightly important", "answer_value": 1},
                {"answer_text": "Not at all important", "answer_value": 0}
            ]
        },
        # RANGE ANSWER SETS
        
        {
            'answer_type': 'range-mins-hours-10-2',
            'answers': [
                {"answer_text": "10 minutes", "answer_value": 0},
                {"answer_text": "20 minutes", "answer_value": 1},
                {"answer_text": "30 minutes", "answer_value": 2},
                {"answer_text": "45 minutes", "answer_value": 3},
                {"answer_text": "1 hour", "answer_value": 4},
                {"answer_text": "90 minutes", "answer_value": 5},
                {"answer_text": "2 hours", "answer_value": 6}
            ]
        }, 
        {
            'answer_type': 'range-hours-0-10+',
            'answers': [
                {"answer_text": "0-1 hour", "answer_value": 0},
                {"answer_text": "1-5 hours", "answer_value": 1},
                {"answer_text": "5-10 hours", "answer_value": 2},
                {"answer_text": "10+ hours", "answer_value": 3}
            ]
        }, 
        {
            'answer_type': 'range-hours-0-20+',
            'answers': [
                {"answer_text": "0-1 hour", "answer_value": 0},
                {"answer_text": "1-5 hours", "answer_value": 1},
                {"answer_text": "5-10 hours", "answer_value": 2},
                {"answer_text": "10-20 hours", "answer_value": 3},
                {"answer_text": "20+ hours", "answer_value": 3}
            ]
        }, 
        # Range Less 5, Greater 8 Hours
        {
            "answer_type": "range-hours-L5-G8",
            "answers": [
                {"answer_text": "Less than 5 hours", "answer_value": 1},
                {"answer_text": "5-6 hours", "answer_value": 2},
                {"answer_text": "7-8 hours", "answer_value": 3},
                {"answer_text": "More than 8 hours", "answer_value": 4}
            ]
        }, 
        {
            'answer_type': 'range-hours-sleep',
            'answers': [
                {"answer_text": "Less than 5 hours", "answer_value": 1},
                {"answer_text": "5-7 hours", "answer_value": 2},
                {"answer_text": "7-8 hours", "answer_value": 3},
                {"answer_text": "8-10 hours", "answer_value": 4},
                {"answer_text": "More than 10 hours", "answer_value": 5}
            ]
        }, 

        # SATISFACTION ANSWERS
        
        {
            "answer_type": "satisfaction",
            "answers": [
                {"answer_text": "Very satisfied", "answer_value": 4},
                {"answer_text": "Mostly satisfied", "answer_value": 3},
                {"answer_text": "Neutral", "answer_value": 2},
                {"answer_text": "Not very satisfied", "answer_value": 1}, 
                {"answer_text": "Dissatisfied", "answer_value": 0}
            ]
        },
        {
            "answer_type": "satisfaction-balance",
            "answers": [
                {"answer_text": "Very balanced", "answer_value": 4},
                {"answer_text": "Mostly balanced", "answer_value": 3},
                {"answer_text": "Could be better", "answer_value": 2},
                {"answer_text": "Not very balanced", "answer_value": 1}, 
                {"answer_text": "Overwhelmed or unbalanced", "answer_value": 0},
            ]
        },

        # SUPPORT SYSTEM

        # MULTIPLE CHOICE

        # Multiple Choice
        {
            "answer_type": "multiple-choice-travel-cat",
            "answers": [
                {"answer_text": "Adventure Travel", "answer_value": 1},
                {"answer_text": "Relaxation and Leisure", "answer_value": 2},
                {"answer_text": "Cultural Exploration", "answer_value": 3},
                {"answer_text": "Family-Friendly", "answer_value": 4},
                {"answer_text": "Luxury Travel", "answer_value": 5}
            ]
        }
    ]

    batched_queries = {}
    question_answer_map = []

    # Prepare data for batch insertion
    for answer_set in survey_answers_data:
        answer_type = answer_set['answer_type']
        for answer in answer_set['answers']:
            # Create answer data structure
            answer_data = {
                'answer_type': answer_type,
                'answer_text': answer['answer_text'],
                'answer_value': answer['answer_value'],
            }

            # Batch answers by slug
            if answer_type not in batched_queries:
                batched_queries[answer_type] = []

            batched_queries[answer_type].append(answer_data)

    # Build and execute the batch insert queries for survey_answers
    for answer_type, answers in batched_queries.items():
        query = """
            INSERT INTO survey_answers (answer_type, answer_text, answer_value, created_at, updated_at)
            VALUES %s
            ON DUPLICATE KEY UPDATE 
                answer_type = answer_type,
                answer_text = answer_text,
                answer_value = VALUES(answer_value),
                updated_at = NOW();
        """
        # Convert the list of tuples into a format MySQL can handle
        query_values = [
            (a['answer_type'], a['answer_text'], a['answer_value']) for a in answers
        ]
        
        # Placeholder for each answer row
        query_values_placeholder = ', '.join(['(%s, %s, %s, NOW(), NOW())' for _ in query_values])
        
        final_query = query % query_values_placeholder
        parameters = [item for sublist in query_values for item in sublist]
        
        UserSurvey.db.query_db(final_query, parameters)

    # Insert the mappings into the intermediate table
    if question_answer_map:
        map_query = """
            INSERT INTO question_answer_map
                (survey_question_id, survey_answer_id, created_at, updated_at)
            VALUES 
                %s
            ON DUPLICATE KEY UPDATE
                updated_at = NOW();
        """
        map_query_values = [
            (mapping['survey_question_id'], mapping['answer_id']) for mapping in question_answer_map
        ]
        
        map_query_placeholder = ', '.join(['(%s, %s, NOW(), NOW())' for _ in map_query_values])
        
        final_map_query = map_query % map_query_placeholder
        map_parameters = [item for sublist in map_query_values for item in sublist]
        
        UserSurvey.db.query_db(final_map_query, map_parameters)

    print("Survey answers and mappings seeded successfully!")




def get_all_survey_category_ids():
    query = "SELECT id, category_slug FROM survey_categories"
    
    # Fetch all category ids and names
    results = UserSurvey.db.query_db(query)

    if not results:  # Handle case where no results are found
        return {}
    # Create a dictionary mapping category names to their IDs
    category_ids = {row['category_slug']: row['id'] for row in results}

    return category_ids


def get_all_survey_topic_ids():
    """
    Fetch all survey_topic_id and topic_name pairs.
    Returns a dictionary mapping topic names to topic IDs.
    """
    query = "SELECT id, topic_slug FROM survey_topics"
    results = UserSurvey.db.query_db(query)
    
    if not results:  # Handle case where no results are found
        return {}

    return {row['topic_slug']: row['id'] for row in results}


def get_all_survey_question_ids():
    """
    Fetch all survey_question_id and survey_answer pairs.
    Returns a dictionary mapping topic names to topic IDs.
    """
    query = "SELECT id, question_text FROM survey_questions"
    results = UserSurvey.db.query_db(query)
    
    if not results:  # Handle case where no results are found
        return {}

    return {row['question_text']: row['id'] for row in results}
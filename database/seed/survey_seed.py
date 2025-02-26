from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask import flash, session, jsonify, flash, redirect

# import asyncio, aiomysql, logging

from flask_app.models.user import User
from flask_app.models.user_survey import UserSurvey

# import pymysql
from database.seed_data.subcategory_data import subcategory_data
from database.seed_data.survey_question_data import survey_question_data
from database.seed_data.generic_survey_answer_data import generic_survey_answer_data
from database.seed_data.survey_branching_data import survey_branching_data

# LOOKS FOR AND SEEDS SURVEY DATA IN DB
def user_survey_seed():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    # REVISIT VALIDATION FOR ENTIRETY OF SEEDING FUNCTIONS
    # goal_category_seed()
    category_seed()
    # goal_subcategory_seed()
    subcategory_seed()
    
    prepared_question_data = prepare_survey_question_data()
    survey_question_seed(prepared_question_data)
    # Seed generic answers first, custom answers second
    generic_survey_answer_seed()
    custom_survey_question_answer_map_data, generic_survey_question_answer_map_data =  process_survey_question_and_map_data(prepared_question_data)

    # Seed generic answers
    seed_generic_question_answer_map(generic_survey_question_answer_map_data)
    # Seed custom answers
    seed_custom_question_answer_map(custom_survey_question_answer_map_data)
    # survey_answer_seed and survey_example_seed in prepare_survey_question_data
    survey_branching_seed(survey_branching_data)

    return

def test_seed():
    category_seed()
    subcategory_seed()

    prepared_question_data = prepare_survey_question_data()
    survey_question_seed(prepared_question_data)
    generic_survey_answer_seed()
    
    custom_survey_question_answer_map_data, generic_survey_question_answer_map_data = process_survey_question_and_map_data(prepared_question_data)
    # Seed generic answers
    seed_generic_question_answer_map(generic_survey_question_answer_map_data)
    # Seed custom answers
    seed_custom_question_answer_map(custom_survey_question_answer_map_data)

    survey_branching_seed(survey_branching_data)

    return


# TODO: survey and goal categories, subcategories and subcategories will be merged.  Temporary independent seed functions until then...
def goal_category_seed():
    query = """
    INSERT INTO categories (category_slug, name, created_at, updated_at)
    VALUES
      ('onboarding', 'Onboarding', NOW(), NOW()),
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

    return


def goal_subcategory_seed():
    batch_data = {}

    # Organize subcategories into batches by category (key)
    for category_slug, subcategories in subcategory_data.items():
        for subcategory in subcategories:
            if category_slug not in batch_data:
                batch_data[category_slug] = []
            batch_data[category_slug].append(
                {"subcategory_slug": subcategory["subcategory_slug"], "subcategory_name": subcategory["name"]}
            )

    # Retrieve the mapping of category slugs to category IDs
    category_ids = (
        get_all_category_ids()
    )  # Should return a dictionary like {'health-wellness': 1, 'social-community': 2, ...}

    # Prepare and execute batch insert queries for each category
    for category_slug, subcategory_batch in batch_data.items():
        # Check if the category slug exists in the retrieved category IDs
        if category_slug in category_ids:
            category_id = category_ids[category_slug]
        else:
            print(f"Category slug '{category_slug}' not found in the database.")
            continue  # Skip this category if the ID is not found

        # Create the base query
        query = "INSERT INTO subcategories (category_id, subcategory_slug, name, created_at, updated_at) VALUES "
        query_values = []

        # Temporary secondary seed to subcategories, merge pending

        # Add the subcategory values to the query
        for subcategory in subcategory_batch:
            values = f"({category_id}, '{subcategory['subcategory_slug']}', '{subcategory['subcategory_name']}', NOW(), NOW())"
            query_values.append(values)

        # Combine the query and execute it
        query += ", ".join(query_values)
        query += " ON DUPLICATE KEY UPDATE updated_at = NOW();"

        # Execute the query using your database method
        UserSurvey.db.query_db(query)

    return


def category_seed():
    query = """
        INSERT INTO categories (category_slug, name, created_at, updated_at)
        VALUES
            ('onboarding', 'Onboarding', NOW(), NOW()),
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

    return


def subcategory_seed():
    # Fetch all subcategory_id and subcategory_name pairs once

    batch_data = {}

    # Organize subcategories into batches by category (key)
    for category_slug, subcategories in subcategory_data.items():
        for subcategory in subcategories:
            if category_slug not in batch_data:
                batch_data[category_slug] = []
            batch_data[category_slug].append(
                {"subcategory_slug": subcategory["subcategory_slug"], "subcategory_name": subcategory["name"]}
            )

    # Retrieve the mapping of category slugs to category IDs
    category_ids = (
        get_all_category_ids()
    )  # Should return a dictionary like {'health-wellness': 1, 'social-community': 2, ...}

    # Prepare and execute batch insert queries for each category
    for category_slug, subcategory_batch in batch_data.items():
        # Check if the category slug exists in the retrieved category IDs
        if category_slug in category_ids:
            category_id = category_ids[category_slug]
        else:
            print(f"Category slug '{category_slug}' not found in the database.")
            continue  # Skip this category if the ID is not found

        # Create the base query
        query = "INSERT INTO subcategories (category_id, subcategory_slug, name, created_at, updated_at) VALUES "
        query_values = []

        # Add the subcategory values to the query
        for subcategory in subcategory_batch:
            values = f"({category_id}, '{subcategory['subcategory_slug']}', '{subcategory['subcategory_name']}', NOW(), NOW())"
            query_values.append(values)

        # Combine the query and execute it
        query += ", ".join(query_values)
        query += " ON DUPLICATE KEY UPDATE updated_at = NOW();"

        # Execute the query using your database method
        UserSurvey.db.query_db(query)

    print(
        f"{sum(len(v) for v in subcategory_data.values())} survey subcategories have been seeded."
    )


def prepare_survey_question_data():
    # ADD QUESTIONS ABOUT SCREEN TIME AND DOPAMINE RELATED DESIRES/DRIVERS/RESPONSES

    # Prepare the batched queries for each subcategory_id
    batched_data = {}

    # Iterate over each subcategory and its questions
    for subcategory in survey_question_data:
        subcategory_data = {"subcategory_slug": subcategory["subcategory_slug"]}
        query = "SELECT id FROM subcategories WHERE subcategory_slug = %(subcategory_slug)s"

        result = UserSurvey.db.query_db(query, subcategory_data)

        if result:
            subcategory_id = result[0]["id"]
        else:
            print(f"No subcategory found for slug: {subcategory_data['subcategory_slug']}")

        for question in subcategory["questions"]:
            answer_data = []
            answer_type = question["type"]

            if "answers" in question:
                for answer in question["answers"]:
                    answer_data.append(
                        {
                            "answer_type": answer_type,
                            "answer_text": answer.get("answer_text", ""),
                            "answer_value": answer.get("answer_value"),
                        }
                    )

            question_data = {
                "subcategory_id": subcategory_id,
                "question_slug": question["question_slug"],
                "question_text": question["question_text"],
                "type": question["type"],
                "answers": answer_data,
            }

            # Batch questions by subcategory_id
            if subcategory_id not in batched_data:
                batched_data[subcategory_id] = []

            batched_data[subcategory_id].append(question_data)
    # print("*****BATCHED DATA*****")
    # pprint(batched_data)
    return batched_data


def survey_question_seed(batched_data):

    for subcategory_id, questions in batched_data.items():
        query = """
            INSERT INTO survey_questions (subcategory_id, question_slug, question_text, type, created_at, updated_at)
            VALUES %s
            ON DUPLICATE KEY UPDATE 
                subcategory_id = VALUES(subcategory_id),
                question_slug = question_slug,
                question_text = question_text,
                type = VALUES(type),
                updated_at = NOW();
        """
        # Prepare values for each question
        query_values = [
            (
                question["subcategory_id"],
                question["question_slug"],
                question["question_text"],
                question["type"],
            )
            for question in questions
        ]

        # Build the placeholders for each question (MySQL-style batch insert)
        query_values_placeholder = ", ".join(
            ["(%s, %s, %s, %s, NOW(), NOW())" for _ in query_values]
        )

        # Format the final query
        final_query = query % query_values_placeholder

        # Flatten the parameters list for the batch execution
        parameters = [item for sublist in query_values for item in sublist]

        try:
            # Execute the query using the database connection
            UserSurvey.db.query_db(final_query, parameters)
            print("Survey questions seeded successfully!")
        except Exception as e:
            print(f"Error while inserting questions for subcategory {subcategory_id}: {e}")


# TODO: ADDRESS GENERIC ANSWER FORMATS, NEW FUNCTION FOR THESE QUESTION TYPES?
# QUERY FOR ANSWERS MATCHING ANSWER_TYPE
# FOR ANSWER IN ANSWERS:
# SEED MANY-TO-MANY TABLE WITH IDS


def process_survey_question_and_map_data(batched_data):
    # These lists will hold mappings for different types of answers
    custom_survey_question_answer_map_data = []
    generic_survey_question_answer_map_data = []

    # Process each question and separate them based on answer type
    for subcategory_id, questions in batched_data.items():
        for question in questions:
            survey_question_id = _get_survey_question_id(
                subcategory_id, question["question_slug"]
            )
            if not survey_question_id:
                print(
                    f"Could not retrieve survey question ID for subcategory {subcategory_id}, question {question['question_slug']}"
                )
                continue

            answers = question.get("answers", [])
            if answers:
                prepare_answer_data(
                    answers, survey_question_id, custom_survey_question_answer_map_data
                )
            else:
                _categorize_generic_question(
                    question,
                    survey_question_id,
                    generic_survey_question_answer_map_data,
                )
    
    return custom_survey_question_answer_map_data, generic_survey_question_answer_map_data

def _get_survey_question_id(subcategory_id, question_slug):
    query = """
        SELECT id FROM survey_questions
        WHERE subcategory_id = %(subcategory_id)s AND question_slug = %(question_slug)s;
    """
    try:
        result = UserSurvey.db.query_db(
            query, {"subcategory_id": subcategory_id, "question_slug": question_slug}
        )
        return result[0]["id"] if result else None
    except Exception as e:
        print(f"Error retrieving survey question ID for subcategory {subcategory_id}: {e}")
        return None
    
def _get_survey_question_id_by_question_slug(question_slug):
    query = """
        SELECT id FROM survey_questions
        WHERE question_slug = %(question_slug)s;
    """
    try:
        result = UserSurvey.db.query_db(
            query, {"question_slug": question_slug}
        )
        return result[0]["id"] if result else None
    except Exception as e:
        print(f"Error retrieving survey question ID for question_slug {question_slug}: {e}")
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
            custom_answer_map_data.append(
                {
                    "survey_question_id": survey_question_id,
                    "survey_answer_id": answer_id,
                }
            )


def _insert_answer(answer, answer_query):
    """
    Insert an individual answer and return its ID if successful.
    """
    try:
        result = UserSurvey.db.query_db(
            answer_query,
            {
                "answer_type": answer["answer_type"],
                "answer_text": answer["answer_text"],
                "answer_value": answer["answer_value"],
            },
        )
        return result if result else None
    except Exception as e:
        print(f"Error inserting answer: {e}")
        return None


def _categorize_generic_question(question, survey_question_id, generic_answer_map_data):
    """
    Add generic questions to a separate list for processing later.
    """
    custom_answer_types = [
        "open-answer",
        "guided-choice",
        "select-any",
        "select-any-add",
    ]
    if question["type"] not in custom_answer_types:
        query = """
            SELECT id FROM survey_answers WHERE survey_answers.answer_type = %(answer_type)s;
        """

        data = {"answer_type": question["type"]}

        results = UserSurvey.db.query_db(query, data)
        if results:
            for result in results:
                survey_answer_id = result["id"]

                generic_answer_map_data.append(
                    {
                        "survey_question_id": survey_question_id,
                        "survey_answer_id": survey_answer_id,  # To be filled in later if applicable
                    }
                )
    return


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


def generic_survey_answer_seed():
    # Answers data with dynamic mappings for questions
    batched_queries = {}
    question_answer_map = []

    # Prepare data for batch insertion
    for answer_set in generic_survey_answer_data:
        answer_type = answer_set["answer_type"]
        for answer in answer_set["answers"]:
            # Create answer data structure
            answer_data = {
                "answer_type": answer_type,
                "answer_text": answer["answer_text"],
                "answer_value": answer["answer_value"],
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
            (a["answer_type"], a["answer_text"], a["answer_value"]) for a in answers
        ]

        # Placeholder for each answer row
        query_values_placeholder = ", ".join(
            ["(%s, %s, %s, NOW(), NOW())" for _ in query_values]
        )

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
            (mapping["survey_question_id"], mapping["answer_id"])
            for mapping in question_answer_map
        ]

        map_query_placeholder = ", ".join(
            ["(%s, %s, NOW(), NOW())" for _ in map_query_values]
        )

        final_map_query = map_query % map_query_placeholder
        map_parameters = [item for sublist in map_query_values for item in sublist]

        UserSurvey.db.query_db(final_map_query, map_parameters)

    print("Survey answers and mappings seeded successfully!")
    return


def survey_branching_seed(survey_branching_data):
    query = """
      INSERT INTO survey_branching
        (survey_question_id, next_question_id, answer_value, created_at, updated_at)
      VALUES
        (%(survey_question_id)s, %(next_question_id)s, %(answer_value)s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        next_question_id = VALUES(next_question_id),
        updated_at = NOW();
    """

    for branch in survey_branching_data:
        survey_question_id = _get_survey_question_id_by_question_slug(branch["survey_question_slug"])
        answer_value = _get_answer_value_by_question_id_and_answer_text(survey_question_id, branch["answer_text"])
        next_question_id = _get_survey_question_id_by_question_slug(branch["next_question_slug"])
        
        # Ensure required data exists
        if survey_question_id is None:
            print(f"Error: survey_question_slug '{branch['survey_question_slug']}' not found.")
            continue
        if next_question_id is None and branch["next_question_slug"] != "end_survey":
            print(f"Error: next_question_slug '{branch['next_question_slug']}' not found.")
            continue
        if answer_value is None:
            print(f"Error: answer_text '{branch['answer_text']}' not found for question_slug '{branch['survey_question_slug']}'.")
            continue

        # Handle special "end_survey" case
        if branch["next_question_slug"] == "end_survey":
            next_question_id = None

        branch_data = {
            "survey_question_id": survey_question_id,
            "answer_value": answer_value,
            "next_question_id": next_question_id
        }

        UserSurvey.db.query_db(query, branch_data)

        print("Survey branching seed complete.")

    return


def _get_answer_value_by_question_id_and_answer_text(survey_question_id, answer_text):
    query = """
      SELECT 
        answer_value
      FROM
        survey_answers sa
      JOIN 
        survey_question_answer_map sqam ON sqam.survey_answer_id = sa.id
      WHERE 
        sqam.survey_question_id = %(survey_question_id)s
      AND
        sa.answer_text = %(answer_text)s;
    """

    data = {
        "survey_question_id": survey_question_id,
        "answer_text": answer_text
    }

    result = UserSurvey.db.query_db(query, data)
    if result:
        return result[0]["answer_value"]
    else:
        print(f"Warning: No answer_value found for question_id {survey_question_id} and answer_text '{answer_text}'.")
        return None

def get_all_category_ids():
    query = "SELECT id, category_slug FROM categories"

    # Fetch all category ids and names
    results = UserSurvey.db.query_db(query)

    if not results:  # Handle case where no results are found
        return {}
    # Create a dictionary mapping category names to their IDs
    category_ids = {row["category_slug"]: row["id"] for row in results}

    return category_ids


def get_all_subcategory_ids():
    """
    Fetch all subcategory_id and subcategory_name pairs.
    Returns a dictionary mapping subcategory names to subcategory IDs.
    """
    query = "SELECT id, subcategory_slug FROM subcategories"
    results = UserSurvey.db.query_db(query)

    if not results:  # Handle case where no results are found
        return {}

    return {row["subcategory_slug"]: row["id"] for row in results}


def get_all_survey_question_ids():
    """
    Fetch all survey_question_id and survey_answer pairs.
    Returns a dictionary mapping subcategory names to subcategory IDs.
    """
    query = "SELECT id, question_text FROM survey_questions"
    results = UserSurvey.db.query_db(query)

    if not results:  # Handle case where no results are found
        return {}

    return {row["question_text"]: row["id"] for row in results}




# def survey_custom_answer_seed(batched_data):
#     custom_answer_types = ['open-answer', 'guided-choice', 'select-any', 'select-any-add']

#     for subcategory_id, questions in batched_data.items():
#         for question in questions:
#             # print("*****Question in survey_custom_answer_seed****")
#             # pprint(question)

#             query = """
#                 SELECT id FROM survey_questions
#                 WHERE subcategory_id = %(subcategory_id)s AND question_slug = %(question_slug)s;
#             """
#             survey_question_data = {
#                 'subcategory_id': subcategory_id,
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

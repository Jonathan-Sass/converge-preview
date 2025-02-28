from flask_app.config.mysqlconnection import connectToMySQL
# import asyncio, aiomysql, logging
# from flask_app.models.user import User
# from flask_app.models.userSurvey import UserSurvey
from database.seed_data.practice_data import practice_data
import pymysql
from pprint import pprint

db = connectToMySQL("converge_schema")


def seed_practice_data():
    # seed practice categories
    seed_practice_categories(practice_data)

    categories = fetch_categories()
    # get practice_durations
    durations = fetch_durations()
    # get engagement levels
    engagement_levels = fetch_engagement_levels()
    # get frequencies
    frequencies = fetch_frequencies()
    # prepare and batch data
    values = prepare_practice_data(categories, frequencies)
    # seed practices
    execute_practice_data_seed(values)

    recommended_durations_values = prepare_recommended_durations_data(durations, engagement_levels)
    execute_recommended_duration_seed(recommended_durations_values)


def seed_practice_categories(practice_data):
    """
    This function separates categories from practice_data and seeds them in the practice_categories table
    """

    categories = [{'name': category} for category in practice_data.keys()]
    values = ", ".join(f"('{category['name']}')" for category in categories)
    
    query = f"INSERT IGNORE INTO practice_categories (name) VALUES {values};"
    db.query_db(query)

def fetch_categories():
    """
    Fetches all categories from categories table

    Returns:

    Raises:
    """
    query = "SELECT * FROM practice_categories;"
    results = db.query_db(query)

    if results:
        return results
    else:
        raise RuntimeError("No practice_categories found in the database.")

def fetch_durations():
    """
    Fetches all durations from the database.

    Queries the durations table and returns the results if available.
    Raises a RuntimeError if the query does not return any results.

    Returns:
        list: A list of dictionaries representing the durations.
    
    Raises:
        RuntimeError: If no durations are found in the database.
    """
    query = "SELECT * FROM durations;"

    results = db.query_db(query)

    if results:
        return results
    else:
        raise RuntimeError("No durations found in the database.")
    
def fetch_engagement_levels():
    """
    Fetchs all engagement levels from the database

    Returns: 

    Raises:
    """
    query = "SELECT * FROM engagement_levels"
    results = db.query_db(query)
    if results:
        return results
    else:
        raise RuntimeError("No engagement levels found in database.")

def fetch_frequencies():
    """
    Fetches all frequencies from the database. 

    Queries the frequencies table and returns the results if available.  
    Raises a RuntimeError if the query does not return any results.

    Returns:
        list: A list of dictionaries representing the frequencies.
    
    Raises:
        RuntimeError: If no practice durations are found in the database.
    """ 
    query = "SELECT * FROM frequencies;"
    results = db.query_db(query)

    if results:
        return results
    else:
        raise RuntimeError("No frequencies found in the database.")

def prepare_practice_data(db_categories, frequencies):
    """
    This function batches and flattens practice_data for seeding into the practices table

    Returns: 

    Raises:
    """

    # Create lookup dictionaries for categories, durations, and frequencies
    category_lookup = {cat['name']: cat['id'] for cat in db_categories}
    # duration_lookup = {dur['duration_label']: dur['id'] for dur in durations}
    frequency_lookup = {freq['frequency_label']: freq['frequency_value'] for freq in frequencies}


    batched_data = []

    for category, practices in practice_data.items():
    # Check if the category exists in the database categories
        if category in category_lookup:
            category_id = category_lookup[category]  # Get the category ID

            for practice in practices:
                # Prepare the practice data dictionary
                prepared_practice_data = {}
                prepared_practice_data['category_id'] = category_id  # Assign category ID
                
                # Assign impact value and difficulty level
                prepared_practice_data['impact_rating_id'] = practice.get('impact_rating_id', 1)
                prepared_practice_data['difficulty_level_id'] = practice.get('difficulty_level_id', 3)

                # Check and assign frequency ID
                prepared_practice_data['frequency_id'] = frequency_lookup.get(practice.get('frequency'), 0)  # Default frequency ID to 0
                
                # Assign practice name, description, is_common and literature_summary
                prepared_practice_data['name'] = pymysql.converters.escape_string(practice.get('name', ''))
                prepared_practice_data['description'] = pymysql.converters.escape_string(practice.get('description', ''))
                prepared_practice_data['benefit_synopsis'] = pymysql.converters.escape_string(practice.get('benefit_synopsis', ''))

                prepared_practice_data['notes'] = pymysql.converters.escape_string(practice.get('notes', ''))

                prepared_practice_data['is_common'] = practice.get('is_common', 0)
                prepared_practice_data['literature_summary'] = pymysql.converters.escape_string(practice.get('literature_summary', ''))

                # Append prepared data to the batch list
                batched_data.append(prepared_practice_data)

    values = [
        (
            data ["category_id"],
            data["impact_rating_id"], 
            data["difficulty_level_id"], 
            data["frequency_id"], 
            data["name"], 
            data["description"], 
            data["benefit_synopsis"],
            data["is_common"], 
            data["notes"], 
            data["literature_summary"]
        )
        for data in batched_data
    ]
    return values

def execute_practice_data_seed(values):
    if not values:
        return print("No values in values")
    
    query = """
        INSERT INTO practices
            (practice_category_id, impact_rating_id, difficulty_level_id, frequency_id, name, description, benefit_synopsis, is_common, notes, literature_summary, created_at, updated_at)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
            practice_category_id = VALUES(practice_category_id),
            impact_rating_id = VALUES(impact_rating_id),
            difficulty_level_id = VALUES(difficulty_level_id),
            frequency_id = VALUES(frequency_id),
            name = name,
            description = VALUES(description),
            benefit_synopsis = VALUES(benefit_synopsis),
            is_common = VALUES(is_common),
            notes = VALUES(notes),
            literature_summary = VALUES(literature_summary),
            updated_at = NOW();
    """
    for value in values:
        db.query_db(query, value)

def prepare_recommended_durations_data(durations, engagement_levels):
    duration_id_lookup = {dur['duration_label']: dur['id'] for dur in durations}
    engagement_level_id_lookup = {eng_lev['level']: eng_lev['id'] for eng_lev in engagement_levels}
    print("***Engagement levels:*****")
    pprint(engagement_levels)
    practice_id_lookup = fetch_practice_ids()

    print("Duration id lookup: ")
    pprint(duration_id_lookup)
    print("engagement level id lookup: ")
    pprint(engagement_level_id_lookup)

    batched_recommended_durations = []

    for category, practices in practice_data.items():
        for practice in practices:    
            practice_id = practice_id_lookup[practice['name']]
           
            if 'recommended_durations' in practice:

                for rd in practice['recommended_durations']:
                    prepared_recommended_durations_data = {
                        "practice_id": practice_id,
                        "duration_id": duration_id_lookup[rd['duration_label']],
                        "engagement_level_id": engagement_level_id_lookup.get(rd.get('engagement_level'), None)
                    }

                    # Add the tuple to the batch
                    batched_recommended_durations.append(
                       prepared_recommended_durations_data
                    )

    values = [
        (
            recommended_duration["duration_id"], 
            recommended_duration["engagement_level_id"], 
            recommended_duration["practice_id"]
        )
        for recommended_duration in batched_recommended_durations
    ]

    return values

def execute_recommended_duration_seed(values):
    query = """
        INSERT INTO recommended_durations
            (duration_id, engagement_level_id, practice_id)
        VALUES
            (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            engagement_level_id = VALUES(engagement_level_id);
    """
    for value in values:
        db.query_db(query, value)

def fetch_practice_ids():
    query = "SELECT id, name FROM practices"
    results = db.query_db(query)
    return {result['name']: result['id'] for result in results}
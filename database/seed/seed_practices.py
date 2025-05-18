from flask_app.config.mysqlconnection import connectToMySQL
# import asyncio, aiomysql, logging
# from flask_app.models.user import User
# from flask_app.models.userSurvey import UserSurvey
from database.seed_data.practice_data import practice_data
from database.seed_data.practice_category_data import (practice_categories, practice_subcategories)
import pymysql
from pprint import pprint

db = connectToMySQL("converge_schema")
        
def seed_practices():
    try:
      seed_practice_categories(practice_categories)
    except Exception as e:
      print(f"Failed to seed practice categories: {e}")
    else:
      print("Practice categories seeded.")

    try:
      execute_practice_subcategories_seed()
    except Exception as e:
      print(f"Failed to seed practice subcategories: {e}")
    else:
      print("Practice subcategories seeded.")

    try:
      db_categories = fetch_categories()
      db_subcategories = fetch_subcategories()
      # get practice_durations
      durations = fetch_durations()
      # get engagement levels
      engagement_levels = fetch_engagement_levels()
      # get frequencies
      frequencies = fetch_frequencies()
      # prepare and batch data
      values = prepare_practice_data(db_categories, db_subcategories, frequencies)
      # seed practices
      execute_practice_data_seed(values)
    except Exception as e:
      print(f"Failed to seed practices: {e}")
    else:
      print("Practices seeded.")

    try:
      recommended_durations_values = prepare_recommended_durations_data(durations, engagement_levels)
      execute_recommended_duration_seed(recommended_durations_values)
    except Exception as e:
      print(f"Failed to seed recommended durations: {e}")
    else:
      print("Recommended durations seeded.")

def test_practice_seed():
    seed_practice_categories(practice_categories)
    execute_practice_subcategories_seed()

    db_categories = fetch_categories()
    db_subcategories = fetch_subcategories()
    # get practice_durations
    durations = fetch_durations()
    # get engagement levels
    engagement_levels = fetch_engagement_levels()
    # get frequencies
    frequencies = fetch_frequencies()

    values = prepare_practice_data(db_categories, db_subcategories, frequencies)
    execute_practice_data_seed(values)

    recommended_durations_values = prepare_recommended_durations_data(durations, engagement_levels)
    execute_recommended_duration_seed(recommended_durations_values)
    
    return

def seed_practice_categories(practice_categories):
    """
    This function seeds practice_categories in the practice_categories table
    """
    query = """
      INSERT INTO practice_categories 
        (name, slug, description, created_at, updated_at)
      VALUES
        (%s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        description = VALUES(description),
        updated_at = NOW();
    """

    params = [(c["name"], c["slug"], c["description"]) for c in practice_categories]
    
    try:
        db.query_db(query, params, many=True)
    except Exception as e:
        print(f"Seeding practice_categories failed: {e}")
    else:
        print("Seeding practice_categories successful!")

def execute_practice_subcategories_seed():
    """
    This function seeds practice_subcategories in the practice_subcategories table
    """
    query = """
      INSERT INTO practice_subcategories
        (practice_category_id, name, slug, description, created_at, updated_at)
      VALUES
        (%s, %s, %s, %s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        practice_category_id = VALUES(practice_category_id),
        name = VALUES(name),
        description = VALUES(description),
        updated_at = NOW();
    """

    params = prepare_subcategory_data()

    try:
        db.query_db(query, params, many=True)
    except Exception as e:
        print(f"Something went wrong seeding practice_subcategories: {e}")
    else:
        print("Practice_subcategories seed successful!")
    return

def prepare_subcategory_data():
    """
      This method prepares practice_subcategory data for seeding into practice_subcategories
    """
    categories = fetch_categories()
    
    category_id_lookup = {c["slug"]: c["id"] for c in categories}

    params = []

    for category_slug, subcats in practice_subcategories.items():
        category_id = category_id_lookup.get(category_slug)

        if category_id is None:
            print(f"No category_id found for slug '{category_slug}'")

        for sc in subcats:
            params.append((
                category_id, 
                sc["name"], 
                sc["slug"],
                sc["description"]
            ))
    return params

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
    
def fetch_subcategories():
    """
        Fetches all practice subcategories from practice_subcategories table
    """

    query = "SELECT * FROM practice_subcategories;"
    results = db.query_db(query)

    if results:
        return results
    else:
        raise RuntimeError("No practice_subcategories found.")

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

def prepare_practice_data(practice_categories, practice_subcategories, frequencies):
    """
    This function batches and flattens practice_data for seeding into the practices table

    Returns: 

    Raises:
    """

    # Create lookup dictionaries for categories, subcategories, durations, and frequencies
    category_lookup = {cat["slug"]: cat["id"] for cat in practice_categories}
    subcategory_lookup = {sc["slug"]: sc["id"] for sc in practice_subcategories}
    frequency_lookup = {freq['frequency_label']: freq['frequency_value'] for freq in frequencies}

    batched_data = []

    for category, subcat_groups in practice_data.items():
        practice_category_id = category_lookup.get(category)


        if category in category_lookup:
            practice_category_id = category_lookup[category]

            if practice_category_id is None:
                print(f"Unknown category_id: {practice_category_id}")
                continue
            
            for subcategory, practices in subcat_groups.items():
                practice_subcategory_id = subcategory_lookup.get(subcategory)
                if practice_subcategory_id is None:
                    print(f"Unknown subcategory id: {practice_subcategory_id}")
                    continue
                
                for practice in practices:
                    prepared_practice_data = {
                        "practice_category_id": practice_category_id,
                        "practice_subcategory_id": practice_subcategory_id,
                        "impact_rating_id": practice["impact_rating_id"],
                        "difficulty_level_id": practice.get("difficulty_level_id", 2),
                        "frequency_id": frequency_lookup.get(practice["frequency"], 1),
                        "slug": practice["slug"],
                        "name": pymysql.converters.escape_string(practice["name"]),
                        "description": pymysql.converters.escape_string(practice.get("description", "")),
                        "benefit_synopsis": pymysql.converters.escape_string(practice.get("benefit_synopsis", "")),
                        "notes": pymysql.converters.escape_string(practice.get("notes", "")),
                        "is_common": practice.get("is_common", 0),
                        "literature_summary": pymysql.converters.escape_string(practice.get("literature_summary", ""))
                    }

                    batched_data.append(prepared_practice_data)

    values = [
        (
            data["practice_category_id"],
            data["practice_subcategory_id"],
            data["impact_rating_id"], 
            data["difficulty_level_id"], 
            data["frequency_id"], 
            data["slug"],
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
            (practice_category_id, practice_subcategory_id, impact_rating_id, difficulty_level_id, frequency_id, slug, name, description, benefit_synopsis, is_common, notes, literature_summary, created_at, updated_at)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
            practice_category_id = VALUES(practice_category_id),
            practice_subcategory_id = VALUES(practice_subcategory_id),
            impact_rating_id = VALUES(impact_rating_id),
            difficulty_level_id = VALUES(difficulty_level_id),
            frequency_id = VALUES(frequency_id),
            slug = slug,
            name = VALUES(name),
            description = VALUES(description),
            benefit_synopsis = VALUES(benefit_synopsis),
            is_common = VALUES(is_common),
            notes = VALUES(notes),
            literature_summary = VALUES(literature_summary),
            updated_at = NOW();
    """
    # for value in values:
    db.query_db(query, values, many=True)

def prepare_recommended_durations_data(durations, engagement_levels):
    duration_id_lookup = {dur['duration_label']: dur['id'] for dur in durations}
    engagement_level_id_lookup = {eng_lev['level']: eng_lev['id'] for eng_lev in engagement_levels}
    # print("***Engagement levels:*****")
    # pprint(engagement_levels)
    practice_id_lookup = fetch_practice_ids()

    # print("Duration id lookup: ")
    # pprint(duration_id_lookup)
    # print("engagement level id lookup: ")
    # pprint(engagement_level_id_lookup)

    batched_recommended_durations = []

    for category, practices in practice_data.items():
        for practice in practices:
            practice_id = practice_id_lookup[practice['slug']]
           
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
    query = "SELECT id, slug FROM practices"
    results = db.query_db(query)
    return {result['slug']: result['id'] for result in results}
from flask_app.config.mysqlconnection import connectToMySQL
from database.seed_data.routine_template_data import routine_template_data

db = connectToMySQL("converge_schema")

def seed_routine_templates():
    frequencies = fetch_frequencies()
    practices = fetch_practices()
    
    routine_template_values, batched_incomplete_routine_template_practice_data = prepare_routine_template_data(frequencies, practices)
    execute_seed_routine_templates(routine_template_values)

    routine_templates = fetch_routine_templates()
    routine_template_practice_values = prepare_routine_template_practices_data(routine_templates, batched_incomplete_routine_template_practice_data)
    execute_seed_routine_template_practices(routine_template_practice_values)


def fetch_frequencies():
    query = "SELECT id, frequency_label FROM frequencies"

    results = db.query_db(query)
    if results:
        frequencies = results
        return frequencies
    else:
        raise RuntimeError("No frequencies found in the database.")

def fetch_practices():
    query = "SELECT id, name FROM practices"

    results = db.query_db(query)
    if results:
        practices = results
        return practices
    else:
        raise RuntimeError("No practices found in database.")

def fetch_routine_templates():
    query = "SELECT id, name from routine_templates;"
    
    results = db.query_db(query)
    if results:
        routine_templates = results
        return routine_templates
    else:
        raise RuntimeError("No routine templates found in database.")

def prepare_routine_template_data(frequencies, practices):
    """
    This function prepares and batches routine_template data and associated routine_template_practices_data
    """
    frequency_lookup = {freq["frequency_label"]: freq["id"] for freq in frequencies}
    practice_lookup = {practice["name"]: practice["id"] for practice in practices}

    batched_routine_template_data = []
    batched_incomplete_routine_template_practice_data = []

    # for items in routine_template_data
    for routine_template in routine_template_data:
        prepared_routine_template_data = {
            "frequency_id": frequency_lookup.get(routine_template["frequency"], 1),
            "name": routine_template["name"],
            "description": routine_template["description"],
            "routine_type": routine_template["routine_type"],
            "category": routine_template["category"],
            "notes": routine_template.get("notes", None)
        }
        batched_routine_template_data.append(prepared_routine_template_data)

        for practice in routine_template["practices"]:
            # Routine Template Name must be swapped for ID after Routine Templates are seeded
            incomplete_routine_template_practice_data = {
                "routine_template_name": routine_template["name"], 
                "practice_id": practice_lookup.get(practice["practice_name"]),
                "position": practice["position"]
            }
            batched_incomplete_routine_template_practice_data.append(incomplete_routine_template_practice_data)
    
    routine_template_values = [
        (
            data["frequency_id"], 
            data["name"], 
            data["description"], 
            data["routine_type"],
            data["category"],
            data["notes"]
        )
        for data in batched_routine_template_data
    ]

    return routine_template_values, batched_incomplete_routine_template_practice_data

def prepare_routine_template_practices_data(routine_templates, batched_incomplete_routine_template_practice_data):
    routine_template_lookup = {rt["name"]: rt["id"] for rt in routine_templates}

    batched_routine_template_practice_data = []

    for routine_template_practice in batched_incomplete_routine_template_practice_data:
        prepared_routine_template_practice_data = {
            "routine_template_id": routine_template_lookup.get(routine_template_practice["routine_template_name"]),
            "practice_id": routine_template_practice["practice_id"],
            "position": routine_template_practice["position"]
        }
        batched_routine_template_practice_data.append(prepared_routine_template_practice_data)

    values = [
        (
            data["routine_template_id"], 
            data["practice_id"], 
            data["position"]
        )
        for data in batched_routine_template_practice_data
    ]

    return values

def execute_seed_routine_templates(values):
    query = """
        INSERT INTO routine_templates
            (frequency_id, name, description, routine_type, category, notes, created_at, updated_at)
        VALUES
            (%s, %s, %s, %s, %s, %s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
            frequency_id = VALUES(frequency_id),
            name = name,
            description = VALUES(description),
            routine_type = VALUES(routine_type),
            category = VALUES(category),
            notes = VALUES(notes),
            updated_at = NOW();
    """

    for value in values:
        db.query_db(query, value)
    return

def execute_seed_routine_template_practices(values):
    query = """
        INSERT INTO routine_template_practices
            (routine_template_id, practice_id, position, created_at, updated_at)
        VALUES
            (%s, %s, %s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
            routine_template_id = routine_template_id,
            practice_id = practice_id,
            position = VALUES(position),
            updated_at = VALUES(updated_at);
    """

    for value in values:
        db.query_db(query, value)
    return
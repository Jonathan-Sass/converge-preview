from flask_app.config.mysqlconnection import connectToMySQL
from database.seed_data.routine_block_template_data import routine_block_templates
from database.seed.seed_helpers import safe_execute
from pprint import pprint

db = connectToMySQL("converge_schema")

def seed_routine_block_templates():
    # frequencies = fetch_frequencies()
    practices = fetch_practices()
    
    routine_block_template_values, batched_incomplete_routine_block_template_practice_data, routine_block_template_trait_data = prepare_routine_block_templates(practices)
    execute_seed_routine_block_templates(routine_block_template_values)
    
    routine_block_templates = fetch_routine_block_templates()
    execute_seed_block_template_traits(routine_block_template_trait_data)

    routine_block_template_practice_values = prepare_routine_block_template_practices_data(routine_block_templates, batched_incomplete_routine_block_template_practice_data)
    execute_seed_routine_block_template_practices(routine_block_template_practice_values)


def fetch_frequencies():
    query = "SELECT id, frequency_label FROM frequencies;"

    results = db.query_db(query)
    if results:
        frequencies = results
        return frequencies
    else:
        raise RuntimeError("No frequencies found in the database.")

def fetch_practices():
    query = "SELECT id, name FROM practices;"

    results = db.query_db(query)
    if results:
        practices = results
        # print("******PRACTICES*****")
        # pprint(practices)
        return practices
    else:
        raise RuntimeError("No practices found in database.")

def fetch_routine_block_templates():
    query = "SELECT id, slug FROM routine_block_templates;"
    
    results = db.query_db(query)
    if results:
        routine_block_templates = results
        return routine_block_templates
    else:
        raise RuntimeError("No routine block templates found in database.")

def fetch_routine_blocks():
    query = "SELECT id, slug FROM routine_blocks;"

    try:
        result = db.query_db(query)
    except Exception as e:
        print(f"Failed to retrieve routine_blocks: {e}")
    else:
        print("Routine blocks retrieved.")
    return result

def prepare_routine_block_templates(practices):
    """
    This function prepares and batches routine_block_template data and associated routine_block_template_practices_data
    """
    # frequency_lookup = {freq["frequency_label"]: freq["id"] for freq in frequencies}
    practice_lookup = {practice["name"]: practice["id"] for practice in practices}

    batched_routine_block_templates = []
    batched_incomplete_routine_block_template_practice_data = []
    batched_block_template_trait_data = []


    # for items in routine_block_templates
    for routine_block_template in routine_block_templates:
        prepared_routine_block_templates = {
            # "frequency_id": frequency_lookup.get(routine_block_template["frequency"], 1),
            "name": routine_block_template["name"],
            "slug": routine_block_template["slug"],
            "description": routine_block_template["description"],
            "routine_type": routine_block_template["routine_type"],
            "notes": routine_block_template.get("notes", None)
        }
        batched_routine_block_templates.append(prepared_routine_block_templates)

        for practice in routine_block_template["practices"]:
            # Routine Template Name must be swapped for ID after Routine Templates are seeded
            practice_name = practice["practice_name"]
            if practice_name is None:
                raise KeyError(f"Missing practice_name in {practice!r}")
            
            practice_id = practice_lookup.get(practice_name)
            if practice_id is None:
                raise KeyError(f"Unknown 'practice_name' {practice_name} in {practice!r}")
            
            incomplete_routine_block_template_practice_data = {
                "routine_block_template_slug": routine_block_template["slug"], 
                "routine_block_slug": practice["routine_block_slug"],
                "practice_id": practice_id,
                "position": practice["position"]
            }
            batched_incomplete_routine_block_template_practice_data.append(incomplete_routine_block_template_practice_data)

        # TODO: FINISH ME!
        for trait_slug, trait_props in routine_block_template["traits"].items():
           
           routine_block_trait_data = {
               "routine_block_template_slug": routine_block_template["slug"],
               "slug": trait_slug,
               "value": trait_props["trait_value"],
               "is_required": bool(trait_props["is_required"]),
               "trait_weight": trait_props.get("weight", 1)
           }
           batched_block_template_trait_data.append(routine_block_trait_data)

    # routine_block_template_values = [
    #     (
    #         # data["frequency_id"], 
    #         data["name"], 
    #         data["slug"],
    #         data["description"], 
    #         data["routine_type"],
    #         data["category"],
    #         data["notes"]
    #     )
    #     for data in batched_routine_block_templates
    # ]

    return batched_routine_block_templates, batched_incomplete_routine_block_template_practice_data, batched_block_template_trait_data

def prepare_routine_block_template_practices_data(routine_block_templates, batched_incomplete_routine_block_template_practice_data):
    routine_blocks = fetch_routine_blocks()
    
    routine_block_template_id_lookup = {rt["slug"]: rt["id"] for rt in routine_block_templates}
    routine_block_id_lookup = {rb["slug"]: rb["id"] for rb in routine_blocks}
    batched_routine_block_template_practice_data = []

    for rtp in batched_incomplete_routine_block_template_practice_data:
        block_slug = rtp.get("routine_block_slug")
        if block_slug is None:
          raise KeyError(f"Missing 'routine_block_slug' in {rtp!r}")
        
        block_id = routine_block_id_lookup.get(block_slug)
        if block_id is None:
            raise KeyError(f"Unknown routine_block_slug '{block_slug} in {rtp!r}")
        
        template_id = routine_block_template_id_lookup.get(rtp["routine_block_template_slug"])
        if template_id is None:
            raise KeyError(f"Unknown template name '{rtp['routine_block_template_slug']}' in {rtp!r}")
        
        batched_routine_block_template_practice_data.append({
            "routine_block_template_id": template_id,
            "routine_block_id": block_id,
            "practice_id": rtp["practice_id"],
            "position": rtp["position"]
        })
        
        # prepared_routine_block_template_practice_data = {
        #     "routine_block_template_id": routine_block_template_id_lookup.get(routine_block_template_practice["routine_block_template_name"]),
        #     "routine_block_id": routine_block_id_lookup.get(routine_block_template_practice["slug"]),
        #     "practice_id": routine_block_template_practice["practice_id"],
        #     "position": routine_block_template_practice["position"]
        # }
        # batched_routine_block_template_practice_data.append(prepared_routine_block_template_practice_data)

    pprint(batched_routine_block_template_practice_data)

    

    return batched_routine_block_template_practice_data

def execute_seed_routine_block_templates(values):
    query = """
        INSERT INTO routine_block_templates
            (name, slug, description, routine_type, notes, created_at, updated_at)
        VALUES
            (%(name)s, %(slug)s, %(description)s, %(routine_type)s, %(notes)s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            slug = slug,
            description = VALUES(description),
            routine_type = VALUES(routine_type),
            notes = VALUES(notes),
            updated_at = NOW();
    """

    try:
      db.query_db(query, values, many=True)
    except Exception as e:
      print(f"Error inserting routine block templates {e}")

def execute_seed_routine_block_template_practices(values):
    query = """
        INSERT INTO routine_block_template_practices
            (routine_block_template_id, practice_id, routine_block_id, position, created_at, updated_at)
        VALUES
            (%(routine_block_template_id)s, %(practice_id)s, %(routine_block_id)s, %(position)s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
            routine_block_template_id = routine_block_template_id,
            practice_id = practice_id,
            routine_block_id = VALUES(routine_block_id),
            position = VALUES(position),
            updated_at = VALUES(updated_at);
    """

    try:
      db.query_db(query, values, many=True)
    except Exception as e:
      print(f"Error inserting routine block template practices: {e}")


def execute_seed_block_template_traits(routine_block_template_trait_data):
  query = """
    INSERT INTO routine_block_template_traits
      (routine_block_template_id, slug, value, is_required, trait_weight, created_at, updated_at)
    VALUES
      (%s, %s, %s, %s, %s, NOW(), NOW())
    ON DUPLICATE KEY UPDATE
      value = VALUES(value),
      is_required = VALUES(is_required),
      trait_weight = VALUES(trait_weight),
      updated_at = NOW();
  """

  routine_block_templates = fetch_routine_block_templates()
  routine_block_template_id_lookup = {bt["slug"]: bt["id"] for bt in routine_block_templates}

  for trait in routine_block_template_trait_data:
      trait["routine_block_template_id"] = routine_block_template_id_lookup.get(trait["routine_block_template_slug"])

  values = [(t["routine_block_template_id"], t["slug"], t["value"], t["is_required"], t["trait_weight"]) for t in routine_block_template_trait_data]
  
  try:
      db.query_db(query, values, many=True)
  except Exception as e:
      print(f"Error inserting block template trait: {e}")
      return None 

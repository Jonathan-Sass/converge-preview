from flask_app.config.mysqlconnection import connectToMySQL

db = connectToMySQL("converge_schema")

# TODO Evaluate other suggested helper methods:
# batch_insert_query(), perpare_value_tuples(), load_json_from_file()

# TODO: Finish integrating safe_execute into existing try, except, else logic.
def safe_execute(name: str, method):
    """
    Executes a function safely with logging.
    
    Args:
        name: A human-readable label for the task (used in logs).
        func: A callable (function reference, not a string).
    """

    try:
        method()
    except Exception as e:
        print(f"{name} failed: {e}")
    else:
        print(f"{name} completed successfully.")

def build_slug_lookup(table_name):
    rows = db.query_db(f"SELECT id, slug FROM {table_name}")

    return {row["slug"]: row["id"] for row in rows}
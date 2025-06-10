from flask_app.config.mysqlconnection import connectToMySQL


class CategoryComponent:
  """
  
  """
  db = connectToMySQL("converge_schema")

  def __init__ (self, data):
    ""
    self.id = data["id"]
    self.goal_category_id = data["goal_category_id"]
    self.slug = data["slug"]
    self.name = data["name"]
    self.description = data["description"], None
    self.role = data["role"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

  @staticmethod
  def build_category_component_from_row(row):
    return {
      "id": row["category_component_id"],
      "goal_category_id": row["goal_category_id"],
      "slug": row["category_component_slug"],
      "name": row["category_component_name"],
      "description": row["category_component_description"],
      "role": row["category_component_role"],
      "created_at": row["category_component_created_at"],
      "updated_at": row["category_component_updated_at"],
    }

  @classmethod
  def get_all_as_dict(cls):
    """Retrieves all category components"""
    query = "SELECT * FROM category_components;"

    try:
      results = cls.db.query_db(query)
      if results:
        return {r["id"]: cls(r) for r in results}
      else:
        return None
    except Exception as e:
      print(f"Error retrieving category components: {e}")
      return None
  
  @classmethod
  def find_category_component_by_slug(cls, component_slug):
    query = "SELECT * FROM category_components WHERE slug = %(slug)s"

    data = {"slug": component_slug}

    # print(f"Component slug in find_by_slug: {component_slug}")

    try: 
      results = cls.db.query_db(query, data)
      if results:
        return cls(results[0])
      else:
        return None
    except Exception as e:
      print(f"Error retrieving category component by slug: {e}")
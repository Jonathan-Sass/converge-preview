from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.goals.category_component import CategoryComponent
from pprint import pprint


class GoalCategory:
    """
    Model representing a top-level category (e.g., Health, Recreation, etc.).
    Includes methods to fetch category data and related category_components.
    """
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """Initialize a GoalCategory object with basic fields and an empty category_components list."""
        self.id = data["id"]
        self.name = data["name"]
        self.slug = data["slug"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.category_components = []

    def build_goal_category_from_row(row):
        return {
            "id": row["goal_category_id"],
            "name": row["goal_category_name"],
            "slug": row["goal_category_slug"],
            "created_at": row["goal_category_created_at"],
            "updated_at": row["goal_category_updated_at"]
        }

    @classmethod
    def get_all_goal_categories_with_category_components(cls):
        """
        Retrieve all goal_categories and their related category_components in a single query.
        Returns:
            dict: Dictionary of goal_categories with category_component lists grouped under each.
        """
        query = """
          SELECT 
            gc.id AS goal_category_id,
            gc.name AS goal_category_name,
            gc.slug AS goal_category_slug,
            gc.created_at AS goal_category_created_at,
            gc.updated_at AS goal_category_updated_at,
            cc.id AS category_component_id,
            cc.name AS category_component_name,
            cc.slug AS category_component_slug,
            cc.created_at AS category_component_created_at,
            cc.updated_at AS category_component_updated_at
          FROM
            goal_categories gc
          JOIN
            category_components cc ON gc.id = cc.goal_category_id
          ORDER BY
            goal_category_id;
        """

        try:
            results = cls.db.query_db(query)

            if results:
                goal_categories_with_components = {}

                for result in results:
                    goal_category_id = result["goal_category_id"]
                    category_component_id = result["category_component_id"]

                    if goal_category_id not in goal_categories_with_components:
                        goal_categories_with_components[goal_category_id] = cls({
                            "goal_category_id": result["goal_category_id"],
                            "goal_category_slug": result["goal_category_slug"],
                            "goal_category_name": result["goal_category_name"],
                            "goal_category_created_at": result["goal_category_created_at"],
                            "goal_category_updated_at": result["goal_category_updated_at"],
                            "category_components": [], 
                            "category_component_ids": set()
                        })

                    if category_component_id not in goal_categories_with_components[goal_category_id]["category_component_ids"]:
                        goal_categories_with_components[goal_category_id]["category_components"].append(CategoryComponent({
                            "category_component_id": result["category_component_id"],
                            "goal_category_id": result["goal_category_id"],
                            "category_component_slug": result["category_component_slug"],
                            "category_component_name": result["category_component_name"],
                            "category_component_description": result["category_component_description"],
                            "category_component_role": result["category_component_role"],
                            "category_component_created_at": result["category_component_created_at"],
                            "category_component_updated_at": result["category_component_updated_at"]
                        }))
                        goal_categories_with_components[goal_category_id]["category_component_ids"].add(category_component_id)

                # Clean up structure for output
                # cleaned_goal_categories = {
                #     key: {
                #         "goal_category_slug": value["goal_category_slug"],
                #         "goal_category_name": value["goal_category_name"],
                #         "category_components": value["category_components"]
                #     }
                #     for key, value in goal_categories_with_components.items()
                # }

                return goal_categories_with_components

            return {}

        except Exception as e:
            raise RuntimeError(f"Error retrieving goal_categories with category_components: {e}")

    @staticmethod
    def get_all_goal_categories_with_name_slug_components():
        return
    
    @classmethod
    def find_category_by_slug(cls, goal_category_slug):
      """
        Retrieves a single category by its slug.

        Args:
          goal_category_id (int): The ID of the category.
      
        Returns:
          list[dict]: Resulting row(s) from the query.
      """
      
      query = "SELECT * FROM goal_categories WHERE slug = %(slug)s;"
      data = {"slug": goal_category_slug}

      results = cls.db.query_db(query, data)
      
      return results[0] if results else None

    @classmethod
    def find_category_by_id(cls, goal_category_id):
      """
      Retrieve a single category by its ID.
      
      Args:
        goal_category_id (int): The ID of the category.
      
      Returns:
        list[dict]: Resulting row(s) from the query.
      """
      query = "SELECT * FROM goal_categories WHERE id = %(id)s;"
      data = {"id": goal_category_id}

      results = cls.db.query_db(query, data)
      
      return cls(results[0]) if results else None

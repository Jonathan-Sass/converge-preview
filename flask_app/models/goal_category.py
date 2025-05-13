from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.subcategory import Subcategory
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
        self.category_slug = data["category_slug"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.category_components = []

    @staticmethod
    def get_all_goal_categories_with_category_components():
        """
        Retrieve all goal_categories and their related category_components in a single query.
        Returns:
            dict: Dictionary of goal_categories with subcategory lists grouped under each.
        """
        query = """
          SELECT 
            c.id AS category_id,
            c.name AS category_name,
            c.category_slug,
            sc.id AS subcategory_id,
            sc.name AS subcategory_name,
            sc.subcategory_slug
          FROM
            goal_categories c
          JOIN
            category_components sc ON c.id = sc.category_id
          ORDER BY
            category_id;
        """

        try:
            results = GoalCategory.db.query_db(query)

            if results:
                goal_categories_with_subcats = {}

                for result in results:
                    category_id = result["category_id"]
                    subcategory_id = result["subcategory_id"]

                    if category_id not in goal_categories_with_subcats:
                        goal_categories_with_subcats[category_id] = {
                            "category_slug": result["category_slug"],
                            "category_name": result["category_name"],
                            "category_components": [], 
                            "subcategory_ids": set()
                        }

                    if subcategory_id not in goal_categories_with_subcats[category_id]["subcategory_ids"]:
                        goal_categories_with_subcats[category_id]["category_components"].append({
                            "subcategory_id": result["subcategory_id"],
                            "subcategory_slug": result["subcategory_slug"],
                            "subcategory_name": result["subcategory_name"]
                        })
                        goal_categories_with_subcats[category_id]["subcategory_ids"].add(subcategory_id)

                # Clean up structure for output
                cleaned_goal_categories = {
                    key: {
                        "category_slug": value["category_slug"],
                        "category_name": value["category_name"],
                        "category_components": value["category_components"]
                    }
                    for key, value in goal_categories_with_subcats.items()
                }

                return cleaned_goal_categories

            return {}

        except Exception as e:
            raise RuntimeError(f"Error retrieving goal_categories with category_components: {e}")

    @staticmethod
    def find_category_by_id(category_id):
        """
        Retrieve a single category by its ID.
        
        Args:
            category_id (int): The ID of the category.
        
        Returns:
            list[dict]: Resulting row(s) from the query.
        """
        query = "SELECT * FROM goal_categories WHERE id = %(id)s;"
        data = {"id": category_id}

        return GoalCategory.db.query_db(query, data)

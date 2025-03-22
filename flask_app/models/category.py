from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.subcategory import Subcategory

from pprint import pprint


class Category:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.category_slug = data["category_slug"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.subcategories = []

    def get_all_categories_with_subcategories():
        query = """
          SELECT 
            c.id AS category_id,
            c.name AS category_name,
            c.category_slug,
            sc.id AS subcategory_id,
            sc.name AS subcategory_name,
            sc.subcategory_slug
          FROM
            categories c
          JOIN
            subcategories sc ON c.id = sc.category_id
          ORDER BY
            category_id;
        """

        try:
            results = Category.db.query_db(query)

            if results:
                categories_with_subcats = {}

                for result in results:
                    category_id = result["category_id"]
                    subcategory_id = result["subcategory_id"]
                    if category_id not in categories_with_subcats:
                        categories_with_subcats[category_id] = {
                            "category_slug": result["category_slug"],
                            "category_name": result["category_name"],
                            "subcategories": [],
                            "subcategory_ids": set()
                        }

                        if subcategory_id not in categories_with_subcats[category_id]["subcategory_ids"]:
                            categories_with_subcats[category_id]["subcategories"].append({
                                "subcategory_id": result["subcategory_id"],
                                "subcategory_slug": result["subcategory_slug"],
                                "subcategory_name": result["subcategory_name"]
                            })
                            categories_with_subcats[category_id]["subcategory_ids"].add(subcategory_id)
                          
                cleaned_categories = {
                  key: {
                      "category_slug": value["category_slug"],
                      "category_name": value["category_name"],
                      "subcategories": value["subcategories"]
                  }
                  for key, value in categories_with_subcats.items()
                }
                    
                return cleaned_categories
        
            return {}

        except Exception as e:
            raise RuntimeError (f"Error retrieving categories with subcategories: {e}")

# DEPRECATED .... TWO QUERIES?!?!?!?! AMATEUR HOUR!
    # def get_category_with_subcategories(category_slug):
    #     query = "SELECT * FROM categories WHERE category_slug = %(category_slug)s;"

    #     category_slug_data = {"category_slug": category_slug}

    #     result = Category.db.query_db(query, category_slug_data)

    #     print("*****Result in get_category_with_subcategories*****")
    #     pprint(result)

    #     if result:
    #         current_category = Category(result[0])
    #         category_id = current_category.id
    #         subcategories = Subcategory.find_subcategories_by_category_id(category_id)

    #         for subcategory in subcategories:
    #             current_category.subcategories.append(subcategory)
    #         return current_category
    #     else:
    #         raise RuntimeError(
    #             "Error retrieving category and associated subcategories for: "
    #             + category_slug
    #         )

    def find_category_by_id(category_id):
        query = "SELECT * FROM categories WHERE id = %(id)s;"

        data = {"id": category_id}

        result = Category.db.query_db(query, data)

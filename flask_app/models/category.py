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

    def get_category_with_subcategories(category_slug):
        query = "SELECT * FROM categories WHERE category_slug = %(category_slug)s;"

        category_slug_data = {"category_slug": category_slug}

        result = Category.db.query_db(query, category_slug_data)

        print("*****Result in get_category_with_subcategories*****")
        pprint(result)

        if result:
            current_category = Category(result[0])
            category_id = current_category.id
            subcategories = Subcategory.find_subcategories_by_category_id(category_id)

            for subcategory in subcategories:
                current_category.subcategories.append(subcategory)
            return current_category
        else:
            raise RuntimeError(
                "Error retrieving category and associated subcategories for: "
                + category_slug
            )

    def find_category_by_id(category_id):
        query = "SELECT * FROM categories WHERE id = %(id)s;"

        data = {"id": category_id}

        result = Category.db.query_db(query, data)

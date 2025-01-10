from flask_app.config.mysqlconnection import connectToMySQL


class Subcategory:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.category_id = data["category_id"]
        self.name = data["name"]
        self.subcategory_slug = data["subcategory_slug"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def find_subcategory_by_slug(subcategory_slug):
        query = (
            "SELECT * FROM subcategories WHERE subcategory_slug = %(subcategory_slug)s"
        )

        subcategory_slug_data = {"subcategory_slug": subcategory_slug}

        result = Subcategory.db.query_db(query, subcategory_slug_data)

        if result:
            subcategory = Subcategory(result[0])
            return subcategory
        else:
            raise RuntimeError("No subcategory found with slug: " + subcategory_slug)

    def find_subcategories_by_category_id(category_id):
        query = "SELECT * FROM subcategories WHERE category_id = %(category_id)s;"

        category_id_data = {"category_id": category_id}

        results = Subcategory.db.query_db(query, category_id_data)

        if results:
            subcategories = []
            for result in results:
                subcategories.append(result)
            return subcategories
        else:
            raise RuntimeError("No subcategories found for this category_id")

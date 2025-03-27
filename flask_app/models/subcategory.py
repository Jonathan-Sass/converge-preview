from flask_app.config.mysqlconnection import connectToMySQL


class Subcategory:
    """Model for managing subcategories associated with main categories in the Converge app."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a Subcategory object.

        Args:
            data (dict): Dictionary containing subcategory fields from the database.
        """
        self.id = data["id"]
        self.category_id = data["category_id"]
        self.name = data["name"]
        self.subcategory_slug = data["subcategory_slug"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def find_subcategory_by_slug(subcategory_slug):
        """
        Find a subcategory by its unique slug.

        Args:
            subcategory_slug (str): Slug of the subcategory to find.

        Returns:
            Subcategory: An instance of the Subcategory object.

        Raises:
            RuntimeError: If no matching subcategory is found.
        """
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
        """
        Find all subcategories that belong to a given category.

        Args:
            category_id (int): ID of the parent category.

        Returns:
            list: List of subcategory dictionaries.

        Raises:
            RuntimeError: If no subcategories are found for the given category.
        """
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

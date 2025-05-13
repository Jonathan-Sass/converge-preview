from flask_app import app
from flask import redirect, jsonify

from flask_app.models.goal_category import GoalCategory
from flask_app.models.user import User


@app.get("/api/categories-with-practices/all")
def fetch_all_categories_with_practices():
    """Fetch all categories with subcategories and associated practices.

    Requires the user to be logged in. If the user is not authenticated,
    the user will be redirected to the homepage.

    Returns:
        A JSON response containing the list of categories with nested subcategories and practices.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    categories_with_subcats = GoalCategory.get_all_categories_with_subcategories()
    return jsonify(categories_with_subcats)

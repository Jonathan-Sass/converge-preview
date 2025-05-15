from flask_app import app
from flask import render_template, redirect, session, request, jsonify, flash
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.goal import Goal
from flask_app.models.goal_category import GoalCategory
from flask_app.models.subcategory import Subcategory


@app.get("/goals/<string:category_slug>")
def set_category_goals(category_slug):
    """
    Display the goal-setting page for a specific category.

    Args:
        category_slug (str): Slug used to retrieve the category and its subcategories.

    Returns:
        Rendered HTML template for setting goals in the category.
    """
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_logged_in_user()
    category = GoalCategory.get_category_with_subcategories(category_slug)

    print("*****GoalCategory with subcategories******")
    pprint(category)
    for subcategory in category.subcategories:
        pprint(subcategory)

    return render_template(
        "/goals/set_goals_for_category.html", user=user, category=category
    )


@app.post("/goals/<string:subcategory_slug>/save")
def save_goals_for_subcategory(subcategory_slug=None):
    """
    Save user-submitted goal data for a specific subcategory.

    Args:
        subcategory_slug (str, optional): Slug of the subcategory. May be used in future refinements.

    Returns:
        JSON response indicating success or failure.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    subcategory_goal_data = request.json

    try:
        result = Goal.process_and_save_subcategory_goals_data(subcategory_goal_data)
        return jsonify({"success": True, "result": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.get("/goals/intro/select-subcategory")
def goals_intro_select_subcategory():
    """
    Display the goal introduction page with a list of categories and subcategories.

    Returns:
        Rendered HTML template allowing the user to select a subcategory to begin setting goals.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    categories_with_components = GoalCategory.get_all_goal_categories_with_category_components()

    return render_template("/goals/set_goal_intro_select_subcat.html", categories_with_components = categories_with_components)


@app.get("/goals/intro/<string:subcategory_slug>")
def goals_intro(subcategory_slug):
    """
    Display the introductory goal-setting page for a specific subcategory.

    Args:
        subcategory_slug (str): The slug used to identify and retrieve the subcategory.

    Returns:
        Rendered HTML template for the subcategory goal introduction.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    subcategory = Subcategory.find_subcategory_by_slug(subcategory_slug)

    return render_template("/goals/set_goal_intro.html", subcategory=subcategory)

from flask_app import app
from flask import render_template, redirect, session, request, jsonify, flash
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.goal import Goal
from flask_app.models.goal_category import GoalCategory
from flask_app.models.category_component import CategoryComponent


@app.get("/goals/<string:category_slug>")
def set_category_goals(category_slug):
    """
    Display the goal-setting page for a specific category.

    Args:
        category_slug (str): Slug used to retrieve the category and its category_components.

    Returns:
        Rendered HTML template for setting goals in the category.
    """
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_logged_in_user()
    category = GoalCategory.get_category_with_category_components(category_slug)

    print("*****GoalCategory with category_components******")
    pprint(category)
    for category_component in category.category_components:
        pprint(category_component)

    return render_template(
        "/goals/set_goals_for_category.html", user=user, category=category
    )


@app.post("/goals/<string:category_component_slug>/save")
def save_goals_for_category_component(category_component_slug=None):
    """
    Save user-submitted goal data for a specific category_component.

    Args:
        category_component_slug (str, optional): Slug of the category_component. May be used in future refinements.

    Returns:
        JSON response indicating success or failure.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    category_component_goal_data = request.json

    try:
        result = Goal.process_and_save_category_component_goals_data(category_component_goal_data)
        return jsonify({"success": True, "result": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.get("/goals/intro/select-category_component")
def goals_intro_select_category_component():
    """
    Display the goal introduction page with a list of categories and category_components.

    Returns:
        Rendered HTML template allowing the user to select a category_component to begin setting goals.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    categories_with_components = GoalCategory.get_all_goal_categories_with_category_components()

    return render_template("/goals/set_goal_intro_select_subcat.html", categories_with_components = categories_with_components)


@app.get("/goals/intro/<string:category_component_slug>")
def goals_intro(category_component_slug):
    """
    Display the introductory goal-setting page for a specific category_component.

    Args:
        category_component_slug (str): The slug used to identify and retrieve the category_component.

    Returns:
        Rendered HTML template for the category_component goal introduction.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    category_component = CategoryComponent.find_category_component_by_slug(category_component_slug)

    return render_template("/goals/set_goal_intro.html", category_component=category_component)

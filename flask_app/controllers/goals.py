from flask_app import app
from flask import render_template, redirect, session, request, jsonify, flash
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.goal import Goal
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory




@app.get("/goals/<string:category_slug>")
def set_recreation_travel_goals(category_slug):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_logged_in_user()
    category = Category.get_category_with_subcategories(category_slug)

    print("*****Category with subcategories******")
    pprint(category)
    for subcategory in category.subcategories:
        pprint(subcategory)

    return render_template(
        "/goals/set_goals_for_category.html", user=user, category=category
    )


# Save goals by subcategory
@app.post("/goals/<string:subcategory_slug>/save")
# Dynamic route may be overkill, may change to simply /goals/save - subcategory_slug=None remains until then
def save_goals_by_subcategory(subcategory_slug=None):
    user = User.get_logged_in_user()
    if not user:
        # jsonify({"error": "Please log in"}), 401
        return redirect("/")

    subcategory_goal_data = request.json

    try:
        result = Goal.process_and_save_subcategory_goals_data(subcategory_goal_data)
        return jsonify({"success": True, "result": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# TODO: DETERMINE GOAL SETTING BREAKDOWN, CATEGORES OR SUBCATEGORIES
# @app.get("/goals/recreation-travel/<string:subcategory_slug>")
# def set_recreation_travel_goals(subcategory_slug):
#     if "user_id" not in session:
#         flash("Please log in.", "login")
#         return redirect("/")

#     user = User.get_logged_in_user()

#     subcategory = Subcategory.find_subcategory_by_name(subcategory_slug)

#     return render_template("/goals/set_goals_for_subcategory.html", user = user, subcategory = subcategory)

@app.get("/goals/intro/select-subcategory")
def goals_intro_select_subcategory():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    categories_with_subcats = Category.get_all_categories_with_subcategories()

    return render_template("/goals/set_goal_intro_select_subcat.html", categories_with_subcats = categories_with_subcats)


@app.get("/goals/intro/<string:subcategory_slug>")
def goals_intro(subcategory_slug):
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    subcategory = Subcategory.find_subcategory_by_slug(subcategory_slug)

    return render_template("/goals/set_goal_intro.html", subcategory = subcategory)
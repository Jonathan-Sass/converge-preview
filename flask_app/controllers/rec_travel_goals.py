from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.user_survey import UserSurvey
from flask_app.models.userHealthGoalDeprecated import UserHealthGoal
from flask_app.models.health_goal_deprecated import HealthGoal
from flask_app.models.time_domain import TimeDomain
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory
from flask_app.models.goal import Goal

from pprint import pprint


@app.get("/goals/intro")
def goals_intro():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    return render_template("/goals/goals_intro.html")


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

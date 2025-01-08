from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.user_survey import UserSurvey
from flask_app.models.userHealthGoalDeprecated import UserHealthGoal
from flask_app.models.health_goal_deprecated import HealthGoal
from flask_app.models.time_domain import TimeDomain
from flask_app.models.category import Category
from flask_app.models.subcategory import Subcategory

from pprint import pprint


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


# TODO: DETERMINE GOAL SETTING BREAKDOWN, CATEGORES OR SUBCATEGORIES
# @app.get("/goals/recreation-travel/<string:subcategory_slug>")
# def set_recreation_travel_goals(subcategory_slug):
#     if "user_id" not in session:
#         flash("Please log in.", "login")
#         return redirect("/")

#     user = User.get_logged_in_user()

#     subcategory = Subcategory.find_subcategory_by_name(subcategory_slug)

#     return render_template("/goals/set_goals_for_subcategory.html", user = user, subcategory = subcategory)

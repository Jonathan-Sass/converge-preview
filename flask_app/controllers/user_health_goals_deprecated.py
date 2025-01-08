from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.user_survey import UserSurvey
from flask_app.models.userHealthGoalDeprecated import UserHealthGoal
from flask_app.models.health_goal_deprecated import HealthGoal
from flask_app.models.time_domain import TimeDomain
from flask_app.models.health_quiz_deprecated import HealthQuiz

from pprint import pprint


@app.get("/newuser/quiz/health")
def new_user_quiz():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    return render_template("generic_page.html")


@app.get("/goals/health/intro")
def health_goals_intro():
    return render_template("health_goals_intro.html")


@app.get("/goals/health/select")
def health_goals_selector():
    """This route displays a form to select health related goal filters."""

    if "user_id" not in session:
        flash("Please log in. ", "login")
        return redirect("/")

    user = User.find_by_id(session["user_id"])
    return render_template("health_goal_selector.html", user=user)


@app.post("/goals/health/select/save")
def save_selected_health_goals():
    """This method creates goal filters in the database."""

    if "user_id" not in session:
        flash("Please log in. ", "login")
        return redirect("/")

    UserHealthGoal.create_health_goals(request.form)

    return redirect("/goals/health/refine")


@app.get("/goals/health/refine")
def refine_health_goals():
    """This method renders a page to refine goals for a user."""

    if "user_id" not in session:
        flash("Please log in. ", "login")
        return redirect("/")

    user = User.find_all_user_health_goals_with_time_domains(session["user_id"])
    return render_template("health_goals_refine.html", user=user)


@app.post("/goals/health/refine/save")
def save_refined_health_goals():

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    TimeDomain.update_time_domain(request.form)
    # HealthGoal.update_details(request.form)

    return redirect("/home")


@app.get("/goals/health/<int:user_health_goal_id>/edit")
def edit_goal(user_health_goal_id):
    """This route displays a form to edit a user health goal."""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user_health_goal = UserHealthGoal.find_one_user_health_goal_with_time_domains(
        user_health_goal_id
    )
    return render_template("edit_health_goal.html", user_health_goal=user_health_goal)


@app.post("/goals/health/<int:time_domain_id>/update")
def update_user_health_goal(time_domain_id):
    """This method updates a user_health_goal"""

    if "user_id" not in session:
        flash("Please log in. ", "login")
        return redirect("/")

    UserHealthGoal.update_user_health_goals(request.form)

    return redirect("/home")


@app.post("/goals/health/<int:health_goal_id>/delete")
def delete_goal(health_goal_id):
    """This method deletes a goal from the database."""

    UserHealthGoal.delete_user_health_goal_and_time_domain(health_goal_id)
    return redirect("/home")

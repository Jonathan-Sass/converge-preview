from flask_app import app
from flask import render_template, redirect, session
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.routine import Routine
from flask_app.models.goal import Goal


@app.get("/home")
def dashboard():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    user_id = user.id
    routine_data = Routine.find_routines_by_user_id(user_id)
    goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)

    if not routine_data:
        return render_template("/home/intro.html", user=user)
    else:
        dashboard_data = {"user": user, "routines": routine_data, "goals": goal_data}

        return render_template("/home/dashboard.html", **dashboard_data)

from flask_app import app
from flask import render_template, redirect, session
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.routine import Routine
from flask_app.models.goal import Goal


@app.get("/dashboard")
def dashboard():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    user_id = user.id
    routine_data = Routine.find_routines_by_user_id(user_id)
    goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)

    dashboard_data = {"user": user, "routines": routine_data, "goals": goal_data}

    print("goals in /dashboard:")
    for goal in goal_data:
        pprint(type(goal))

    print("routine in /dashboard")
    for routine in routine_data:
        pprint(type(routine))

    return render_template("/home/dashboard.html", **dashboard_data)

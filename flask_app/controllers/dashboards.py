from flask_app import app
from flask import render_template, redirect, session

from flask_app.models.user import User


@app.get("/dashboard")
def dashboard():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    dashboard_data = {
        user: user,
        # routines: routine_data,
        # goals: goal_data
    }

    return render_template("/home/dashboard.html")

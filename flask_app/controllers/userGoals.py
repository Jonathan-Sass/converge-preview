from flask_app import app
from flask import render_template, redirect, session
from flask_app.models.user import User

@app.get("/goals/intro")
def goals_intro():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    return render_template("/goals/goals_intro.html")
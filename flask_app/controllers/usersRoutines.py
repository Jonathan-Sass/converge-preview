from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.userSurvey import UserSurvey
from database.seed import survey_seed
from pprint import pprint
from datetime import datetime

@app.get("/test")
def test_route():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")

    return render_template("routines/routines_template.html")
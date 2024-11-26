from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.userSurvey import UserSurvey
from pprint import pprint
from datetime import datetime

@app.get("/practices/intro")
def building_practices_intro():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    return render_template("practices/building_practices_intro.html")

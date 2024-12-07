from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.userHealthGoalDeprecated import UserHealthGoal
from flask_app.models.healthGoalDeprecated import HealthGoal
from flask_app.models.timeDomain import TimeDomain
from flask_app.models.healthQuizDeprecated import HealthQuiz

from pprint import pprint

@app.get("/goals/recreation/quiz")
def recreation_and_travel_quiz():
    # user = User.find_all_user_health_goals_with_time_domains(session["user_id"])

    return render_template("quiz_rec_and_travel_goals.html")
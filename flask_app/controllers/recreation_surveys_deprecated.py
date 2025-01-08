from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.userHealthGoalDeprecated import UserHealthGoal
from flask_app.models.health_goal_deprecated import HealthGoal
from flask_app.models.time_domain import TimeDomain
from flask_app.models.health_quiz_deprecated import HealthQuiz

from pprint import pprint


@app.get("/goals/recreation/survey")
def recreation_and_travel_quiz():
    # user = User.find_all_user_health_goals_with_time_domains(session["user_id"])

    return render_template("/surveys/survey_rec_and_travel_goals.html")

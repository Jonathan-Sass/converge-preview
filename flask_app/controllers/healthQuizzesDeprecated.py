from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.userHealthGoalDeprecated import UserHealthGoal
from flask_app.models.healthGoalDeprecated import HealthGoal
from flask_app.models.timeDomain import TimeDomain
from flask_app.models.healthQuizDeprecated import HealthQuiz

from pprint import pprint

# @app.get("/goals/test")
# def test_route():
#     user = User.find_all_user_health_goals_with_time_domains(session["user_id"])

#     return render_template("survey_template.html")

@app.get("/goals/health/quiz")
def health_quiz():
    HealthQuiz.create_health_quiz()
    return render_template("quiz_health_goals.html")

# @app.post('/goals/health/quiz/create')
# def create_health_quiz():
#     return HealthQuiz.create_health_quiz()

@app.post('/goals/health/quiz/submit/column')
def submit_quiz_column():
    data = request.json
    return HealthQuiz.update_health_quiz_single_column(data)



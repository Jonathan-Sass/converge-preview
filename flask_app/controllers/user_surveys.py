from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.user_survey import UserSurvey
from flask_app.models.user_response import UserResponse
from database.seed import seed_surveys
from pprint import pprint
from datetime import datetime


@app.post("/surveys/questions/retrieve")
def retrieve_survey_questions():
    """
    Retrieves survey questions and survey branches based on category and subcategory
    passed in the request JSON body.

    Returns:
        JSON containing the question set and associated branch logic.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    category = request.json.get("category")
    subcategory = request.json.get("subcategory")

    if not category or not subcategory:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    user_category_subcategory_data = {
        "category": category,
        "subcategory": subcategory
    }

    question_set, survey_branches = UserSurvey.find_questions_by_category_and_subcategory(
        user_category_subcategory_data
    )

    return jsonify({
        "currentQuestionSet": question_set,
        "surveyBranches": survey_branches
    })


@app.post("/surveys/<string:category>/submit")
def save_survey_answers(category):
    """
    Saves user responses to survey questions for a given category.

    Args:
        category (str): The survey category, used to track route source.

    Returns:
        JSON indicating success or failure of saving answers.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    print(f"Post received from: /surveys/{category}/submit")
    collected_answers = request.json

    try:
        result = UserResponse.process_user_responses_to_save(collected_answers)
        return jsonify({"success": True, "result": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# ----------- MAP SURVEY ROUTES ----------- #

@app.get("/surveys/user-objectives")
def survey_user_objectives():
  """
  Displays the User Objective survey for onboarding.
  """
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")

  return render_template("/surveys/user_objectives.html")

@app.get("/surveys/digital-disconnect-map")
def survey_digital_disconnect_map():
  """
  Displays the Digital Disconnect Map for onboarding.
  """
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")

  return render_template("/surveys/digital_disconnect_map.html")
  
@app.get("/surveys/core-primer-map")
def survey_core_system_primers_map():
  """
  Displays the Core System Primers Map for onboarding.
  """
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")

  return render_template("/surveys/core_primer-map.html")

@app.get("/surveys/core-builder-map")
def survey_core_system_builders_map():
  """
  Displays the Core System Builders Map for onboarding.
  """
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")

  return render_template("/surveys/core_builder_map.html")

@app.get("/surveys/day-map")
def survey_day_map():
  """
  Displays the Day Map survey to assess the user's daily patterns and routines.
  """
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")

  return render_template("/surveys/day_map.html")


@app.get("/surveys/interest-map")
def survey_interest_map():
  """
  Displays the Interest Map survey to gather user preferences and passions.
  """
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")

  return render_template("/surveys/interest_map.html")


@app.get("/surveys/discipline-motivation-focus-map")
def survey_discipline_motivation_focus_map():
  """
  Displays the Discipline, Motivation & Focus Map survey to assess user self-regulation strengths and challenges.
  """
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")

  return render_template("/surveys/discipline_motivation_focus_map.html")


from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.user import User
from flask_app.models.user_survey import UserSurvey
from flask_app.models.user_response import UserResponse
from database.seed import survey_seed
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


@app.post("/surveys/<string:category>/answers")
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

    print(f"Post received from: /surveys/{category}/answers")
    collected_answers = request.json

    try:
        result = UserResponse.process_user_responses_to_save(collected_answers)
        return jsonify({"success": True, "result": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# ----------- MAP SURVEY ROUTES ----------- #

@app.get("/surveys/user-orientation")
def survey_new_user_orientation():
    """
    Displays the User Orientation survey for onboarding.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    return render_template("/surveys/user_orientation.html")


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

    return render_template("/surveys/interest-map.html")


@app.get("/surveys/discipline-motivation-focus-map")
def survey_discipline_motivation_focus_map():
    """
    Displays the Discipline, Motivation & Focus Map survey to assess user self-regulation strengths and challenges.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    return render_template("/surveys/discipline_motivation_focus_map.html")


# ALL DEPRECATED IN FAVOR OF NEW MAP SURVEYS

# @app.get("/getting-started")
# def new_user_getting_started():
#     user = User.get_logged_in_user()
#     if not user:
#         return redirect("/")

#     return render_template("/surveys/survey_getting_started.html")

# @app.get("/process-getting-started")
# def process_getting_started_answers():
#     user = User.get_logged_in_user()
#     if not user:
#         return redirect("/")
    
#     responses = UserResponse.find_user_responses_by_user_id_and_subcategory_slug(user, "getting-started")

#     response_dict = {
#         res.question_slug: res.answer_text
#         for res in responses
#         if res.question_slug in {"existing-routines-check", "wellness-survey-check", "assistance-building-routines-check", "build-your-own-routine-check"}
#     }

#     existing_routines_check = response_dict.get("existing-routines-check")
#     wellness_survey_check = response_dict.get("wellness-survey-check")
#     assistance_building_routines_check = response_dict.get("assistance-building-routines-check")
#     build_your_own_routine_check = response_dict.get("build-your-own-routine-check")

#     print("*****responses in process_getting_started_answers*****")
#     print(existing_routines_check)
#     print(wellness_survey_check)

#     if existing_routines_check == "Yes" and wellness_survey_check == "No":
#         return redirect ("/routines/am/intro-build-your-own")
    
#     return redirect("surveys/foundations/getting-to-know-you")


# @app.get("/surveys/foundations/getting-to-know-you")
# def survey_introduction_getting_to_know_you():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_foundations_getting_to_know_you.html")


# @app.get("/surveys/foundations/current-habits-patterns")
# def survey_foundations_current_habits_patterns():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_foundations_current_habits_patterns.html")


# @app.get("/surveys/foundations/social-support-accountability")
# def survey_foundations_social_support_accountability():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template(
#         "surveys/survey_foundations_social_support_accountability.html"
#     )


# @app.get("/surveys/foundations/reflecting-purpose-motivation")
# def survey_foundations_reflecting_purpose_motivation():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template(
#         "surveys/survey_foundations_reflecting_purpose_motivation.html"
#     )


# YOUR WHY SURVEY ROUTES
# ALL DEPRECATED

# @app.get("/surveys/your-why/intro")
# def survey_why_intro():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_why_intro.html")


# @app.get("/surveys/your-why/define-your-purpose")
# def survey_define_your_purpose():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_why_define_your_purpose.html")


# @app.get("/surveys/your-why/define-your-values")
# def survey_define_your_values():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_why_define_your_values.html")


# @app.get("/surveys/your-why/growth-drivers")
# def survey_growth_drivers():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_why_growth_drivers.html")


# @app.get("/surveys/your-why/long-term-vision")
# def survey_long_term_vision():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_why_long_term_vision.html")


# RECREATION AND TRAVEL SURVEY ROUTES
# ALL DEPRECATED


# @app.get("/surveys/recreation-travel/intro")
# def survey_recreation_travel_intro():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_rec_travel_intro.html")


# @app.get("/surveys/recreation-travel/frequent-hobbies-activities")
# def survey_frequent_hobbies_activities():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_rec_travel_frequent_hobbies_activities.html")


# @app.get("/surveys/recreation-travel/adventure-travel")
# def survey_adventure_travel():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_rec_travel_adventure_travel.html")


# @app.get("/surveys/recreation-travel/family-group-events")
# def survey_family_group_events():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_rec_travel_family_group_events.html")


# @app.get("/surveys/recreation-travel/cultural-exploration")
# def survey_cultural_exploration():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_rec_travel_cultural_exploration.html")


# @app.get("/surveys/recreation-travel/special-events")
# def survey_special_events():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_rec_travel_special_events.html")


# @app.get("/surveys/recreation-travel/competitive-events")
# def survey_competitive_events():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("surveys/survey_rec_travel_competitive_events.html")


# @app.get("/surveys/recreation-travel/bucket-list")
# def survey_bucket_list():
#     user = User.get_logged_in_user()
#     if not user:
#         # jsonify({"error": "Please log in"}), 401
#         return redirect("/")

#     return render_template("/surveys/survey_rec_travel_bucket_list.html")

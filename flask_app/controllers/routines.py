from flask_app import app
from flask import render_template, redirect, jsonify, request
from flask_app.models.user import User
from flask_app.models.routine import Routine
from flask_app.models.routine_template import RoutineTemplate
from flask_app.models.user_response import UserResponse
from flask_app.models.duration import Duration
from flask_app.models.practice import Practice

from pprint import pprint


@app.get("/test")
def test_route():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")

    return render_template("routines/routines_template.html")


@app.get("/routines/am/manage")
def manage_am_routines():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")
    
    routines = Routine.find_routines_by_user_id(user.id)

    return render_template("/routines/am_routine_build_your_own.html", routines = routines)


@app.get("/routines/am/intro")
def building_practices_intro():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    # TODO: If pre-existing routines --> routine_builder or wellness survey?, else template below
    subcategory_slug = "day-map"

    routine = Routine.select_and_fetch_routine_template(user, subcategory_slug)
    
    return render_template("routines/am_routine_intro_carousel.html", routine = routine)

@app.get("/routines/am/intro-basic")
def view_basic_intro_routine():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    routine = Practice.select_intro_practices()
    
    return render_template("/routines/am_routine_intro_practices.html", routine = routine)

@app.get("/routines/am/intro-builder")
def set_initial_am_routines():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")

    recommended_routine = Routine.select_and_fetch_routine_template(
        user, "getting-to-know-you"
    )
    # durations = Duration.fetch_all_durations()
    # TODO: Implement Personal Routine Progress - allows user to slowly build habits without being overwhelming/defeating

    return render_template(
        "routines/am_routine_builder.html", recommended_routine=recommended_routine
    )



@app.post("/routines/am/intro-builder/save")
def save_am_routine():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")

    am_routine_data = request.json

    Routine.create_routine(am_routine_data)

    return jsonify({"success": True, "redirect": "/dashboard/intro-am-practices"})

@app.get("/routines/am/intro-build-your-own")
def build_your_own_am_routine():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")
    
    routine = Routine.select_and_fetch_routine_template(user, None)
    # practices, practice_categories = Practice.find_all_practices_with_practice_categories()

    return render_template("routines/am_routine_intro_build_your_own.html", routine = routine)

@app.post("/routines/am/intro-build-your-own/save")
def save_build_your_own_routine():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")

    am_routine_data = request.json

    Routine.create_routine(am_routine_data)

    return jsonify({"success": True, "redirect": "/dashboard/intro-am-practices"})
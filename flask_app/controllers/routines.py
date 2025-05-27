from flask_app import app
from flask import render_template, redirect, jsonify, request
from flask_app.models.user import User
from flask_app.models.routine import Routine
from flask_app.models.routine_block_template import RoutineBlockTemplate
from flask_app.models.user_response import UserResponse
from flask_app.models.duration import Duration
from flask_app.models.practice import Practice

from pprint import pprint


@app.get("/routines/test")
def routine_test_route():
    """
    Test route to confirm user authentication and render a test routine template.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    return render_template("routines/routines_template.html")


@app.get("/routines/<string:routine_type>/manage")
def manage_am_routines(routine_type):
    """
    Render the AM routine management interface for a given routine type.

    Args:
        routine_type (str): The type of routine to manage (e.g., "am", "pm").

    Returns:
        Rendered template for editing the user’s routine.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    routine = Routine.find_routine_by_user_id_and_routine_type(user.id, routine_type)
    return render_template("/routines/am_routine_build_your_own.html", routine=routine)


@app.get("/routines/am/intro")
def building_practices_intro():
    """
    Handle logic for introducing the user to AM routines.

    Checks user responses to the day-map survey and determines whether to 
    show the default routine carousel or jump directly to the builder.

    Returns:
        Template for either carousel or builder depending on user's progress.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    subcategory_slug = "day-map"
    responses = UserResponse.find_user_responses_by_user_id_and_subcategory_slug(user, subcategory_slug)
    routine_template_name, existing_routine_status = UserResponse.process_day_map(responses)
    routine = RoutineTemplate.find_routine_template_by_name_with_practices(routine_template_name)

    if existing_routine_status is False:
        return render_template("/routines/am_routine_intro_carousel.html", routine=routine)
    else:
        return render_template("/routines/am_routine_intro_build_your_own.html", routine=routine)


@app.get("/routines/am/intro-basic")
def view_basic_intro_routine():
    """
    Render a basic default AM routine with pre-selected intro practices.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    routine = Practice.select_intro_practices()
    return render_template("/routines/am_routine_intro_practices.html", routine=routine)


@app.get("/routines/am/intro-builder")
def set_initial_am_routines():
    """
    Render the routine builder page for setting the user's initial AM routine.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    recommended_routine = Routine.select_and_fetch_routine_template(user, "day-map")
    return render_template("routines/am_routine_builder.html", recommended_routine=recommended_routine)


@app.post("/routines/am/intro-builder/save")
def save_am_routine():
    """
    Save the initial AM routine submitted by the user and return a redirect path.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    am_routine_data = request.json
    Routine.create_routine(am_routine_data)

    return jsonify({"success": True, "redirect": "/dashboard/intro-am-practices"})


@app.get("/routines/am/intro-build-your-own")
def build_your_own_am_routine():
    """
    Render the 'build your own' version of the AM routine intro page.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    routine = Routine.select_and_fetch_routine_template(user, None)
    return render_template("routines/am_routine_intro_build_your_own.html", routine=routine)


@app.post("/routines/am/intro-build-your-own/save")
def save_build_your_own_routine():
    """
    Save a custom-built AM routine created by the user.

    Note:
        This may be redundant with /intro-builder/save.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    am_routine_data = request.json
    Routine.create_routine(am_routine_data)

    return jsonify({"success": True, "redirect": "/dashboard/intro-am-practices"})


@app.get("/routines/am/edit")
def edit_user_routine():
    """
    Render the page for editing a previously saved user AM routine.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    routine = Routine.find_routines_by_user_id(user.id)
    return render_template("/routines/edit_user_routine.html", routine=routine)

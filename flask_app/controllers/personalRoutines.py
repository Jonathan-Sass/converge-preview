from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User
from flask_app.models.personalRoutine import PersonalRoutine
from flask_app.models.routineTemplate import RoutineTemplate
from flask_app.models.userResponse import UserResponse
from flask_app.models.duration import Duration

from pprint import pprint


@app.get("/test")
def test_route():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")

    return render_template("routines/routines_template.html")


@app.get("/routines/intro")
def building_practices_intro():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    return render_template("routines/building_routines_intro.html")

@app.get("/routines/am/builder/initial")
def set_initial_am_routines():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")
    
    recommended_routine = PersonalRoutine.select_and_fetch_initial_am_routine(user, "getting-to-know-you")
    durations = Duration.fetch_all_durations()
    # TODO: Implement Personal Routine Progress - allows user to slowly build habits without being overwhelming/defeating

    print("*****recommended_routine in controllers*****")
    pprint(vars(recommended_routine))
    for practice in recommended_routine.practices:
        pprint(vars(practice))
        for duration in practice.durations:
            pprint(vars(duration))

    return render_template("routines/am_routine_builder.html", recommended_routine = recommended_routine)

@app.post("/routines/am/builder/initial/save")
def save_am_routine():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")
    
    am_routine = request.json
    PersonalRoutine.create_am_routine(am_routine)
    
    return redirect ("/surveys/foundations/current-habits-patterns")


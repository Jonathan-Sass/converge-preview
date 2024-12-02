from flask_app import app
from flask import render_template, redirect, session
from flask_app.models.user import User
from flask_app.models.personalRoutine import PersonalRoutine
from flask_app.models.routineTemplate import RoutineTemplate
from flask_app.models.userResponse import UserResponse


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

    

    user_with_am_personal_routine = PersonalRoutine.build_initial_am_routine(user, "getting-to-know-you")
    # RoutineTemplate.am_routine_template_selector(user, survey_topic_slug_string)

    return render_template("routines/am_routine_builder.html")
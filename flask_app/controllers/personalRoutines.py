from flask_app import app
from flask import render_template, redirect, session
from flask_app.models.user import User
from flask_app.models.personalRoutine import PersonalRoutine


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
    
    return render_template("routines/building_practices_intro.html")

@app.get("/routines/am/set")
def set_am_routines():
    user = User.get_logged_in_user()
    print(user)
    if not user:
        return redirect("/")

    return render_template("routines/routines_template.html")
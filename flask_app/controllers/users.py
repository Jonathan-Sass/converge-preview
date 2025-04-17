from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from database.seed import (
    seed_misc_practice_data,
    seed_practices,
    seed_routine_template,
    seed_routines,
    seed_surveys,
)
# from database.seed.survey_seed import user_survey_seed
# from database.seed.misc_practice_data_seed import seed_misc_practice_data
# from database.seed.routine_seed import seed_routine_data
from pprint import pprint

bcrypt = Bcrypt(app)


@app.get("/")
def root():
    """Renders the welcome/landing page."""
    return render_template("home/index.html")


@app.get("/seed")
def seed_route():
    """
    Seeds the database with core data including survey questions,
    practices, and routine templates. For development/testing only.
    
    Returns:
        Rendered template for new user dashboard.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    seed_surveys.user_survey_seed()
    seed_misc_practice_data.seed_misc_practice_data()
    seed_practices.seed_practices()
    seed_routine_template.seed_routine_templates()

    return render_template("dashboard/new_user.html")


@app.get("/testseed")
def test_seed_route():
    """
    This route is for testing seed functions independently.
    """
    seed_practices.test_practice_seed()

    # seed_routines.seed_routine_data()

    return render_template("/dashboard/new_user.html")


@app.get("/login")
def login():
    """Renders the login form."""
    return render_template("auth/login.html")


@app.get("/register")
def register():
    """Renders the registration form."""
    return render_template("auth/registration.html")


@app.post("/loginuser")
def loginuser():
    """
    Validates and logs in an existing user.
    
    Redirects to the dashboard if login is successful.
    """
    if not User.login_is_valid(request.form):
        return redirect("/login")

    potential_user = User.find_by_email(request.form)

    if potential_user is None:
        flash("Invalid credentials.", "login")
        return redirect("/login")

    user = potential_user

    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid credentials.", "login")
        return redirect("/login")

    session["user_id"] = user.id
    return redirect("/home")


@app.post("/registeruser")
def registeruser():
    """
    Handles new user registration:
    - Validates form input
    - Ensures email uniqueness
    - Hashes the password
    - Saves the user record
    - Starts a session
    
    Returns:
        Redirect to new user onboarding route.
    """
    if not User.validate_registration(request.form):
        return redirect("/register")

    user_in_db = User.find_by_email(request.form)
    if user_in_db is not None:
        flash("This email is already registered, please login!", "registration")
        return redirect("/register")

    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
    }

    user_id = User.save(data)
    session["user_id"] = user_id
    session["first_name"] = request.form["first_name"]

    return redirect("/newuser")


@app.get("/newuser")
def new_user():
    """
    Displays the new user dashboard after registration.
    Used to guide onboarding flow.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    return render_template("dashboard/new_user.html")


@app.post("/users/logout")
def logout():
    """
    Clears session and logs user out.
    
    Returns:
        Redirect to home page.
    """
    session.clear()
    return redirect("/")

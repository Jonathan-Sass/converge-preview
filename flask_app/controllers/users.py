from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from database.seed import survey_seed, misc_practice_data_seed, practice_seed, routine_template_seed
from database.seed.survey_seed import user_survey_seed
from database.seed.misc_practice_data_seed import seed_misc_practice_data
from pprint import pprint

bcrypt = Bcrypt(app)

@app.get("/")
def root():
    """This is a generic welcome page"""
    return render_template("home/index.html")

@app.get("/seed")
def seed_route():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    survey_seed.user_survey_seed()
    misc_practice_data_seed.seed_misc_practice_data()
    practice_seed.seed_practice_data()
    routine_template_seed.seed_routine_templates()


    return render_template("dashboard/new_user.html")

@app.get("/dashboard")
def user_dashboard():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_logged_in_user()

    return render_template("home/dashboard.html", user = user)

@app.get("/home")
def home_page():
    """This route renders a table with daily practices"""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_logged_in_user()

    return render_template("home/home.html", user = user)

@app.get("/login")
def login():
    return render_template("auth/login.html")

@app.get("/register")
def register():
    return render_template("auth/registration.html")

@app.post("/loginuser")
def loginuser():
    """This route processes user login"""

    # Check if form valid, if not redirect
    if not User.login_is_valid(request.form):
        return redirect("/login")

    # Check if user exists
    potential_user = User.find_by_email(request.form)

    # If user does not exist, redirect
    if potential_user == None:
        flash ("Invalid credentials.", "login")
        return redirect("/login")
    
    # user exists
    user = potential_user

    # Check password
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid credentials.", "login")
        return redirect("/login")

    session["user_id"] = user.id
    return redirect("/home")

@app.post("/registeruser")
def registeruser():
    """This route processes user registration"""

    # If form not valid, redirect
    if not User.validate_registration(request.form):
        return redirect("/register")
    
    # Check if user exists, redirect if so
    user_in_db = User.find_by_email(request.form)
    if user_in_db != None:
        flash("This email is already registered, please login!", "registration")
        return redirect("/register")

    # If user does not exist, safe to create and hash password
    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    # health_quiz_id = HealthQuiz.create_health_quiz
    # print("**************")
    # print(health_quiz_id)
    # print("**************")

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
        # "health_quiz_id": session["health_quiz_id"]
    }
    print(data)
    user_id = User.save(data)

    # Save user id and first name in session
    session["user_id"] = user_id
    session["first_name"] = request.form["first_name"]
  
    return redirect("/newuser")

@app.get("/newuser")
def new_user():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/login")

    return render_template("dashboard/new_user.html")

@app.post("/users/logout")
def logout():
    session.clear()
    return redirect("/")


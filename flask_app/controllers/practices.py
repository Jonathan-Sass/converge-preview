from flask_app import app
from flask import render_template, redirect, session
from flask_app.models.practice import Practice
from flask_app.models.user import User

@app.post("/api/practices-categories/all")
def find_all_practices():
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")
  
  practices, categories = Practice.find_all_practices_with_practice_categories

  

# @app.get("/practices/intro")
# def building_practices_intro():
#     user = User.get_logged_in_user()
#     if not user:
#         return redirect("/")
    
#     return render_template("practices/building_practices_intro.html")
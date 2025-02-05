from flask_app import app
from flask import render_template, redirect, session, jsonify
from flask_app.models.practice import Practice
from flask_app.models.user import User

@app.get("/api/categorized-practices/all")
def get_all_practices():
  user = User.get_logged_in_user()
  if not user:
    return redirect("/")
  

  all_practices = Practice.get_all_practices_grouped_by_category()

  return jsonify(all_practices)

# @app.get("/practices/intro")
# def building_practices_intro():
#     user = User.get_logged_in_user()
#     if not user:
#         return redirect("/")
    
#     return render_template("practices/building_practices_intro.html")
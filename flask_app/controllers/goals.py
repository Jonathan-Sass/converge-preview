from flask_app import app
from flask import render_template, redirect, session, request, jsonify
from flask_app.models.user import User
from flask_app.models.goal import Goal


@app.get("/goals/intro")
def goals_intro():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    return render_template("/goals/goals_intro.html")


# Save goals by subcategory
@app.post("/goals/<string:subcategory_slug>/save")
def save_goals_by_subcategory():
    user = User.get_logged_in_user()
    if not user:
        # jsonify({"error": "Please log in"}), 401
        return redirect("/")

    subcategory_goal_data = request.json

    try:
        result = Goal.save_user_goal(subcategory_goal_data)
        return jsonify({"success": True, "result": result}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

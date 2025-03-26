from flask_app import app
from flask import redirect, jsonify

from flask_app.models.user import User
from flask_app.models.flex_task import FlexTask



@app.post("/flex-tasks/add-goal/<int:goal_id>")
def add_goal_to_flex_tasks(goal_id):
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    try:
        FlexTask.save_flex_task(user.id, goal_id)
        return jsonify({"success": True, "goal_id": goal_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

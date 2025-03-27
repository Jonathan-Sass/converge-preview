from flask_app import app
from flask import redirect, jsonify, request

from flask_app.models.user import User
from flask_app.models.flex_task import FlexTask


@app.post("/flex-tasks")
def add_goal_to_flex_tasks():
    """
    Adds a goal to the user's Flex Tasks list.

    Args:
        goal_id (int): The ID of the goal to be added to Flex Tasks.

    Returns:
        JSON: A success response if the goal was added successfully, or an error response.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    goal_id = request.json.get("goal_id")

    try:
        FlexTask.save_flex_task(user.id, goal_id)
        return jsonify({"success": True, "goal_id": goal_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.delete("/flex-tasks/<int:goal_id>")
def remove_flex_task(goal_id):
    """
    Deletes a goal from the user's Flex Tasks list.

    Args:
        goal_id (int): The ID of the goal to be removed from Flex Tasks.

    Returns:
        JSON: A success response if the goal was removed successfully.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    try:
        FlexTask.delete_flex_task(goal_id, user.id)
        return jsonify({"success": True, "goal_id": goal_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

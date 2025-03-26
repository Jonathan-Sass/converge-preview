from flask_app import app
from flask import render_template, redirect, session
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.routine import Routine
from flask_app.models.goal import Goal
from flask_app.models.user_response import UserResponse


# Dashboard and home page with personal metrics for an existing user
@app.get("/home")
def dashboard():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    user_id = user.id
    routine_data = Routine.find_routines_by_user_id(user_id)
    goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)
    priority_order = {
        1: "Urgent", 
        2: "High", 
        3: "Medium", 
        4: "Low"
    }

    if not routine_data:
        return redirect ("/dashboard/intro")
    else:
        dashboard_data = {"user": user, "routines": routine_data, "goals": goal_data, "priority_order": priority_order}

        # print("goals in /home route")
        # for goal in goal_data:
        #   print("***************************************************************************")
        #   pprint(vars(goal))
        #   if goal.milestones:
        #       print(" ")
        #       print(f"Milestones for: {goal.name}")
        #       for milestone in goal.milestones:
        #           pprint(vars(milestone))
        #           if milestone.action_items:
        #               print("")
        #               print("Action items")
        #               for action_item in milestone.action_items:
        #                   pprint(vars(action_item))
                      
              

        return render_template("/dashboard/dashboard.html", **dashboard_data)

@app.get("/dashboard/intro")
def dashboard_intro():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    # IF NOT orientation-data, redirect /surveys/new-user-orientation
    subcategory_slug = "user-orientation"
    user_responses = UserResponse.find_user_responses_by_user_id_and_subcategory_slug(user, subcategory_slug)
    
    if not user_responses:
        return redirect ("/surveys/user-orientation.html")
    
    return render_template("/dashboard/dashboard_intro.html")

# Introduction page for introducing new users to the morning practices section of their dashboard
@app.get("/dashboard/intro-am-practices")
def dashboard_intro_am_practices():
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")
    
    user_id = user.id
    routine_data = Routine.find_routines_by_user_id(user_id)
    goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)
    priority_order = {
        1: "Urgent", 
        2: "High", 
        3: "Medium", 
        4: "Low"
    }

    dashboard_data = {"user": user, "routines": routine_data, "goals": goal_data, "priority_order": priority_order}

    return render_template("/dashboard/dashboard_intro_am_practices.html", **dashboard_data)
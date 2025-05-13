from flask_app import app
from flask import render_template, redirect, session
from pprint import pprint

from flask_app.models.user import User
from flask_app.models.routine import Routine
from flask_app.models.routine_block import RoutineBlock
from flask_app.models.user_routine_block_practice import UserRoutineBlockPractice
from flask_app.models.goal import Goal
from flask_app.models.flex_task import FlexTask
from flask_app.models.user_response import UserResponse


@app.get("/home")
def dashboard():
    """Render the main dashboard page for a logged-in user.

    Retrieves routine, goal, and flex task data for the current user.
    Redirects to onboarding if no routines are found.

    Returns:
        Rendered dashboard template with user-specific data.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    user_id = user.id
    routine_data = Routine.find_routine_blocks_by_user_id(user_id)
    goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)
    flex_task_goal_ids = FlexTask.find_flex_tasks_goal_ids_by_user_id(user_id)
    flex_task_data = FlexTask.assemble_flex_task_data_by_goal_id(flex_task_goal_ids, goal_data)
    filtered_goal_data = Goal.filter_flex_task_goals_from_goal_data(goal_data, flex_task_goal_ids)

    priority_order = {
        1: "Urgent", 
        2: "High", 
        3: "Medium", 
        4: "Low"
    }

    dashboard_data = {
        "user": user,
        "routines": routine_data,
        "goals": goal_data,
        "filtered_goals": filtered_goal_data,
        "flex_tasks": flex_task_data,
        "priority_order": priority_order
    }

    if not routine_data:
        return redirect("/dashboard/intro")

    return render_template("/home/dashboard.html", **dashboard_data)


@app.get("/dashboard/intro")
def dashboard_intro():
    """Render the introductory dashboard page for first-time users.

    Checks for user responses in the 'user-orientation' subcategory.
    Redirects to the orientation survey if none are found.

    Returns:
        Rendered intro template or redirect to orientation survey.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    subcategory_slug = "user-objectives"
    user_responses = UserResponse.find_user_responses_by_user_id_and_subcategory_slug(user, subcategory_slug)

    priority_order = {
        1: "Urgent", 
        2: "High", 
        3: "Medium", 
        4: "Low"
    }

    if not user_responses:
        return redirect("/surveys/user-objectives")

    return render_template("/onboarding/dashboard_intro.html", priority_order = priority_order, user_responses = user_responses)

@app.get("/dashboard/intro/digital-disconnect-block")
def dashboard_intro_digital_disconnect_block():
  """
    Render the introductory dashboard page to set initial digital disconnects.
  """
  user = User.get_logged_in_user()
  if not user:
      return redirect("/")

  user_id = user.id

  # Process digital disconnect responses to select a template
  block_slug = "digital-disconnect-map"
  block_template_slug = UserResponse.process_responses_for_routine_block_template_selection(user, block_slug)
  UserRoutineBlockPractice.save_user_routine_block_practices_from_block_template_slug(user, block_template_slug)

  # Load data for dashboard
  routine_block_data = RoutineBlock.find_routine_blocks_by_user_id(user_id)
  print("*****routine_block_data in dashboard_intro_digital_disconnect")
  for block in routine_block_data:
    print("---- Routine Block ----")
    pprint(vars(block))
    if hasattr(block, "practices"):
        print("---- Practices ----")
        for practice in block.practices:
            pprint(vars(practice))

  # goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)
  # flex_task_goal_ids = FlexTask.find_flex_tasks_goal_ids_by_user_id(user_id)
  # flex_task_data = FlexTask.assemble_flex_task_data_by_goal_id(flex_task_goal_ids, goal_data)
  # filtered_goal_data = Goal.filter_flex_task_goals_from_goal_data(goal_data, flex_task_goal_ids)

  priority_order = {
      1: "Urgent", 
      2: "High", 
      3: "Medium", 
      4: "Low"
  }

  dashboard_data = {
      "user": user,
      "routine_blocks": routine_block_data,
  #     "goals": goal_data,
  #     "filtered_goals": filtered_goal_data,
  #     "flex_tasks": flex_task_data,
  #     "priority_order": priority_order
  }

  return render_template("/onboarding/dashboard_intro_digital_disconnect_block.html", **dashboard_data)

@app.get("/dashboard/intro/core-primer-block")
def dashboard_intro_core_primer_block():
  """
    Render the introductory dashboard page to set initial digital disconnects.
  """
  user = User.get_logged_in_user()
  if not user:
      return redirect("/")

  user_id = user.id

  # Process digital disconnect responses to select a template
  block_slug = "core-primer"
  block_template_slug = UserResponse.process_responses_for_routine_block_template_selection(user, block_slug)
  UserRoutineBlockPractice.save_user_routine_block_practices_from_block_template_slug(user, block_template_slug)

  # Load data for dashboard
  routine_block_data = RoutineBlock.find_routine_blocks_by_user_id(user_id)
  print("*****routine_block_data in dashboard_intro_digital_disconnect")
  for block in routine_block_data:
    print("---- Routine Block ----")
    pprint(vars(block))
    if hasattr(block, "practices"):
        print("---- Practices ----")
        for practice in block.practices:
            pprint(vars(practice))

  # goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)
  # flex_task_goal_ids = FlexTask.find_flex_tasks_goal_ids_by_user_id(user_id)
  # flex_task_data = FlexTask.assemble_flex_task_data_by_goal_id(flex_task_goal_ids, goal_data)
  # filtered_goal_data = Goal.filter_flex_task_goals_from_goal_data(goal_data, flex_task_goal_ids)

  priority_order = {
      1: "Urgent", 
      2: "High", 
      3: "Medium", 
      4: "Low"
  }

  dashboard_data = {
      "user": user,
      "routine_blocks": routine_block_data,
  #     "goals": goal_data,
  #     "filtered_goals": filtered_goal_data,
  #     "flex_tasks": flex_task_data,
      "priority_order": priority_order
  }

  return render_template("/onboarding/dashboard_intro_core_primer_block.html", **dashboard_data)

@app.get("/dashboard/intro/core-builder-block")
def dashboard_intro_core_builder_block():
  """
    Render the introductory dashboard page to set initial digital disconnects.
  """
  user = User.get_logged_in_user()
  if not user:
      return redirect("/")

  user_id = user.id

  # Process digital disconnect responses to select a template
  block_slug = "core-builder"
  block_template_slug = UserResponse.process_responses_for_routine_block_template_selection(user, block_slug)
  UserRoutineBlockPractice.save_user_routine_block_practices_from_block_template_slug(user, block_template_slug)

  # Load data for dashboard
  routine_block_data = RoutineBlock.find_routine_blocks_by_user_id(user_id)
  print("*****routine_block_data in dashboard_intro_digital_disconnect")
  for block in routine_block_data:
    print("---- Routine Block ----")
    pprint(vars(block))
    if hasattr(block, "practices"):
        print("---- Practices ----")
        for practice in block.practices:
            pprint(vars(practice))

  # goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)
  # flex_task_goal_ids = FlexTask.find_flex_tasks_goal_ids_by_user_id(user_id)
  # flex_task_data = FlexTask.assemble_flex_task_data_by_goal_id(flex_task_goal_ids, goal_data)
  # filtered_goal_data = Goal.filter_flex_task_goals_from_goal_data(goal_data, flex_task_goal_ids)

  priority_order = {
      1: "Urgent", 
      2: "High", 
      3: "Medium", 
      4: "Low"
  }

  dashboard_data = {
      "user": user,
      "routine_blocks": routine_block_data,
  #     "goals": goal_data,
  #     "filtered_goals": filtered_goal_data,
  #     "flex_tasks": flex_task_data,
      "priority_order": priority_order
  }

  return render_template("/onboarding/dashboard_intro_core_builder_block.html", **dashboard_data)

@app.get("/dashboard/intro-am-practices")
def dashboard_intro_am_practices():
    """Render the onboarding page for AM practices on the dashboard.

    Displays routine and goal data relevant to the user's morning routine.

    Returns:
        Rendered AM practices intro dashboard template.
    """
    user = User.get_logged_in_user()
    if not user:
        return redirect("/")

    user_id = user.id
    routine_block_data = RoutineBlock.find_routine_blocks_by_user_id(user_id)
    print("*****routine_block_data in dashboard_intro_am_practices")
    pprint(routine_block_data)
    goal_data = Goal.find_goals_with_milestones_and_action_items_by_user_id(user_id)

    priority_order = {
        1: "Urgent", 
        2: "High", 
        3: "Medium", 
        4: "Low"
    }

    dashboard_data = {
        "user": user,
        "routine_blocks": routine_block_data,
        "goals": goal_data,
        "priority_order": priority_order
    }

    return render_template("/dashboard/dashboard_intro_am_practices.html", **dashboard_data)

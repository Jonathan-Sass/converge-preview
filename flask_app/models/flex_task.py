from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

from flask_app.models.goal import Goal


class FlexTask:
  db = connectToMySQL("converge_schema")


  def find_flex_tasks_goal_ids_by_user_id(user_id):
    query = "SELECT * FROM user_flex_tasks WHERE user_id = %(user_id)s;"

    data = {"user_id": user_id}

    try:
      results = FlexTask.db.query_db(query, data)
      if not results:
          return []

      flex_tasks = [row["goal_id"] for row in results]
      
      return flex_tasks
    
    except Exception as e:
      raise RuntimeError(f"Error finding flex_tasks: {e}")


  def find_flex_tasks_objects_by_user_id(user_id):
    query = "SELECT * FROM user_flex_tasks WHERE user_id = %(user_id)s;"

    data = {"user_id": user_id}

    try:
      results = FlexTask.db.query_db(query, data)
      if not results:
          return []

      goal_ids = [row["goal_id"] for row in results]
      flex_tasks = Goal.find_goals_with_milestones_and_action_items_by_goal_ids(goal_ids, user_id)
      return flex_tasks
    
    except Exception as e:
      raise RuntimeError(f"Error finding flex_tasks: {e}")


  def assemble_flex_task_data_by_goal_id(flex_task_goal_ids, goal_data):
    flex_tasks = []

    goal_lookup = {goal.id:goal for goal in goal_data}
    flex_tasks = [goal_lookup[goal_id] for goal_id in flex_task_goal_ids if goal_id in goal_lookup]

    pprint(flex_tasks)

    return flex_tasks


  def save_flex_task(user_id, goal_id):
    query = """
      INSERT INTO 
        user_flex_tasks (user_id, goal_id, created_at, updated_at)
      VALUES
        (%(user_id)s, %(goal_id)s, NOW(), NOW())
      ON DUPLICATE KEY UPDATE
        updated_at = NOW();
    """

    data = {
      "user_id": user_id,
      "goal_id": goal_id
    }

    try:
      result = FlexTask.db.query_db(query, data)
      return result
    except Exception as e:
      raise RuntimeError(f"Error saving goal to Flex Tasks: {e}")
  
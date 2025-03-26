from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.goal import Goal


class FlexTask:
  db = connectToMySQL("converge_schema")


  def find_flex_tasks_by_user_id(user_id):
    query = "SELECT * FROM user_flex_tasks WHERE user_id = %(user_id)s;"

    data = {"user_id": user_id}

    try:
      results = FlexTask.db.query_db(query, data)
      if not results:
          return []

      goal_ids = [row["goal_id"] for row in results]
      Goal.find_goals_with_milestones_and_action_items_by_goal_ids(goal_ids, user_id)

    except Exception as e:
      raise RuntimeError(f"Error finding flex_tasks: {e}")


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
  
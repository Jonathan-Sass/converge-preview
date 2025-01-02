from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

def build_time_intervals_array():
  time_intervals = []

  # Days 1 - 31
  for day in range (1, 32):
    time_intervals.append(value = day, unit = "day")

  # Weeks 1 - 4
  for week in range (1, 5):
    time_intervals.append(value = week, unit = "week")

  # Months 1 - 12
  for month in range (1, 13):
    time_intervals.append(value = month, unit = "month")

  # Years 1 - 30

def seed_time_intervals():
  query = 

User.db.query_db(query, data)
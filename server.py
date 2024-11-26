from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import userHealthGoals
from flask_app.controllers import healthQuizzes
from flask_app.controllers import recreationQuizzes
from flask_app.controllers import userSurveys

if __name__ == "__main__":
    app.run(debug=True)
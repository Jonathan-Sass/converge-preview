from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import userSurveys
from flask_app.controllers import personalRoutines
from flask_app.controllers import routineTemplates
from flask_app.controllers import practices
from flask_app.controllers import userGoals
from flask_app.controllers import recTravelGoals

if __name__ == "__main__":
    app.run(debug=True)
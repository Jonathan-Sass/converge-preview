from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import user_surveys
from flask_app.controllers import personal_routines
from flask_app.controllers import routine_templates
from flask_app.controllers import practices
from flask_app.controllers import goals

if __name__ == "__main__":
    app.run(debug=True)

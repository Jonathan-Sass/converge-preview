from flask_app.config.mysqlconnection import connectToMySQL


class HealthGoal:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["id"]
        self.column = data["column"]
        self.column = data["column"]
        self.column = data["column"]
        self.column = data["column"]
        self.column = data["column"]
        self.column = data["column"]
        self.column = data["column"]
        self.column = data["column"]
        self.column = data["column"]

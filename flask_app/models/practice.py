from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from flask_app.models.user import User
from flask_app.models.duration import Duration


class Practice:
    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        self.id = data["practice_id"]
        self.name = data["practice_name"]
        self.description = data["practice_description"]
        self.practice_category = data["practice_category"]
        self.impact_rating_description = data["impact_rating_description"]
        self.impact_rating_value = data["impact_rating_value"]
        self.difficulty = data["practice_difficulty"]
        self.is_common = data["practice_is_common"]
        self.notes = data["practice_notes"]
        self.literature_summary = data["literature_summary"]
        self.durations = []
        # DO WE NEED A self.frequency?

    def create_practice_with_durations(routine_template_and_practice_data):
        practice = Practice(routine_template_and_practice_data)

        durations = Duration.fetch_durations_by_practice_id(practice)
        for duration in durations:
            practice.durations.append(duration)

        return practice

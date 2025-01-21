from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, redirect
from flask_app.models.user import User
from flask_app.models.duration import Duration


class Practice:
    db = connectToMySQL("converge_schema")

    # TODO: Need to update routine/routine_template retrieving logic to account for changes to Practice class
    def __init__(self, data):
        self.id = data["practice_id"]
        self.routine_id = data["routine_id"]
        self.name = data["practice_name"]
        self.description = data["practice_description"]
        self.practice_category = data["practice_category"]
        self.impact_rating_description = data["impact_rating_description"]
        # TODO: Condense difficulties and impact_ratings column names for consistency
        self.difficulty = data["practice_difficulty"]
        self.is_common = data["practice_is_common"]
        self.notes = data["practice_notes"]
        self.literature_summary = data["literature_summary"]
        self.selected_duration = data.get("selected_duration", None)
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.durations = []
        # DO WE NEED A self.frequency?

    def create_practice_with_durations(routine_template_and_practice_data):
        practice = Practice(routine_template_and_practice_data)

        durations = Duration.fetch_durations_by_practice_id(practice)
        for duration in durations:
            practice.durations.append(duration)

        return practice

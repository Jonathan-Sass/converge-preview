from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, jsonify, redirect
from pprint import pprint
import logging

from flask_app.models.practice import Practice
from flask_app.models.routine_block_template import RoutineBlockTemplate
from flask_app.models.duration import Duration
# from flask_app.models.user_response import UserResponse
from flask_app.models.user import User


class UserRoutineBlockPractice:
    """Model representing a reusable user's routine block practices, the individual practices to build routine blocks."""

    db = connectToMySQL("converge_schema")

    def __init__(self, data):
        """
        Initialize a RoutineTemplate object.

        Args:
            data (dict): Dictionary containing routine template fields.
        """
        self.id = data["user_routine_block_practice_id"]
        self.user_id = data["user_routine_block_practice_user_id"]
        self.routine_block_id = data["user_routine_block_practice_routine_block_id"]
        self.practice_id = data["user_routine_block_practice_practice_id"]
        self.duration_id = data["user_routine_block_practice_duration_id"]
        self.position = data["user_routine_block_practice_position"]
        self.is_active = data["user_routine_block_practice_is_active"]
        self.created_at = data["user_routine_block_practice_created_at"]
        self.updated_at = data["user_routine_block_updated_at"]

    def find_user_routine_block_practices_by_user_id(user):
        
        return
    
    @classmethod
    def save_user_routine_block_practices(cls, user, urbp_data_list):
        """
        Insert or update user_routine_block_practices in bulk.
        Each item in urbp_data_list should be a tuple:
        (user_id, routine_block_id, practice_id, duration_id, position, is_active)
        """
        if not urbp_data_list:
            logging.warning("[save_user_routine_block_practices] No data provided.")
            return 0

        query = """
            INSERT INTO user_routine_block_practices 
                (user_id, routine_block_id, practice_id, duration_id, position, is_active, created_at, updated_at)
            VALUES 
                (%s, %s, %s, %s, %s, %s, NOW(), NOW())
            ON DUPLICATE KEY UPDATE
                duration_id = VALUES(duration_id),
                position = VALUES(position),
                is_active = VALUES(is_active),
                updated_at = VALUES(updated_at);
        """

        try:
            return cls.db.query_db(query, urbp_data_list, many=True)
        except Exception as e:
            logging.error(f"[save_user_routine_block_practices] Failed to insert data: {e}")
            return 0

    @classmethod
    def save_user_routine_block_practices_from_block_template_slug(cls, user, block_template_slug):
        """
        Loads a routine block template by slug and saves all associated practices
        into user_routine_block_practices for the current user.
        """
        routine_block_template = RoutineBlockTemplate.find_routine_block_template_by_slug(block_template_slug)

        if not routine_block_template:
            logging.error(f"[save_user_routine_block_practices_from_block_template_slug] Template not found for slug: {block_template_slug}")
            return 0

        print("*****routine_block_template in save_user_routine_block_practices_etc*****")
        pprint(vars(routine_block_template))

        routine_block_id = routine_block_template.routine_block_id
        practice_data = []

        for i, practice in enumerate(routine_block_template.practices, start=1):
            practice_data.append((
                user.id,
                routine_block_id,
                practice.id,
                practice.durations[0].id if practice.durations else None,
                i,
                1  # is_active
            ))

        return cls.save_user_routine_block_practices(user, practice_data)
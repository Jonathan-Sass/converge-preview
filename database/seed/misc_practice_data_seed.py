from flask_app.config.mysqlconnection import connectToMySQL
"""
This module contains seed queries for small, static datasets related to practices, 
such as durations, frequencies, impact values, and difficulties.
"""

# Consider moving difficulties, frequencies, durations, etc. to a common module if shared outside practices
db = connectToMySQL("converge_schema")

def seed_misc_practice_data():
    seed_impact_value_data()
    seed_frequency_data()
    seed_duration_data()
    seed_engagement_level_data()
    seed_difficulty_data()
    seed_practice_objectives_data()
    seed_resources_data()


# Impact values for practices range from 1 - 5
def seed_impact_value_data():
    table_name = "Impact ratings"
    query = """ 
        INSERT IGNORE INTO impact_ratings
            (impact_rating_description, impact_rating_value)
        VALUES 
            ('Introductory impact: A gentle start with foundational benefits', 1),
            ('Moderate impact: A meaningful contribution to progress', 2),
            ('Notable impact: Has a clear and noticeable benefit', 3),
            ('High impact: Significant contribution to wellness and/or goals', 4),
            ('Very high impact: Transformative or critical benefits', 5);
    """
    execute_seed_query(query, table_name)

# CONSIDER BUILDING DYNAMIC INSERTS USING REGEX AS PRACTICE DATA GROWS

# Recommended frequencies for practices
def seed_frequency_data():
    table_name = "Frequencies"
        # ADD IS_CANONICAL COLUMN OR CONTEXTUAL COLUMN TO AVOID FUTURE AMBIGUITY

    query = """
        INSERT IGNORE INTO frequencies 
            (frequency_label, frequency_value)
        VALUES
            ('As needed', 1),
            ('Throughout the day', 2),
            ('Three times daily', 3),
            ('Twice daily', 4),
            ('Daily', 5),
            ('Every other day', 6),
            ('6 times per week', 7),
            ('5 times per week', 8),
            ('4 times per week', 9),
            ('3-5 times per week', 10),
            ('3-4 times per week', 11),
            ('2-4 times per week', 12),
            ('2-5 times per week', 13),
            ('3 times per week', 14),
            ('2-3 times per week', 15),
            ('2 times per week', 16),
            ('1-3 times per week', 17),
            ('1-2 times per week', 18),
            ('Once per week', 19),
            ('Weekdays', 20),
            ('Weekends', 21),
            ('Twice weekly', 22),
            ('Weekly', 23),
            ('Every other week', 24),
            ('Twice monthly', 25),
            ('Every three weeks', 26),
            ('Monthly', 27),
            ('Every 2 months', 28),
            ('Quarterly', 29),
            ('Semi-annually', 30),
            ('Annually', 31),
            ('Every 3 years', 32),
            ('Every 5 years', 33),
            ('Every 10 years', 34),
            ('At least 5 servings daily', 35),
            ('Each meal', 36),
            ('Before meals', 37),
            ('Nightly', 38),
            ('Ongoing', 39),
            ('Occasional', 40),
            ('Custom', 41);
    """
    execute_seed_query(query, table_name)

# Durations for practices (and likely later also goal action items)
def seed_duration_data():

    # ADD IS_CANONICAL COLUMN OR CONTEXTUAL COLUMN TO AVOID FUTURE AMBIGUITY
    table_name = "Durations"
    query = """
        INSERT IGNORE INTO durations
            (duration_label, duration_seconds)
        VALUES
            ('Ongoing', 0),
            ('1 minute', 60),
            ('2 minutes', 120),
            ('3 minutes', 180),
            ('4 minutes', 240),
            ('5 minutes', 300),
            ('10 minutes', 600),
            ('15 minutes', 900),
            ('20 minutes', 1200),
            ('25 minutes', 1500),
            ('30 minutes', 1800),
            ('35 minutes', 2100),
            ('40 minutes', 2400),
            ('45 minutes', 2700),
            ('50 minutes', 3000),
            ('55 minutes', 3300),
            ('1 hour', 3600),
            ('60 minutes', 3600),
            ('1 hour 15 minutes', 4500),
            ('1 hour 30 minutes', 5400),
            ('90 minutes', 5400),
            ('1 hour 45 minutes', 6300),
            ('2 hours', 7200),
            ('120 minutes', 7200),
            ('2 hours 30 minutes', 9000),
            ('3 hours', 10800),
            ('3 hours 30 minutes', 12600),
            ('4 hours', 14400),
            ('4 hours 30 minutes', 16200),
            ('5 hours', 18000),
            ('7 hours', 25200),
            ('8 hours', 28800),
            ('9 hours', 32400),
            ('Half day', 43200),
            ('Full day', 86400),
            ('Ongoing', NULL),
            ('Throughout the day', NULL),
            ('25 minutes work, 5 minutes break', NULL),
            ('4 cycles of 25/5 minutes with a 15-minute break', NULL), 
            ('4-6 cycles of 90 minutes (ultradian rhythm blocks)', NULL),
            ('10 minutes (planning)', 600),
            ('15 minutes (planning)', 900),
            ('1-2 hours (morning routine block)', NULL),
            ('1-3 hours (deep work block)', NULL),
            ('30 minutes (break/transition block)', NULL),
            ('1-2 hours (administrative block)', NULL),
            ('8 hours (daily schedule)', NULL),
            ('1-2 hours (evening routine block)', NULL);
    """
    execute_seed_query(query, table_name)

def seed_engagement_level_data():
    table_name = "Engagement levels"
    query = """
        INSERT IGNORE INTO engagement_levels
            (level)
        VALUES
            ('Introductory'), 
            ('Beginner'), 
            ('Intermediate'), 
            ('Advanced'), 
            ('Expert'), 
            ('Master');
    """
    execute_seed_query(query, table_name)

# Difficulties to complete a practice
def seed_difficulty_data():
    table_name = "Difficulty levels"
    query = """
        INSERT IGNORE INTO difficulty_levels
            (difficulty_label, difficulty_value)
        VALUES
            ('Very easy', 1),
            ('Easy', 2),
            ('Moderate', 3),
            ('Hard', 4),
            ('Very Challenging', 5);
    """
    execute_seed_query(query, table_name)

def seed_practice_objectives_data():
    table_name = "Practice objectives"
    query = """
        INSERT IGNORE INTO practice_objectives
            (objective_slug, objective_name, created_at, updated_at)
        VALUES
            ('hydrate', 'Hydrate', NOW(), NOW()),
            ('focus', 'Improve Focus', NOW(), NOW()),
            ('stress_resilience', 'Increase Stress Resilience', NOW(), NOW()),
            ('emotional_regulation', 'Improve Emotional Regulation', NOW(), NOW()),
            ('self_awareness', 'Increase Self-Awareness', NOW(), NOW()),
            ('clarity', 'Improve Mental Clarity', NOW(), NOW()),
            ('patience', 'Develop Patience', NOW(), NOW()),
            ('gratitude', 'Cultivate Gratitude', NOW(), NOW()),
            ('acceptance', 'Practice Acceptance', NOW(), NOW()),
            ('compassion', 'Enhance Compassion', NOW(), NOW()),
            ('strength', 'Increase Strength', NOW(), NOW()),
            ('flexibility', 'Improve Flexibility', NOW(), NOW()),
            ('bone_density', 'Maintain Bone Mineral Density', NOW(), NOW()),
            ('healthy_aging', 'Promote Healthy Aging', NOW(), NOW()),
            ('mobility', 'Enhance Mobility', NOW(), NOW()),
            ('balance', 'Improve Balance', NOW(), NOW()),
            ('endurance', 'Increase Endurance', NOW(), NOW()),
            ('posture', 'Improve Posture', NOW(), NOW()),
            ('reaction_time', 'Enhance Reaction Time', NOW(), NOW()),
            ('coordination', 'Improve Coordination', NOW(), NOW()),
            ('resilience', 'Develop Emotional Resilience', NOW(), NOW()),
            ('anxiety_management', 'Manage Anxiety', NOW(), NOW()),
            ('mood_stability', 'Enhance Mood Stability', NOW(), NOW()),
            ('sleep_quality', 'Improve Sleep Quality', NOW(), NOW()),
            ('optimism', 'Increase Optimism', NOW(), NOW()),
            ('self_compassion', 'Develop Self-Compassion', NOW(), NOW()),
            ('stress_management', 'Reduce Stress', NOW(), NOW()),
            ('creative_thinking', 'Enhance Creative Thinking', NOW(), NOW()),
            ('storytelling', 'Improve Storytelling', NOW(), NOW()),
            ('problem_solving', 'Enhance Problem Solving', NOW(), NOW()),
            ('visualization', 'Strengthen Visualization Skills', NOW(), NOW()),
            ('playfulness', 'Develop a Sense of Playfulness', NOW(), NOW()),
            ('artistic_skills', 'Build Artistic Skills', NOW(), NOW()),
            ('memory', 'Strengthen Memory', NOW(), NOW()),
            ('critical_thinking', 'Enhance Critical Thinking', NOW(), NOW()),
            ('language_skills', 'Improve Language Skills', NOW(), NOW()),
            ('pattern_recognition', 'Develop Pattern Recognition', NOW(), NOW()),
            ('active_recall', 'Strengthen Active Recall', NOW(), NOW()),
            ('note_taking', 'Improve Note-Taking', NOW(), NOW()),
            ('empathy', 'Develop Empathy', NOW(), NOW()),
            ('listening', 'Practice Active Listening', NOW(), NOW()),
            ('communication', 'Improve Communication Skills', NOW(), NOW()),
            ('collaboration', 'Foster Collaboration', NOW(), NOW()),
            ('conflict_resolution', 'Enhance Conflict Resolution Skills', NOW(), NOW()),
            ('negotiation', 'Improve Negotiation Skills', NOW(), NOW()),
            ('assertiveness', 'Practice Assertiveness', NOW(), NOW()),
            ('trust_building', 'Build Trust', NOW(), NOW()),
            ('values_reflection', 'Reflect on Personal Values', NOW(), NOW()),
            ('forgiveness', 'Practice Forgiveness', NOW(), NOW()),
            ('spiritual_resilience', 'Build Spiritual Resilience', NOW(), NOW()),
            ('sense_of_wonder', 'Deepen a Sense of Wonder', NOW(), NOW()),
            ('purpose', 'Develop a Sense of Purpose', NOW(), NOW());
    """
    execute_seed_query(query, table_name)

def seed_resources_data():
    table_name = "Resources"
    query = """
        INSERT IGNORE INTO resources
            (resource_name, resource_description, resource_link, created_at, updated_at)
        VALUES
            ('Waking Up App', 'Meditation App in Mobile App Stores', 'Search your local app store', NOW(), NOW()), 
            ('Duolingo', 'Language learning app', 'Search your local app store', NOW(), NOW())
    """
    execute_seed_query(query, table_name)

def execute_seed_query(query, table_name):
    """
    Executes a seed query and handles errors gracefully.
    """
    try:
        db.query_db(query)
        print(f"Successfully seeded {table_name}.")
    except Exception as e:
        print(f"Error seeding {table_name}: {e}")
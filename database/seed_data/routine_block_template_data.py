
# These will shift to "categorical recommendations"
routine_block_templates = [
    # AM Starter Routines for early users getting their first routines
    {
        "name": "Core Reset & Prime",
        "slug": "core-reset",
        "routine_block_slug": "core-reset",
        "description": "A simple morning routine designed to cultivate calm, clarity, and a strong start to the day.",
        "routine_type": "AM Starter",
        "category": "Mindfulness & Presence",
        "notes": "Best for users who want to feel centered before engaging with the day.",
        "practices": [
            {"practice_name": "No Screen Mornings", "routine_block_slug": "core-reset", "position": 1},
            {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 2},
            {"practice_name": "Mindfulness Meditation", "routine_block_slug": "core-reset", "position": 3}
        ],
        "traits": {
          "habit_adoption_pattern": {"trait_value": 0, "is_required": 0},
          "am_energy_pattern": {"trait_value": 0, "is_required": 0},
          "am_routine_time_availability": {"trait_value": 0, "is_required": 0},
          "movement_level": {"trait_value": 0, "is_required": 0},
          "am_exercise": {"trait_value": 0, "is_required": 0},
          "has_focus_block": {"trait_value": 0, "is_required": 0},
        }
    },
]
    # {
    #     "name": "The Energized Start",
    #     "slug": "energized-start",
    #     "description": "A quick and effective routine to activate the body and mind.",
    #     "routine_type": "AM Starter",
    #     "category": "Energy & Activation",
    #     "notes": "Great for those who want to shake off grogginess and start the day feeling strong.",
    #     "practices": [
    #         {"practice_name": "Cold Exposure", "routine_block_slug": "core-reset", "position": 1},
    #         {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "Sunrise Walk", "routine_block_slug": "core-reset", "position": 3}
    #     ]
    # },
    # {
    #     "name": "Mindful Focus Start",
    #     "slug": "mindful-focus",
    #     "description": "A structured start for a distraction-free and productive day.",
    #     "routine_type": "AM Starter",
    #     "category": "Focus & Discipline",
    #     "notes": "Best for those who need mental clarity and structured focus time.",
    #     "practices": [
    #         {"practice_name": "No Screen Mornings", "routine_block_slug": "core-reset", "position": 1},
    #         {"practice_name": "Mindfulness Meditation", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "Deep Work Session", "routine_block_slug": "productivity", "position": 3}
    #     ]
    # },
    # {
    #     "name": "The Restorative Start",
    #     "slug": "restorative-start",
    #     "description": "A slow and nourishing start that emphasizes self-care and stress resilience.",
    #     "routine_type": "AM Starter",
    #     "category": "Restoration & Self-Care",
    #     "notes": "Ideal for those who need a calm and soothing start without pressure.",
    #     "practices": [
    #         {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 1},
    #         {"practice_name": "Mindfulness Meditation", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "No Screen Mornings", "routine_block_slug": "expanded-core", "position": 3}
    #     ]
    # },
    # {
    #     "name": "Active Focus Start",
    #     "slug": "active-focus",
    #     "description": "A disciplined approach to morning routines, focusing on resilience and structure.",
    #     "routine_type": "AM Starter",
    #     "category": "Self-Discipline & Mental Strength",
    #     "notes": "Designed for those who want to cultivate consistency and fortitude.",
    #     "practices": [
    #         {"practice_name": "Cold Exposure", "routine_block_slug": "core-reset", "position": 1},
    #         {"practice_name": "Sunrise Walk", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "Deep Work Session", "routine_block_slug": "productivity", "position": 3}
    #     ]
    # },

    # {
    #     "name": "Balanced Start",
    #     "slug": "balanced-start",
    #     "description": "A simple and effective routine to kickstart the day with focus and energy.",
    #     "routine_type": "AM",
    #     "category":"Generic",
    #     "notes": "Designed for flexibility; suitable for users seeking structure without complexity.",
    #     "practices": [
    #         {"practice_name": "No Screen Mornings", "routine_block_slug": "expanded-core", "position": 1}, 
    #         {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 2}, 
    #         {"practice_name": "Cold Exposure", "routine_block_slug": "core-reset", "position": 3}, 
    #         {"practice_name": "Mindfulness Meditation", "routine_block_slug": "expanded-core", "position": 4}, 
    #         {"practice_name": "Movement/Stretch", "routine_block_slug": "expanded-core", "position": 5}, 
    #         {"practice_name": "Sunrise Walk", "routine_block_slug": "core-reset", "position": 6}, 
    #         {"practice_name": "Deep Work Session", "routine_block_slug": "productivity", "position": 7}
    #     ]
    # },
    # {
    #     "name": "Energized Focus",
    #     "slug": "energized-focus",
    #     "description": "A morning routine designed to help individuals expressing ADHD symptoms or tendencies transition smoothly into the day.",
    #     "routine_type": "AM",
    #     "category": "ADHD",
    #     "notes": "Includes sensory engagement and dopamine-building practices to maintain focus.",
    #     "practices": [
    #         {"practice_name": "No Screen Mornings", "routine_block_slug": "expanded-core", "position": 1},
    #         {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "Cold Exposure", "routine_block_slug": "core-reset", "position": 3}, 
    #         {"practice_name": "Mindfulness Meditation", "routine_block_slug": "expanded-core", "position": 4},
    #         {"practice_name": "Sunrise Walk", "routine_block_slug": "core-reset", "position": 5},
    #         {"practice_name": "Daily Prioritization", "routine_block_slug": "productivity", "position": 6},
    #         {"practice_name": "Gratitude Practice", "routine_block_slug": "expanded-core", "position": 7},
    #         {"practice_name": "Deep Work Session", "routine_block_slug": "productivity", "position": 8}
    #     ]
    # },
    # {
    #     "name": "Connected Start",
    #     "slug": "connected-start",
    #     "description": "A structured routine for individuals expressing ADHD symptoms or tendencies, with an emphasis on fostering meaningful connections.",
    #     "routine_type": "AM",
    #     "category": "ADHD",
    #     "notes": "Encourages focus and connection early in the day.",
    #     "practices": [
    #         {"practice_name": "No Screen Mornings", "routine_block_slug": "expanded-core", "position": 1},
    #         {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "Cold Exposure", "routine_block_slug": "core-reset", "position": 3}, 
    #         {"practice_name": "Mindfulness Meditation", "routine_block_slug": "expanded-core", "position": 4},
    #         {"practice_name": "Sunrise Walk", "routine_block_slug": "core-reset", "position": 5},
    #         {"practice_name": "Gratitude or Reflection Journaling", "routine_block_slug": "expanded-core", "position": 6},
    #         {"practice_name": "Check-In Message or Call", "routine_block_slug": "relationship-builder", "position": 7},
    #         {"practice_name": "Daily Prioritization", "routine_block_slug": "productivity", "position": 8},
    #         {"practice_name": "Deep Work Session", "routine_block_slug": "productivity", "position": 9}
    #     ]
    # },
    # {
    #     "name": "Peak Performance Start",
    #     "slug": "peak-performance-start",
    #     "description": "A performance-driven routine focusing on hydration, movement, and mental preparation.",
    #     "routine_type": "AM",
    #     "category": "Athlete",
    #     "notes": "Supports physical and mental readiness for peak performance.",
    #     "practices": [
    #         {"practice_name": "No Screen Mornings", "routine_block_slug": "expanded-core", "position": 1},
    #         {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "Cold Exposure", "routine_block_slug": "core-reset", "position": 3},
    #         {"practice_name": "Mindfulness Meditation", "routine_block_slug": "expanded-core", "position": 4},
    #         {"practice_name": "Structured Training Block", "routine_block_slug": "sport-training", "position": 5},
    #         {"practice_name": "Skill Practice or Morning Mobility", "routine_block_slug": "sport-training", "position": 6},
    #         {"practice_name": "Performance Visualization", "routine_block_slug": "sport-training", "position": 7},
    #         {"practice_name": "Deep Work Session", "routine_block_slug": "productivity", "position": 8}
    #     ]
    # },
    # {
    #     "name": "Momentum Builder",
    #     "slug": "momentum-builder",
    #     "description": "A routine for ADHD athletes to harness energy and focus on training goals.",
    #     "routine_type": "AM",
    #     "category": "Athlete",
    #     "notes": "Combines physical activity with practices to reinforce focus and discipline.",
    #     "practices": [
    #         {"practice_name": "No Screen Mornings", "routine_block_slug": "expanded-core", "position": 1},
    #         {"practice_name": "Morning Hydration", "routine_block_slug": "core-reset", "position": 2},
    #         {"practice_name": "Cold Exposure", "routine_block_slug": "core-reset", "position": 3},
    #         {"practice_name": "Mindfulness Meditation", "routine_block_slug": "expanded-core", "position": 4},
    #         {"practice_name": "Structured Training Block", "routine_block_slug": "sport-training", "position": 5},
    #         {"practice_name": "Skill Practice or Morning Mobility", "routine_block_slug": "sport-training", "position": 6},
    #         {"practice_name": "Performance Visualization", "routine_block_slug": "sport-training", "position": 7},
    #         {"practice_name": "Daily Prioritization", "routine_block_slug": "productivity", "position": 8},
    #         {"practice_name": "Deep Work Session", "routine_block_slug": "productivity", "position": 9}
    #     ]
    # }
# ]
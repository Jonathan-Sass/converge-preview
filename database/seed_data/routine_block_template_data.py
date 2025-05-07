
# These will shift to "categorical recommendations"
routine_block_templates = [
    # AM Starter Routines for early users getting their first routines

    # Templates for: Digital Disconnect Block
    {
      "name": "Keepin' It Real",
      "slug": "keepin-it-real",
      "routine_block_slug": "digital-disconnect",
      "description": "Start your day clear, calm, and connected to yourself, not a screen.",
      "routine_type": "AM",
      "notes": "Ideal for reducing digital noise and comparison stress early in the day.",
      "practices": [
        {"practice_name": "Tech-Free Morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice_name": "Screen Time Limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice_name": "Social Media Limit", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
      "traits": {
        "digital-hygiene": {"trait_value": 2, "is_required": 1},
        "digital-detox-willingness": {"trait_value": 2, "is_required": 0},
        "am-routine-comprehensiveness": {"trait_value": 0, "is_required": 0}
      }
    },
    {
      "name": "News‑Light Boundaries",
      "slug": "news-light-boundaries",
      "routine_block_slug": "digital-disconnect",
      "description": "Pair a tech‑free start with breaks and a cap on your news intake.",
      "routine_type": "AM",
      "notes": "Great for users who want to reduce news‑driven stress without giving up all screens.",
      "practices": [
        {"practice_name": "Tech-Free Morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice_name": "Screen Time Limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice_name": "News Limit", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
      "traits": {
        "digital-hygiene": {"trait_value": 3, "is_required": 1},
        "digital-detox-willingness": {"trait_value": 2, "is_required": 0}
      }
    },
    {
      "name": "Focus‑Block Boundaries",
      "slug": "focus-block-boundaries",
      "routine_block_slug": "digital-disconnect",
      "description": "Combine a phone‑free morning, screen breaks, and dedicated no‑phone focus slots.",
      "routine_type": "AM Starter",
      "notes": "Perfect for users aiming to preserve deep focus throughout the day.",
      "practices": [
        {"practice_name": "Tech‑Free Morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice_name": "Screen Time Limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice_name": "Phone‑Free Block", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
      "traits": {
        "digital-hygiene": {"trait_value": 3, "is_required": 1},
        "digital-detox-willingness": {"trait_value": 3, "is_required": 0},
        "has_focus_block": {"trait_value": 1, "is_required": 0}
      }
    },

    # CORE SYSTEM PRIMER TEMPLATES
    {
      "name": "Basic Primer",
      "slug": "basic-primer",
      "routine_block_slug": "core-primers",
      "description": "Hydrate, take a quick cold exposure, then enjoy a sunrise coffee.",
      "routine_type": "AM Starter",
      "notes": "A three‑step energizer to kickstart body and mind in under 5 minutes.",
      "practices": [
        {"practice_name": "Morning Hydration", "routine_block_slug": "core-primers", "position": 1},
        {"practice_name": "Cold Exposure", "routine_block_slug": "core-primers", "position": 2},
        {"practice_name": "Sunrise Beverage", "routine_block_slug": "core-primers", "position": 3}
      ],
      "traits": {
        "am-routine-comprehensiveness": {"trait_value": 1, "is_required": 1},
        "fuel-and-hydration": {"trait_value": 2, "is_required": 1}
      }
    },
    {
      "name": "Basic Primer & Walk",
      "slug": "basic-primer-walk",
      "routine_block_slug": "core-primers",
      "description": "Hydrate, cold exposure, then a brief sunrise walk for gentle movement.",
      "routine_type": "AM Starter",
      "notes": "Adds circulation benefits to your core primer trio.",
      "practices": [
        {"practice_name": "Morning Hydration", "routine_block_slug": "core-primers", "position": 1},
        {"practice_name": "Cold Exposure", "routine_block_slug": "core-primers", "position": 2},
        {"practice_name": "Sunrise Walk", "routine_block_slug": "core-primers", "position": 3}
      ],
      "traits": {
        "am-routine-comprehensiveness": {"trait_value": 1, "is_required": 1},
        "movement_level": {"trait_value": 1, "is_required": 0}
      }
    },

    # Templates for: Core System Builders Block
    {
      "name": "HIIT and Sit",
      "slug": "hiit-and-sit",
      "routine_block_slug": "core-system-builders",
      "description": "High-intensity movement followed by mobility and meditation to reset body and mind.",
      "routine_type": "Any",
      "category": "Mind-Body Reset",
      "notes": "Pairs a quick energy spike with grounding recovery and calm.",
      "practices": [
        { "practice_name": "HIIT Workout", "position": 1 },
        { "practice_name": "Mobility Circuit", "position": 2 },
        { "practice_name": "Mindfulness Meditation", "position": 3 }
      ]
    },
    {
      "name": "Mindful Movement",
      "slug": "mindful-movement",
      "routine_block_slug": "core-system-builders",
      "description": "A mobility-focused flow with attention to presence and gratitude.",
      "routine_type": "Any",
      "category": "Mind-Body Reset",
      "notes": "Ideal for morning movement or a mid-day stress release.",
      "practices": [
        { "practice_name": "Yoga Flow or Pilates Routine", "position": 1 },
        { "practice_name": "Gratitude Practice", "position": 2 },
        { "practice_name": "Mindfulness Meditation", "position": 3 }
      ]
    },
    {
      "name": "Fit & Strong",
      "slug": "fit-and-strong",
      "routine_block_slug": "core-system-builders",
      "description": "A combined cardio and strength routine, finished with mindful grounding.",
      "routine_type": "Any",
      "category": "Mind-Body Reset",
      "notes": "Great for days where you want to hit body and mind with purpose.",
      "practices": [
        { "practice_name": "Aerobic Workout", "position": 1 },
        { "practice_name": "Strength Training", "position": 2 },
        { "practice_name": "Breath-Based Stillness Practice", "position": 3 }
      ]
    },
    {
      "name": "Ground & Reset",
      "slug": "ground-and-reset",
      "routine_block_slug": "core-system-builders",
      "description": "Gentle mobility, breath, and presence to reset the nervous system.",
      "routine_type": "Any",
      "category": "Mind-Body Reset",
      "notes": "Great for evenings or high-stress days where calm is a priority.",
      "practices": [
        { "practice_name": "Mobility Flow", "position": 1 },
        { "practice_name": "Box Breathing", "position": 2 },
        { "practice_name": "Walking Reflection", "position": 3 }
      ]
    },
    {
      "name": "Resilience Circuit",
      "slug": "resilience-circuit",
      "routine_block_slug": "core-system-builders",
      "description": "Light strength, mobility, and cognitive training for mental and physical resilience.",
      "routine_type": "Any",
      "category": "Mind-Body Reset",
      "notes": "For days you want to train durability—body and mind together.",
      "practices": [
        { "practice_name": "Meditation", "position": 1 },
        { "practice_name": "Functional Strength Primer", "position": 2 },
        { "practice_name": "Mobility Circuit", "position": 3 }
      ]
    },
    {
      "name": "Flow & Focus",
      "slug": "flow-and-focus",
      "routine_block_slug": "core-system-builders",
      "description": "A full-body movement flow followed by breath and visualization.",
      "routine_type": "Any",
      "category": "Mind-Body Reset",
      "notes": "Use this block to build creative energy and mental clarity.",
      "practices": [
        { "practice_name": "Dynamic Mobility Flow", "position": 1 },
        { "practice_name": "Breath Ladder", "position": 2 },
        { "practice_name": "Visualization Practice", "position": 3 }
      ]
    }
]
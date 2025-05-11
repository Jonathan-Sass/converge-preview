
# These will shift to "categorical recommendations"
routine_block_templates = [
    # AM Starter Routines for early users getting their first routines

    # Templates for: Digital Disconnect Block
    {
      "name": "Keepin' It Simple",
      "slug": "keepin-it-real",
      "routine_block_slug": "digital-disconnect",
      "description": "Start your day clear, calm, and connected to yourself, not a screen.",
      "routine_type": "AM",
      "notes": "Ideal for reducing digital noise and comparison stress early in the day.",
      "practices": [
        {"practice-slug": "tech-free-morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice-slug": "screen-time-limit", "routine_block_slug": "digital-disconnect", "position": 2},
      ],
      # DEPRECATED - Keeping example snippet matching existing seed logic in case of reimplementation of traits
      # "traits": {
      #   "digital-hygiene": {"trait_value": 2, "is_required": 1},
      #   "digital-detox-willingness": {"trait_value": 2, "is_required": 0},
      #   "am-routine-comprehensiveness": {"trait_value": 0, "is_required": 0}
      # }
    },
    {
      "name": "Keepin' It Real",
      "slug": "keepin-it-real",
      "routine_block_slug": "digital-disconnect",
      "description": "Start your day clear, calm, and connected to yourself, not a screen.",
      "routine_type": "AM",
      "notes": "Ideal for reducing digital noise and comparison stress early in the day.",
      "practices": [
        {"practice-slug": "tech-free-morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice-slug": "screen-time-limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice-slug": "social-media-limit", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
    },
    {
      "name": "News‑Light Boundaries",
      "slug": "news-light-boundaries",
      "routine_block_slug": "digital-disconnect",
      "description": "Pair a tech‑free start with breaks and a cap on your news intake.",
      "routine_type": "AM",
      "notes": "Great for users who want to reduce news‑driven stress without giving up all screens.",
      "practices": [
        {"practice-slug": "tech-free-morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice-slug": "screen-time-limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice-slug": "news-limit", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
    },
    {
      "name": "Focus‑Block Boundaries",
      "slug": "focus-block-boundaries",
      "routine_block_slug": "digital-disconnect",
      "description": "Combine a phone‑free morning, screen breaks, and dedicated no‑phone focus slots.",
      "routine_type": "AM Starter",
      "notes": "Perfect for users aiming to preserve deep focus throughout the day.",
      "practices": [
        {"practice-slug": "tech-free-morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice-slug": "screen-time-limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice-slug": "phone-free-block", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
    },
    # {
    #   "name": "Micro‑Break Reset",
    #   "slug": "micro-break-reset",
    #   "routine_block_slug": "digital-disconnect",
    #   "description": "Ease into digital boundaries with short, intentional breaks and a gentle morning start.",
    #   "routine_type": "AM",
    #   "notes": "Designed for users new to the idea of digital limits, or those not yet ready for full screen-free periods.",
    #   "practices": [
    #     {"practice-slug": "Short Morning Screen Break", "routine_block_slug": "digital-disconnect", "position": 1},
    #     {"practice-slug": "Scheduled Micro‑Breaks", "routine_block_slug": "digital-disconnect", "position": 2},
    #     {"practice-slug": "5‑Minute Phone-Free Pause", "routine_block_slug": "digital-disconnect", "position": 3}
    #   ],
    # },
    {
      "name": "Social Scroll Reset",
      "slug": "social-scroll-reset",
      "routine_block_slug": "digital-disconnect",
      "description": "Reclaim your mornings and reduce social media overwhelm with targeted screen breaks.",
      "routine_type": "AM Starter",
      "notes": "Ideal for users who feel drained or distracted by social feeds early in the day.",
      "practices": [
        {"practice-slug": "tech-free-morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice-slug": "social-media-limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice-slug": "doomscroll-break-reminder", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
    },
    {
      "name": "All‑Day Digital Detox Lite",
      "slug": "digital-detox-lite",
      "routine_block_slug": "digital-disconnect",
      "description": "Anchor your day with a screen-free start and spaced breaks to reduce overload.",
      "routine_type": "AM Starter",
      "notes": "A well-rounded plan for users wanting to reduce screen fatigue without hard limits.",
      "practices": [
        {"practice-slug": "tech-free-morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice-slug": "screen-break", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice-slug": "app-limits", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
    },
    {
      "name": "News Limits",
      "slug": "news-limits",
      "routine_block_slug": "digital-disconnect",
      "description": "Create a buffer from news overwhelm with calm, screen-free mornings.",
      "routine_type": "AM",
      "notes": "Designed for users feeling tension or anxiety from early news exposure.",
      "practices": [
        {"practice-slug": "tech-free-morning", "routine_block_slug": "digital-disconnect", "position": 1},
        {"practice-slug": "news-limit", "routine_block_slug": "digital-disconnect", "position": 2},
        {"practice-slug": "screen-time-limit", "routine_block_slug": "digital-disconnect", "position": 3}
      ],
      "traits": {
        "digital-hygiene": {"trait_value": 2, "is_required": 1},
        "news-anxiety": {"trait_value": 1, "is_required": 1}
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
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primers", "position": 1},
        {"practice-slug": "cold-exposure", "routine_block_slug": "core-primers", "position": 2},
        {"practice-slug": "sunrise-beverage", "routine_block_slug": "core-primers", "position": 3}
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
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primers", "position": 1},
        {"practice-slug": "cold-exposure", "routine_block_slug": "core-primers", "position": 2},
        {"practice-slug": "sunrise-walk", "routine_block_slug": "core-primers", "position": 3}
      ],
      "traits": {
        "am-routine-comprehensiveness": {"trait_value": 1, "is_required": 1},
        "movement_level": {"trait_value": 1, "is_required": 0}
      }
    },

    # Templates for: Core System Builders Block
    # {
    #   "name": "HIIT and Sit",
    #   "slug": "hiit-and-sit",
    #   "routine_block_slug": "core-system-builders",
    #   "description": "High-intensity movement followed by mobility and meditation to reset body and mind.",
    #   "routine_type": "Any",
    #   "category": "Mind-Body Reset",
    #   "notes": "Pairs a quick energy spike with grounding recovery and calm.",
    #   "practices": [
    #     { "practice-slug": "HIIT Workout", "position": 1 },
    #     { "practice-slug": "Mobility Circuit", "position": 2 },
    #     { "practice-slug": "Mindfulness Meditation", "position": 3 }
    #   ]
    # },
    # {
    #   "name": "Mindful Movement",
    #   "slug": "mindful-movement",
    #   "routine_block_slug": "core-system-builders",
    #   "description": "A mobility-focused flow with attention to presence and gratitude.",
    #   "routine_type": "Any",
    #   "category": "Mind-Body Reset",
    #   "notes": "Ideal for morning movement or a mid-day stress release.",
    #   "practices": [
    #     { "practice-slug": "Yoga Flow or Pilates Routine", "position": 1 },
    #     { "practice-slug": "Gratitude Practice", "position": 2 },
    #     { "practice-slug": "Mindfulness Meditation", "position": 3 }
    #   ]
    # },
    # {
    #   "name": "Fit & Strong",
    #   "slug": "fit-and-strong",
    #   "routine_block_slug": "core-system-builders",
    #   "description": "A combined cardio and strength routine, finished with mindful grounding.",
    #   "routine_type": "Any",
    #   "category": "Mind-Body Reset",
    #   "notes": "Great for days where you want to hit body and mind with purpose.",
    #   "practices": [
    #     { "practice-slug": "Aerobic Workout", "position": 1 },
    #     { "practice-slug": "Strength Training", "position": 2 },
    #     { "practice-slug": "Breath-Based Stillness Practice", "position": 3 }
    #   ]
    # },
    # {
    #   "name": "Ground & Reset",
    #   "slug": "ground-and-reset",
    #   "routine_block_slug": "core-system-builders",
    #   "description": "Gentle mobility, breath, and presence to reset the nervous system.",
    #   "routine_type": "Any",
    #   "category": "Mind-Body Reset",
    #   "notes": "Great for evenings or high-stress days where calm is a priority.",
    #   "practices": [
    #     { "practice-slug": "Mobility Flow", "position": 1 },
    #     { "practice-slug": "Box Breathing", "position": 2 },
    #     { "practice-slug": "Walking Reflection", "position": 3 }
    #   ]
    # },
    # {
    #   "name": "Resilience Circuit",
    #   "slug": "resilience-circuit",
    #   "routine_block_slug": "core-system-builders",
    #   "description": "Light strength, mobility, and cognitive training for mental and physical resilience.",
    #   "routine_type": "Any",
    #   "category": "Mind-Body Reset",
    #   "notes": "For days you want to train durability—body and mind together.",
    #   "practices": [
    #     { "practice-slug": "Meditation", "position": 1 },
    #     { "practice-slug": "Functional Strength Primer", "position": 2 },
    #     { "practice-slug": "Mobility Circuit", "position": 3 }
    #   ]
    # },
    # {
    #   "name": "Flow & Focus",
    #   "slug": "flow-and-focus",
    #   "routine_block_slug": "core-system-builders",
    #   "description": "A full-body movement flow followed by breath and visualization.",
    #   "routine_type": "Any",
    #   "category": "Mind-Body Reset",
    #   "notes": "Use this block to build creative energy and mental clarity.",
    #   "practices": [
    #     { "practice-slug": "Dynamic Mobility Flow", "position": 1 },
    #     { "practice-slug": "Breath Ladder", "position": 2 },
    #     { "practice-slug": "Visualization Practice", "position": 3 }
    #   ]
    # }
]
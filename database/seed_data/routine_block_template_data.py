
# These will shift to "categorical recommendations"
routine_block_templates = [
    # AM Starter Routines for early users getting their first routines

    # Templates for: Digital Disconnect Block
    {
      "name": "Keepin' It Simple",
      "slug": "keepin-it-simple",
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
      "routine_type": "AM",
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
      "routine_type": "AM",
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
      "routine_type": "AM",
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
      ]
    },

    # CORE SYSTEM PRIMER TEMPLATES

    {
      "name": "Basic Primer",
      "slug": "basic-primer",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, take a quick cold exposure, then enjoy a sunrise coffee.",
      "routine_type": "AM",
      "notes": "A three‑step energizer to kickstart body and mind in under 5 minutes.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-face-rinse", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sunrise-beverage", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    {
      "name": "Basic Primer Sun Walk",
      "slug": "basic-primer-walk",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, cold exposure, then a brief sunrise walk for gentle movement.",
      "routine_type": "AM",
      "notes": "Adds circulation benefits to your core primer trio.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-face-rinse", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sun-walk", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    {
      "name": "Basic Primer Sun Workout",
      "slug": "basic-primer-sun-run",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, get a quick cold burst, then head out for a sunrise jog or run to elevate energy and mood.",
      "routine_type": "AM",
      "notes": "A physically activating start that syncs circadian rhythms, boosts endorphins, and clears mental fog.",
      "practices": [
        {
          "practice-slug": "morning-hydration",
          "routine_block_slug": "core-primer",
          "position": 1
        },
        {
          "practice-slug": "cold-face-rinse",
          "routine_block_slug": "core-primer",
          "position": 2
        },
        {
          "practice-slug": "sun-run",
          "routine_block_slug": "core-primer",
          "position": 3
        }
      ]
    },
    {
      "name": "Intermediate Primer",
      "slug": "intermediate-primer",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, take a brief cold shower, then enjoy a sunrise coffee.",
      "routine_type": "AM",
      "notes": "Boost alertness and energy with a stronger cold exposure and your favorite morning beverage.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-shower", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sunrise-beverage", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    {
      "name": "Intermediate Primer Sun Walk",
      "slug": "intermediate-primer-walk",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, take a cold shower, then head out for a light sunrise walk.",
      "routine_type": "AM",
      "notes": "Upgrades your morning reset with invigorating contrast and light movement.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-shower", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sun-walk", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    {
      "name": "Intermediate Primer Sun Workout",
      "slug": "intermediate-primer-sun-run",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, power up with a cold shower, then go for a sunrise run to elevate mood and clarity.",
      "routine_type": "AM",
      "notes": "Activates thermogenesis, sharpens focus, and builds mental resilience.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-shower", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sun-run", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    {
      "name": "Advanced Primer",
      "slug": "advanced-primer",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, take a cold plunge, then savor a sunrise beverage with calm alertness.",
      "routine_type": "AM",
      "notes": "A high-intensity reset for stress adaptation, willpower training, and lasting focus.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-plunge", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sunrise-beverage", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    {
      "name": "Advanced Primer Sun Walk",
      "slug": "advanced-primer-walk",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, take a cold plunge, then walk into the sunlight for a full-spectrum recharge.",
      "routine_type": "AM",
      "notes": "A bold start for physical and emotional resilience — gentle movement after cold enhances recovery.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-plunge", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sun-walk", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    {
      "name": "Advanced Primer Sun Workout",
      "slug": "advanced-primer-sun-run",
      "routine_block_slug": "core-primer",
      "description": "Hydrate, brave a cold plunge, then run into the rising sun to train discipline, energy, and mood.",
      "routine_type": "AM",
      "notes": "High-octane primer for those building grit, stamina, and inner fire.",
      "practices": [
        {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
        {"practice-slug": "cold-plunge", "routine_block_slug": "core-primer", "position": 2},
        {"practice-slug": "sun-run", "routine_block_slug": "core-primer", "position": 3}
      ]
    },
    # {
    #   "name": "Focus Primer",
    #   "slug": "focus-primer",
    #   "routine_block_slug": "core-primer",
    #   "description": "Hydrate, engage in breathwork, and take a brief cold exposure to sharpen focus.",
    #   "routine_type": "AM",
    #   "notes": "Designed for mental clarity and alertness.",
    #   "practices": [
    #     {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 1},
    #     {"practice-slug": "breathwork", "routine_block_slug": "core-primer", "position": 2},
    #     {"practice-slug": "cold-exposure", "routine_block_slug": "core-primer", "position": 3}
    #   ]
    # },
    
    # {
    #   "name": "Resilience Primer",
    #   "slug": "resilience-primer",
    #   "routine_block_slug": "core-primer",
    #   "description": "A high-impact start with cold exposure, breath control, and hydration to build stress resilience.",
    #   "routine_type": "AM",
    #   "notes": "Best for users seeking peak performance through physiological challenge.",
    #   "practices": [
    #     {"practice-slug": "cold-exposure", "routine_block_slug": "core-primer", "position": 1},
    #     {"practice-slug": "breath-control", "routine_block_slug": "core-primer", "position": 2},
    #     {"practice-slug": "morning-hydration", "routine_block_slug": "core-primer", "position": 3}
    #   ]
    # },


  # Templates for: Core System Builders Block
  {
    "name": "Sit & HIIT",
    "slug": "sit-and-hiit",
    "routine_block_slug": "core-builder",
    "description": "Mindfulness first, followed by high-intensity movement and mobility for a total reset.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Trains discipline, spikes energy, then grounds the system.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "hiit-workout", "position": 2 },
      { "practice-slug": "dynamic-stretch-flow", "position": 3 }
    ]
  },
  {
    "name": "Mindful Flow with Gratitude",
    "slug": "mindful-flow-gratitude",
    "routine_block_slug": "core-builder",
    "description": "A grounding meditation followed by flowing movement and gratitude.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Designed to ease stress while building presence and mobility.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "gentle-yoga-flow", "position": 2 },
      { "practice-slug": "gratitude-practice", "position": 3 }
    ]
  },
  {
    "name": "Strong Start",
    "slug": "strong-start",
    "routine_block_slug": "core-builder",
    "description": "Begin with stillness, then build strength and cardio conditioning.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Balances inner calm with outer intensity.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "running", "position": 2 },
      { "practice-slug": "strength-training-circuit", "position": 3 }
    ]
  },
  {
    "name": "Centered Strength",
    "slug": "centered-strength",
    "routine_block_slug": "core-builder",
    "description": "Build core strength and mental calm through martial-influenced movement and deep focus.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Anchors your energy with breath and bodyweight strength.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "tai-chi", "position": 2 },
      { "practice-slug": "calisthenic-strength-training", "position": 3 }
    ]
  },
  {
    "name": "Martial Discipline",
    "slug": "martial-discipline",
    "routine_block_slug": "core-builder",
    "description": "Begin with clarity, then train functional martial movement and calisthenic strength.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Sharpens attention and builds physical resilience through martial fundamentals.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "mma-training", "position": 2 },
      { "practice-slug": "calisthenic-strength-training", "position": 3 }
    ]
  },
  {
    "name": "Internal Power Flow",
    "slug": "internal-power-flow",
    "routine_block_slug": "core-builder",
    "description": "Cultivate presence through meditation, then move slowly with strength through traditional internal arts.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Combines stillness, breath, and soft strength for nervous system balance and control.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "tai-chi", "position": 2 },
      { "practice-slug": "nei-gong", "position": 3 }
    ]
  },
  {
    "name": "Reset & Rise",
    "slug": "reset-and-rise",
    "routine_block_slug": "core-builder",
    "description": "Calm your system, then restore mobility and integrate reflection.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Great for high-stress days or evening transitions.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "daily-mobility", "position": 2 },
      { "practice-slug": "gratitude-journaling", "position": 3 }
    ]
  },
  {
    "name": "Resilience Stack",
    "slug": "resilience-stack",
    "routine_block_slug": "core-builder",
    "description": "Build mental clarity, then train functional strength and movement durability.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Best for cultivating long-term focus and physical resilience.",
    "practices": [
      { "practice-slug": "mindfulness-meditation", "position": 1 },
      { "practice-slug": "functional-strength-training", "position": 2 },
      { "practice-slug": "dynamic-stretch-flow", "position": 3 }
    ]
  },
  {
    "name": "Mindful Movement",
    "slug": "mindful-movement",
    "routine_block_slug": "core-builder",
    "description": "A mobility-focused flow with attention to presence and gratitude.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Ideal for morning movement or a mid-day stress release.",
    "practices": [
      { "practice-slug": "gentle-yoga-flow", "position": 1 },
      { "practice-slug": "gratitude-practice", "position": 2 },
      { "practice-slug": "mindfulness-meditation", "position": 3 }
    ]
  },
  {
    "name": "Fit & Strong",
    "slug": "fit-and-strong",
    "routine_block_slug": "core-builder",
    "description": "A combined cardio and strength routine, finished with mindful grounding.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Great for days where you want to hit body and mind with purpose.",
    "practices": [
      { "practice-slug": "running", "position": 1 },
      { "practice-slug": "strength-training-circuit", "position": 2 },
      { "practice-slug": "mindfulness-meditation", "position": 3 }
    ]
  },
  {
    "name": "Ground & Reset",
    "slug": "ground-and-reset",
    "routine_block_slug": "core-builder",
    "description": "Gentle mobility, breath, and presence to reset the nervous system.",
    "routine_type": "Any",
    "category": "Mind-Body Reset",
    "notes": "Great for evenings or high-stress days where calm is a priority.",
    "practices": [
      { "practice-slug": "daily-mobility", "position": 1 },
      { "practice-slug": "box-breathing", "position": 2 },
      { "practice-slug": "mindfulness-meditation", "position": 3 }
    ]
  }
]
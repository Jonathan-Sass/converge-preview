"""
practice_data: dict
A structured dictionary of practices, organized by categories(e.g. "Grounding & Internal Reset") and subcategories(e.g. "Cold Exposure").
Each category contains a list of practice entries, which include metadata for:

- name: Name of the practice.
- description: Short summary of the practice.
- benefit_synopsis: Summary of health/wellness benefits.
- recommended_durations: List of durations (as dicts).
- impact_rating_id: Foreign key to impact rating scale.
- difficulty_level_id: Foreign key to difficulty scale.
- frequency: Human-readable recommendation for how often to practice.
- is_common: Boolean to indicate prevalence among users.
- notes: Longer explanation or context.
- objectives: Tags used for matching with goals or user needs.
"""


new_practice_data = {

  # CATEGORY
  "Grounding & Internal Reset": {
    
    # PRACTICE SUBCATEGORY
    "Morning Hydration": 
    [
      {
        "name": "Morning Hydration",
        "category": "Grounding & Internal Reset",
        "subcategory": "Morning Hydration",
        "description": "Drink a full glass of water shortly after waking up.",
        "benefit_synopsis": "Rehydrates the body, supports metabolism, and boosts energy.",
        "recommended_durations": [
          { "duration_label": "2 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Every morning",
        "is_common": True,
        "notes": "After hours without fluids, your body is in a mild state of dehydration. Morning hydration kickstarts metabolism, improves cognitive function, and primes the digestive system.",
        "objectives": [
          "hydrate",
          "boost_energy_levels",
          "support_metabolism"
        ]
      },
      {
        "name": "Sole Hydration",
        "category": "Grounding & Internal Reset",
        "subcategory": "Morning Hydration",
        "description": "Add a pinch of natural sea salt or sole to your morning water.",
        "benefit_synopsis": "Replenishes minerals and supports adrenal function.",
        "recommended_durations": [
          { "duration_label": "2 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Every morning or as needed",
        "is_common": False,
        "notes": "Adding electrolytes or sole (a concentrated sea or himalayan salt water solution) may support hydration more effectively by aiding cellular absorption, especially if you're low in minerals after sleep.",
        "objectives": [
          "enhance_hydration",
          "replenish_minerals",
          "support_adrenal_health"
        ]
      },
      {
        "name": "Lemon Water",
        "category": "Grounding & Internal Reset",
        "subcategory": "Morning Hydration",
        "description": "Squeeze fresh lemon into your morning water for added benefits.",
        "benefit_synopsis": "Aids digestion, supports liver function, and adds flavor.",
        "recommended_durations": [
          { "duration_label": "2 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Every morning or as preferred",
        "is_common": True,
        "notes": "Lemon adds vitamin C and can help stimulate the digestive system in the morning. It may also support liver detox pathways and make hydration more enjoyable.",
        "objectives": [
          "aid_digestion",
          "support_liver_health",
          "make_hydration_enjoyable"
        ]
      },
    ],

    # PRACTICE SUBCATEGORY
    "Cold Immersion": [
      {
        "name": "Cold Face Rinse",
        "category": "Grounding & Internal Reset",
        "subcategory": "Cold Immersion",
        "description": "Splash cold water on your face for a short, energizing reset.",
        "benefit_synopsis": "Activates the diving reflex to calm your nervous system and boost alertness.",
        "recommended_durations": [{"duration_label": "1 minute"}, {"duration_label": "2 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": True,
        "notes": "Cold water on the face stimulates the vagus nerve and triggers the mammalian diving reflex, helping slow your heart rate and regulate stress.",
        "objectives": ["reset_nervous_system", "increase_alertness", "stimulate_vagus_nerve"]
      },
      {
        "name": "Cold Hand Wash or Dip",
        "category": "Grounding & Internal Reset",
        "subcategory": "Cold Immersion",
        "description": "Dip your hands or wrists into cold water to stimulate a quick reset.",
        "benefit_synopsis": "Rapidly cools the body and stimulates parasympathetic calm.",
        "recommended_durations": [{"duration_label": "2 minutes"}, {"duration_label": "3 minutes"}],
        "impact_rating_id": 2,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "A low-barrier practice for people not ready for full cold exposure. Activates thermoreceptors and initiates vagal stimulation.",
        "objectives": ["cool_down", "reduce_overwhelm", "promote_regulation"]
      },
      {
        "name": "Cold Shower",
        "category": "Grounding & Internal Reset",
        "subcategory": "Cold Immersion",
        "description": "Take a full shower using only cold water from start to finish.",
        "benefit_synopsis": "Boosts dopamine, sharpens focus, and strengthens stress tolerance.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" },
          { "duration_label": "3 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–5 times per week",
        "is_common": False,
        "notes": "Cold showers activate the sympathetic nervous system initially, followed by a calming parasympathetic rebound. They may increase dopamine by up to 250%, improve mental resilience, reduce inflammation, and promote clarity.",
        "objectives": [
          "boost_mood",
          "increase_focus",
          "build_stress_resilience"
        ]
      },
      {
        "name": "Cold Shower Finisher",
        "category": "Grounding & Internal Reset",
        "subcategory": "Cold Immersion",
        "description": "Finish your shower with 30–60 seconds of cold water. ",
        "benefit_synopsis": "Boosts energy, improves circulation, and builds mental toughness.",
        "recommended_durations": [{"duration_label": "30 seconds"}, {"duration_label": "1 minute"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily or every other day",
        "is_common": True,
        "notes": "Cold showers may increase dopamine, enhance circulation, and help train stress resilience — all with minimal time commitment.",
        "objectives": ["boost_energy_levels", "enhance_resilience", "increase_alertness"]
      },
      {
        "name": "Cold Plunge or Ice Bath",
        "category": "Grounding & Internal Reset",
        "subcategory": "Cold Immersion",
        "description": "Submerge your body in cold water up to your neck for a short time.",
        "benefit_synopsis": "Reduces inflammation, boosts mood, and sharpens focus.",
        "recommended_durations": [{"duration_label": "2 minutes"}, {"duration_label": "3 minutes"}, {"duration_label": "5 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–4 times per week",
        "is_common": False,
        "notes": "Cold immersion increases norepinephrine and dopamine, improves mood, and reduces post-exercise soreness. May enhance long-term resilience and mental clarity.",
        "objectives": ["reduce_inflammation", "improve_mood", "build_mental_toughness"]
      },
      {
        "name": "Cold Water Face Immersion",
        "category": "Grounding & Internal Reset",
        "subcategory": "Cold Immersion",
        "description": "Dunk your face in a bowl of ice water to quickly reset your system.",
        "benefit_synopsis": "Activates the diving reflex and shifts your body into a calm state.",
        "recommended_durations": [{"duration_label": "15 seconds"}, {"duration_label": "30 seconds"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Used in some therapeutic settings for acute anxiety or panic. Lowers heart rate and rapidly soothes the nervous system.",
        "objectives": ["interrupt_panic_cycle", "soothe_nervous_system", "regulate_breathing"]
      },
    ],
    
    # PRACTICE SUBCATEGORY
    "Breathing Practices": 
    [
      {
        "name": "Box Breathing",
        "category": "Grounding & Internal Reset",
        "subcategory": "Breathing Practices",
        "description": "Inhale for 4 seconds, hold for 4, exhale for 4, hold for 4 — repeat in a steady rhythm.",
        "benefit_synopsis": "Balances the nervous system and reduces stress.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "4 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Used by high-performers like Navy SEALs, this rhythmic breathing technique helps regulate the nervous system and create a sense of calm and control.",
        "objectives": [
          "regulate_nervous_system",
          "reduce_stress",
          "enhance_focus"
        ]
      },
      {
        "name": "4-7-8 Breathing",
        "category": "Grounding & Internal Reset",
        "subcategory": "Breathing Practices",
        "description": "Inhale for 4 seconds, hold for 7, exhale slowly for 8 seconds.",
        "benefit_synopsis": "Slows heart rate and encourages deep calm.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "3 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "As needed or before bed",
        "is_common": True,
        "notes": "Promotes a parasympathetic state and can be especially helpful for winding down before sleep or calming anxiety.",
        "objectives": [
          "reduce_anxiety",
          "promote_rest",
          "slow_heart_rate"
        ]
      },
      {
        "name": "Coherent Breathing",
        "category": "Grounding & Internal Reset",
        "subcategory": "Breathing Practices",
        "description": "Breathe slowly and evenly at around 5–6 breaths per minute.",
        "benefit_synopsis": "Promotes heart rate variability and emotional balance.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily or during stress",
        "is_common": False,
        "notes": "This method synchronizes heart rate, breath, and brain rhythms — often used in trauma recovery and stress reduction protocols.",
        "objectives": [
          "enhance_hrv",
          "support_emotional_regulation",
          "stabilize_nervous_system"
        ]
      },
      {
        "name": "Physiological Sigh",
        "category": "Grounding & Internal Reset",
        "subcategory": "Breathing Practices",
        "description": "Take two quick inhales through the nose, then a long slow sigh through the mouth.",
        "benefit_synopsis": "Quickly reduces anxiety and physical tension.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Backed by neuroscience, this technique helps offload excess CO₂ and calms both body and brain rapidly.",
        "objectives": [
          "release_tension",
          "interrupt_anxiety",
          "calm_physiology"
        ]
      },
      {
        "name": "Extended Exhale Breathing",
        "category": "Grounding & Internal Reset",
        "subcategory": "Breathing Practices",
        "description": "Inhale for a short count, then exhale slowly for twice as long.",
        "benefit_synopsis": "Activates the parasympathetic system and soothes the body.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "4 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Exhaling longer than you inhale signals safety to your body and helps release accumulated stress and tension.",
        "objectives": [
          "activate_rest_response",
          "promote_nervous_system_reset",
          "slow_breathing_rate"
        ]
      }
    ],

        # PRACTICE SUBCATEGORY
    "Somatic Reset and Body Awareness": [
      {
        "name": "Progressive Muscle Relaxation",
        "category": "Grounding & Internal Reset",
        "subcategory": "Somatic Reset and Body Awareness",
        "description": "Tense and release each muscle group from head to toe.",
        "benefit_synopsis": "Releases tension and promotes bodily awareness.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Optional or before bed",
        "is_common": True,
        "notes": "This classic technique helps reduce chronic muscle tension and shift awareness from racing thoughts to the physical body.",
        "objectives": [
            "release_physical_tension",
            "enhance_body_awareness",
            "reduce_stress"
        ]
      },
      {
        "name": "Full Body Shakeout",
        "category": "Grounding & Internal Reset",
        "subcategory": "Somatic Reset and Body Awareness",
        "description": "Shake your arms, legs, and whole body to discharge excess energy.",
        "benefit_synopsis": "Releases stuck energy and promotes emotional reset.",
        "recommended_durations": [
            {"duration_label": "1 minute"},
            {"duration_label": "2 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Used in somatic therapy and trauma-informed practices, shaking helps discharge tension and bring awareness back into the body.",
        "objectives": [
            "discharge_energy",
            "interrupt_stress_response",
            "reconnect_with_body"
        ]
      },
      {
        "name": "Body Scan (Awareness-Based)",
        "category": "Grounding & Internal Reset",
        "subcategory": "Somatic Reset and Body Awareness",
        "description": "Bring gentle awareness to each part of your body from head to toe.",
        "benefit_synopsis": "Enhances connection to the body and calms the mind.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily or as needed",
        "is_common": True,
        "notes": "A slower, less structured scan where you simply observe sensations and reconnect with your body as it is — great for grounding and self-awareness.",
        "objectives": [
            "cultivate_embodiment",
            "reduce_anxiety",
            "improve_self_awareness"
        ]
      },
      {
        "name": "Gentle Self-Touch",
        "category": "Grounding & Internal Reset",
        "subcategory": "Somatic Reset and Body Awareness",
        "description": "Place your hand over your chest, stomach, or another comforting area and pause.",
        "benefit_synopsis": "Provides a felt sense of safety and connection.",
        "recommended_durations": [
            {"duration_label": "1 minute"},
            {"duration_label": "3 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Light, intentional touch (such as hand to heart or cradling the head) helps the nervous system downshift and improves internal connection.",
        "objectives": [
            "signal_safety",
            "support_self_regulation",
            "nurture_self_connection"
        ]
      }
    ],

        # PRACTICE SUBCATEGORY
    "Temperature and Sensory Regulation": [
      {
        "name": "Cold Shower",
        "category": "Grounding & Internal Reset",
        "subcategory": "Temperature and Sensory Regulation",
        "description": "Take a full shower using only cold water from start to finish.",
        "benefit_synopsis": "Boosts dopamine, sharpens focus, and strengthens stress tolerance.",
        "recommended_durations": [
            {"duration_label": "1 minute"},
            {"duration_label": "2 minutes"},
            {"duration_label": "3 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–5 times per week",
        "is_common": False,
        "notes": "Cold exposure increases norepinephrine and dopamine, improves mood, and reduces inflammation. Great for building mental resilience.",
        "objectives": [
            "boost_mood",
            "increase_focus",
            "build_stress_resilience"
        ]
      },
      {
        "name": "Cold Face Rinse",
        "category": "Grounding & Internal Reset",
        "subcategory": "Temperature and Sensory Regulation",
        "description": "Splash cold water on your face to quickly reset your system.",
        "benefit_synopsis": "Triggers the diving reflex to calm and refocus.",
        "recommended_durations": [
            {"duration_label": "1 minute"},
            {"duration_label": "2 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": True,
        "notes": "Activates the vagus nerve and reduces sympathetic overdrive — ideal for anxiety or mental reset moments.",
        "objectives": [
            "reset_nervous_system",
            "stimulate_vagus_nerve",
            "reduce_overwhelm"
        ]
      },
      {
        "name": "Savor Something Warm",
        "category": "Grounding & Internal Reset",
        "subcategory": "Temperature and Sensory Regulation",
        "description": "Slowly enjoy a warm drink or food as a sensory ritual to calm and reset.",
        "benefit_synopsis": "Warmth promotes safety and slows the nervous system.",
        "recommended_durations": [
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": False,
        "notes": "Drinking or holding something warm can provide grounding comfort. Used intentionally, this becomes a soothing transition practice.",
        "objectives": [
            "soothe_nervous_system",
            "promote_calm",
            "create_transition_ritual"
        ]
      },
      {
        "name": "Texture Anchor",
        "category": "Grounding & Internal Reset",
        "subcategory": "Temperature and Sensory Regulation",
        "description": "Hold or touch a grounding object like a stone, fabric, or fidget.",
        "benefit_synopsis": "Provides sensory feedback to anchor attention.",
        "recommended_durations": [
            {"duration_label": "1 minute"},
            {"duration_label": "2 minutes"}
        ],
        "impact_rating_id": 2,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Simple sensory tools like smooth stones, beads, or grounding fabrics can help shift attention back into the body when feeling scattered or anxious.",
        "objectives": [
            "anchor_attention",
            "enhance_sensory_awareness",
            "regulate_emotions"
        ]
      }
    ],

        # PRACTICE SUBCATEGORY
    "Environmental Anchoring": [
      {
        "name": "Barefoot Grounding",
        "category": "Grounding & Internal Reset",
        "subcategory": "Environmental Anchoring",
        "description": "Step outside barefoot for a few minutes, ideally on grass, dirt, or sand.",
        "benefit_synopsis": "Reduces stress and restores balance through contact with the Earth.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": False,
        "notes": "Physical contact with the earth may help rebalance the body’s electrical field, lower cortisol, and promote presence.",
        "objectives": [
            "reduce_stress",
            "enhance_presence",
            "regulate_nervous_system"
        ]
      },
      {
        "name": "Open Window Pause",
        "category": "Grounding & Internal Reset",
        "subcategory": "Environmental Anchoring",
        "description": "Stand near an open window and take a few deep breaths while observing your surroundings.",
        "benefit_synopsis": "Combines fresh air, light, and natural sights to ground and refresh.",
        "recommended_durations": [
            {"duration_label": "2 minutes"},
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": True,
        "notes": "Increases light exposure, reduces stuffy indoor overstimulation, and reconnects you to natural rhythms — especially helpful in mornings.",
        "objectives": [
            "refresh_senses",
            "support_natural_rhythm",
            "promote_stillness"
        ]
      },
      {
        "name": "Touch the Earth",
        "category": "Grounding & Internal Reset",
        "subcategory": "Environmental Anchoring",
        "description": "Kneel, sit, or lie down directly on the ground and feel your body supported.",
        "benefit_synopsis": "Connects you to the physical environment and slows internal momentum.",
        "recommended_durations": [
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "This somatic-geographic practice emphasizes the weight and support of the Earth, which can be calming and grounding during stress or mental overstimulation.",
        "objectives": [
            "ground_body",
            "feel_supported",
            "reduce_internal_noise"
        ]
      }
    ],

        # PRACTICE SUBCATEGORY
    "Micro Mindfulness & Sensory Check-Ins": [
      {
        "name": "5-4-3-2-1 Check-In",
        "category": "Grounding & Internal Reset",
        "subcategory": "Micro Mindfulness & Sensory Check-Ins",
        "description": "Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, and 1 you taste.",
        "benefit_synopsis": "Disrupts anxious spirals and returns you to the present.",
        "recommended_durations": [
            {"duration_label": "2 minutes"},
            {"duration_label": "3 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "This grounding technique is commonly used in anxiety therapy. It activates sensory awareness to interrupt overthinking and bring you back to the here and now.",
        "objectives": [
            "anchor_in_present",
            "reduce_anxiety",
            "engage_senses"
        ]
      },
      {
        "name": "Mindful Tea Sipping",
        "category": "Grounding & Internal Reset",
        "subcategory": "Micro Mindfulness & Sensory Check-Ins",
        "description": "Drink water, tea, or any warm beverage slowly and with full awareness.",
        "benefit_synopsis": "Turns a routine moment into a grounding sensory ritual.",
        "recommended_durations": [
            {"duration_label": "2 minutes"},
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Focus on temperature, texture, and taste as you sip. Even a few breaths of mindful attention while drinking can reset mental noise.",
        "objectives": [
            "cultivate_micro_mindfulness",
            "promote_presence",
            "engage_senses"
        ]
      },
      {
        "name": "Noticing the Breath (Consciousness)",
        "category": "Grounding & Internal Reset",
        "subcategory": "Micro Mindfulness & Sensory Check-Ins",
        "description": "Spend a minute simply observing your natural breathing rhythm.",
        "benefit_synopsis": "Creates calm awareness without changing anything.",
        "recommended_durations": [
            {"duration_label": "1 minute"},
            {"duration_label": "2 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Anytime",
        "is_common": True,
        "notes": "This simple awareness shift brings you out of autopilot. Focus on the rise and fall of your breath without needing to control it.",
        "objectives": [
            "build_awareness",
            "pause_autopilot",
            "reset_focus"
        ]
      }
    ],
      
       # PRACTICE SUBCATEGORY
    "Stillness Practices & Restorative Postures": [
      {
        "name": "Lying on the Floor or other surface",
        "category": "Grounding & Internal Reset",
        "subcategory": "Stillness Practices & Restorative Postures",
        "description": "Lie flat on your back and let your body fully relax into the surface beneath you.",
        "benefit_synopsis": "Helps reset overwhelm and reconnect with the body.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Physical stillness offers a reset for both body and mind. The floor provides full support, signaling safety to the nervous system.",
        "objectives": [
            "release_tension",
            "feel_supported",
            "reduce_overwhelm"
        ]
      },
      {
        "name": "Legs Up the Wall",
        "category": "Grounding & Internal Reset",
        "subcategory": "Stillness Practices & Restorative Postures",
        "description": "Lie on your back and rest your legs vertically against a wall or surface.",
        "benefit_synopsis": "Improves circulation and induces deep calm.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Optional daily",
        "is_common": False,
        "notes": "This gentle inversion helps drain lymph, relieve lower-body fatigue, and shift the body into parasympathetic mode. Often used in restorative yoga.",
        "objectives": [
            "support_circulation",
            "reset_nervous_system",
            "induce_stillness"
        ]
      },
      {
        "name": "Seated Grounding Pause",
        "category": "Grounding & Internal Reset",
        "subcategory": "Stillness Practices & Restorative Postures",
        "description": "Sit with both feet planted, hands resting on your lap, and simply be still.",
        "benefit_synopsis": "Signals a clear pause and return to presence.",
        "recommended_durations": [
            {"duration_label": "2 minutes"},
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "This is one of the lowest-barrier grounding techniques. Use during transitions, before tasks, or after overstimulation.",
        "objectives": [
            "reset_attention",
            "cultivate_stillness",
            "signal_transition"
        ]
      }
    ],

    # PRACTICE SUBCATEGORY
    "Mindful Rituals": [
      {
        "name": "Tea Ritual",
        "category": "Grounding & Internal Reset",
        "subcategory": "Mindful Rituals",
        "description": "Prepare and sip tea slowly, using the process as a calming, intentional moment.",
        "benefit_synopsis": "Signals safety to the nervous system and fosters presence through sensory ritual.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": True,
        "notes": "This ritual can be as simple or elaborate as you like. The act of brewing and sipping tea creates a structured pause that encourages grounding, calm, and transition into the day.",
        "objectives": [
            "anchor_routine",
            "cultivate_intention",
            "support_nervous_system"
        ]
      },
      {
        "name": "Mindful Tea Sipping",
        "category": "Grounding & Internal Reset",
        "subcategory": "Mindful Rituals",
        "description": "Drink water, tea, or any warm beverage slowly and with full awareness.",
        "benefit_synopsis": "Creates a pocket of mindfulness using a simple, sensory habit.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "This practice uses ordinary drinking moments as mindfulness anchors. The key is to slow down and focus fully on the act — the texture, temperature, and taste — to reorient attention and nervous system tone.",
        "objectives": [
          "ground_attention",
          "enhance_presence",
          "foster_micro_mindfulness"
        ]
      },
      {
        "name": "Hand-to-Heart Pause",
        "category": "Grounding & Internal Reset",
        "subcategory": "Mindful Rituals",
        "description": "Place your hand on your chest and breathe slowly for a moment.",
        "benefit_synopsis": "Activates calm and fosters self-connection.",
        "recommended_durations": [
            {"duration_label": "1 minute"},
            {"duration_label": "2 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": False,
        "notes": "This somatic cue increases heart-brain coherence and promotes a felt sense of calm and grounding.",
        "objectives": [
            "foster_self_connection",
            "activate_parasympathetic_response",
            "calm_emotions"
        ]
      },
      {
        "name": "Light a Candle or Incense",
        "category": "Grounding & Internal Reset",
        "subcategory": "Mindful Rituals",
        "description": "Light a candle or incense with intention and take a moment to breathe and observe.",
        "benefit_synopsis": "Creates ritual space and anchors the mind in presence.",
        "recommended_durations": [
            {"duration_label": "2 minutes"},
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional or symbolic moments",
        "is_common": False,
        "notes": "Simple symbolic acts like lighting a candle help shift internal state and invite a transition into focused, calm presence.",
        "objectives": [
            "create_transition",
            "set_intention",
            "invite_calm"
        ]
      }
    ],
  },

  # PRACTICE CATEGORY
  "Mindfulness & Spirituality": {
        # PRACTICE SUBCATEGORY
    "Mindfulness, Awareness & Consciousness": [
      {
          "name": "Mindfulness Meditation (Anapanasati)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Focus your awareness on the natural breath, observing each inhale and exhale without control.",
          "benefit_synopsis": "Builds concentration and cultivates calm awareness.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or daily",
          "is_common": True,
          "notes": "A classical Buddhist meditation practice foundational in Theravāda and widely taught in secular mindfulness. The breath is used as a central anchor for attention.",
          "objectives": [
              "build_concentration",
              "reduce_reactivity",
              "anchor_attention"
          ]
      },
      {
          "name": "Zazen (Seated Zen Meditation)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Sit in a stable posture and maintain open awareness, allowing thoughts and sensations to come and go.",
          "benefit_synopsis": "Develops inner stillness and non-attachment.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 3,
          "frequency": "Optional or regular",
          "is_common": True,
          "notes": "Zazen is the core of Soto Zen practice. It's often practiced without a specific object of focus, emphasizing just sitting, stillness, and present-moment awareness.",
          "objectives": [
              "cultivate_stillness",
              "observe_without_judgment",
              "develop_non_reactivity"
          ]
      },
      {
          "name": "Vipassana (Insight Meditation)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Observe bodily sensations, thoughts, and emotions with equanimity as they arise and pass.",
          "benefit_synopsis": "Strengthens insight into impermanence and self-awareness.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 5,
          "difficulty_level_id": 3,
          "frequency": "Regular or during retreats",
          "is_common": True,
          "notes": "Taught widely through traditions such as S.N. Goenka’s lineage. Practitioners scan awareness through the body, noting sensations and mental events without attachment.",
          "objectives": [
              "cultivate_insight",
              "observe_impermanence",
              "increase_awareness"
          ]
      },
      {
          "name": "Samatha (Calm Abiding)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Focus single-pointedly on an object (commonly the breath) to calm the mind and develop stability.",
          "benefit_synopsis": "Stabilizes attention and prepares the mind for deeper insight.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or foundational",
          "is_common": True,
          "notes": "This foundational practice from early Buddhist meditation focuses on concentration (samadhi) to quiet inner distractions. Often paired with insight (vipassana) in tandem.",
          "objectives": [
              "develop_focus",
              "calm_the_mind",
              "prepare_for_insight"
          ]
      },
      {
          "name": "Metta Bhavana (Loving-Kindness Meditation)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Silently repeat phrases of goodwill, directing them toward yourself and others.",
          "benefit_synopsis": "Builds compassion and softens self-judgment.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or regular",
          "is_common": True,
          "notes": "This classical practice develops loving-kindness (metta) through intentional phrases like 'May I be well' or 'May all beings be safe'. Often used to transform difficult emotions.",
          "objectives": [
              "build_compassion",
              "increase_emotional_resilience",
              "soften_self_judgment"
          ]
      },
      {
          "name": "Choiceless Awareness",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Rest in open awareness without choosing a particular object of focus.",
          "benefit_synopsis": "Encourages spacious presence and non-reactive witnessing.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 3,
          "frequency": "Optional or advanced",
          "is_common": False,
          "notes": "This style, emphasized in some Zen and Krishnamurti traditions, involves noticing whatever arises without clinging or aversion — resting in pure awareness.",
          "objectives": [
              "cultivate_equanimity",
              "witness_without_judgment",
              "develop_spacious_mind"
          ]
      },
      {
          "name": "Mindfulness Meditation (MBSR Style)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Sit quietly and observe your breath, body, sounds, and thoughts with gentle curiosity.",
          "benefit_synopsis": "Builds awareness of the present moment without judgment.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or daily",
          "is_common": True,
          "notes": "Popularized by Jon Kabat-Zinn’s Mindfulness-Based Stress Reduction (MBSR), this practice blends breath focus with open awareness in a flexible, user-friendly approach.",
          "objectives": [
              "increase_present_moment_awareness",
              "reduce_stress",
              "train_non_judgmental_attention"
          ]
      },
      {
          "name": "Breath Counting",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Count each breath cycle up to ten, starting over if you lose track.",
          "benefit_synopsis": "Trains mental discipline and improves sustained focus.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or focus warmup",
          "is_common": True,
          "notes": "A widely practiced concentration method used in many traditions. It’s deceptively simple — and highly effective for developing focus and self-awareness.",
          "objectives": [
              "build_concentration",
              "improve_attention_span",
              "increase_awareness_of_drift"
          ]
      },
      {
          "name": "Mantra Meditation (Japa)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Silently or softly repeat a mantra or phrase in rhythm with your breath.",
          "benefit_synopsis": "Calms mental chatter and connects breath with intention.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or devotional",
          "is_common": True,
          "notes": "Common in Hindu and Buddhist traditions. Repetition of a word like 'So Hum' or 'Om Mani Padme Hum' helps center the mind. Can be secularized using phrases like 'peace' or 'I am here'.",
          "objectives": [
              "quiet_the_mind",
              "enhance_focus",
              "cultivate_intention"
          ]
      },
      {
          "name": "Sound Awareness Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Rest your attention on ambient sounds, letting them come and go without judgment.",
          "benefit_synopsis": "Expands awareness and trains receptivity.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "As needed or for sensory reset",
          "is_common": True,
          "notes": "Practiced in both Zen and secular mindfulness contexts. A helpful method when breath feels difficult to track or when anchoring attention outward is more accessible.",
          "objectives": [
              "expand_sensory_awareness",
              "enhance_presence",
              "reduce_internal_noise"
          ]
      },
      {
          "name": "Walking Meditation (Seated Transition Style)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Mentally note the movement of your feet or legs with each step as you walk slowly and mindfully.",
          "benefit_synopsis": "Brings mindful presence into gentle movement.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional daily or post-sitting",
          "is_common": True,
          "notes": "Often taught after seated practice, this builds awareness during transitions. Focus on the rhythm and feel of each step, using phrases like 'lifting, placing'.",
          "objectives": [
              "maintain_presence_through_movement",
              "extend_mindfulness_off_cushion",
              "cultivate_body_awareness"
          ]
      },
      {
          "name": "Body Scan Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Slowly bring awareness to each part of your body, starting at your feet and moving upward.",
          "benefit_synopsis": "Promotes embodiment and relaxation while training sustained awareness.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or before sleep",
          "is_common": True,
          "notes": "A foundational MBSR practice often used for stress, anxiety, and pain relief. You scan through the body non-judgmentally, noticing sensations and letting go of tension.",
          "objectives": [
              "enhance_body_awareness",
              "reduce_stress",
              "cultivate_non_judgmental_presence"
          ]
      },
      {
          "name": "RAIN Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Follow four steps: Recognize, Allowing, Investigate, and Nurture whatever is arising.",
          "benefit_synopsis": "Supports emotional processing with mindfulness and self-compassion.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 5,
          "difficulty_level_id": 3,
          "frequency": "As needed during emotional difficulty",
          "is_common": True,
          "notes": "Popularized by Tara Brach, RAIN is a structured practice for staying present with difficult emotions. Ideal for users working through reactivity, grief, or stress.",
          "objectives": [
              "process_emotions",
              "cultivate_self_compassion",
              "develop_emotional_resilience"
          ]
      },
      {
          "name": "Just One Minute Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "Take a single minute to sit still and focus gently on your breath.",
          "benefit_synopsis": "Reduces resistance to practice and builds consistency.",
          "recommended_durations": [
              {"duration_label": "1 minute"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Daily or as a reset",
          "is_common": True,
          "notes": "A perfect entry point for busy or hesitant beginners. One mindful minute helps establish habit, calm the nervous system, and reorient attention.",
          "objectives": [
              "create_micro_habit",
              "build_consistency",
              "reduce_mental_resistance"
          ]
      },
      {
          "name": "Mindfulness Bell Pause",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Mindfulness, Awareness & Consciousness",
          "description": "When you hear a bell or chime, stop and take one mindful breath.",
          "benefit_synopsis": "Builds presence through auditory cues during daily life.",
          "recommended_durations": [
              {"duration_label": "1 minute"},
              {"duration_label": "2 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "As needed or daily",
          "is_common": True,
          "notes": "Inspired by Thich Nhat Hanh and the Plum Village tradition, this practice uses a bell to return attention to the present. It can be used with real-world sounds or app reminders.",
          "objectives": [
              "build_momentary_awareness",
              "integrate_mindfulness_into_daily_life",
              "reset_attention"
          ]
      }
    ],

        # PRACTICE SUBCATEGORY
    "Guided Awareness & Visualization": [
      {
          "name": "Body Scan Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Gently bring awareness to different parts of the body in sequence, guided by internal or external cues.",
          "benefit_synopsis": "Increases embodiment and calms the nervous system.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Daily or as needed",
          "is_common": True,
          "notes": "A central technique in MBSR and many meditation apps. This version is often guided via audio and helps train attention and presence through somatic awareness.",
          "objectives": [
              "enhance_body_awareness",
              "calm_nervous_system",
              "train_attention"
          ]
      },
      {
          "name": "Loving-Kindness (Guided Metta)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Follow guided phrases of goodwill directed toward yourself and others.",
          "benefit_synopsis": "Builds empathy, compassion, and emotional warmth.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or regular",
          "is_common": True,
          "notes": "Often delivered in calm, slow narration (as on apps like Calm or Headspace), this practice improves emotional balance and softens inner judgment.",
          "objectives": [
              "increase_self_compassion",
              "cultivate_warmth",
              "reduce_negative_bias"
          ]
      },
      {
          "name": "Visualization Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Visualize a peaceful or empowering image, like light radiating from your body or walking through a serene landscape.",
          "benefit_synopsis": "Engages imagination to calm the mind and create positive mental states.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or during stress",
          "is_common": True,
          "notes": "Common in guided meditations across Calm, Insight Timer, and yoga nidra. Helps shift internal state by focusing on soothing mental imagery.",
          "objectives": [
              "relax_nervous_system",
              "generate_positive_emotion",
              "engage_imagination"
          ]
      },
      {
          "name": "Gratitude Meditation (Guided)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Follow prompts to reflect on people, moments, or things you're thankful for.",
          "benefit_synopsis": "Builds positive perspective and reduces negative spiraling.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Daily or weekly",
          "is_common": True,
          "notes": "Gratitude meditations are featured in nearly every major app and positive psychology framework. They're accessible, uplifting, and neurochemically beneficial.",
          "objectives": [
              "increase_positive_emotion",
              "rewire_focus",
              "foster_resilience"
          ]
      },
      {
          "name": "Emotional Check-In",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Be guided through identifying, labeling, and holding space for your current emotional state.",
          "benefit_synopsis": "Increases emotional intelligence and self-regulation.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "8 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "As needed",
          "is_common": True,
          "notes": "Often paired with breath awareness or light body sensing. This practice is used in modern apps (e.g. Balance, Ten Percent) and therapy-informed mindfulness sessions.",
          "objectives": [
              "enhance_emotional_awareness",
              "support_self_regulation",
              "cultivate_self_understanding"
          ]
      },
      {
          "name": "Mountain Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Visualize yourself as a mountain — stable, grounded, and unmoved by weather or change.",
          "benefit_synopsis": "Builds inner strength and non-reactivity.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or weekly",
          "is_common": False,
          "notes": "Taught in MBSR and many guided series. Symbolic imagery like the mountain helps embody emotional stability during uncertainty or intensity.",
          "objectives": [
              "cultivate_resilience",
              "anchor_stillness",
              "support_emotional_grounding"
          ]
      },
      {
          "name": "Inner Sanctuary Visualization",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Create a vivid mental image of a personal safe space you can return to at any time.",
          "benefit_synopsis": "Builds internal refuge and emotional safety.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 2,
          "frequency": "Optional or during stress",
          "is_common": False,
          "notes": "Used in trauma-informed mindfulness, this practice helps develop an internal resource for comfort, protection, or calm. Ideal for anxiety, re-centering, or grounding.",
          "objectives": [
              "create_safe_space",
              "reduce_anxiety",
              "support_emotional_recovery"
          ]
      },
      {
          "name": "7 Days of Calm (Calm App)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "A week-long introductory program teaching the basics of mindfulness meditation.",
          "benefit_synopsis": "Establishes foundational meditation skills and daily practice habits.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Daily for one week",
          "is_common": True,
          "notes": "Offered by the Calm app, this series is designed for beginners to build a consistent meditation routine.",
          "objectives": [
              "build_mindfulness_basics",
              "develop_consistent_practice",
              "reduce_stress"
          ]
      },
      {
          "name": "Basics Course (Headspace App)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "A 10-day course introducing fundamental meditation techniques and concepts.",
          "benefit_synopsis": "Provides a structured introduction to meditation, enhancing focus and reducing stress.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Daily for ten days",
          "is_common": True,
          "notes": "Available on the Headspace app, this course is tailored for newcomers to meditation.",
          "objectives": [
              "learn_meditation_fundamentals",
              "increase_focus",
              "manage_stress"
          ]
      },
      {
          "name": "Daily Meditation (Waking Up App)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "A new guided meditation each day, covering various themes and techniques.",
          "benefit_synopsis": "Encourages daily mindfulness practice with diverse approaches.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Daily",
          "is_common": True,
          "notes": "Offered by the Waking Up app, these meditations provide fresh daily content to support ongoing practice.",
          "objectives": [
              "maintain_daily_meditation",
              "explore_varied_techniques",
              "enhance_mindfulness"
          ]
      },
      {
          "name": "Sleep Stories (Calm App)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Narrated tales designed to help listeners relax and drift into sleep.",
          "benefit_synopsis": "Promotes relaxation and improves sleep quality.",
          "recommended_durations": [
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Nightly as needed",
          "is_common": True,
          "notes": "Featured in the Calm app, these stories are read by soothing voices to aid in falling asleep.",
          "objectives": [
              "facilitate_sleep",
              "reduce_nighttime_anxiety",
              "enhance_relaxation"
          ]
      },
      {
          "name": "Basics Series (10% Happier App)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Introductory guided meditations focusing on mindfulness and stress reduction.",
          "benefit_synopsis": "Helps beginners understand and practice mindfulness meditation.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Daily",
          "is_common": True,
          "notes": "Provided by the 10% Happier app, this series is aimed at those new to meditation.",
          "objectives": [
              "introduce_mindfulness",
              "reduce_stress",
              "establish_meditation_habit"
          ]
      },
      {
          "name": "Mindfulness Daily (Insight Timer App)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Guided Awareness & Visualization",
          "description": "Short daily guided meditations to cultivate mindfulness throughout the day.",
          "benefit_synopsis": "Supports the development of a consistent mindfulness practice.",
          "recommended_durations": [
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Daily",
          "is_common": True,
          "notes": "Available on the Insight Timer app, these sessions are designed for daily mindfulness reinforcement.",
          "objectives": [
              "cultivate_daily_mindfulness",
              "enhance_present_moment_awareness",
              "reduce_daily_stress"
          ]
      }
    ],

        # PRACTICE SUBCATEGORY
    "Journaling & Reflection": [
      {
          "name": "Morning Pages",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write three pages of freeform, stream-of-consciousness thoughts each morning.",
          "benefit_synopsis": "Clears mental clutter and uncovers subconscious patterns.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Daily",
          "is_common": True,
          "notes": "Popularized by Julia Cameron’s *The Artist’s Way*, this practice invites uncensored writing to clear the mind and spark creative or emotional insight.",
          "objectives": [
              "clear_mental_clutter",
              "stimulate_self_reflection",
              "support_creativity"
          ]
      },
      {
          "name": "Gratitude Journaling",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "List three things you’re grateful for — daily or whenever needed.",
          "benefit_synopsis": "Shifts attention toward positivity and builds emotional resilience.",
          "recommended_durations": [
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Daily or weekly",
          "is_common": True,
          "notes": "A widely practiced positive psychology method. Simple but powerful — consistency matters more than depth. Can include people, moments, or personal strengths.",
          "objectives": [
              "cultivate_positivity",
              "rewire_attention",
              "enhance_wellbeing"
          ]
      },
      {
          "name": "Evening Reflection",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write about how your day went, what you learned, and how you felt.",
          "benefit_synopsis": "Creates closure and reveals daily emotional patterns.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Nightly or as needed",
          "is_common": True,
          "notes": "This is a grounded way to review your day with mindfulness. Can be paired with breathwork or used as a transition into sleep. Promotes integration and self-check-in.",
          "objectives": [
              "increase_self_awareness",
              "promote_reflection",
              "support_emotional_regulation"
          ]
      },
      {
          "name": "Values Clarification Journaling",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write about what really matters to you and how you’re living in alignment with it.",
          "benefit_synopsis": "Clarifies purpose and boosts motivation for meaningful change.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Weekly or during goal-setting",
          "is_common": False,
          "notes": "A favorite in ACT (Acceptance and Commitment Therapy) and coaching. Use prompts like ‘When do I feel most alive?’ or ‘What’s been calling for more of my attention?’",
          "objectives": [
              "clarify_personal_values",
              "align_actions_with_purpose",
              "fuel_intrinsic_motivation"
          ]
      },
      {
          "name": "Reflective Prompt Journaling",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Answer a daily or weekly prompt that encourages self-inquiry or emotional awareness.",
          "benefit_synopsis": "Guides attention to inner growth and key life themes.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Daily or weekly",
          "is_common": True,
          "notes": "Prompts may ask things like: ‘What’s one thing I avoided today?’ or ‘What am I proud of this week?’ Often used in coaching, therapy, or growth journals.",
          "objectives": [
              "stimulate_self_inquiry",
              "build_self_knowledge",
              "support_emotional_processing"
          ]
      },
      {
          "name": "Emotion Naming & Reflection",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write down what you’re feeling and explore where it’s coming from.",
          "benefit_synopsis": "Supports emotional regulation through awareness and articulation.",
          "recommended_durations": [
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "As needed",
          "is_common": True,
          "notes": "Labeling emotions and writing about them reduces their intensity. Use basic terms like ‘angry’ or more specific ones like ‘resentful’ — no need to be poetic.",
          "objectives": [
              "regulate_emotions",
              "increase_emotional_clarity",
              "reduce_reactivity"
          ]
      },
      {
          "name": "Cognitive Distortion Reframe (CBT Journaling)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Identify a recurring negative thought and write out a more balanced, realistic version.",
          "benefit_synopsis": "Increases cognitive flexibility and reduces unhelpful thought loops.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "As needed",
          "is_common": True,
          "notes": "One of the most effective journaling formats from CBT. Helps reduce anxiety, perfectionism, and rumination by training the brain to reframe automatic thoughts.",
          "objectives": [
              "reduce_cognitive_distortions",
              "increase_self_regulation",
              "improve_thought_clarity"
          ]
      },
      {
          "name": "ABC Thought Record (CBT)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write down the activating event (A), your belief or thought (B), and the consequence or emotion (C).",
          "benefit_synopsis": "Builds insight into the link between thoughts, emotions, and behaviors.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "As needed",
          "is_common": False,
          "notes": "Classic CBT technique for emotional awareness and change. You can expand the model with D (dispute) and E (new effect) for deeper reappraisal.",
          "objectives": [
              "track_thought_emotion_patterns",
              "increase_behavioral_insight",
              "support_emotion_regulation"
          ]
      },
      {
          "name": "Parts Dialogue (IFS-Inspired)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write from the perspective of a part of you — such as your inner critic, protector, or inner child.",
          "benefit_synopsis": "Fosters self-compassion and deeper understanding of internal conflicts.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 3,
          "frequency": "Optional or during emotional intensity",
          "is_common": False,
          "notes": "This practice helps create distance between your core self and reactive inner parts. Especially useful when emotions feel overwhelming or stuck.",
          "objectives": [
              "enhance_self_leadership",
              "increase_internal_harmony",
              "build_self_compassion"
          ]
      },
      {
          "name": "Limiting Belief Exploration (NLP/Coaching)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Identify a limiting belief and journal about its origin, consequences, and counter-evidence.",
          "benefit_synopsis": "Loosens fixed mindsets and supports identity growth.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or during transition periods",
          "is_common": False,
          "notes": "Used in coaching and NLP-style frameworks to rewire identity-level beliefs. Encourages intentional re-authoring of self-narrative.",
          "objectives": [
              "identify_limiting_beliefs",
              "support_growth_mindset",
              "reframe_self_identity"
          ]
      },
      {
          "name": "Trigger Journal (EMDR/Trauma-Informed)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "After an emotional trigger, describe what happened, how your body responded, and what memory or theme it connects to.",
          "benefit_synopsis": "Increases trauma awareness and integrates emotional material.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 5,
          "difficulty_level_id": 3,
          "frequency": "As needed",
          "is_common": False,
          "notes": "Often paired with EMDR, this journal supports emotional processing and nervous system recovery after dysregulation. Can include resourcing or breath after.",
          "objectives": [
              "track_triggers",
              "build_trauma_awareness",
              "support_emotional_integration"
          ]
      },
      {
          "name": "Letter to Self",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write a letter to your past, future, or present self from a place of compassion and insight.",
          "benefit_synopsis": "Strengthens self-connection and emotional repair.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or for reflection",
          "is_common": True,
          "notes": "Used in coaching, therapy, and trauma work. You might write to your younger self with encouragement, or your future self with vision and hope.",
          "objectives": [
              "foster_self_connection",
              "reprocess_past_experience",
              "cultivate_emotional_resilience"
          ]
      },
      {
          "name": "Weekly Review & Reset",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Reflect on the highs, lows, learnings, and patterns of the past week. Then set your intentions for the next.",
          "benefit_synopsis": "Improves self-awareness and supports intentional weekly rhythm.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Weekly",
          "is_common": True,
          "notes": "Used in productivity systems and reflective journaling alike. This format encourages continuity and pattern tracking, preventing autopilot weeks.",
          "objectives": [
              "integrate_weekly_experience",
              "promote_self_direction",
              "build_reflective_consistency"
          ]
      },
      {
          "name": "Future Self Letter",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write a letter from your future self, describing who you’ve become and how you got there.",
          "benefit_synopsis": "Builds self-belief and clarifies long-term vision.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or during life planning",
          "is_common": False,
          "notes": "Powerful for reorienting perspective and motivation. This is used in vision work, career coaching, and resilience training alike.",
          "objectives": [
              "strengthen_personal_vision",
              "increase_motivation",
              "enhance_self_narrative"
          ]
      },
      {
          "name": "Dream Journal",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Record your dreams upon waking, noting symbols, emotions, and potential meanings.",
          "benefit_synopsis": "Builds inner awareness and supports unconscious integration.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 2,
          "frequency": "Daily upon waking",
          "is_common": False,
          "notes": "Especially helpful for creatives, introspective users, or those doing inner child or trauma work. Over time, reveals inner themes and shifts in psyche.",
          "objectives": [
              "increase_symbolic_awareness",
              "connect_with_subconscious",
              "support_inner_processing"
          ]
      },
      {
          "name": "Goal Progress Reflection",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "Write about what you’ve done toward your goal, what’s working, and what could improve.",
          "benefit_synopsis": "Reinforces action and keeps goals top-of-mind.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Weekly or after key steps",
          "is_common": True,
          "notes": "Used in behavioral psychology and productivity systems alike. This helps users track effort and stay in proactive mode rather than discouragement or drift.",
          "objectives": [
              "reinforce_goal_momentum",
              "track_barriers_and_successes",
              "sustain_motivation"
          ]
      },
      {
          "name": "Values in Action Check-In",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Journaling & Reflection",
          "description": "List your core values and reflect on how they showed up (or didn’t) in recent choices.",
          "benefit_synopsis": "Strengthens identity alignment and self-trust.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Biweekly or monthly",
          "is_common": False,
          "notes": "Drawn from ACT and coaching work, this keeps deeper principles visible in day-to-day life. Helps counter distraction and misalignment.",
          "objectives": [
              "strengthen_values_alignment",
              "improve_decision_making",
              "increase_self_integrity"
          ]
      }

    ],

        # PRACTICE SUBCATEGORY
    "Spiritual Connection & Devotion": [
      {
          "name": "Prayer",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Sit in stillness and offer silent prayer, gratitude, or surrender to a higher power.",
          "benefit_synopsis": "Fosters humility, reverence, and trust in something greater.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or daily",
          "is_common": True,
          "notes": "Used in many traditions. Can include gratitude, requests for guidance, or quiet presence with the divine. No specific wording is required.",
          "objectives": [
              "foster_spiritual_connection",
              "cultivate_gratitude_or_surrender",
              "support_inner_peace"
          ]
      },
      {
          "name": "Devotional",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Chant, sing, or offer loving expression toward something greater.",
          "benefit_synopsis": "Opens the heart and channels emotion into spiritual connection.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or ceremonial",
          "is_common": False,
          "notes": "Practiced in Bhakti Yoga, Sufi traditions, and spiritual singing. Can include personal mantras or traditional call-and-response (e.g. kirtan).",
          "objectives": [
              "elevate_emotional_state",
              "connect_with_devotion",
              "express_inner_spirit"
          ]
      },
      {
          "name": "Mantra",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Repeat a sacred word or phrase silently or aloud, letting it anchor your attention.",
          "benefit_synopsis": "Calms the mind and connects breath to intention or sacred sound.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or during devotion",
          "is_common": True,
          "notes": "Mantras may include 'Om', 'Amen', 'Shalom', 'So Hum', or others depending on tradition. Practiced in Hinduism, Buddhism, Christianity, and universal spiritual practice.",
          "objectives": [
              "quiet_mental_noise",
              "anchor_attention_spiritually",
              "build_spiritual_focus"
          ]
      },
      {
          "name": "Read Scripture Passage",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Read a passage from a sacred or spiritual text and reflect on its meaning.",
          "benefit_synopsis": "Connects you to timeless wisdom and inner reflection.",
          "recommended_durations": [
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or weekly",
          "is_common": True,
          "notes": "Passages can come from the Bible, Bhagavad Gita, Tao Te Ching, Rumi, or other sources of spiritual depth. Let the reading become contemplation.",
          "objectives": [
              "connect_with_wisdom",
              "expand_spiritual_perspective",
              "support_contemplative_practice"
          ]
      },
      {
          "name": "Light a Candle",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Light a candle while setting an intention or offering a quiet moment of thanks.",
          "benefit_synopsis": "Creates a moment of reverence and presence.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or ritual days",
          "is_common": True,
          "notes": "Used across many traditions — lighting a candle can mark a transition, remembrance, intention, or simply a sacred pause. Accessible and powerful.",
          "objectives": [
              "create_sacred_space",
              "mark_intention_moment",
              "cultivate_presence"
          ]
      },
      {
          "name": "Tend Altar",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Place an offering or gently care for your sacred space.",
          "benefit_synopsis": "Fosters reverence, grounding, and symbolic connection.",
          "recommended_durations": [
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 2,
          "frequency": "Optional or weekly",
          "is_common": False,
          "notes": "Altar tending is a physical form of spiritual expression. It encourages mindfulness, gratitude, and intention through objects and symbolic care.",
          "objectives": [
              "nurture_sacred_connection",
              "honor_spiritual_space",
              "express_gratitude"
          ]
      },
      {
          "name": "Nature Bathing",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Spend quiet, undistracted time in nature — walking slowly or sitting still.",
          "benefit_synopsis": "Regulates the nervous system and opens the senses.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Weekly or as needed",
          "is_common": True,
          "notes": "Inspired by the Japanese practice of shinrin-yoku. There’s no goal but to *be* — take in the sounds, colors, textures, and stillness of the natural world.",
          "objectives": [
              "calm_nervous_system",
              "connect_with_nature",
              "enhance_sensory_awareness"
          ]
      },
      {
          "name": "Touch the Earth",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Stand or sit with your bare feet or hands touching natural ground.",
          "benefit_synopsis": "Supports grounding and energetic reset.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or daily",
          "is_common": True,
          "notes": "Sometimes called ‘earthing’ — this practice reconnects your body’s electrical system with the earth’s. Can be done on soil, grass, sand, or rock.",
          "objectives": [
              "support_grounding",
              "regulate_energy",
              "reduce_stress"
          ]
      },
      {
          "name": "Look at the Sky",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Pause and look at the open sky — letting your thoughts soften and your breath expand.",
          "benefit_synopsis": "Creates spaciousness and reduces mental tension.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Daily or when overwhelmed",
          "is_common": True,
          "notes": "This small act can instantly shift your nervous system and bring emotional perspective. Pairs beautifully with breath or prayer.",
          "objectives": [
              "increase_spaciousness",
              "release_tension",
              "reconnect_with_wonder"
          ]
      },
      {
          "name": "Offer to Nature",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Place a small offering — like a flower, stone, or breath — as a gesture of respect and gratitude.",
          "benefit_synopsis": "Deepens reverence and symbolic connection with the earth.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or during nature walks",
          "is_common": False,
          "notes": "This practice exists in many traditions. You can whisper a word of thanks, leave a symbolic gift, or simply acknowledge the place around you with care.",
          "objectives": [
              "cultivate_reverence",
              "practice_gratitude",
              "connect_symbolically_with_nature"
          ]
      },
      {
          "name": "Sit with a Tree",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Find a tree and sit near it quietly — letting it hold your attention and stillness.",
          "benefit_synopsis": "Builds inner calm and a sense of rootedness.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or weekly",
          "is_common": True,
          "notes": "Trees have a unique calming presence. Choose one that draws you in. Just sit and breathe. Some people like to rest a hand on the trunk or lean against it.",
          "objectives": [
              "promote_inner_stillness",
              "build_grounded_presence",
              "feel_part_of_nature"
          ]
      },
      {
          "name": "Past Life Reflection",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Sit quietly and imagine a life you've lived before — noticing themes, imagery, or lessons that arise.",
          "benefit_synopsis": "Explores patterns and soul-level insights beyond the present lifetime.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 3,
          "frequency": "Optional or during spiritual inquiry",
          "is_common": False,
          "notes": "You don’t have to believe in reincarnation to try this — it's an exercise in symbolic memory and inner storytelling. Let imagery come gently, without force.",
          "objectives": [
              "explore_symbolic_self",
              "gain_archetypal_insight",
              "release_unconscious_patterns"
          ]
      },
      {
          "name": "Meet Your Higher Self",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Visualize your highest, most expanded version of you — and listen inward for guidance.",
          "benefit_synopsis": "Connects with your inner wisdom and long-view perspective.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or during transition",
          "is_common": True,
          "notes": "You can speak to or embody this self — ask questions, receive insight, or simply observe. Often used in meditation and guided visualization work.",
          "objectives": [
              "strengthen_inner_guidance",
              "connect_with_future_self",
              "build_self_leadership"
          ]
      },
      {
          "name": "Ancestral Reflection",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Think about or write to an ancestor — known or unknown — and reflect on what they carried and passed on.",
          "benefit_synopsis": "Deepens belonging and self-understanding through lineage.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or around transition/holidays",
          "is_common": False,
          "notes": "This practice can be emotional and symbolic — you're connecting with those who came before you and shaped your story, even subtly.",
          "objectives": [
              "connect_with_lineage",
              "honor_inherited_strengths",
              "release_generational_patterns"
          ]
      },
      {
          "name": "Call in a Guide",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Visualize a guide — spiritual, ancestral, animal, or imagined — and receive support or clarity.",
          "benefit_synopsis": "Offers insight, support, or perspective through symbolic connection.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 2,
          "frequency": "Optional or during uncertainty",
          "is_common": False,
          "notes": "Your guide may appear as a light, figure, voice, or feeling. Let it emerge naturally. This is a powerful tool for intuition and symbolic problem solving.",
          "objectives": [
              "receive_support",
              "build_intuitive_connection",
              "access_alternate_perspectives"
          ]
      },
      {
          "name": "Energetic Reset",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Visualize clearing your body and energy field of stress, tension, or external noise.",
          "benefit_synopsis": "Supports energetic clarity and nervous system reset.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "As needed",
          "is_common": True,
          "notes": "Can be imagined as light, breath, or water moving through you. Many users find this helpful after social overstimulation or tech use.",
          "objectives": [
              "clear_energetic_residue",
              "support_self_regulation",
              "restore_sense_of_self"
          ]
      },
      {
          "name": "Symbolic Dream Reflection",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Reflect on a recent dream and journal about its emotional tone, symbols, and messages.",
          "benefit_synopsis": "Reveals hidden insights and emotional patterns.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 2,
          "frequency": "Optional or after vivid dreams",
          "is_common": False,
          "notes": "You don’t need to interpret dreams literally — instead, focus on how they *felt* and what patterns or themes stand out. A gentle way to access deeper layers.",
          "objectives": [
              "process_unconscious_content",
              "recognize_inner_themes",
              "expand_self_insight"
          ]
      },
      {
          "name": "Pull a Card",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Draw a tarot or oracle card and reflect on the message it brings.",
          "benefit_synopsis": "Offers intuitive insight through symbol and story.",
          "recommended_durations": [
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or when seeking clarity",
          "is_common": True,
          "notes": "You don’t need to ‘believe’ anything specific. The images, phrases, or archetypes often stir reflection. Let the message meet you where you are.",
          "objectives": [
              "invite_symbolic_insight",
              "strengthen_self_reflection",
              "enhance_intuitive_clarity"
          ]
      },
      {
          "name": "Consult the I Ching",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Open to or cast a hexagram from the I Ching and reflect on its passage.",
          "benefit_synopsis": "Provides ancient wisdom for times of transition or uncertainty.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 3,
          "frequency": "Optional or when at a crossroads",
          "is_common": False,
          "notes": "The I Ching (‘Book of Changes’) offers poetic responses to life’s transitions. Use a digital version or yarrow coins, and reflect on what resonates.",
          "objectives": [
              "connect_with_ancient_wisdom",
              "receive_symbolic_guidance",
              "navigate_uncertainty"
          ]
      },
      {
          "name": "Stream-of-Consciousness Writing",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Let your hand move freely across the page — writing whatever flows without judgment.",
          "benefit_synopsis": "Bypasses inner filters and reveals hidden patterns or insight.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or weekly",
          "is_common": True,
          "notes": "This practice is often used in creativity, trauma healing, and spiritual inquiry. Don’t edit — just let thoughts, phrases, or emotions move freely.",
          "objectives": [
              "access_inner_voices",
              "release_stuck_energy",
              "discover_unfiltered_truths"
          ]
      },
      {
          "name": "Centering Breath",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Take a few deep, steady breaths to bring yourself fully into the moment.",
          "benefit_synopsis": "Anchors awareness and reduces mental noise.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Anytime focus is needed",
          "is_common": True,
          "notes": "This is the most accessible and immediate presence practice — useful before conversations, creative sessions, or transitions.",
          "objectives": [
              "regulate_breath",
              "return_to_the_present",
              "prepare_for_focus"
          ]
      },
      {
          "name": "Set an Intention",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Pause and set a clear intention for how you want to show up today.",
          "benefit_synopsis": "Strengthens focus, motivation, and alignment with values.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Daily or before any important moment",
          "is_common": True,
          "notes": "This can be spoken, written, or simply felt — ex: 'I move with compassion today.' Great before work, movement, or spiritual practice.",
          "objectives": [
              "clarify_mindset",
              "reinforce_intention",
              "prime_daily_alignment"
          ]
      },
      {
          "name": "Focus Ritual",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Do a short, consistent ritual to mark the shift into focused work or presence.",
          "benefit_synopsis": "Creates mental association and reduces resistance to starting.",
          "recommended_durations": [
              {"duration_label": "2 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Before work or deep thinking",
          "is_common": True,
          "notes": "Light a candle, play a chime, breathe deeply — whatever signals to your mind: 'We're entering a focused state now.' Repetition is key.",
          "objectives": [
              "reduce_context_switching",
              "create_attention_cue",
              "anchor_transition_into_focus"
          ]
      },
      {
          "name": "Morning Visualization",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Imagine your ideal flow through the day, from morning to evening.",
          "benefit_synopsis": "Mentally primes your actions, emotions, and outcomes.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Each morning or before big events",
          "is_common": True,
          "notes": "Picture yourself staying calm, hitting your stride, moving with intention. Keep it gentle and optimistic — don’t over-script.",
          "objectives": [
              "strengthen_daily_mindset",
              "visualize_successful_actions",
              "reinforce_personal_alignment"
          ]
      },
      {
          "name": "Mirror Intention",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Spiritual Connection & Devotion",
          "description": "Look in the mirror and speak a chosen word or phrase that aligns with how you want to show up.",
          "benefit_synopsis": "Builds clarity and emotional commitment to your intention.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or daily",
          "is_common": False,
          "notes": "Can be as simple as: 'I meet today with strength and kindness.' Eye contact with yourself reinforces emotional anchoring.",
          "objectives": [
              "amplify_self_direction",
              "strengthen_embodiment",
              "align_energy_with_intention"
          ]
      },

    ],

        # PRACTICE SUBCATEGORY - 
        # TODO: Likely to be dissolved and joined with other subcategories.  
    "Presence, Creativity & Intention Rituals": [
      {
          "name": "Draw a Mandala",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Create a circular design by drawing, coloring, or patterning from the center outward.",
          "benefit_synopsis": "Supports emotional balance, inner focus, and symbolic reflection.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or during emotional reset",
          "is_common": True,
          "notes": "Mandalas are found in spiritual traditions worldwide — but you don’t need any training. Let the circular shape guide a calming, meditative flow of patterns, colors, or emotions.",
          "objectives": [
              "promote_inner_balance",
              "express_through_pattern",
              "anchor_attention_in_shape"
          ]
      },
      {
          "name": "Draw a Symbol",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Draw a shape, image, or mark that represents what you’re feeling or calling in.",
          "benefit_synopsis": "Connects abstract emotion to tangible expression.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or during transitions",
          "is_common": False,
          "notes": "No need for artistic skill — just let the pen move. Symbols often carry emotional weight and can become anchors for reflection or intention.",
          "objectives": [
              "externalize_inner_states",
              "spark_symbolic_awareness",
              "activate_creative_connection"
          ]
      },
      {
          "name": "Write a Letter to the Universe",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Write out your thoughts, desires, or worries as if writing to a loving, listening universe.",
          "benefit_synopsis": "Releases control and opens space for trust and surrender.",
          "recommended_durations": [
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or during uncertainty",
          "is_common": True,
          "notes": "This can be written as a journal entry, a literal letter, or poetic request. You can keep it, burn it, or leave it in a sacred space. Let it be honest.",
          "objectives": [
              "release_attachment",
              "clarify_intentions",
              "invite_spiritual_support"
          ]
      },
    ],

        # PRACTICE SUBCATEGORY
    "Mantra, Sound & Vibration Practices": [
      {
          "name": "Mantra Repetition (Japa)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Silently or softly repeat a sacred word or phrase with steady rhythm.",
          "benefit_synopsis": "Centers the mind and connects breath with sacred sound.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or devotional",
          "is_common": True,
          "notes": "Traditionally practiced with mala beads or mental repetition. Common mantras include 'Om Mani Padme Hum', 'So Hum', or personal affirmations.",
          "objectives": [
              "focus_attention",
              "quiet_the_mind",
              "cultivate_intention"
          ]
      },
      {
          "name": "Chanting or Devotional Singing",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Sing, hum, or repeat devotional phrases with heartful presence.",
          "benefit_synopsis": "Opens the heart and shifts emotional energy through sound.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or ritual",
          "is_common": False,
          "notes": "Common in Bhakti yoga and spiritual traditions. Kirtan, call-and-response, or free vocal toning can all apply. Let emotion move through voice.",
          "objectives": [
              "release_emotional_tension",
              "connect_through_voice",
              "engage_in_devotion"
          ]
      },
      {
          "name": "Bell or Singing Bowl Listening",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Focus on the sound of a bell or bowl, allowing it to anchor attention.",
          "benefit_synopsis": "Promotes stillness and opens auditory awareness.",
          "recommended_durations": [
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "As needed or for sound-based meditation",
          "is_common": True,
          "notes": "Can be a single strike of a bell, a singing bowl, or a short chime sequence. Listen until the sound fades completely, then return to the next tone.",
          "objectives": [
              "enhance_sensory_awareness",
              "slow_the_mind",
              "anchor_to_sound"
          ]
      },
      {
          "name": "Humming for Calm",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Hum softly on the exhale, letting the vibration soothe your nervous system.",
          "benefit_synopsis": "Downregulates stress and stimulates the vagus nerve.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "As needed or during stress",
          "is_common": True,
          "notes": "Try 3–5 slow, steady breaths, humming on each exhale. Keep the tone soft and smooth. Great for anxiety or sensory overload.",
          "objectives": [
              "regulate_nervous_system",
              "create_internal_resonance",
              "reduce_anxiety"
          ]
      },
      {
          "name": "Breath-Linked Mantra",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Mentally link a short mantra to your inhale and exhale.",
          "benefit_synopsis": "Combines rhythm, breath, and intention into a cohesive practice.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or daily",
          "is_common": True,
          "notes": "Classic pairings include 'So' on inhale and 'Hum' on exhale. Can also be customized with phrases like 'I am' / 'at peace'.",
          "objectives": [
              "synchronize_breath_and_mind",
              "enhance_focus",
              "deepen_internal_alignment"
          ]
      },
      {
          "name": "Vocal Toning",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Sustain a single tone (like 'Aaaah' or 'Om') to create internal vibration.",
          "benefit_synopsis": "Stimulates the body through sound and calms internal noise.",
          "recommended_durations": [
              {"duration_label": "3 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 2,
          "frequency": "Optional or ritual",
          "is_common": False,
          "notes": "Choose a vowel or sound that feels resonant. Tone it slowly, letting the vibration move through your chest, throat, or head.",
          "objectives": [
              "create_vocal_resonance",
              "stimulate_energy_flow",
              "focus_through_sound"
          ]
      },
      {
          "name": "Listen to a Sound Bath or Binaural Track",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Close your eyes and listen to a calming soundscape or frequency-based track.",
          "benefit_synopsis": "Induces deep relaxation and entrains brainwaves.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "As needed or during rest",
          "is_common": True,
          "notes": "Use headphones for binaural beats or sound bath recordings. Let the tones wash over you and reset your nervous system.",
          "objectives": [
              "entrain_brainwaves",
              "reduce_cognitive_noise",
              "promote_deep_relaxation"
          ]
      },
      {
          "name": "Affirmation-Based Mantra",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Presence, Creativity & Intention Rituals",
          "description": "Repeat a positive phrase silently or aloud to reinforce desired qualities.",
          "benefit_synopsis": "Builds self-trust and shifts internal dialogue.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Daily or situational",
          "is_common": True,
          "notes": "Choose a phrase that resonates with your intention, such as 'I am grounded', 'I am enough', or 'I move with ease'. Repeat rhythmically or with breath.",
          "objectives": [
              "shift_inner_state",
              "reinforce_positive_identity",
              "anchor_self-belief"
          ]
      },
      {
        "name": "Create Your Own Mantra",
        "category": "Mindfulness & Spirituality",
        "subcategory": "Presence, Creativity & Intention Rituals",
        "description": "Choose a word or phrase that resonates with you and repeat it with breath or rhythm.",
        "benefit_synopsis": "Personalizes intention and builds emotional resonance.",
        "recommended_durations": [
            {"duration_label": "2 minutes"},
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional or daily",
        "is_common": False,
        "notes": "Your mantra can be a value ('compassion'), an intention ('trust the process'), or a phrase that helps you return to yourself. Try it silently, aloud, or with a breath rhythm.",
        "objectives": [
            "personalize_intention",
            "anchor_thought_and_energy",
            "create_ritual_through_words"
        ]
      },
    ],
        
        # PRACTICE SUBCATEGORY
    "Walking & Movement-Based Meditation": [
      {
          "name": "Walking Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Walk slowly and mindfully, placing attention on the sensation of each step.",
          "benefit_synopsis": "Brings awareness into motion and transitions.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "Optional or post-sitting",
          "is_common": True,
          "notes": "Use phrases like 'lifting, stepping, placing' or simply observe the rhythm of your movement. A foundational practice in many Buddhist traditions.",
          "objectives": [
              "cultivate_mindful_presence",
              "transition_between_states",
              "build_body_awareness"
          ]
      },
      {
          "name": "Qi Gong Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "A practice of slow, flowing movements with relaxed breathing and attention on building energy.",
          "benefit_synopsis": "Circulates and builds energy, Cultivates relaxed focus",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or energizing",
          "is_common": False,
          "notes": "This ancient Chinese movement meditation blends physical flow with breath and energy cultivation practices. Many beginner sequences are accessible and deeply calming.",
          "objectives": [
              "cultivate_energy_awareness",
              "enhance_breath_body_synchrony",
              "relax_while_moving"
          ]
      },
      {
          "name": "Nei Gong Practice",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "A practice of slow, deliberate flows and postures that train alignment, mobility, and internal strength.",
          "benefit_synopsis": "Improves posture, builds body awareness, and strengthens foundational movement patterns.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "15 minutes"}
          ],
          "impact_rating_id": 5,
          "difficulty_level_id": 3,
          "frequency": "Optional or as a deeper practice",
          "is_common": False,
          "notes": "Nei Gong emphasizes refined body mechanics through rooted stances, breath-aligned motion, and slow calisthenic strength. The practice enhances energy circulation and cultivates presence through movement. Accessible sequences can improve balance, flexibility, and structural resilience.",
          "objectives": [
              "develop_postural_integrity",
              "enhance_body_control",
              "strengthen_internal_alignment"
          ]
      },
      {
          "name": "Mindful Stretching",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Stretch gently while focusing on the sensations in your body.",
          "benefit_synopsis": "Releases tension and anchors awareness in movement.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or post-work",
          "is_common": True,
          "notes": "Move slowly between stretches. Breathe steadily. Focus on how your body feels — not how far it goes.",
          "objectives": [
              "release_physical_tension",
              "anchor_in_sensation",
              "create_body_mind_connection"
          ]
      },
      {
          "name": "Intuitive Movement Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Let your body move freely and slowly, following internal cues rather than form.",
          "benefit_synopsis": "Encourages embodied presence and emotional release.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or during emotional processing",
          "is_common": False,
          "notes": "No choreography. Let your breath lead your body. Trust the impulse to sway, shift, stretch, or pause. Great for unwinding emotion or internal disconnection.",
          "objectives": [
              "cultivate_embodiment",
              "release_stored_emotion",
              "build_movement_awareness"
          ]
      },
      {
          "name": "Posture-Based Breath Synchronization",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Match slow breath with simple body movements like raising arms or shifting stance.",
          "benefit_synopsis": "Unites breath, awareness, and action in rhythmic alignment.",
          "recommended_durations": [
              {"duration_label": "3 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "As needed or to transition into mindfulness",
          "is_common": True,
          "notes": "Inhale while gently lifting the arms or rising slightly; exhale as you lower or return. Useful for nervous system settling and breath anchoring.",
          "objectives": [
              "build_breath_body_connection",
              "reset_focus",
              "reduce_cognitive_load"
          ]
        },
        {
          "name": "Tai Chi (Restorative Flow)",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Practice slow, flowing Tai Chi movements to calm the mind and balance the body.",
          "benefit_synopsis": "Enhances balance, body awareness, and inner calm.",
          "recommended_durations": [
              {"duration_label": "10 minutes"},
              {"duration_label": "20 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or regular",
          "is_common": True,
          "notes": "This gentle practice emphasizes breath-linked motion, rooted stances, and circular flow. Focus on quality of movement over precision. Ideal for stress relief and postural health.",
          "objectives": [
              "build_body_awareness",
              "cultivate_inner_balance",
              "reduce_stress_through_motion"
          ]
        },
        {
          "name": "Dao Yin Flow",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Move through breath-guided stretches and rotations to stimulate energy flow.",
          "benefit_synopsis": "Opens the body, releases tension, and supports energy alignment.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Optional or energizing",
          "is_common": False,
          "notes": "Dao Yin (道引) blends breath, intention, and stretching. Often practiced standing or seated, it's a great middle ground between static poses and flowing sequences.",
          "objectives": [
              "stimulate_energy_meridians",
              "mobilize_stiffness",
              "combine_breath_and_movement"
          ]
        },
        {
          "name": "Shaking Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Let your body gently shake or bounce to release tension and re-regulate your system.",
          "benefit_synopsis": "Relieves stress and resets the nervous system.",
          "recommended_durations": [
              {"duration_label": "2 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 4,
          "difficulty_level_id": 1,
          "frequency": "As needed or daily",
          "is_common": True,
          "notes": "Start by bouncing gently on the heels, then let spontaneous shaking emerge. Keep the jaw soft and breath steady. Great after long sitting or emotional build-up.",
          "objectives": [
              "release_stored_tension",
              "regulate_nervous_system",
              "reconnect_with_body"
          ]
        },
        {
          "name": "Gentle Dance Flow",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Move intuitively with soft rhythm and breath, letting music or inner feeling guide you.",
          "benefit_synopsis": "Invites playfulness, freedom, and embodied presence.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or during creative reset",
          "is_common": False,
          "notes": "No choreography — just allow your body to move, sway, or stretch with gentle rhythm. Can be done in silence or with music.",
          "objectives": [
              "cultivate_playful_awareness",
              "express_through_motion",
              "build_embodied_freedom"
          ]
        },
        {
          "name": "Walking Labyrinth Meditation",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Walk in a simple circular or spiraling path as a symbolic journey inward and outward.",
          "benefit_synopsis": "Focuses attention and invites reflection through movement.",
          "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or ritual-based",
          "is_common": False,
          "notes": "Use a real or imagined labyrinth. Walk slowly and mindfully, pausing in the center to reflect or set an intention before walking out.",
          "objectives": [
              "anchor_focus_in_motion",
              "engage_in_symbolic_reflection",
              "mark_transitions_intentionally"
          ]
        },
        {
          "name": "Breath & Gesture Flow",
          "category": "Mindfulness & Spirituality",
          "subcategory": "Walking & Movement-Based Meditation",
          "description": "Link simple breath cycles with hand or body gestures to center yourself.",
          "benefit_synopsis": "Combines intention, rhythm, and movement for deepened presence.",
          "recommended_durations": [
              {"duration_label": "3 minutes"},
              {"duration_label": "5 minutes"}
          ],
          "impact_rating_id": 3,
          "difficulty_level_id": 1,
          "frequency": "Optional or during transitions",
          "is_common": True,
          "notes": "Examples: inhale while sweeping arms up, exhale while lowering; inhale 'gather', exhale 'ground'. Use gestures like opening, releasing, or centering.",
          "objectives": [
              "create_movement_breath_alignment",
              "ground_with_intention",
              "establish_centered_focus"
          ]
        }
    ]
  },

# PRACTICE CATEGORY
  "Recreation, Play & Creative Hobbies": {
    #  PRACTICE SUBCATEGORY
      "Visual & Craft-Based Creativity (Art, Crafts, Photography)": [
          {
            "name": "Draw, Sketch, Paint For Fun",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Doodle, sketch, or throw down some color — no rules, just creative play.",
            "benefit_synopsis": "Reduces stress and encourages free expression.",
            "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "20 minutes"}],
            "impact_rating_id": 3,
            "difficulty_level_id": 1,
            "frequency": "Optional or daily",
            "is_common": True,
            "notes": "Use whatever tools you have — pencil, pen, markers, or watercolor. It’s not about the result, just the act of making marks.",
            "objectives": ["express_creatively", "reduce_mental_pressure", "stimulate_flow"]
          },
          {
            "name": "Practice an Art Skill",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Spend time practicing a technique like shading, proportions, or brushwork.",
            "benefit_synopsis": "Improves focus and builds creative confidence.",
            "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
            "impact_rating_id": 4,
            "difficulty_level_id": 2,
            "frequency": "Optional or weekly",
            "is_common": True,
            "notes": "Pick one element of technique to explore. Keep it casual — it’s about the reps, not perfection.",
            "objectives": ["develop_skills", "build_focus", "gain_artistic_confidence"]
          },
          {
            "name": "Pottery for Fun",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Get your hands into clay and shape something — a bowl, a creature, or just texture.",
            "benefit_synopsis": "Deepens tactile engagement and grounds awareness.",
            "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
            "impact_rating_id": 4,
            "difficulty_level_id": 2,
            "frequency": "Optional or recreational",
            "is_common": False,
            "notes": "No wheel needed — try pinch pots or hand-building with air-dry clay or real ceramic clay at a studio.",
            "objectives": ["engage_senses", "slow_down", "explore_shape_and_form"]
          },
          {
            "name": "Art Inspiration Adventure",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Go out and explore art in the world — murals, galleries, or public sculpture.",
            "benefit_synopsis": "Refuels creative vision and sparks new ideas.",
            "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "1 hour"}],
            "impact_rating_id": 3,
            "difficulty_level_id": 1,
            "frequency": "Optional or when creatively dry",
            "is_common": False,
            "notes": "Take photos, sketch what you see, or just soak it in. Visit a museum, check out local art, or browse unique design stores.",
            "objectives": ["stimulate_inspiration", "expand_visual_language", "refill_creative_well"]
          },
          {
            "name": "Photography Nature Walk",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Take a slow walk through nature and capture moments that move you.",
            "benefit_synopsis": "Builds connection to environment and quiet visual mindfulness.",
            "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
            "impact_rating_id": 3,
            "difficulty_level_id": 1,
            "frequency": "Optional or calming reset",
            "is_common": True,
            "notes": "Don’t worry about gear — your phone works fine. Look for light, shadows, shapes, or subtle motion.",
            "objectives": ["ground_in_nature", "train_visual_awareness", "reduce_stress"]
          },
          {
            "name": "Art Walk with a Theme",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Choose a visual theme and go find it out in the world.",
            "benefit_synopsis": "Turns everyday walks into creative missions.",
            "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
            "impact_rating_id": 3,
            "difficulty_level_id": 1,
            "frequency": "Optional or weekly",
            "is_common": True,
            "notes": "Themes can be color-based (like 'blue'), shape-driven ('circles'), or mood-based ('abandoned'). Document what you find however you like.",
            "objectives": ["engage_with_environment", "practice_observational_focus", "spark_playful_exploration"]
          }
      ],

    #  PRACTICE SUBCATEGORY
      "Writing & Storytelling (Journaling, Poetry, Fiction)": [],

    #  PRACTICE SUBCATEGORY
      "Music & Rhythm (Instruments, Drumming, Dance)": [
          {
            "name": "Practice an Instrument",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Spend focused time refining chords, scales, or pieces on your instrument of choice.",
            "benefit_synopsis": "Builds discipline and deepens musical fluency.",
            "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
            "impact_rating_id": 4,
            "difficulty_level_id": 2,
            "frequency": "Optional or consistent",
            "is_common": True,
            "notes": "Try a practice ritual that works for you — metronome drills, ear training, or scales. Track progress over time.",
            "objectives": ["develop_skill", "enhance_focus", "build_musical_fluency"]
          },
          {
            "name": "Play Music (Jam Sesh)",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Let go and just play — improvise, mess around, or find your groove.",
            "benefit_synopsis": "Releases creative energy and boosts mood.",
            "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
            "impact_rating_id": 4,
            "difficulty_level_id": 1,
            "frequency": "Optional or energizing",
            "is_common": True,
            "notes": "Alone or with others, unplugged or electric, acoustic or digital. Just play.",
            "objectives": ["have_fun_creating", "release_energy", "get_into_flow"]
          },
          {
            "name": "Practice with the Band",
            "category": "Recreation, Play & Creative Hobbies",
            "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
            "description": "Join your band or group and run through songs, riffs, or rhythms together.",
            "benefit_synopsis": "Strengthens coordination, timing, and connection.",
            "recommended_durations": [{"duration_label": "20 minutes"}, {"duration_label": "45 minutes"}],
            "impact_rating_id": 5,
            "difficulty_level_id": 3,
            "frequency": "Scheduled or recurring",
            "is_common": False,
            "notes": "Even one shared practice locks in musical chemistry and shared focus. Practice dynamics, transitions, and listening.",
            "objectives": ["enhance_collaboration", "train_listening", "refine_timing"]
          },
      ],

    #  PRACTICE SUBCATEGORY
      "Games & Puzzles (Board Games, Video Games, Strategy)": [],

    #  PRACTICE SUBCATEGORY
      "Tactile & Mindful Hobbies (Knitting, Coloring, Sculpting)": [],

    #  PRACTICE SUBCATEGORY
      "DIY, Gardening & Home Projects (Gardening, Repairs, Woodworking)": [],

    #  PRACTICE SUBCATEGORY
      "Food & Flavor (Cooking, Baking, Ferments, Plating)": [],

    #  PRACTICE SUBCATEGORY
      "Collections & Curated Interests (Cards, Coins, etc.)": [],

    #  PRACTICE SUBCATEGORY
      "Social Activities & Sports (Recreational Movement & Group Games)": [],

    #  PRACTICE SUBCATEGORY
      "Exploration & Experience (Outdoor Activities, Travel, Culture)": []
  },


  # PRACTICE CATEGORY
  # "Restoration, Relaxation & Self-Care": {

  # },

# "Mental Clarity & Cognitive Priming": [
  
# ],
# "Movement: Exercise, Sports & Physical Activation": [
  
# ],
# "Digital Boundaries & Dopamine Regulation": [
  
# ],
# "Nutrition & Fuel": [
  
# ],
# "Purpose, Planning, and Deep Work": [
  
# ],
# "Building Connections": [
  
# ],
}


practice_data = {
# TODO: Consolidate the following practices into the new super duper categories above
"AM Routine Recommendations": [
    {
        "name": "Morning Hydration",
        "description": "Drink a glass of water to start your day hydrated and support your body's metabolism.",
        "benefit_synopsis": "Boosts metabolism, cognitive function, and energy.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Every morning",
        "is_common": True,
        "notes": "Drinking water upon waking replenishes fluids lost during sleep, enhancing energy levels, cognitive function, and overall health.",
        "objectives": ["hydrate", "boost_energy_levels", "promote_healthy_digestion"]
    },
    {
        "name": "Cold Exposure",
        "description": "Incorporate cold exposure through a cold face rinse, cold shower or cold plunge to invigorate the body.",
        "benefit_synopsis": "Increases dopamine, alertness, and metabolism.",
        "recommended_durations": [{"duration_label": "1 minute"}, {"duration_label": "2 minutes"}, {"duration_label": "5 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Every morning",
        "is_common": False,
        "notes": "Regular cold exposure improves mood, alertness, and metabolic health.",
        "objectives": ["boost_energy_levels", "build_resilience", "improve_circulation"]
    },
    {
        "name": "Morning Mindfulness",
        "description": "Begin your day with mindfulness practices such as meditation, gratitude journaling, or breathing exercises.",
        "benefit_synopsis": "Reduces stress, enhances focus, and emotional balance.",
        "recommended_durations": [{"duration_label": "2 minutes"}, {"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}, {"duration_label": "20 minutes"}, {"duration_label": "30 minutes"}, {"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Every morning",
        "is_common": True,
        "notes": "Mindfulness enhances focus, reduces stress, and fosters emotional balance.",
        "objectives": ["reduce_stress", "improve_focus", "promote_emotional_wellbeing"]
    },
    {
        "name": "Morning Movement",
        "description": "Engage in light stretching, yoga, or other gentle movement to wake up the body.",
        "benefit_synopsis": "Improves circulation, mobility, and flexibility.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "15 minutes"}, {"duration_label": "20 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Every morning",
        "is_common": True,
        "notes": "Movement increases circulation, reduces stiffness, and promotes flexibility.",
        "objectives": ["increase_circulation", "reduce_stiffness", "improve_flexibility"]
    },
    {
        "name": "Morning Sun/Walk",
        "description": "Start your day with exposure to natural sunlight and light physical activity to boost mood and regulate your circadian rhythm.",
        "benefit_synopsis": "Regulates sleep, boosts mood, and energy.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Aim to spend time outdoors in the morning sun, whether through a walk, sitting in natural light, or light activity.",
        "objectives": ["regulate_circadian_rhythm", "boost_mood", "enhance_energy_levels"]
    },
    {
        "name": "Morning Sunlight",
        "description": "Spend a few minutes outside or near a window to get natural sunlight exposure.",
        "benefit_synopsis": "Boosts vitamin D, mood, and circadian rhythm.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}, {"duration_label": "20 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Every morning",
        "is_common": True,
        "notes": "Natural sunlight supports circadian rhythm and boosts vitamin D levels.",
        "objectives": ["regulate_circadian_rhythm", "boost_vitamin_d", "improve_mood"]
    },
    {
        "name": "Set Daily Intentions",
        "description": "Take time to reflect and set intentions for the day, focusing on your goals and priorities.",
        "benefit_synopsis": "Enhances motivation, clarity, and focus.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Every morning",
        "is_common": True,
        "notes": "Setting intentions helps create focus, purpose, and motivation for the day.",
        "objectives": ["improve_focus", "enhance_motivation", "build_consistency"]
    }
],

"General Health": [
    {
        "name": "Morning Hydration",
        "description": "Drink a glass of water to kickstart your metabolism and hydration.",
        "benefit_synopsis": "Supports digestion, metabolism, and hydration.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Start your day with water and consider adding lemon for a refreshing boost.",
        "objectives": ["hydrate", "boost_energy_levels", "promote_healthy_aging"]
    },
    {
        "name": "Morning Sun Exposure",
        "description": "Spend time in sunlight to boost mood and regulate circadian rhythm.",
        "benefit_synopsis": "Regulates circadian rhythm and enhances mood.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Morning sun exposure helps reset your internal clock and boosts vitamin D levels.",
        "objectives": ["enhance_mood_stability", "promote_healthy_aging", "improve_sleep_quality"]
    },
    {
        "name": "Walk in Morning Sun",
        "description": "Take a walk in the sunlight to combine movement and sunlight exposure.",
        "benefit_synopsis": "Boosts immune function and mood stability.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Choose a safe route and make this part of your morning routine for enhanced benefits.",
        "objectives": ["enhance_mood_stability", "increase_endurance", "boost_immune_system"]
    },
    {
        "name": "Evening Hydration",
        "description": "Drink a glass of water before bed to maintain hydration overnight.",
        "benefit_synopsis": "Aids digestion and prevents dehydration overnight.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Avoid drinking excessive amounts right before bed to prevent sleep interruptions.",
        "objectives": ["hydrate", "promote_healthy_digestion", "support_healthy_aging"]
    },
    {
        "name": "Midday Stretch Break",
        "description": "Take a break during the day to stretch and re-energize.",
        "benefit_synopsis": "Reduces tension, improves circulation, and mobility.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on stretching areas where you feel tension, such as your neck, shoulders, or back.",
        "objectives": ["reduce_stress", "enhance_mobility", "promote_circulation"]
    },
    {
        "name": "Weekly Health Check-In",
        "description": "Take time to assess your physical and mental health for the week.",
        "benefit_synopsis": "Improves self-awareness and health monitoring.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Reflect on areas like sleep, hydration, and nutrition to identify improvements or adjustments.",
        "objectives": ["enhance_self-awareness", "promote_healthy_aging", "support_goal_alignment"]
    },
    {
        "name": "Meal Preparation Planning",
        "description": "Plan your meals for the week to support healthy eating habits.",
        "benefit_synopsis": "Enhances nutrition, reduces stress, saves time.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Focus on balanced meals with whole foods. Use meal prep containers for convenience.",
        "objectives": ["improve_nutrition", "reduce_stress", "enhance_energy_levels"]
    },
    {
        "name": "Posture Check-In",
        "description": "Take a moment to assess and correct your posture during the day.",
        "benefit_synopsis": "Prevents strain, improves energy, reduces pain.",
        "recommended_durations": [{"duration_label": "1 minute"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Adjust your chair, desk, and screen height to maintain an ergonomic setup.",
        "objectives": ["reduce_muscle_tension", "enhance_mobility", "promote_energy_efficiency"]
    },
    {
        "name": "AM Digital Wellness",
        "description": "Begin your day with intentional screen-free time to foster mental clarity and set a focused tone for the day.",
        "benefit_synopsis": "Reduces overstimulation, enhances focus, and calm.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "notes": "This time can be used for mindfulness practices, light exercise, or preparing for the day without digital distractions.",
        "objectives": ["reduce_digital_dependency", "enhance_focus", "improve_overall_wellness"]
    },
    {
        "name": "Digital Detox Period",
        "description": "Spend time away from screens to reset your mind and reduce strain.",
        "benefit_synopsis": "Improves focus, reduces stress, and eye strain.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Use this time for hobbies, outdoor activities, or connecting with others.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "promote_mind-body_connection"]
    },
    {
        "name": "Health Progress Journaling",
        "description": "Document your health goals and track your progress weekly.",
        "benefit_synopsis": "Enhances self-awareness and accountability.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Focus on small, actionable goals like increasing water intake or adding vegetables to meals.",
        "objectives": ["enhance_self-awareness", "improve_goal_alignment", "promote_healthy_habits"]
    },
    {
        "name": "Alcohol Abstinence",
        "description": "Commit to abstaining from alcohol to improve physical and mental health.",
        "benefit_synopsis": "Enhances sleep, mood, and overall health.",
        "recommended_durations": [{"duration_label": "Ongoing"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Abstaining from alcohol can support better sleep, improved mood, and overall health. Seek support groups if needed.",
        "objectives": ["enhance_mood_stability", "promote_healthy_aging", "reduce_risk_of_disease"]
    },
    {
        "name": "Substance Abstinence",
        "description": "Commit to abstaining from non-prescription substances to support long-term health and well-being.",
        "benefit_synopsis": "Promotes clarity, stability, and longevity.",
        "recommended_durations": [{"duration_label": "Ongoing"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 5,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Abstaining from substances promotes better mental clarity, physical health, and emotional stability. Seek professional help or join support groups if needed.",
        "objectives": ["reduce_health_risks", "enhance_emotional_resilience", "promote_mental_clarity"]
    }
],

"Nutrition": [
    {
        "name": "Morning Hydration",
        "description": "Drink a glass of water to rehydrate after waking up and periodically throughout the day.",
        "benefit_synopsis": "Boosts hydration, digestion, and brain function.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Aim to drink water consistently throughout the day, particularly before meals and after physical activity.",
        "objectives": ["hydrate", "improve_mental_clarity", "promote_healthy_aging"]
    },
    {
        "name": "Balanced Breakfast",
        "description": "Eat a nutrient-dense breakfast balanced between protein, carbohydrates, healthy fats, and ideally some veggies.",
        "benefit_synopsis": "Regulates blood sugar, boosts energy, focus.",
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Consider preparing your breakfast the night before if mornings are rushed. Avoid high-sugar options like pastries or sugary cereals.",
        "objectives": ["promote_healthy_aging", "enhance_mood_stability", "increase_energy_levels"]
    },
    {
        "name": "Take Supplements",
        "description": "Take any necessary morning supplements (e.g., vitamins, minerals).",
        "benefit_synopsis": "Supports immune function and nutrient balance.",
        "recommended_durations": [{"duration_label": "2 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Ensure supplements are checked by a healthcare professional. Oversupplementation can be harmful and should not replace a healthy diet.",
        "objectives": ["boost_immune_system", "promote_healthy_aging", "improve_mental_clarity"]
    },
    {
        "name": "Balanced Macronutrient Choices",
        "description": "Aim to balance macronutrients in each meal, including a source of protein, complex carbohydrates, and healthy fats.",
        "benefit_synopsis": "Stabilizes energy, enhances metabolism, focus.",
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Each meal",
        "is_common": True,
        "notes": "Experiment with portion sizes that work for your energy levels and appetite. Consider tracking your meals to better understand your macronutrient balance.",
        "objectives": ["increase_energy_levels", "enhance_mood_stability", "improve_overall_nutrition"]
    },
    {
        "name": "Focus on Whole Foods",
        "description": "Incorporate more whole, minimally processed foods into your meals, such as fresh vegetables, fruits, whole grains, and lean proteins.",
        "benefit_synopsis": "Reduces inflammation, supports gut and brain.",
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Look for minimally processed options when shopping. Foods with fewer ingredients and no added sugars or preservatives are good choices.",
        "objectives": ["improve_overall_nutrition", "reduce_added_sugars", "promote_healthy_aging"]
    },
    {
        "name": "Drink Water",
        "description": "Consume water equal to half your body weight in ounces daily to stay hydrated.",
        "benefit_synopsis": "Aids digestion, circulation, and mental clarity.",
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Throughout the day",
        "is_common": True,
        "notes": "Carry a reusable water bottle to track your intake and stay hydrated, especially in hot weather or during physical activity.",
        "objectives": ["hydrate", "promote_healthy_digestion", "improve_mental_clarity"]
    },
    {
        "name": "Minimize Added Sugars",
        "description": "Reduce your intake of added sugars by opting for natural sweeteners or unsweetened options.",
        "benefit_synopsis": "Balances blood sugar, reduces inflammation.",
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Read labels carefully—many processed foods contain hidden added sugars. Consider tracking sugar intake for a week to identify patterns.",
        "objectives": ["reduce_inflammation", "improve_energy_levels", "promote_healthy_aging"]
    },
    {
        "name": "Home-Cooked Meals",
        "description": "Prioritize home-cooked meals to gain control over ingredients and promote healthier eating habits.",
        "benefit_synopsis": "Reduces processed food intake, enhances nutrition.",
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Batch cooking or meal prepping can save time and reduce reliance on processed or takeout meals.",
        "objectives": ["enhance_mood_stability", "improve_overall_nutrition", "reduce_added_sugars"]
    },
    {
        "name": "Eat More Vegetables",
        "description": "Add a variety of colorful vegetables to your meals to boost fiber and nutrient intake.",
        "benefit_synopsis": "Boosts gut health, fiber, and immune function.",
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "At least 5 servings daily",
        "is_common": True,
        "notes": "Focus on seasonal and locally sourced vegetables for better flavor and cost efficiency. Consider blending them into smoothies or soups if you’re not a fan of raw vegetables.",
        "objectives": ["promote_healthy_digestion", "improve_overall_nutrition", "reduce_inflammation"]
    },
    {
        "name": "Mindful Eating Pause",
        "description": "Take a moment before meals to appreciate your food and eat mindfully, focusing on each bite.",
        "benefit_synopsis": "Improves digestion, portion control, and awareness.",
        "recommended_durations": [{"duration_label": "2 minutes"}],
        "impact_rating_id": 2,
        "difficulty_level_id": 1,
        "frequency": "Before meals",
        "is_common": False,
        "notes": "Mindful eating can help with portion control and enhance your enjoyment of meals. Avoid distractions like phones or TV while eating.",
        "objectives": ["improve_digestion", "reduce_overeating", "enhance_mood_stability"]
    }
],

"Sleep Hygiene": [
    {
        "name": "Bedtime Routine Planning",
        "description": "Plan a consistent bedtime routine to wind down effectively.",
        "benefit_synopsis": "Signals body to relax, improves sleep.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "A well-planned bedtime routine can help signal your body that it’s time to relax and prepare for sleep. Include calming activities like reading, light stretching, or meditation.",
        "objectives": ["improve_sleep_quality", "reduce_stress", "enhance_mood_stability"]
    },
    {
        "name": "Device Shut-Off",
        "description": "Turn off all electronic devices before bedtime to reduce blue light exposure and promote relaxation.",
        "benefit_synopsis": "Reduces blue light, improves melatonin release.",
        "recommended_durations": [
            {"duration_label": "30 minutes", "engagement_level": "Beginner"},
            {"duration_label": "1 hour", "engagement_level": "Intermediate"},
            {"duration_label": "2 hours", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Avoid bright screens from phones, tablets, or TVs before bed. Consider using blue light-blocking glasses or night mode if device use is unavoidable.",
        "objectives": ["improve_sleep_quality", "reduce_anxiety", "enhance_mood_stability"]
    },
    {
        "name": "Bedroom Optimization",
        "description": "Prepare your bedroom environment to encourage restful sleep by reducing light, noise, and maintaining a comfortable temperature.",
        "benefit_synopsis": "Enhances sleep depth and relaxation.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Consider blackout curtains, a white noise machine, and setting the thermostat to a cool temperature for optimal sleep conditions.",
        "objectives": ["improve_sleep_quality", "reduce_stress", "enhance_mood_stability"]
    },
    {
        "name": "Pre-Sleep Relaxation",
        "description": "Engage in relaxing activities like reading, light yoga, or meditation before bedtime.",
        "benefit_synopsis": "Calms nervous system, reduces stress.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Find what works for you to create a calming pre-sleep routine. Avoid stimulating activities like exercise or intense conversations.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "improve_sleep_quality"]
    },
    {
        "name": "Consistent Sleep Schedule",
        "description": "Aim for a consistent sleep and wake time, even on weekends.",
        "benefit_synopsis": "Regulates circadian rhythm, stabilizes energy.",
        "recommended_durations": [{"duration_label": "7 hours"}, {"duration_label": "8 hours"}, {"duration_label": "9 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Nightly",
        "is_common": True,
        "notes": "Consistency helps regulate your body’s internal clock. Avoid sleeping in significantly on weekends to maintain a healthy rhythm.",
        "objectives": ["improve_sleep_quality", "reduce_stress", "enhance_energy_levels"]
    },
    {
        "name": "Caffeine Curfew",
        "description": "Avoid caffeine intake in the afternoon and evening to prevent sleep disturbances.",
        "benefit_synopsis": "Prevents sleep disruption, lowers anxiety.",
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Try to limit caffeine consumption after 2 PM. Herbal teas like chamomile or peppermint can be a great alternative in the evening.",
        "objectives": ["improve_sleep_quality", "reduce_anxiety", "enhance_mood_stability"]
    },
    {
        "name": "Evening Reflection or Gratitude Journal",
        "description": "Take time before bed to reflect on the day or write down things you are grateful for.",
        "benefit_synopsis": "Reduces stress, enhances positive emotions.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "notes": "This practice can help clear your mind and reduce anxiety before sleep. Use a simple notebook or a journaling app (preferably the notebook if within an hour of bedtime).",
        "objectives": ["reduce_stress", "enhance_mood_stability", "improve_sleep_quality"]
    }
],

"Movement": [
    {
        "name": "Movement/Stretch",
        "description": "Incorporate gentle movements and stretches to wake up your body and improve flexibility.",
        "benefit_synopsis": "Boosts circulation, flexibility, and mobility.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on light stretching, yoga poses, or dynamic movements to energize and prepare for the day.",
        "objectives": ["improve_flexibility", "boost_energy", "reduce_muscle_tension"]
    },
    {
        "name": "General Workout",
        "description": "Engage in a workout of your choice, including strength training, cardio, or a mix of both.",
        "benefit_synopsis": "Enhances fitness, strength, and endurance.",
        "recommended_durations": [
            {"duration_label": "15 minutes", "engagement_level": "Beginner"},
            {"duration_label": "30 minutes", "engagement_level": "Intermediate"},
            {"duration_label": "1 hour", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "3-5 times per week",
        "is_common": True,
        "notes": "Tailor your workout to your goals, whether it's building strength, improving endurance, or maintaining general fitness.",
        "objectives": ["increase_fitness", "enhance_mood_stability", "boost_energy_levels"]
    },
    {
        "name": "Running",
        "description": "Go for a run to improve cardiovascular health, build endurance, and clear your mind.",
        "benefit_synopsis": "Boosts heart health, endurance, and mood.",
        "recommended_durations": [
            {"duration_label": "15 minutes", "engagement_level": "Beginner"},
            {"duration_label": "30 minutes", "engagement_level": "Intermediate"},
            {"duration_label": "1 hour", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "3-5 times per week",
        "is_common": True,
        "notes": "Start with short distances or intervals if you're new to running. Ensure proper footwear to avoid injuries.",
        "objectives": ["increase_endurance", "enhance_mood_stability", "promote_healthy_aging"]
    },
    {
        "name": "Cycling",
        "description": "Ride a bike outdoors or use a stationary bike to build endurance and strengthen lower body muscles.",
        "benefit_synopsis": "Strengthens legs, boosts endurance, heart health.",
        "recommended_durations": [
            {"duration_label": "20 minutes", "engagement_level": "Beginner"},
            {"duration_label": "45 minutes", "engagement_level": "Intermediate"},
            {"duration_label": "1 hour", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "3-5 times per week",
        "is_common": True,
        "notes": "Choose routes or resistance levels suited to your fitness level. Consider a helmet for safety during outdoor rides.",
        "objectives": ["increase_endurance", "improve_cardiovascular_health", "enhance_mood_stability"]
    },
    {
        "name": "Strength Training",
        "description": "Engage in weightlifting or resistance exercises to build muscle, boost metabolism, and improve bone density.",
        "benefit_synopsis": "Builds strength, metabolism, and bone health.",
        "recommended_durations": [
            {"duration_label": "20 minutes", "engagement_level": "Beginner"},
            {"duration_label": "30 minutes", "engagement_level": "Intermediate"},
            {"duration_label": "1 hour", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "3-4 times per week",
        "is_common": True,
        "notes": "Focus on form to prevent injuries. Incorporate rest days to allow muscle recovery and growth.",
        "objectives": ["increase_strength", "improve_bone_density", "enhance_mobility"]
    },
    {
        "name": "CrossFit",
        "description": "Participate in high-intensity functional fitness workouts to improve overall strength, stamina, and endurance.",
        "benefit_synopsis": "Increases power, endurance, metabolic function.",
        "recommended_durations": [
            {"duration_label": "20 minutes", "engagement_level": "Beginner"},
            {"duration_label": "45 minutes", "engagement_level": "Intermediate"},
            {"duration_label": "1 hour", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "3-4 times per week",
        "is_common": False,
        "notes": "Workouts are scalable for all fitness levels but can be intense. Warm up thoroughly and listen to your body to avoid injury.",
        "objectives": ["increase_strength", "improve_endurance", "boost_energy_levels"]
    },
    {
        "name": "Pilates",
        "description": "Engage in Pilates to strengthen your core, improve posture, and enhance flexibility.",
        "benefit_synopsis": "Strengthens core, improves posture, flexibility.",
        "recommended_durations": [
            {"duration_label": "30 minutes", "engagement_level": "Beginner"},
            {"duration_label": "1 hour", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Twice weekly",
        "is_common": True,
        "notes": "Pilates is particularly effective for building core strength and supporting mobility. Consider a class or online video for proper guidance.",
        "objectives": ["improve_flexibility", "enhance_core_strength", "promote_injury_prevention"]
    },
    {
        "name": "Yoga",
        "description": "Engage in a yoga session to enhance flexibility, balance, and mindfulness.",
        "benefit_synopsis": "Improves flexibility, balance, and relaxation.",
        "recommended_durations": [
            {"duration_label": "30 minutes", "engagement_level": "Beginner"},
            {"duration_label": "1 hour", "engagement_level": "Intermediate"},
            {"duration_label": "90 minutes", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "3-4 times per week",
        "is_common": True,
        "notes": "Yoga can be tailored to any fitness level. Try various styles (e.g., Hatha, Vinyasa, or Yin) to suit your goals.",
        "objectives": ["enhance_flexibility", "reduce_stress", "improve_balance"]
    },
    {
        "name": "Orange Theory",
        "description": "Participate in guided group workouts that combine cardio and strength training for an all-around fitness boost.",
        "benefit_synopsis": "Enhances endurance, strength, and heart health.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "3-4 times per week",
        "is_common": False,
        "notes": "Orange Theory offers a blend of treadmill, rowing, and strength exercises in an engaging group environment.",
        "objectives": ["increase_endurance", "improve_strength", "enhance_cardiovascular_health"]
    },
    {
        "name": "Hiking",
        "description": "Explore trails and hike outdoors to improve endurance and connect with nature.",
        "benefit_synopsis": "Boosts endurance, heart health, mental well-being.",
        "recommended_durations": [
            {"duration_label": "30 minutes", "engagement_level": "Beginner"},
            {"duration_label": "1 hour", "engagement_level": "Intermediate"},
            {"duration_label": "2 hours", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Choose trails suited to your fitness level. Bring water, wear appropriate footwear, and let someone know your route.",
        "objectives": ["increase_endurance", "reduce_stress", "enhance_mood_stability"]
    },
    {
        "name": "Rowing",
        "description": "Use a rowing machine or row on water to engage the entire body and improve cardiovascular health.",
        "benefit_synopsis": "Full-body workout with strength and cardio benefits.",
        "recommended_durations": [
            {"duration_label": "20 minutes", "engagement_level": "Beginner"},
            {"duration_label": "45 minutes", "engagement_level": "Intermediate"},
            {"duration_label": "1 hour", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "3-5 times per week",
        "is_common": False,
        "notes": "Focus on form to avoid injury. Rowing combines strength and cardio for an effective full-body workout.",
        "objectives": ["improve_endurance", "increase_strength", "enhance_mood_stability"]
    },
    {
        "name": "Dance",
        "description": "Dance to your favorite music or participate in dance fitness classes to boost cardio and mood.",
        "benefit_synopsis": "Boosts heart health and coordination in a fun way.",
        "recommended_durations": [
            {"duration_label": "15 minutes", "engagement_level": "Beginner"},
            {"duration_label": "30 minutes", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "3-5 times per week",
        "is_common": True,
        "notes": "Dancing is a great way to make exercise fun. Options include Zumba, hip-hop, ballroom, and even virtual dance workouts.",
        "objectives": ["improve_cardiovascular_health", "enhance_mood_stability", "increase_energy_levels"]
    },
    {
        "name": "Martial Arts",
        "description": "Martial arts class to develop your technique, improve strength, and build self-discipline.",
        "benefit_synopsis": "Enhances coordination, confidence, and physical resilience.",
        "recommended_durations": [
            {"duration_label": "1 hour"},
            {"duration_label": "90 minutes"},
            {"duration_label": "2 hours"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2-4 times per week",
        "is_common": True,
        "notes": "Styles like Brazilian jiu-jitsu focus on grappling and ground techniques, while Muay Thai and kickboxing emphasize striking. Martial arts can boost confidence, coordination, fitness, and stress relief/resilience.",
        "objectives": ["increase_strength", "improve_coordination", "reduce_stress"]
    },
    {
        "name": "Recreational Sports",
        "description": "Play sports like basketball, tennis, soccer, or volleyball for exercise and fun.",
        "benefit_synopsis": "Combines exercise with social engagement and competition.",
        "recommended_durations": [
            {"duration_label": "30 minutes"},
            {"duration_label": "45 minutes"},
            {"duration_label": "60 minutes"},
            {"duration_label": "90 minutes"},
            {"duration_label": "2 hours"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Join a local league, play casually with friends, or practice solo to stay active.",
        "objectives": ["improve_coordination", "increase_endurance", "enhance_mood_stability"]
    },
    {
        "name": "Swimming",
        "description": "Swim laps or engage in water aerobics to improve strength and cardiovascular health with low joint impact.",
        "benefit_synopsis": "Low-impact full-body workout for strength and endurance.",
        "recommended_durations": [
            {"duration_label": "20 minutes", "engagement_level": "Beginner"},
            {"duration_label": "45 minutes", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "3 times per week",
        "is_common": True,
        "notes": "Swimming is excellent for full-body conditioning and is particularly beneficial for those with joint pain or injuries.",
        "objectives": ["improve_endurance", "increase_strength", "reduce_stress"]
    },
    {
        "name": "Tai Chi",
        "description": "Practice Tai Chi to improve balance, flexibility, and mental focus.",
        "benefit_synopsis": "Promotes relaxation, balance, and joint health.",
        "recommended_durations": [
            {"duration_label": "10 minutes", "engagement_level": "Beginner"},
            {"duration_label": "30 minutes", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Tai Chi is a low-intensity activity suitable for all ages. Look for local classes or online videos to learn basic movements.",
        "objectives": ["improve_balance", "reduce_stress", "enhance_mood_stability"]
    },
    {
        "name": "Climbing",
        "description": "Engage in indoor or outdoor climbing to build strength, coordination, and focus.",
        "benefit_synopsis": "Builds upper-body strength and problem-solving skills.",
        "recommended_durations": [
            {"duration_label": "20 minutes", "engagement_level": "Beginner"},
            {"duration_label": "1 hour", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "3-5 times per week",
        "is_common": False,
        "notes": "Climbing gyms often offer beginner lessons. Proper safety equipment is essential for outdoor climbing.",
        "objectives": ["increase_strength", "improve_balance", "enhance_problem_solving"]
    },
    {
        "name": "Barre",
        "description": "Engage in Barre workouts to improve strength, posture, and flexibility with low impact.",
        "benefit_synopsis": "Enhances core strength and posture with low impact.",
        "recommended_durations": [
            {"duration_label": "15 minutes", "engagement_level": "Beginner"},
            {"duration_label": "45 minutes", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Twice weekly",
        "is_common": True,
        "notes": "Barre combines ballet, yoga, and Pilates techniques and is great for building core strength.",
        "objectives": ["improve_flexibility", "enhance_core_strength", "promote_posture"]
    },
    {
        "name": "High-Intensity Interval Training (HIIT)",
        "description": "Perform short bursts of intense exercise alternated with recovery periods to maximize efficiency.",
        "benefit_synopsis": "Burns fat efficiently and improves cardiovascular health.",
        "recommended_durations": [
            {"duration_label": "1 hour", "engagement_level": "Beginner"},
            {"duration_label": "90 minutes", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "3 times per week",
        "is_common": True,
        "notes": "HIIT can be done with bodyweight exercises, cardio machines, or weights. Tailor intervals to your fitness level.",
        "objectives": ["increase_fitness", "improve_cardio_health", "boost_metabolism"]
    },
    {
        "name": "Trail Running",
        "description": "Run on natural trails to build endurance, strengthen lower body muscles, and enjoy nature.",
        "benefit_synopsis": "Strengthens endurance, reduces stress, and engages stabilizing muscles.",
        "recommended_durations": [
            {"duration_label": "45 minutes", "engagement_level": "Beginner"},
            {"duration_label": "1 hour", "engagement_level": "Intermediate"},
            {"duration_label": "2 hours", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "3-5 times per week",
        "is_common": True,
        "notes": "Trail running offers a low-impact alternative to road running. Wear trail-specific shoes for better grip and safety.",
        "objectives": ["increase_endurance", "enhance_mood_stability", "reduce_stress"]
    },
    {
        "name": "Paddleboarding or Kayaking",
        "description": "Engage in water-based activities to improve balance, core strength, and enjoy the outdoors.",
        "benefit_synopsis": "Builds core strength, balance, and provides a meditative experience.",
        "recommended_durations": [
            {"duration_label": "1 hour", "engagement_level": "Beginner"},
            {"duration_label": "2 hours", "engagement_level": "Intermediate"},
            {"duration_label": "Full day", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Occasional",
        "is_common": False,
        "notes": "These activities offer a full-body workout and can double as a relaxing recreational activity. Start with calm waters.",
        "objectives": ["enhance_balance", "improve_core_strength", "reduce_stress"]
    },
    {
        "name": "Group Fitness Classes",
        "description": "Participate in group classes like spin, aerobics, or bootcamp for a guided, social workout.",
        "benefit_synopsis": "Enhances motivation and accountability through structured workouts.",
        "recommended_durations": [
            {"duration_label": "30 minutes", "engagement_level": "Beginner"},
            {"duration_label": "1 hour", "engagement_level": "Intermediate"},
            {"duration_label": "90 minutes", "engagement_level": "Advanced"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Twice weekly",
        "is_common": True,
        "notes": "Group classes can motivate you to push harder and stay consistent. Try different formats to find one you enjoy.",
        "objectives": ["improve_cardio_health", "increase_fitness", "enhance_mood_stability"]
    },
    {
        "name": "Parkour",
        "description": "Practice parkour to improve agility, coordination, and confidence in navigating obstacles.",
        "benefit_synopsis": "Improves reaction time, body control, and mental agility.",
        "recommended_durations": [
            {"duration_label": "20 minutes", "engagement_level": "Beginner"},
            {"duration_label": "45 minutes", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Twice weekly",
        "is_common": False,
        "notes": "Parkour can be done in gyms or urban areas. Start with basic movements like vaulting and balancing.",
        "objectives": ["improve_agility", "enhance_coordination", "boost_confidence"]
    },
    {
        "name": "Jumping Rope",
        "description": "Jump rope for a high-intensity cardio workout that improves coordination and endurance.",
        "benefit_synopsis": "Boosts cardiovascular fitness and improves coordination.",
        "recommended_durations": [
            {"duration_label": "10 minutes", "engagement_level": "Beginner"},
            {"duration_label": "20 minutes", "engagement_level": "Intermediate"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Jumping rope is an affordable, effective workout. Focus on proper form to avoid strain on the knees.",
        "objectives": ["improve_cardio_health", "enhance_coordination", "increase_fitness"]
    },
    {
        "name": "Aerial Silks",
        "description": "Aerial silks class to build strength, flexibility, and confidence through acrobatic movements.",
        "benefit_synopsis": "Develops upper-body strength, balance, and body awareness.",
        "recommended_durations": [
            {"duration_label": "1 hour"},
            {"duration_label": "90 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1-3 times per week",
        "is_common": False,
        "notes": "Aerial silks require upper body strength and balance. Beginners often start with basic climbs and wraps, progressing to more advanced poses.",
        "objectives": ["increase_strength", "improve_flexibility", "enhance_balance"]
    },
    {
        "name": "Pole Fitness",
        "description": "Pole fitness class focusing on strength, coordination, and body control.",
        "benefit_synopsis": "Enhances core strength and coordination through dynamic movement.",
        "recommended_durations": [
            {"duration_label": "1 hour"},
            {"duration_label": "90 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "1-3 times per week",
        "is_common": False,
        "notes": "Pole fitness combines elements of dance and acrobatics, engaging the core and upper body. Classes often progress from basic spins to advanced routines.",
        "objectives": ["increase_strength", "enhance_core_strength", "improve_flexibility", "boost_confidence"]
    },
    {
        "name": "Calisthenics",
        "description": "Perform bodyweight exercises to improve strength, flexibility, and endurance.",
        "benefit_synopsis": "Strengthens functional movement using only body weight.",
        "recommended_durations": [
            {"duration_label": "20 minutes"},
            {"duration_label": "30 minutes"},
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "2-5 times per week",
        "is_common": True,
        "notes": "Calisthenics can be adapted to all fitness levels. Examples include push-ups, pull-ups, squats, and planks. Progressions like handstands or muscle-ups offer advanced challenges.",
        "objectives": ["increase_strength", "improve_flexibility", "boost_body_control"]
    }
],

"Mobility": [
    {
        "name": "Joint Circles",
        "description": "Perform joint circles to enhance range of motion and reduce stiffness.",
        "benefit_synopsis": "Improves joint lubrication and range of motion, reducing stiffness.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Focus on slow, controlled movements through the full range of motion for each joint. This is great for warm-ups or recovery days.",
        "objectives": ["enhance_mobility", "reduce_stiffness", "promote_healthy_aging"]
    },
    {
        "name": "Dynamic Stretching",
        "description": "Engage in dynamic stretches to prepare your body for movement.",
        "benefit_synopsis": "Increases flexibility, circulation, and prepares muscles for activity.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "3 times per week",
        "is_common": True,
        "notes": "Dynamic stretches improve flexibility and prepare muscles for activity. Examples include leg swings and arm circles.",
        "objectives": ["improve_flexibility", "reduce_injury_risk", "enhance_mobility"]
    },
    {
        "name": "Foam Rolling",
        "description": "Use a foam roller to release tension and improve muscle recovery.",
        "benefit_synopsis": "Relieves muscle tightness and enhances post-workout recovery.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on tight areas like the quads, hamstrings, and back. Roll slowly and pause on tender spots for best results.",
        "objectives": ["reduce_muscle_tension", "enhance_recovery", "improve_flexibility"]
    },
    {
        "name": "Mobility Ball Release",
        "description": "Target specific muscle knots and tension points with a mobility ball.",
        "benefit_synopsis": "Pinpoints and releases tension in deep muscle areas.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Use a lacrosse ball or mobility ball for areas like the shoulders, glutes, or feet. Apply gentle pressure and move slowly.",
        "objectives": ["reduce_muscle_tension", "improve_recovery", "enhance_joint_health"]
    },
    {
        "name": "Animal Flow",
        "description": "Perform fluid, ground-based movements to improve mobility, strength, and coordination.",
        "benefit_synopsis": "Improves movement efficiency, mobility, and core control.",
        "recommended_durations": [{"duration_label": "20 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2-3 times per week",
        "is_common": False,
        "notes": "Animal Flow combines elements of yoga, breakdancing, and martial arts to enhance body control. It’s suitable for all fitness levels.",
        "objectives": ["enhance_mobility", "increase_strength", "improve_coordination"]
    },
    {
        "name": "Foundation Training",
        "description": "Practice foundational movements to build core strength, improve posture, and enhance mobility.",
        "benefit_synopsis": "Develops postural strength and mobility for pain-free movement.",
        "recommended_durations": [{"duration_label": "20 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Twice weekly",
        "is_common": False,
        "notes": "Foundation Training emphasizes breathing and posterior chain activation to address posture-related issues and build resilience.",
        "objectives": ["improve_posture", "enhance_mobility", "reduce_injury_risk"]
    },
    {
        "name": "Core Balance Training",
        "description": "Engage in core balance movements to improve stability, alignment, and body awareness.",
        "benefit_synopsis": "Strengthens deep core muscles for better stability and control.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Twice weekly",
        "is_common": False,
        "notes": "Core Balance integrates stability-focused exercises with mobility work to strengthen the core and improve body control.",
        "objectives": ["enhance_balance", "improve_core_strength", "reduce_injury_risk"]
    },
    {
        "name": "Mobility Flow Systems",
        "description": "Practice mobility flow systems designed to enhance flexibility, joint health, and fluid movement.",
        "benefit_synopsis": "Encourages smooth, controlled movement transitions to improve flexibility.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "1-2 times per week",
        "is_common": False,
        "notes": "Flow systems integrate movements that transition smoothly, focusing on joints, muscles, and overall fluidity.",
        "objectives": ["improve_flexibility", "reduce_stiffness", "enhance_joint_health"]
    },
    {
        "name": "Bodyweight Mobility Circuits",
        "description": "Perform bodyweight circuits designed to enhance mobility and dynamic strength.",
        "benefit_synopsis": "Combines mobility with strength for fluid and functional movement.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "20 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "3 times per week",
        "is_common": True,
        "notes": "Bodyweight mobility circuits include transitions like deep squats, lunges, and floor work, ideal for all fitness levels.",
        "objectives": ["enhance_mobility", "increase_strength", "improve_flexibility"]
    },
    {
        "name": "Movement Restoration Programs",
        "description": "Follow guided restoration programs focused on rebuilding movement patterns and reducing pain.",
        "benefit_synopsis": "Targets dysfunctional movement patterns to restore pain-free mobility.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Programs often focus on restoring balance, flexibility, and mobility through targeted exercises. Ideal for injury recovery or prevention.",
        "objectives": ["restore_movement_patterns", "reduce_pain", "enhance_mobility"]
    }
],

"Mindfulness & Self-Reflection": [
    {
        "name": "Meditation",
        "description": "Practice mindfulness meditation to center yourself and start the day calmly.",
        "benefit_synopsis": "Enhances mental clarity, reduces stress, and promotes emotional balance.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"},
            {"duration_label": "20 minutes"},
            {"duration_label": "30 minutes"},
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Explore different types of meditation, such as focused attention, loving-kindness, or mantra-based meditation.",
        "objectives": ["reduce_stress", "enhance_self-awareness", "improve_focus"]
    },
    {
        "name": "Body Scan",
        "description": "Perform a body scan meditation to connect with and relax your body.",
        "benefit_synopsis": "Promotes deep relaxation and mindfulness by heightening body awareness.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Start at the top of your head and move down, focusing on each area and releasing tension.",
        "objectives": ["reduce_stress", "enhance_self-awareness", "promote_relaxation"]
    },
    {
        "name": "Guided Visualization",
        "description": "Use a guided visualization to focus on positive outcomes and goals.",
        "benefit_synopsis": "Enhances motivation and optimism by mentally rehearsing success.",
        "recommended_durations": [
            {"duration_label": "10 minutes"},
            {"duration_label": "20 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Common themes include imagining yourself achieving goals or relaxing in peaceful environments.",
        "objectives": ["increase_optimism", "reduce_stress", "enhance_creative_thinking"]
    },
    {
        "name": "Mantra Meditation",
        "description": "Focus on repeating a calming word, phrase, or sound to settle the mind.",
        "benefit_synopsis": "Improves focus and emotional regulation through rhythmic repetition.",
        "recommended_durations": [
            {"duration_label": "10 minutes"},
            {"duration_label": "15 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Common mantras include 'Om' or phrases like 'I am at peace.' This practice helps focus the mind and reduce distractions.",
        "objectives": ["enhance_focus", "reduce_stress", "increase_self-awareness"]
    },
    {
        "name": "Transcendental Meditation (TM)",
        "description": "Practice TM by repeating a personal mantra in a structured meditation.",
        "benefit_synopsis": "Promotes deep relaxation and heightened self-awareness.",
        "recommended_durations": [
            {"duration_label": "10 minutes"},
            {"duration_label": "20 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": False,
        "notes": "TM is often taught through formal programs. It focuses on achieving a deep state of relaxation and self-awareness.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "increase_self-awareness"]
    },
    {
        "name": "Zen Meditation (Zazen)",
        "description": "Sit in quiet reflection, focusing on the breath and observing thoughts without judgment.",
        "benefit_synopsis": "Enhances emotional resilience and inner peace through non-attachment.",
        "recommended_durations": [
            {"duration_label": "15 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Zen meditation emphasizes posture and breathing. Often practiced in a seated position with minimal distractions.",
        "objectives": ["increase_self-awareness", "reduce_stress", "enhance_emotional_resilience"]
    },
    {
        "name": "Gratitude Journaling",
        "description": "Write down 3-5 things you’re grateful for each day to foster positivity.",
        "benefit_synopsis": "Strengthens positive thinking and emotional stability.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on specific moments or people that made an impact to cultivate appreciation over time.",
        "objectives": ["increase_optimism", "enhance_mood_stability", "reduce_stress"]
    },
    {
        "name": "Sensory Grounding (5-4-3-2-1 Technique)",
        "description": "Engage the five senses to bring yourself to the present moment.",
        "benefit_synopsis": "Helps reduce anxiety by anchoring awareness to the present.",
        "recommended_durations": [
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Use techniques like naming five things you can see, four things you can feel, three things you can hear, two you can smell, and one you can taste.",
        "objectives": ["reduce_anxiety", "promote_mind-body_connection", "enhance_focus"]
    },
    {
        "name": "Aromatherapy",
        "description": "Use essential oils to activate your sense of smell and promote calm.",
        "benefit_synopsis": "Enhances mood stability and focus through scent-based relaxation.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Twice daily",
        "is_common": True,
        "objectives": ["reduce_stress", "enhance_mood_stability", "improve_focus"]
    },
    {
        "name": "Nature Walk",
        "description": "Take a walk in a park or forest to connect with nature.",
        "benefit_synopsis": "Boosts mental clarity, reduces stress, and enhances mood.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "objectives": ["reduce_stress", "enhance_mood_stability", "increase_optimism"]
    },
    {
        "name": "Vipassana Meditation",
        "description": "Engage in focused meditation aimed at gaining insight into the nature of reality.",
        "recommended_durations": [
            {"duration_label": "15 minutes"},
            {"duration_label": "30 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Vipassana involves observing sensations, emotions, and thoughts with mindful awareness. Often practiced in silent retreats.",
        "objectives": ["increase_self-awareness", "enhance_focus", "promote_emotional_clarity"]
    },
    {
        "name": "Self-Inquiry",
        "description": "Ask reflective questions to deepen your understanding of yourself and your actions.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Sample questions: 'What are my current challenges?' or 'What are my priorities today?'",
        "objectives": ["enhance_self-awareness", "improve_emotional_resilience", "reduce_stress"]
    },
    {
        "name": "Gratitude Journaling",
        "description": "Write down 3-5 things you’re grateful for each day to foster positivity.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on specific moments or people that made an impact to cultivate appreciation over time.",
        "objectives": ["increase_optimism", "enhance_mood_stability", "reduce_stress"]
    },
    {
        "name": "Reflective Journaling",
        "description": "Explore your thoughts and feelings through journaling to deepen self-awareness.",
        "recommended_durations": [
            {"duration_label": "10 minutes"},
            {"duration_label": "20 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Use prompts such as 'What did I learn today?' or 'What challenges am I facing?'",
        "objectives": ["enhance_self-awareness", "reduce_stress", "improve_problem_solving"]
    },
    {
        "name": "Future Vision Journaling",
        "description": "Visualize your ideal future and write about the goals and experiences you hope to achieve.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": False,
        "notes": "This practice is especially helpful for long-term planning and goal setting.",
        "objectives": ["enhance_focus", "increase_optimism", "promote_goal_alignment"]
    },
    {
        "name": "Grounding Exercise",
        "description": "Walk barefoot on grass or sand to reconnect with the earth.",
        "benefit_synopsis": "Stabilizes emotions and enhances physical grounding.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "objectives": ["reduce_stress", "enhance_emotional_regulation", "improve_balance"]
    }
],

"Spiritual Connection & Gratitude": [
    {
        "name": "Gratitude Practice",
        "description": "List three things you are grateful for to foster a positive mindset.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Focusing on gratitude can reframe negative thoughts and increase life satisfaction.",
        "benefit_synopsis": "Cultivates appreciation, boosts emotional well-being, and reduces stress.",
        "objectives": ["cultivate_gratitude", "increase_optimism", "reduce_stress"]
    },
    {
        "name": "Gratitude Journaling",
        "description": "Write down 3-5 things you’re grateful for each day to foster positivity.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on specific moments or people that made an impact to cultivate appreciation over time.",
        "benefit_synopsis": "Enhances emotional resilience, strengthens perspective, and reduces stress.",
        "objectives": ["increase_optimism", "enhance_mood_stability", "reduce_stress"]
    },
    {
        "name": "Gratitude Letters",
        "description": "Write a letter to someone you’re grateful for, expressing your appreciation.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": False,
        "notes": "Consider delivering the letter in person or reading it aloud to deepen the connection.",
        "benefit_synopsis": "Deepens relationships, fosters emotional expression, and enhances empathy.",
        "objectives": ["strengthen_relationships", "increase_empathy", "enhance_mood_stability"]
    },
    {
        "name": "Prayer",
        "description": "Engage in personal or traditional prayer to connect spiritually.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Prayer can provide comfort, clarity, and a sense of connectedness to a higher power.",
        "benefit_synopsis": "Strengthens spiritual resilience, encourages reflection, and provides inner peace.",
        "objectives": ["develop_spiritual_resilience", "enhance_self-awareness", "reduce_stress"]
    },
    {
        "name": "Devotional Reading",
        "description": "Read passages from sacred texts to gain insight and reflect on purpose.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Devotional reading can inspire a sense of purpose and provide wisdom for daily life.",
        "benefit_synopsis": "Increases clarity, cultivates patience, and encourages spiritual growth.",
        "objectives": ["increase_clarity", "cultivate_a_sense_of_wonder", "develop_patience"]
    },
    {
        "name": "Loving-Kindness Meditation",
        "description": "Send kindness and compassion to yourself and others.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Repeat phrases like 'May I be happy, may I be healthy' for yourself and extend them to others.",
        "benefit_synopsis": "Enhances empathy, reduces stress, and promotes emotional well-being.",
        "objectives": ["increase_empathy", "enhance_mood_stability", "reduce_stress"]
    },
    {
        "name": "Nature Immersion",
        "description": "Spend time in nature to recharge and reduce stress.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Taking time in natural settings can reduce anxiety and improve overall mood.",
        "benefit_synopsis": "Lowers stress, boosts mental clarity, and enhances mood stability.",
        "objectives": ["enhance_mood_stability", "reduce_stress", "promote_mind-body_connection"]
    },
    {
        "name": "Daily Intention",
        "description": "Set a daily intention or affirmation to align your actions with your values and goals.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Pair this ritual with prayer, journaling, or quiet reflection for added meaning.",
        "benefit_synopsis": "Improves focus, enhances self-discipline, and promotes goal alignment.",
        "objectives": ["improve_focus", "enhance_spiritual_connection", "promote_goal_alignment"]
    },
    {
        "name": "Mantra Meditation",
        "description": "Focus on repeating a calming word, phrase, or sound to settle the mind.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Mantras like 'Om' or personal phrases can promote clarity and a sense of peace.",
        "benefit_synopsis": "Encourages mindfulness, enhances focus, and reduces mental distractions.",
        "objectives": ["enhance_spiritual_connection", "reduce_stress", "improve_focus"]
    },
    {
        "name": "Call to Purpose Affirmation",
        "description": "Recite affirmations that align with your higher purpose or core values.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use affirmations like 'I am here to contribute to the well-being of others' or 'I act in alignment with my values.'",
        "benefit_synopsis": "Boosts self-confidence, aligns actions with values, and increases motivation.",
        "objectives": ["enhance_spiritual_connection", "improve_goal_alignment", "increase_focus"]
    },
    {
        "name": "Reflective Gratitude Walk",
        "description": "Take a walk, reflecting on things you’re grateful for as you move.",
        "recommended_durations": [
            {"duration_label": "10 minutes"},
            {"duration_label": "20 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "This combines light physical activity with gratitude, ideal for starting or ending your day on a positive note.",
        "benefit_synopsis": "Combines movement with mindfulness to enhance gratitude and reduce stress.",
        "objectives": ["enhance_mood_stability", "reduce_stress", "promote_mind-body_connection"]
    },
    {
        "name": "Reflective Reading",
        "description": "Read spiritual or inspirational texts to deepen your sense of connection and purpose.",
        "recommended_durations": [
            {"duration_label": "15 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Choose texts that resonate with your values, such as religious scripture, philosophy, or motivational writings.",
        "benefit_synopsis": "Encourages introspection, strengthens spiritual connection, and increases clarity.",
        "objectives": ["enhance_spiritual_connection", "increase_optimism", "promote_emotional_resilience"]
    },
    {
        "name": "Affirmation Repetition",
        "description": "Repeat positive affirmations aloud or silently to reinforce confidence and self-worth.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Choose affirmations that align with your goals, such as 'I am enough' or 'I am capable of achieving my dreams.'",
        "benefit_synopsis": "Reinforces self-confidence, reduces self-doubt, and improves focus.",
        "objectives": ["increase_self-confidence", "enhance_focus", "reduce_negative_self-talk"]
    },
    {
        "name": "Mantra Practice",
        "description": "Repeat a mantra to promote mindfulness, spiritual connection, and focus.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Suggested mantras include: \n- 'Om' for grounding and spiritual alignment. \n- 'So Hum' (I am that) to connect with universal presence. \n- 'May I be peaceful, may I be safe, may I be free from suffering' for cultivating compassion. \n- Modern options like 'I am present' or 'I release what no longer serves me' also work well. Choose a mantra that resonates with your spiritual or meditative goals.",
        "benefit_synopsis": "Supports mindfulness, strengthens spiritual alignment, and calms the mind.",
        "objectives": ["enhance_spiritual_connection", "reduce_stress", "improve_focus"]
    },
    {
        "name": "Self-Affirmation Practice",
        "description": "Repeat positive affirmations to reinforce self-worth, focus, and confidence.",
        "recommended_durations": [
            {"duration_label": "5 minutes"},
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Suggested affirmations include: \n- 'I am enough.' \n- 'I am strong, resilient, and capable.' \n- 'I choose progress over perfection.' \n- 'I am safe and grounded in this moment.' \n- 'I release the need to control what I cannot change.' \n- 'I deserve rest and balance in my life.' Research shows affirmations work best when they align with personal values and goals, so adapt these as needed.",
        "benefit_synopsis": "Boosts self-worth, strengthens resilience, and promotes goal alignment.",
        "objectives": ["increase_self-confidence", "reduce_negative_self-talk", "promote_goal_alignment"]
    }
],

'Cold Exposure': [
    {
        "name": "Cold Shower",
        "description": "Take a cold shower to invigorate the body and improve circulation.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Gradually lower the temperature over time to build cold tolerance. Focus on deep breathing to manage discomfort.",
        "benefit_synopsis": "Boosts circulation, improves stress resilience, and enhances emotional regulation.",
        "objectives": ["increase_stress_resilience", "improve_emotional_regulation", "enhance_mood_stability"]
    },
    {
        "name": "Cold Face Rinse",
        "description": "Splash cold water on your face to awaken your senses and reduce puffiness.",
        "recommended_durations": [{"duration_label": "1 minute"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 4,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Ideal as a morning refresher or a quick midday reset. Helps reduce facial puffiness and stimulate circulation.",
        "benefit_synopsis": "Enhances alertness, soothes inflammation, and supports emotional regulation.",
        "objectives": ["increase_alertness", "improve_emotional_regulation", "reduce_inflammation"]
    },
    {
        "name": "Cold Plunge",
        "description": "Immerse yourself in cold water to boost circulation and mental toughness.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 5,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Cold plunges require gradual adaptation. Begin with short immersions and focus on steady breathing to maximize benefits.",
        "benefit_synopsis": "Strengthens stress resilience, reduces inflammation, and enhances mood stability.",
        "objectives": ["increase_stress_resilience", "reduce_inflammation", "enhance_mood_stability"]
    }
],

'Focused Value Time': [
    {
        "name": "Deep Work Session",
        "description": "Dedicate time to focused, undistracted work on a high-value task.",
        "recommended_durations": [
            {"duration_label": "20 minutes"},
            {"duration_label": "30 minutes"},
            {"duration_label": "45 minutes"},
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Eliminate distractions by using techniques like the Pomodoro method or setting clear work intervals.",
        "benefit_synopsis": "Maximizes productivity, improves concentration, and reduces cognitive overload.",
        "objectives": ["increase_productivity", "enhance_focus", "reduce_stress"]
    },
    {
        "name": "Value Alignment Journaling",
        "description": "Reflect on your goals and values to ensure alignment with your actions.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Three times daily",
        "is_common": True,
        "notes": "Use prompts like 'What actions today align with my values?' or 'What small steps move me toward my larger goals?'",
        "benefit_synopsis": "Enhances clarity, strengthens motivation, and deepens self-awareness.",
        "objectives": ["clarity", "increase_self-awareness", "enhance_motivation"]
    }
],

'Skill Learning': [
    {
        "name": "Language Practice",
        "description": "Practice a new language using an app or flashcards.",
        "recommended_durations": [{"duration_label": "20 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Use spaced repetition and active recall methods to improve retention.",
        "benefit_synopsis": "Improves cognitive resilience, boosts memory, and enhances problem-solving skills.",
        "objectives": ["improve_language_skills", "enhance_memory", "develop_cognitive_resilience"]
    },
    {
        "name": "Instrument Practice",
        "description": "Learn or practice a musical instrument to enhance coordination and memory.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Three times daily",
        "is_common": True,
        "notes": "Structured practice with scales, chord progressions, and songs will accelerate skill development.",
        "benefit_synopsis": "Enhances coordination, strengthens memory, and fosters creative thinking.",
        "objectives": ["improve_coordination", "enhance_creative_thinking", "reduce_stress"]
    }
],

'Creative Flow Time': [
    {
        "name": "Free Writing", 
        "description": "Spend time writing whatever comes to mind to unleash creativity.", 
        "recommended_durations": [{"duration_label": "30 minutes"}], 
        "impact_rating_id": 5, 
        "difficulty_level_id": 3,
        "frequency": "Daily",  
        "is_common": True,
        "benefit_synopsis": "Free writing helps overcome creative blocks, improve language skills, and reduce stress by encouraging uninhibited self-expression.",
        "objectives": ["enhance_creative_thinking", "improve_language_skills", "reduce_stress"]
    },
    {
        "name": "Sketching", 
        "description": "Draw or doodle to foster creative expression and mindfulness.", 
        "recommended_durations": [{"duration_label": "20 minutes"}], 
        "impact_rating_id": 4, 
        "difficulty_level_id": 3,
        "frequency": "Twice daily",  
        "is_common": True,
        "benefit_synopsis": "Sketching strengthens visual thinking, improves focus, and promotes relaxation by engaging the mind in a non-verbal creative process.",
        "objectives": ["develop_artistic_skills", "enhance_pattern_recognition", "reduce_stress"]
    }
],

"Self Development & Skills": [
    {
        "name": "Language Practice",
        "description": "Practice a new language using an app, flashcards, or conversational exercises.",
        "recommended_durations": [
            {"duration_label": "20 minutes"},
            {"duration_label": "30 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Learning a new language enhances cognitive flexibility, improves memory retention, and strengthens cultural awareness.",
        "objectives": ["improve_language_skills", "enhance_memory", "develop_cognitive_resilience"]
    },
    {
        "name": "Instrument Practice",
        "description": "Learn or practice a musical instrument to improve coordination, creativity, and memory.",
        "recommended_durations": [
            {"duration_label": "20 minutes"},
            {"duration_label": "30 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Playing an instrument strengthens neural connections, enhances creativity, and improves fine motor coordination.",
        "objectives": ["improve_coordination", "enhance_creative_thinking", "reduce_stress"]
    },
    {
        "name": "Reading",
        "description": "Read a book, an article, or educational material on a topic of interest/desired proficiency.",
        "recommended_durations": [
            {"duration_label": "15 minutes"},
            {"duration_label": "30 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Reading enhances knowledge retention, sharpens focus, and promotes relaxation by immersing the mind in structured thought.",
        "objectives": ["improve_knowledge", "enhance_focus", "promote_relaxation"]
    },
    {
        "name": "Creative Writing",
        "description": "Engage in creative writing, such as poetry, short stories, or journaling, to enhance creativity and emotional expression.",
        "recommended_durations": [
            {"duration_label": "20 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": False,
        "benefit_synopsis": "Creative writing strengthens imaginative thinking, aids emotional processing, and enhances storytelling abilities.",
        "objectives": ["enhance_creative_thinking", "reduce_stress", "improve_emotional_resilience"]
    },
    {
        "name": "Coding Practice",
        "description": "Practice coding or learn a new programming language to build problem-solving skills.",
        "recommended_durations": [
            {"duration_label": "30 minutes"},
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Coding enhances logical thinking, problem-solving skills, and computational creativity, providing a valuable technical skill set.",
        "objectives": ["develop_problem_solving", "enhance_focus", "improve_technical_skills"]
    },
    {
        "name": "Public Speaking Practice",
        "description": "Practice speaking skills to build confidence and communication abilities.",
        "recommended_durations": [
            {"duration_label": "15 minutes"},
            {"duration_label": "30 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": False,
        "benefit_synopsis": "Public speaking practice improves articulation, boosts confidence, and enhances persuasion and leadership skills.",
        "objectives": ["improve_communication", "increase_self-confidence", "reduce_speaking_anxiety"]
    },
    {
        "name": "Problem-Solving Puzzles",
        "description": "Solve puzzles such as crosswords, Sudoku, or logic games to improve cognitive function.",
        "recommended_durations": [
            {"duration_label": "15 minutes"}
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Engaging in puzzles strengthens problem-solving abilities, enhances pattern recognition, and keeps the mind sharp.",
        "objectives": ["enhance_memory", "develop_cognitive_resilience", "improve_problem_solving"]
    },
    {
        "name": "DIY Projects",
        "description": "Work on do-it-yourself projects to build creativity and practical skills.",
        "recommended_durations": [
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "DIY projects foster self-reliance, problem-solving skills, and hands-on creativity through practical engagement.",
        "objectives": ["enhance_creative_thinking", "improve_problem_solving", "increase_self-confidence"]
    },
    {
        "name": "Networking",
        "description": "Engage with industry professionals to exchange ideas and opportunities.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Networking broadens career opportunities, enhances communication skills, and builds professional relationships for future growth.",
        "objectives": ["build_professional_network", "gain_new_opportunities", "enhance_communication_skills"]
    },
    {
        "name": "Time Management Practice",
        "description": "Develop better time management habits using tools like planners or time-blocking techniques.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Practicing time management increases productivity, reduces stress, and creates a balanced, structured daily routine.",
        "objectives": ["increase_productivity", "reduce_stress", "enhance_focus"]
    },
    {
        "name": "Cooking or Baking",
        "description": "Experiment with new recipes or techniques to improve culinary skills.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Cooking promotes creativity, mindfulness, and practical self-sufficiency, making it a rewarding and stress-reducing activity.",
        "objectives": ["enhance_creative_thinking", "develop_practical_skills", "reduce_stress"]
    },
    {
        "name": "Art Practice",
        "description": "Engage in drawing, painting, or other artistic practices to enhance creativity and mindfulness.",
        "recommended_durations": [{"duration_label": "20 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Art practice encourages self-expression, improves focus, and reduces stress through creative engagement.",
        "objectives": ["enhance_creative_thinking", "reduce_stress", "promote_mindfulness"]
    },
    {
        "name": "Debate Practice",
        "description": "Engage in friendly debates to improve critical thinking and communication skills.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": False,
        "benefit_synopsis": "Debate practice strengthens logical reasoning, improves articulation, and boosts confidence in public speaking.",
        "objectives": ["improve_communication", "enhance_critical_thinking", "increase_self-confidence"]
    },
    {
        "name": "Gardening",
        "description": "Spend time gardening to connect with nature and build patience and responsibility.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Gardening promotes relaxation, enhances mindfulness, and provides physical activity through nature engagement.",
        "objectives": ["enhance_mood_stability", "promote_mindfulness", "increase_self-confidence"]
    },
    {
        "name": "Career Skill Practice",
        "description": "Dedicate time to learning or improving a career-specific skill, such as coding, data analysis, or public speaking.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Practicing career skills increases job competency, enhances confidence, and opens opportunities for growth.",
        "objectives": ["improve_professional_skills", "increase_confidence", "enhance_career_progression"]
    },
    {
        "name": "Certification Preparation",
        "description": "Study for a professional certification, such as PMP, CPA, or AWS.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Preparing for certifications enhances professional credibility, increases knowledge, and boosts career advancement.",
        "objectives": ["gain_certification", "enhance_professional_skills", "increase_career_opportunities"]
    },
    {
        "name": "Resume/CV Update",
        "description": "Review and update your professional profile to reflect recent accomplishments.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Keeping a resume updated ensures readiness for career opportunities and highlights professional growth.",
        "objectives": ["increase_hiring_chances", "enhance_career_progression", "develop_self-confidence"]
    },
    {
        "name": "Photography Session",
        "description": "Learn photography techniques or practice taking and editing photos.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Photography enhances creativity, sharpens attention to detail, and provides a mindful artistic outlet.",
        "objectives": ["enhance_creative_skills", "develop_attention_to_detail", "reduce_stress"]
    },
    {
        "name": "Acting or Improv",
        "description": "Participate in acting classes or improvisation workshops to improve self-expression and confidence.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "90 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": False,
        "benefit_synopsis": "Acting and improv improve emotional expression, adaptability, and confidence in social interactions.",
        "objectives": ["increase_self-confidence", "enhance_creative_expression", "develop_public_speaking_skills"]
    },
    {
        "name": "Conflict Resolution Training",
        "description": "Learn and practice techniques for managing interpersonal conflicts constructively.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": False,
        "benefit_synopsis": "Conflict resolution training enhances communication skills, emotional resilience, and relationship management.",
        "objectives": ["enhance_emotional_resilience", "improve_communication_skills", "reduce_interpersonal_tension"]
    },
    {
        "name": "Time Management Practice",
        "description": "Develop better time management habits using tools like planners or time-blocking techniques.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Effective time management reduces stress, increases productivity, and creates structured daily routines.",
        "objectives": ["increase_productivity", "reduce_stress", "enhance_focus"]
    },
    {
        "name": "Engineering Project",
        "description": "Work on a small-scale engineering project, such as building a robot or a functional model.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Weekly",
        "is_common": False,
        "benefit_synopsis": "Engineering projects develop problem-solving skills, enhance creativity, and improve technical knowledge.",
        "objectives": ["develop_problem_solving", "enhance_creative_thinking", "improve_technical_skills"]
    },
    {
        "name": "AI/ML Training",
        "description": "Dive into artificial intelligence or machine learning concepts and tools.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Weekly",
        "is_common": False,
        "benefit_synopsis": "AI/ML training enhances problem-solving abilities, career growth, and technical expertise in an evolving field.",
        "objectives": ["enhance_career_skills", "develop_problem_solving", "increase_knowledge"]
    },
    {
        "name": "First Aid Training",
        "description": "Learn or refresh basic first aid and CPR skills.",
        "recommended_durations": [{"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Annually",
        "is_common": False,
        "benefit_synopsis": "First aid training prepares individuals to respond effectively in emergencies, potentially saving lives.",
        "objectives": ["enhance_safety_awareness", "increase_confidence", "reduce_emergency_risk"]
    },
    {
        "name": "Esports Practice",
        "description": "Dedicate time to improving competitive gaming skills for esports or tournaments.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Esports practice enhances strategic thinking, reaction time, and teamwork in a competitive setting.",
        "objectives": ["develop_strategic_thinking", "improve_reaction_time", "enhance_teamwork"]
    }
],

'Social Connection': [
    {
        "name": "Networking Events",
        "description": "Attend professional or casual networking events to build connections and expand opportunities.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Networking enhances career opportunities, builds confidence, and strengthens professional relationships.",
        "objectives": ["expand_professional_network", "improve_communication_skills", "increase_opportunities"]
    },
    {
        "name": "Random Acts of Kindness",
        "description": "Perform small acts of kindness, such as paying for a stranger’s coffee or leaving a positive note.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Acts of kindness foster social connection, improve mood, and create a ripple effect of positivity.",
        "objectives": ["enhance_emotional_resilience", "promote_community_engagement", "increase_happiness"]
    },
    {
        "name": "Pen Pal or Letter Writing",
        "description": "Write a letter or email to a friend, family member, or pen pal to deepen connections.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Letter writing enhances emotional expression, strengthens relationships, and fosters mindfulness.",
        "objectives": ["improve_relationships", "develop_patience", "enhance_written_communication"]
    },
    {
        "name": "Community Meetups",
        "description": "Attend local meetups or events centered around shared interests or causes.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Community meetups provide social engagement, networking, and opportunities for shared learning.",
        "objectives": ["develop_common_interests", "enhance_social_skills", "increase_community_involvement"]
    },
    {
        "name": "Mentorship",
        "description": "Offer or seek mentorship in personal or professional growth areas.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Mentorship strengthens leadership skills, provides guidance, and fosters career and personal growth.",
        "objectives": ["develop_leadership", "enhance_professional_growth", "build_support_networks"]
    },
    {
        "name": "Cultural Exchange",
        "description": "Engage in cultural activities, such as learning a new language with a partner or attending cultural events.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Cultural exchanges foster global awareness, strengthen empathy, and broaden perspectives.",
        "objectives": ["increase_cultural_awareness", "develop_empathy", "enhance_social_connection"]
    },
    {
        "name": "Team Sports",
        "description": "Join a recreational sports team to build camaraderie and stay active.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "90 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Team sports enhance teamwork, boost physical fitness, and create lasting friendships.",
        "objectives": ["develop_teamwork", "increase_fitness", "enhance_relationships"]
    },
    {
        "name": "Friendship Maintenance Day",
        "description": "Dedicate a day each month to checking in with friends and nurturing relationships.",
        "recommended_durations": [{"duration_label": "2 hours"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Regularly maintaining friendships strengthens connections, provides emotional support, and enhances well-being.",
        "objectives": ["enhance_relationships", "reduce_social_isolation", "promote_emotional_resilience"]
    },
    {
        "name": "Social Media Detox & In-Person Socializing",
        "description": "Reduce screen time and focus on face-to-face interactions with friends and family.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "Half day"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Reducing digital distractions fosters meaningful in-person connections and improves mental clarity.",
        "objectives": ["enhance_social_connection", "reduce_screen_time", "improve_relationships"]
    },
    {
        "name": "Hosting Gatherings",
        "description": "Host a casual gathering, such as a potluck or themed night, to bring people together.",
        "recommended_durations": [{"duration_label": "2 hours"}, {"duration_label": "3 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Hosting gatherings strengthens social bonds, fosters community, and promotes inclusivity.",
        "objectives": ["enhance_relationships", "develop_social_skills", "increase_community_engagement"]
    },
    {
        "name": "Walk and Talk",
        "description": "Go for a walk with a friend, partner, or colleague to connect while staying active.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Walking and talking encourage open communication, reduce stress, and support healthy relationships.",
        "objectives": ["enhance_relationships", "reduce_stress", "promote_healthy_lifestyles"]
    },
    {
        "name": "Board Game Café Outing",
        "description": "Visit a board game café or host a similar social activity to enjoy strategic and cooperative play.",
        "recommended_durations": [{"duration_label": "2 hours"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Playing board games together enhances critical thinking, teamwork, and social bonding.",
        "objectives": ["develop_teamwork", "enhance_problem_solving", "strengthen_social_bonds"]
    },
    {
        "name": "Virtual Game Night",
        "description": "Host or participate in an online game night to maintain social bonds despite distance.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Monthly",
        "is_common": True,
        "benefit_synopsis": "Virtual game nights allow remote social engagement, fostering connection and fun across distances.",
        "objectives": ["enhance_relationships", "reduce_feelings_of_isolation", "improve_social_interaction"]
    },
    {
        "name": "Family Game Night",
        "description": "Spend quality time playing games with family members to bond and create shared experiences.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Engaging in playful activities strengthens family relationships, reduces stress, and fosters teamwork.",
        "objectives": ["strengthen_family_bonds", "develop_teamwork", "enhance_social_connection"]
    }
],

'Productivity Anchors': [
    {
      "name": "Daily Prioritization",
      "description": "Begin the day by identifying the three most important tasks to focus on.",
      "recommended_durations": [
        { "duration_label": "5 minutes" },
        { "duration_label": "10 minutes" }
      ],
      "impact_rating_id": 5,
      "difficulty_level_id": 1,
      "frequency": "Daily",
      "is_common": True,
      "benefit_synopsis": "Setting daily priorities provides clarity, reduces overwhelm, and boosts productivity by focusing on what truly matters.",
      "objectives": ["enhance_focus", "reduce_cognitive_load", "increase_productivity"]
    },
    {
        "name": "Midday Reset",
        "description": "Take a short break in the middle of the day to recharge and refocus.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "A midday reset prevents mental fatigue, boosts energy, and enhances focus for the remainder of the day.",
        "objectives": ["reduce_mental_fatigue", "enhance_focus", "increase_productivity"]
    },
    {
        "name": "Accountability Partner Check-In",
        "description": "Regularly check in with an accountability partner to review progress and stay on track.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Regular check-ins provide motivation, reinforce commitment, and create external accountability for goals.",
        "objectives": ["increase_motivation", "enhance_goal_tracking", "reduce_procrastination"]
    },
    {
        "name": "Single-Tasking",
        "description": "Focus on one task at a time to improve efficiency and reduce mental overload.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Single-tasking improves concentration, reduces cognitive fatigue, and increases overall efficiency.",
        "objectives": ["enhance_focus", "increase_efficiency", "reduce_cognitive_overload"]
    },
    {
        "name": "Distraction-Free Work Zone",
        "description": "Set up a dedicated workspace free from interruptions to enhance focus.",
        "recommended_durations": [{"duration_label": "Throughout work sessions"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "A distraction-free workspace minimizes interruptions, allowing for deeper concentration and increased productivity.",
        "objectives": ["enhance_focus", "increase_efficiency", "reduce_context_switching"]
    },
    {
        "name": "Pre-Work Ritual",
        "description": "Establish a consistent routine before starting work to set the tone for productivity.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "A structured pre-work ritual helps transition into focused work mode and builds consistency.",
        "objectives": ["enhance_focus", "increase_productivity", "reduce_procrastination"]
    },
    {
        "name": "Inbox Zero",
        "description": "Process emails efficiently and clear your inbox regularly to maintain organization.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "A decluttered inbox reduces cognitive load, improves responsiveness, and prevents email overload.",
        "objectives": ["enhance_organization", "reduce_information_overload", "increase_efficiency"]
    },
    {
        "name": "Decision Fatigue Reduction",
        "description": "Limit daily decisions by planning ahead and creating routines.",
        "recommended_durations": [{"duration_label": "10 minutes (planning)"}, {"duration_label": "Throughout the day"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Reducing decision fatigue preserves mental energy for high-priority tasks and prevents burnout.",
        "objectives": ["enhance_decision_making", "increase_efficiency", "reduce_cognitive_overload"]
    },
    {
        "name": "Sunday Reset",
        "description": "Dedicate time on Sundays to organize, plan, and prepare for the week ahead.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "A weekly reset improves time management, reduces stress, and ensures a productive start to the week.",
        "objectives": ["enhance_time_management", "reduce_overwhelm", "increase_productivity"]
    },
    {
        "name": "No Meeting Days",
        "description": "Set aside certain days with no scheduled meetings to focus on deep work.",
        "recommended_durations": [{"duration_label": "Full workday"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": False,
        "benefit_synopsis": "No-meeting days protect deep work time, reduce distractions, and enhance task completion rates.",
        "objectives": ["increase_productivity", "enhance_focus", "reduce_meeting_overload"]
    },
    {
        "name": "Work Sprint Challenge",
        "description": "Use time-bound challenges to push through work quickly and efficiently.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "benefit_synopsis": "Timed sprints build momentum, improve efficiency, and create a sense of urgency to complete tasks.",
        "objectives": ["increase_efficiency", "enhance_focus", "reduce_procrastination"]
    },
    {
        "name": "Mindful Task Transitions",
        "description": "Use a brief pause between tasks to reset and refocus.",
        "recommended_durations": [{"duration_label": "1-2 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "Transitioning mindfully between tasks prevents burnout and improves task-switching efficiency.",
        "objectives": ["reduce_mental_fatigue", "enhance_focus", "increase_productivity"]
    },
    {
        "name": "Automating Repetitive Tasks",
        "description": "Use tools and software to automate recurring or manual tasks.",
        "recommended_durations": [{"duration_label": "Ongoing"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Automation reduces time spent on repetitive work, freeing up energy for higher-priority tasks.",
        "objectives": ["increase_efficiency", "reduce_manual_workload", "enhance_time_management"]
    },
    {
        "name": "End-of-Week Reflection",
        "description": "Review the past week's successes, challenges, and areas for improvement.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "benefit_synopsis": "Reflecting on the past week enhances learning, improves planning, and increases self-awareness.",
        "objectives": ["enhance_self-awareness", "improve_time_management", "increase_motivation"]
    },
    {
        "name": "Morning Mind Dump",
        "description": "Write down all thoughts, ideas, and tasks to clear your mind before starting work.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "benefit_synopsis": "A mind dump reduces mental clutter, increases focus, and helps organize priorities for the day.",
        "objectives": ["reduce_mental_clutter", "enhance_focus", "increase_productivity"]
    }
],

'Downtime/Relaxation': [
    {
        "name": "Reading for Pleasure",
        "description": "Read a book or article for enjoyment and relaxation.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Choose genres or topics you enjoy, such as fiction, fantasy, or self-help.",
        "benefit_synopsis": "Reading for pleasure enhances relaxation, reduces stress, and improves cognitive function.",
        "objectives": ["reduce_stress", "enhance_focus", "improve_sleep_quality"]
    },
    {
        "name": "Mindful Breathing",
        "description": "Focus on deep breathing to calm the mind and body.",
        "recommended_durations": [{"duration_label": "20 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use techniques like box breathing or 4-7-8 breathing to enhance relaxation.",
        "benefit_synopsis": "Mindful breathing reduces anxiety, improves emotional regulation, and enhances overall well-being.",
        "objectives": ["reduce_anxiety", "enhance_self_awareness", "improve_emotional_regulation"]
    },
    {
        "name": "Gentle Stretching",
        "description": "Perform light stretches to release tension and relax the body.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on areas that feel tight, such as the neck, shoulders, and lower back.",
        "benefit_synopsis": "Gentle stretching improves flexibility, reduces muscle tension, and enhances relaxation.",
        "objectives": ["reduce_muscle_tension", "enhance_flexibility", "promote_relaxation"]
    },
    {
        "name": "Listening to Music",
        "description": "Play soothing or favorite music to unwind and improve mood.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Consider creating a playlist of calming songs or music that brings joy.",
        "benefit_synopsis": "Listening to music relieves stress, boosts mood, and promotes emotional well-being.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "promote_relaxation"]
    },
    {
        "name": "Nature Time",
        "description": "Spend time outdoors to relax and connect with nature.",
        "recommended_durations": [{"duration_label": "20 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Visit a park, sit under a tree, or take a leisurely walk outdoors.",
        "benefit_synopsis": "Spending time in nature reduces stress, enhances mood, and strengthens mind-body connection.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "promote_mind-body_connection"]
    },
    {
        "name": "Meditative Coloring",
        "description": "Use coloring books or sketch to relax and engage your creativity.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Focus on patterns that you find enjoyable. This activity is particularly effective for reducing stress.",
        "benefit_synopsis": "Meditative coloring improves focus, relieves stress, and fosters creative expression.",
        "objectives": ["enhance_creative_expression", "reduce_stress", "promote_mindfulness"]
    },
    {
        "name": "Guided Relaxation",
        "description": "Follow a guided relaxation or progressive muscle relaxation session.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use apps or videos to guide the session. Focus on areas where you hold tension.",
        "benefit_synopsis": "Guided relaxation helps reduce stress, improve sleep quality, and restore mental balance.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "improve_sleep_quality"]
    },
    {
        "name": "Tea or Coffee Ritual",
        "description": "Sip a warm beverage mindfully to unwind and savor the moment.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Opt for decaffeinated options in the evening to avoid disrupting sleep.",
        "benefit_synopsis": "A mindful tea or coffee ritual enhances relaxation and promotes a sense of calm.",
        "objectives": ["promote_relaxation", "enhance_mindfulness", "reduce_stress"]
    },
    {
        "name": "Soothing Bath",
        "description": "Take a warm bath to relax your muscles and mind.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Add Epsom salts or essential oils like lavender to enhance relaxation.",
        "benefit_synopsis": "A warm bath soothes sore muscles, reduces tension, and improves sleep quality.",
        "objectives": ["reduce_muscle_tension", "promote_relaxation", "enhance_mood_stability"]
    },
    {
        "name": "Watching a Comfort Show or Movie",
        "description": "Watch a favorite or feel-good show to decompress and enjoy downtime.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Choose content that makes you feel happy or relaxed. Avoid heavy or stressful shows before bed.",
        "benefit_synopsis": "Watching a comfort show provides emotional relief, reduces stress, and promotes relaxation.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "promote_relaxation"]
    },
    {
        "name": "Gratitude Practice",
        "description": "Take a few minutes to reflect on things you’re grateful for.",
        "recommended_durations": [{"duration_label": "5 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Think of specific moments or things that brought joy or comfort to your day.",
        "benefit_synopsis": "Practicing gratitude enhances mood stability, fosters positivity, and reduces stress.",
        "objectives": ["enhance_mood_stability", "reduce_stress", "promote_positivity"]
    },
    {
        "name": "Gratitude or Reflection Journaling",
        "description": "Spend time writing down things you're grateful for or reflecting on your thoughts to cultivate a positive mindset and increase self-awareness.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "10 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Consider noting three things you're grateful for or journaling about your experiences and feelings.",
        "benefit_synopsis": "Journaling encourages self-awareness, emotional regulation, and long-term mindset shifts.",
        "objectives": ["enhance_mood_stability", "increase_self_awareness", "reduce_stress"]
    }
],


'Sports': [
    {
        "name": "Structured Training Block",
        "description": "Structure dedicated training time for your sport or discipline to improve performance and achieve your athletic goals.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use this time to focus on sport-specific drills, conditioning, or skill refinement, tailored to your training objectives.",
        "benefit_synopsis": "Enhances athletic performance, builds endurance, and improves sport-specific skills.",
        "objectives": ["enhance_performance", "build_strength_and_endurance", "improve_technical_skills"]
    },
    {
        "name": "Skill Practice or Morning Mobility",
        "description": "Dedicate time in the morning to practice specific skills or engage in mobility exercises to prepare your body for peak performance.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on refining technical skills or performing mobility exercises to enhance flexibility, prevent injury, and optimize readiness for training or competition.",
        "benefit_synopsis": "Improves flexibility, reduces injury risk, and enhances readiness for training.",
        "objectives": ["improve_flexibility", "refine_technical_skills", "enhance_performance"]
    },
    {
        "name": "Performance Visualization",
        "description": "Take time to mentally rehearse your performance, focusing on executing skills, strategies, and achieving success in your sport or discipline.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Visualize yourself performing at your best, overcoming challenges, and achieving your goals to build confidence and sharpen focus.",
        "benefit_synopsis": "Boosts confidence, sharpens focus, and enhances mental resilience.",
        "objectives": ["boost_confidence", "enhance_focus", "improve_performance"]
    },
    {
        "name": "Racquetball",
        "description": "A fast-paced indoor sport that enhances agility, reflexes, and cardiovascular fitness.",
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Ensure you wear protective eyewear and warm up properly before playing.",
        "benefit_synopsis": "Improves agility, cardiovascular endurance, and hand-eye coordination.",
        "objectives": ["improve_fitness", "enhance_agility", "increase_endurance"]
    },
    {
        "name": "Pickleball",
        "description": "A paddle sport that combines elements of tennis, badminton, and ping-pong, perfect for light activity and social engagement.",
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Twice weekly",
        "is_common": True,
        "notes": "Great for all skill levels and a fun way to stay active.",
        "benefit_synopsis": "Encourages social interaction, enhances coordination, and improves cardio health.",
        "objectives": ["improve_cardio_health", "social_interaction", "boost_coordination"]
    },
    {
        "name": "Basketball",
        "description": "A dynamic team sport that builds endurance, coordination, and strategic thinking.",
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Play on a court with proper footwear to avoid injuries.",
        "benefit_synopsis": "Boosts endurance, strengthens teamwork, and develops quick decision-making skills.",
        "objectives": ["build_strength", "promote_teamwork", "enhance_endurance"]
    },
    {
        "name": "Soccer",
        "description": "A globally loved team sport that combines skill, strategy, and cardiovascular fitness.",
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Ideal for improving stamina and teamwork skills.",
        "benefit_synopsis": "Enhances endurance, improves coordination, and builds team strategy skills.",
        "objectives": ["increase_stamina", "improve_coordination", "build_team_skills"]
    },
    {
        "name": "Tennis",
        "description": "A skill-based sport that promotes cardiovascular health and strategic thinking.",
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Consider joining a local tennis club for regular practice.",
        "benefit_synopsis": "Enhances agility, cardiovascular fitness, and strategic planning.",
        "objectives": ["improve_fitness", "develop_strategy", "enhance_agility"]
    },
    {
        "name": "Surfing",
        "description": "A water sport that combines balance, strength, and agility on waves.",
        "recommended_durations": [{"duration_label": "60 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 4,
        "frequency": "Monthly",
        "is_common": True,
        "notes": "Excellent for building core strength and balance.",
        "benefit_synopsis": "Improves balance, strengthens the core, and enhances focus.",
        "objectives": ["improve_balance", "build_core_strength", "enhance_focus"]
    },
    {
        "name": "Bowling",
        "description": "An enjoyable indoor activity that develops hand-eye coordination and social connections.",
        "recommended_durations": [{"duration_label": "90 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Occasional",
        "is_common": True,
        "notes": "Great for all skill levels and ages, often paired with social outings.",
        "benefit_synopsis": "Enhances coordination, fosters social bonding, and provides recreational enjoyment.",
        "objectives": ["promote_social_interaction", "improve_hand_eye_coordination", "provide_recreational_fun"]
    },
    {
        "name": "Lacrosse",
        "description": "A fast-paced team sport combining elements of basketball, soccer, and hockey.",
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Requires good hand-eye coordination and stamina.",
        "benefit_synopsis": "Improves coordination, builds endurance, and enhances teamwork.",
        "objectives": ["enhance_coordination", "promote_teamwork", "increase_endurance"]
    },
    {
        "name": "Table Tennis",
        "description": "A quick-paced indoor game that enhances reflexes and precision.",
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "A great way to enjoy light exercise and improve focus.",
        "benefit_synopsis": "Boosts reflexes, enhances hand-eye coordination, and sharpens focus.",
        "objectives": ["improve_reflexes", "enhance_precision", "boost_focus"]
    },
    {
        "name": "Golf",
        "description": "A relaxing sport that combines precision, focus, and moderate physical activity.",
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": True,
        "notes": "A good walk on a course can also improve mental clarity.",
        "benefit_synopsis": "Improves focus, enhances precision, and promotes relaxation.",
        "objectives": ["improve_focus", "enhance_precision", "promote_relaxation"]
    }
  ]
}
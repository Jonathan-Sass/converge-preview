"""
practice_data: dict
A structured dictionary of practices, organized by categories(e.g. "mind-body-reset") and subcategories(e.g. "cold-exposure").
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


practice_data = {

  # PRACTICE CATEGORY
  "mind-body-reset": {
    
    # PRACTICE SUBCATEGORY
    "digital-boundaries": [
      {
        "name": "Digital Detox",
        "slug": "digital-detox",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Unplug from non-essential digital devices for an extended period.",
        "benefit_synopsis": "Resets attention, reduces screen fatigue, and enhances real-world engagement.",
        "recommended_durations": [
          { "duration_label": "3 hours" },
          { "duration_label": "24 hours" },
          { "duration_label": "1 week" },
          { "duration_label": "1 month" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Monthly or as needed",
        "is_common": False,
        "notes": "Pick a window—from an afternoon to a full weekend or longer—where you completely step away from social media, email, and streaming. Use the time for offline hobbies, nature, or deep rest.",
        "objectives": ["reset_attention", "reduce_screen_fatigue", "boost_presence"]
      },
      {
        "name": "Phone-Free Block",
        "slug": "phone-free-block",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Designated time window to be completely free of phone use.",
        "benefit_synopsis": "Creates mental space and reduces habitual phone checking.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "1 hour" },
          { "duration_label": "90 minutes" },
          { "duration_label": "2 hours" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Pick a consistent time—like during meals, creative work, or before bed—and physically distance yourself from your phone or use Do Not Disturb mode.",
        "objectives": ["reduce_digital_dependency", "increase_presence", "enhance_wellbeing"]
      },
      {
        "name": "Tech-Free Morning",
        "slug": "tech-free-morning",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Start your morning mindfully without your phone or other devices to distract you.",
        "benefit_synopsis": "Cultivates a calm, focused start and prevents reactive scrolling.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" },
          { "duration_label": "1 hour" },
          { "duration_label": "2 hours" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Store your phone in another room or on airplane mode, and use that time for hydration, movement, or planning instead of digital distractions.",
        "objectives": ["boost_focus", "reduce_morning_anxiety", "establish_intentional_start"]
      },
      {
        "name": "No Screen Evenings",
        "slug": "no-screen-evenings",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Power down all screens at least 2 hours before bedtime.",
        "benefit_synopsis": "Improves sleep quality by reducing blue light exposure and mental stimulation.",
        "recommended_durations": [
          { "duration_label": "2 hours" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Create a no-screen ritual: read, journal, or practice light stretching instead of watching or scrolling.",
        "objectives": ["improve_sleep_quality", "reduce_blue_light", "enhance_relaxation"]
      },
      {
        "name": "Screen Break",
        "slug": "screen-break",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Step away from your screen at regular intervals throughout the day.",
        "benefit_synopsis": "Prevents eye strain and cognitive fatigue while supporting sustained focus.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "3 hours" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use a timer or break-reminder tool to take short walks, stretch, or rest your eyes at least every hour—up to a longer midday pause.",
        "objectives": ["prevent_eye_strain", "maintain_focus", "reduce_fatigue"]
      },
      {
        "name": "App Limits",
        "slug": "app-limits",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Set daily time caps on the apps you find most distracting.",
        "benefit_synopsis": "Helps curb compulsive checking and improves overall time management.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" },
          { "duration_label": "1 hour" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Use built-in screen-time settings or a digital-wellness app to impose limits on apps like social media, news, or games.",
        "objectives": ["reduce_compulsive_use", "improve_time_management", "enhance_self_control"]
      },
      {
        "name": "Social Media Limit",
        "slug": "social-media-limit",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Restrict total daily time spent on social platforms.",
        "benefit_synopsis": "Reduces comparison stress and frees up time for meaningful activities.",
        "recommended_durations": [
          { "duration_label": "As configured" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Set a firm daily allowance for social apps using your device’s settings or a dedicated app, and honor that boundary.",
        "objectives": ["reduce_comparison_stress", "free_time_for_productivity", "enhance_wellbeing"]
      },
      {
        "name": "Screen Time Limit",
        "slug": "screen-time-limit",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Setting daily boundaries on non-essential screen time to reduce excessive device use.",
        "benefit_synopsis": "Lessens digital overstimulation to improve focus and wellbeing.",
        "recommended_durations": [
          { "duration_label": "2 hours (non-work) per day" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Use screen-time settings or apps to enforce your limit. For example, set a digital curfew in the evening to help your mind unwind.",
        "objectives": ["reduce_overstimulation", "improve_focus", "enhance_wellbeing"]
      },
      {
        "name": "News Limit",
        "slug": "news-limit",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Establishing boundaries for daily news consumption to avoid constant updates and emotional overload.",
        "benefit_synopsis": "Reduces stress and anxiety from news overload.",
        "recommended_durations": [
          { "duration_label": "15 minutes twice a day" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Disable push notifications from news apps to avoid constant interruptions. Stick to checking updates at set times. Avoid doomscrolling, especially if news makes you anxious.",
        "objectives": ["reduce_overstimulation", "improve_focus", "enhance_wellbeing"]
      },
      {
        "name": "Doomscroll Break Reminder",
        "slug": "doomscroll-break-reminder",
        "category": "mind-body-reset",
        "subcategory": "digital-boundaries",
        "description": "Set a recurring reminder or timer to interrupt compulsive doomscrolling sessions and prompt a conscious reset.",
        "benefit_synopsis": "Helps break scrolling loops, reduce stress, and promote intentional tech use.",
        "recommended_durations": [
          { "duration_label": "15 minutes" },
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Use a timer, scheduled alarm, or app-based nudge to remind yourself to pause, close the app, and redirect your attention. Great paired with a quick reset activity like breathwork or movement.",
        "objectives": [
          "interrupt_doomscrolling",
          "boost_self_awareness",
          "reduce_screen_stress"
        ]
      }

    ],

    # PRACTICE SUBCATEGORY
    "am-hydration": [
      {
        "name": "Morning Hydration",
        "slug": "morning-hydration",
        "category": "mind-body-reset",
        "subcategory": "am-hydration",
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
        "slug": "sole-hydration",
        "category": "mind-body-reset",
        "subcategory": "am-hydration",
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
        "slug": "lemon-water",
        "category": "mind-body-reset",
        "subcategory": "am-hydration",
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
      }
    ],

    # PRACTICE SUBCATEGORY
    "morning-sun": [
      {
        "name": "Sunrise Beverage",
        "slug": "sunrise-beverage",
        "category": "mind-body-reset",
        "subcategory": "morning-sun",
        "description": "Enjoy a beverage of your choice outdoors to pair your morning beverage with natural light exposure.",
        "benefit_synopsis": "Early-morning light entrains your circadian clock via retinal photoreceptors, while caffeine triggers norepinephrine release for improved alertness and mood regulation.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" },
          { "duration_label": "3 minutes" },
          { "duration_label": "5 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Sipping coffee outside activates the suprachiasmatic nucleus to sync your sleep–wake cycle and ramps up cortical arousal, supporting a smooth transition into the day.",
        "objectives": [
          "regulate_circadian_rhythm",
          "boost_alertness",
          "enhance_mood"
        ]
      },
      {
        "name": "Sun Walk",
        "slug": "sun-walk",
        "category": "mind-body-reset",
        "subcategory": "morning-sun",
        "description": "Take a brisk walk outdoors during sunrise to combine moderate aerobic activity with natural light intake.",
        "benefit_synopsis": "Sunlight-driven serotonin release plus elevated heart rate enhances blood flow, reinforces circadian alignment, and supports cognitive performance.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" },
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Walking in early light boosts endorphins, strengthens vascular function, and entrains your internal clock for better sleep quality and daytime focus.",
        "objectives": [
          "boost_serotonin",
          "improve_circulation",
          "regulate_circadian_rhythm"
        ]
      },
      {
        "name": "Sun Run",
        "slug": "sun-run",
        "category": "mind-body-reset",
        "subcategory": "morning-sun",
        "description": "Go for a light jog or run during sunrise to combine aerobic activation with full-spectrum natural light.",
        "benefit_synopsis": "Boosts mood, metabolic function, and mental clarity through sun-driven hormone activation and cardiovascular engagement.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily or 2–4 times per week",
        "is_common": True,
        "notes": "A sunrise run supports dopamine and cortisol rhythms, energizes your system, and improves sleep-wake timing when done consistently.",
        "objectives": [
          "boost_mood",
          "increase_cardiovascular_output",
          "entrain_circadian_clock"
        ]
      },
      {
        "name": "Sunrise Exercise",
        "slug": "sunrise-exercise",
        "category": "mind-body-reset",
        "subcategory": "morning-sun",
        "description": "Perform light to moderate exercise outdoors at sunrise to blend physical activation with photic stimulation.",
        "benefit_synopsis": "Morning light suppresses melatonin as exercise-induced BDNF and endorphins elevate energy, enhance neuroplasticity, and stabilize mood.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Exercising in sunrise light amplifies the cortisol awakening response, increases brain-derived neurotrophic factor, and supports metabolic health.",
        "objectives": [
          "increase_bdnf",
          "enhance_cognitive_function",
          "stabilize_mood"
        ]
      },
      {
        "name": "Sunrise Stretch",
        "slug": "sunrise-stretch",
        "category": "mind-body-reset",
        "subcategory": "morning-sun",
        "description": "Perform gentle stretches or yoga poses outdoors at sunrise to lengthen muscles while absorbing natural light.",
        "benefit_synopsis": "Combines proprioceptive muscle activation with photic input to reduce stiffness, enhance parasympathetic tone, and set your circadian rhythm.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Morning stretching in natural light increases flexibility, promotes vagal activation for stress reduction, and signals your brain that it’s time to wake up.",
        "objectives": [
          "enhance_flexibility",
          "increase_vagal_tone",
          "regulate_circadian_rhythm"
        ]
      }
    ],

    # PRACTICE SUBCATEGORY
    "cold-exposure": [
      {
        "name": "Cold Exposure",
        "slug": "cold-exposure",
        "category": "mind-body-reset",
        "subcategory": "cold-exposure",
        "description": "Any version of cold exposure for a short, energizing reset.",
        "benefit_synopsis": "Activates the diving reflex to calm your nervous system and boost alertness.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": True,
        "notes": "Cold water on the face stimulates the vagus nerve and triggers the mammalian diving reflex, helping slow your heart rate and regulate stress.",
        "objectives": [
          "reset_nervous_system",
          "increase_alertness",
          "boost stress resilience",
          "stimulate_vagus_nerve"
        ]
      },
      {
        "name": "Cold Face Rinse",
        "slug": "cold-face-rinse",
        "category": "mind-body-reset",
        "subcategory": "cold-exposure",
        "description": "Splash cold water on your face for a short, energizing reset.",
        "benefit_synopsis": "Activates the diving reflex to calm your nervous system and boost alertness.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Optional daily",
        "is_common": True,
        "notes": "Cold water on the face stimulates the vagus nerve and triggers the mammalian diving reflex, helping slow your heart rate and regulate stress.",
        "objectives": [
          "reset_nervous_system",
          "increase_alertness",
          "stimulate_vagus_nerve"
        ]
      },
      {
        "name": "Cold Hand Wash or Dip",
        "slug": "cold-hand-wash-or-dip",
        "category": "mind-body-reset",
        "subcategory": "cold-exposure",
        "description": "Dip your hands or wrists into cold water to stimulate a quick reset.",
        "benefit_synopsis": "Rapidly cools the body and stimulates parasympathetic calm.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "3 minutes" }
        ],
        "impact_rating_id": 2,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": False,
        "notes": "A low-barrier practice for people not ready for full cold exposure. Activates thermoreceptors and initiates vagal stimulation.",
        "objectives": [
          "cool_down",
          "reduce_overwhelm",
          "promote_regulation"
        ]
      },
      {
        "name": "Cold Shower",
        "slug": "cold-shower",
        "category": "mind-body-reset",
        "subcategory": "cold-exposure",
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
        "slug": "cold-shower-finisher",
        "category": "mind-body-reset",
        "subcategory": "cold-exposure",
        "description": "Finish your shower with 30–60 seconds of cold water.",
        "benefit_synopsis": "Boosts energy, improves circulation, and builds mental toughness.",
        "recommended_durations": [
          { "duration_label": "30 seconds" },
          { "duration_label": "1 minute" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily or every other day",
        "is_common": True,
        "notes": "Cold showers may increase dopamine, enhance circulation, and help train stress resilience — all with minimal time commitment.",
        "objectives": [
          "boost_energy_levels",
          "enhance_resilience",
          "increase_alertness"
        ]
      },
      {
        "name": "Cold Plunge or Ice Bath",
        "slug": "cold-plunge",
        "category": "mind-body-reset",
        "subcategory": "cold-exposure",
        "description": "Submerge your body in cold water up to your neck for a short time.",
        "benefit_synopsis": "Reduces inflammation, boosts mood, and sharpens focus.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "3 minutes" },
          { "duration_label": "5 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–4 times per week",
        "is_common": False,
        "notes": "Cold immersion increases norepinephrine and dopamine, improves mood, and reduces post-exercise soreness. May enhance long-term resilience and mental clarity.",
        "objectives": [
          "reduce_inflammation",
          "improve_mood",
          "build_mental_toughness"
        ]
      },
      {
        "name": "Cold Water Face Immersion",
        "slug": "cold-water-face-immersion",
        "category": "mind-body-reset",
        "subcategory": "cold-exposure",
        "description": "Dunk your face in a bowl of ice water to quickly reset your system.",
        "benefit_synopsis": "Activates the diving reflex and shifts your body into a calm state.",
        "recommended_durations": [
          { "duration_label": "15 seconds" },
          { "duration_label": "30 seconds" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Used in some therapeutic settings for acute anxiety or panic. Lowers heart rate and rapidly soothes the nervous system.",
        "objectives": [
          "interrupt_panic_cycle",
          "soothe_nervous_system",
          "regulate_breathing"
        ]
      }
    ],
    
    # PRACTICE SUBCATEGORY
    "breath-reset": [
      {
        "name": "Box Breathing",
        "slug": "box-breathing",
        "category": "mind-body-reset",
        "subcategory": "breath-reset",
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
        "slug": "4-7-8-breathing",
        "category": "mind-body-reset",
        "subcategory": "breath-reset",
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
        "slug": "coherent-breathing",
        "category": "mind-body-reset",
        "subcategory": "breath-reset",
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
        "slug": "physiological-sigh",
        "category": "mind-body-reset",
        "subcategory": "breath-reset",
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
        "slug": "extended-exhale-breathing",
        "category": "mind-body-reset",
        "subcategory": "breath-reset",
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
    "somatic-awareness-reset": [
      {
        "name": "5-4-3-2-1 Check-In",
        "slug": "5-4-3-2-1-check-in",
        "category": "mind-body-reset",
        "subcategory": "somatic-awareness-reset",
        "description": "Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, and 1 you taste.",
        "benefit_synopsis": "Disrupts anxious spirals and returns you to the present.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "3 minutes" }
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
        "name": "Progressive Muscle Relaxation",
        "slug": "progressive-muscle-relaxation",
        "category": "mind-body-reset",
        "subcategory": "somatic-awareness-reset",
        "description": "Tense and release each muscle group from head to toe.",
        "benefit_synopsis": "Releases tension and promotes bodily awareness.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "full-body-shakeout",
        "category": "mind-body-reset",
        "subcategory": "somatic-awareness-reset",
        "description": "Shake your arms, legs, and whole body to discharge excess energy.",
        "benefit_synopsis": "Releases stuck energy and promotes emotional reset.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" }
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
        "slug": "body-scan-awareness-based",
        "category": "mind-body-reset",
        "subcategory": "somatic-awareness-reset",
        "description": "Bring gentle awareness to each part of your body from head to toe.",
        "benefit_synopsis": "Enhances connection to the body and calms the mind.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "name": "Savor Something Warm",
        "slug": "savor-something-warm",
        "category": "mind-body-reset",
        "subcategory": "somatic-awareness-reset",
        "description": "Slowly enjoy a warm drink, food, or bath as a sensory ritual to calm and reset.",
        "benefit_synopsis": "Warmth promotes safety and slows the nervous system.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
        "slug": "texture-anchor",
        "category": "mind-body-reset",
        "subcategory": "somatic-awareness-reset",
        "description": "Hold or touch a grounding object like a stone, fabric, or fidget.",
        "benefit_synopsis": "Provides sensory feedback to anchor attention.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" }
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
    "environmental-anchoring": [
      {
        "name": "Barefoot Grounding",
        "slug": "barefoot-grounding",
        "category": "mind-body-reset",
        "subcategory": "environmental-anchoring",
        "description": "Step outside barefoot for a few minutes, ideally on grass, dirt, or sand.",
        "benefit_synopsis": "Reduces stress and restores balance through contact with the Earth.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "open-window-pause",
        "category": "mind-body-reset",
        "subcategory": "environmental-anchoring",
        "description": "Stand near an open window and take a few deep breaths while observing your surroundings.",
        "benefit_synopsis": "Combines fresh air, light, and natural sights to ground and refresh.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "touch-the-earth",
        "category": "mind-body-reset",
        "subcategory": "environmental-anchoring",
        "description": "Kneel, sit, or lie down directly on the ground and feel your body supported.",
        "benefit_synopsis": "Connects you to the physical environment and slows internal momentum.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
    "mindful-rituals": [
      {
        "name": "Tea Ritual",
        "slug": "tea-ritual",
        "category": "mind-body-reset",
        "subcategory": "mindful-rituals",
        "description": "Prepare and sip tea slowly, using the process as a calming, intentional moment.",
        "benefit_synopsis": "Signals safety to the nervous system and fosters presence through sensory ritual.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "mindful-tea-sipping",
        "category": "mind-body-reset",
        "subcategory": "mindful-rituals",
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
        "slug": "hand-to-heart-pause",
        "category": "mind-body-reset",
        "subcategory": "mindful-rituals",
        "description": "Place your hand on your chest and breathe slowly for a moment.",
        "benefit_synopsis": "Activates calm and fosters self-connection.",
        "recommended_durations": [
          { "duration_label": "1 minute" },
          { "duration_label": "2 minutes" }
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
        "slug": "light-a-candle-or-incense",
        "category": "mind-body-reset",
        "subcategory": "mindful-rituals",
        "description": "Light a candle or incense with intention and take a moment to breathe and observe.",
        "benefit_synopsis": "Creates ritual space and anchors the mind in presence.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
  "spirituality-mindfulness": {
        # PRACTICE SUBCATEGORY
    "meditation-consciousness": [
      {
          "slug": "mindfulness-meditation",
          "name": "Mindfulness Meditation",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
            "slug": "gratitude-practice",
            "name": "Gratitude Practice",
            "category": "spirituality-mindfulness",
            "subcategory": "meditation-consciousness",
            "description": "List at least three things you are grateful for to foster a positive mindset.",
            "benefit_synopsis": "Builds a connection with the positives in your life.",
            "recommended_durations": [
              {"duration_label": "5 minutes"},
              {"duration_label": "10 minutes"}
            ],
            "impact_rating_id": 4,
            "difficulty_level_id": 1,
            "frequency": "Twice daily",
            "is_common": True,
            "notes": "Focusing on gratitude can reframe negative thoughts and increase life satisfaction.",
            "benefit_synopsis": "Cultivates appreciation, boosts emotional well-being, and reduces stress.",
            "objectives": ["cultivate_gratitude", "increase_optimism", "reduce_stress"]
        },
      {
          "slug": "zazen-seated-zen-meditation",
          "name": "Zazen (Seated Zen Meditation)",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "vipassana-insight-meditation",
          "name": "Vipassana (Insight Meditation)",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "samatha-calm-abiding",
          "name": "Samatha (Calm Abiding)",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "metta-bhavana-loving-kindness-meditation",
          "name": "Metta Bhavana (Loving-Kindness Meditation)",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "choiceless-awareness",
          "name": "Choiceless Awareness",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "mindfulness-meditation-mbsr-style",
          "name": "Mindfulness Meditation (MBSR Style)",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "breath-counting",
          "name": "Breath Counting",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "mantra-meditation-japa",
          "name": "Mantra Meditation (Japa)",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "sound-awareness-meditation",
          "name": "Sound Awareness Meditation",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "walking-meditation-seated-transition-style",
          "name": "Walking Meditation (Seated Transition Style)",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "body-scan-meditation",
          "name": "Body Scan Meditation",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "rain-meditation",
          "name": "RAIN Meditation",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "just-one-minute-meditation",
          "name": "Just One Minute Meditation",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
          "slug": "mindfulness-bell-pause",
          "name": "Mindfulness Bell Pause",
          "category": "spirituality-mindfulness",
          "subcategory": "meditation-consciousness",
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
    "guided-visualization": [
      {
        "name": "Body Scan Meditation",
        "slug": "body-scan-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Gently bring awareness to different parts of the body in sequence, guided by internal or external cues.",
        "benefit_synopsis": "Increases embodiment and calms the nervous system.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
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
        "slug": "loving-kindness-guided-metta",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Follow guided phrases of goodwill directed toward yourself and others.",
        "benefit_synopsis": "Builds empathy, compassion, and emotional warmth.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "visualization-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Visualize a peaceful or empowering image, like light radiating from your body or walking through a serene landscape.",
        "benefit_synopsis": "Engages imagination to calm the mind and create positive mental states.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "gratitude-meditation-guided",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Follow prompts to reflect on people, moments, or things you're thankful for.",
        "benefit_synopsis": "Builds positive perspective and reduces negative spiraling.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "emotional-check-in",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Be guided through identifying, labeling, and holding space for your current emotional state.",
        "benefit_synopsis": "Increases emotional intelligence and self-regulation.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "8 minutes" }
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
        "slug": "mountain-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Visualize yourself as a mountain — stable, grounded, and unmoved by weather or change.",
        "benefit_synopsis": "Builds inner strength and non-reactivity.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "inner-sanctuary-visualization",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Create a vivid mental image of a personal safe space you can return to at any time.",
        "benefit_synopsis": "Builds internal refuge and emotional safety.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "7-days-of-calm-calm-app",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "A week-long introductory program teaching the basics of mindfulness meditation.",
        "benefit_synopsis": "Establishes foundational meditation skills and daily practice habits.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "basics-course-headspace-app",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "A 10-day course introducing fundamental meditation techniques and concepts.",
        "benefit_synopsis": "Provides a structured introduction to meditation, enhancing focus and reducing stress.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "daily-meditation-waking-up-app",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "A new guided meditation each day, covering various themes and techniques.",
        "benefit_synopsis": "Encourages daily mindfulness practice with diverse approaches.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "sleep-stories-calm-app",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Narrated tales designed to help listeners relax and drift into sleep.",
        "benefit_synopsis": "Promotes relaxation and improves sleep quality.",
        "recommended_durations": [
          { "duration_label": "20 minutes" }
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
        "slug": "basics-series-10-percent-happier-app",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Introductory guided meditations focusing on mindfulness and stress reduction.",
        "benefit_synopsis": "Helps beginners understand and practice mindfulness meditation.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "mindfulness-daily-insight-timer-app",
        "category": "spirituality-mindfulness",
        "subcategory": "guided-visualization",
        "description": "Short daily guided meditations to cultivate mindfulness throughout the day.",
        "benefit_synopsis": "Supports the development of a consistent mindfulness practice.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
      },
    ],
    
    # PRACTICE SUBCATEGORY
    "journaling-reflection": [
      {
        "name": "Morning Pages",
        "slug": "morning-pages",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write one or more pages of freeform, stream-of-consciousness thoughts each morning.",
        "benefit_synopsis": "Clears mental clutter and uncovers subconscious patterns.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "gratitude-journaling",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "List three things you’re grateful for — daily or whenever needed.",
        "benefit_synopsis": "Shifts attention toward positivity and builds emotional resilience.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
        "slug": "evening-reflection",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write about how your day went, what you learned, and how you felt.",
        "benefit_synopsis": "Creates closure and reveals daily emotional patterns.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "values-clarification-journaling",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write about what really matters to you and how you’re living in alignment with it.",
        "benefit_synopsis": "Clarifies purpose and boosts motivation for meaningful change.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "reflective-prompt-journaling",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Answer a daily or weekly prompt that encourages self-inquiry or emotional awareness.",
        "benefit_synopsis": "Guides attention to inner growth and key life themes.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "emotion-naming-reflection",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write down what you’re feeling and explore where it’s coming from.",
        "benefit_synopsis": "Supports emotional regulation through awareness and articulation.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
        "slug": "cognitive-distortion-reframe",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Identify a recurring negative thought and write out a more balanced, realistic version.",
        "benefit_synopsis": "Increases cognitive flexibility and reduces unhelpful thought loops.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "abc-thought-record",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write down the activating event (A), your belief or thought (B), and the consequence or emotion (C).",
        "benefit_synopsis": "Builds insight into the link between thoughts, emotions, and behaviors.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "parts-dialogue-ifs",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write from the perspective of a part of you — such as your inner critic, protector, or inner child.",
        "benefit_synopsis": "Fosters self-compassion and deeper understanding of internal conflicts.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "limiting-belief-exploration",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Identify a limiting belief and journal about its origin, consequences, and counter-evidence.",
        "benefit_synopsis": "Loosens fixed mindsets and supports identity growth.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "trigger-journal",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "After an emotional trigger, describe what happened, how your body responded, and what memory or theme it connects to.",
        "benefit_synopsis": "Increases trauma awareness and integrates emotional material.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "letter-to-self",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write a letter to your past, future, or present self from a place of compassion and insight.",
        "benefit_synopsis": "Strengthens self-connection and emotional repair.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "weekly-review-reset",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Reflect on the highs, lows, learnings, and patterns of the past week. Then set your intentions for the next.",
        "benefit_synopsis": "Improves self-awareness and supports intentional weekly rhythm.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "future-self-letter",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write a letter from your future self, describing who you’ve become and how you got there.",
        "benefit_synopsis": "Builds self-belief and clarifies long-term vision.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "dream-journal",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Record your dreams upon waking, noting symbols, emotions, and potential meanings.",
        "benefit_synopsis": "Builds inner awareness and supports unconscious integration.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "goal-progress-reflection",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "Write about what you’ve done toward your goal, what’s working, and what could improve.",
        "benefit_synopsis": "Reinforces action and keeps goals top-of-mind.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "values-in-action-checkin",
        "category": "spirituality-mindfulness",
        "subcategory": "journaling-reflection",
        "description": "List your core values and reflect on how they showed up (or didn’t) in recent choices.",
        "benefit_synopsis": "Strengthens identity alignment and self-trust.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
      },
    ],
    
    # PRACTICE SUBCATEGORY
    "prayer-devotion": [
      {
        "name": "Prayer",
        "slug": "prayer",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Sit in stillness and offer silent prayer, gratitude, or surrender to a higher power.",
        "benefit_synopsis": "Fosters humility, reverence, and trust in something greater.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "devotional",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Chant, sing, or offer loving expression toward something greater.",
        "benefit_synopsis": "Opens the heart and channels emotion into spiritual connection.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "name": "Read Scripture Passage",
        "slug": "read-scripture-passage",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Read a passage from a sacred or spiritual text and reflect on its meaning.",
        "benefit_synopsis": "Connects you to timeless wisdom and inner reflection.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
        "name": "Conversation with God or Spiritual Guide",
        "slug": "conversation-with-god",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Speak freely to a higher power or spiritual presence — as you would a trusted friend or guide.",
        "benefit_synopsis": "Promotes trust, emotional clarity, and a sense of companionship on your path.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Optional or daily",
        "is_common": True,
        "notes": "This can be spoken aloud or internal. Tone can be formal, casual, questioning, grateful, or seeking. The goal is honest relational connection, not performance.",
        "objectives": [
          "foster_spiritual_connection",
          "process_emotions_through_dialogue",
          "deepen_personal_faith_or_guidance"
        ]
      },
      {
        "name": "Light a Candle",
        "slug": "light-a-candle",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Light a candle while setting an intention or offering a quiet moment of thanks.",
        "benefit_synopsis": "Creates a moment of reverence and presence.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "tend-altar",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Place an offering or gently care for your sacred space.",
        "benefit_synopsis": "Fosters reverence, grounding, and symbolic connection.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
        "slug": "nature-bathing",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Spend quiet, undistracted time in nature — walking slowly or sitting still.",
        "benefit_synopsis": "Regulates the nervous system and opens the senses.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
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
        "name": "Look at the Sky or Stars",
        "slug": "look-at-the-sky-or-stars",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Pause and look at the open sky — letting your thoughts soften and your breath expand.",
        "benefit_synopsis": "Creates spaciousness and reduces mental tension.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "offer-to-nature",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Place a small offering — like a flower, stone, or breath — as a gesture of respect and gratitude.",
        "benefit_synopsis": "Deepens reverence and symbolic connection with the earth.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "sit-with-a-tree",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Find a tree and sit near it quietly — letting it hold your attention and stillness.",
        "benefit_synopsis": "Builds inner calm and a sense of rootedness.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "past-life-reflection",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Sit quietly and imagine a life you've lived before — noticing themes, imagery, or lessons that arise.",
        "benefit_synopsis": "Explores patterns and soul-level insights beyond the present lifetime.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "meet-your-higher-self",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Visualize your highest, most expanded version of you — and listen inward for guidance.",
        "benefit_synopsis": "Connects with your inner wisdom and long-view perspective.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "ancestral-reflection",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Think about or write to an ancestor — known or unknown — and reflect on what they carried and passed on.",
        "benefit_synopsis": "Deepens belonging and self-understanding through lineage.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "call-in-a-guide",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Visualize a guide — spiritual, ancestral, animal, or imagined — and receive support or clarity.",
        "benefit_synopsis": "Offers insight, support, or perspective through symbolic connection.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "energetic-reset",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Visualize clearing your body and energy field of stress, tension, or external noise.",
        "benefit_synopsis": "Supports energetic clarity and nervous system reset.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "symbolic-dream-reflection",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Reflect on a recent dream and journal about its emotional tone, symbols, and messages.",
        "benefit_synopsis": "Reveals hidden insights and emotional patterns.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "pull-a-card",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Draw a tarot or oracle card and reflect on the message it brings.",
        "benefit_synopsis": "Offers intuitive insight through symbol and story.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
        "slug": "consult-the-i-ching",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Open to or cast a hexagram from the I Ching and reflect on its passage.",
        "benefit_synopsis": "Provides ancient wisdom for times of transition or uncertainty.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
        "slug": "stream-of-consciousness-writing",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Let your hand move freely across the page — writing whatever flows without judgment.",
        "benefit_synopsis": "Bypasses inner filters and reveals hidden patterns or insight.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "centering-breath",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Take a few deep, steady breaths to bring yourself fully into the moment.",
        "benefit_synopsis": "Anchors awareness and reduces mental noise.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "set-an-intention",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Pause and set a clear intention for how you want to show up today.",
        "benefit_synopsis": "Strengthens focus, motivation, and alignment with values.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "focus-ritual",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Do a short, consistent ritual to mark the shift into focused work or presence.",
        "benefit_synopsis": "Creates mental association and reduces resistance to starting.",
        "recommended_durations": [
          { "duration_label": "2 minutes" }
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
        "slug": "morning-visualization",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Imagine your ideal flow through the day, from morning to evening.",
        "benefit_synopsis": "Mentally primes your actions, emotions, and outcomes.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "mirror-intention",
        "category": "spirituality-mindfulness",
        "subcategory": "prayer-devotion",
        "description": "Look in the mirror and speak a chosen word or phrase that aligns with how you want to show up.",
        "benefit_synopsis": "Builds clarity and emotional commitment to your intention.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
    
    # PRACTICE SUBCATEGORY
    "creativity-intention": [
      {
        "name": "Draw a Mandala",
        "slug": "draw-a-mandala",
        "category": "spirituality-mindfulness",
        "subcategory": "creativity-intention",
        "description": "Create a circular design by drawing, coloring, or patterning from the center outward.",
        "benefit_synopsis": "Supports emotional balance, inner focus, and symbolic reflection.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
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
        "slug": "draw-a-symbol",
        "category": "spirituality-mindfulness",
        "subcategory": "creativity-intention",
        "description": "Draw a shape, image, or mark that represents what you’re feeling or calling in.",
        "benefit_synopsis": "Connects abstract emotion to tangible expression.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "write-a-letter-to-the-universe",
        "category": "spirituality-mindfulness",
        "subcategory": "creativity-intention",
        "description": "Write out your thoughts, desires, or worries as if writing to a loving, listening universe.",
        "benefit_synopsis": "Releases control and opens space for trust and surrender.",
        "recommended_durations": [
          { "duration_label": "10 minutes" }
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
    
    # PRACTICE SUBCATEGORY
    "mantra-sound": [
      {
        "name": "Mantra Repetition (Japa)",
        "slug": "mantra-repetition-japa",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Silently or softly repeat a sacred word or phrase with steady rhythm.",
        "benefit_synopsis": "Centers the mind and connects breath with sacred sound.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "chanting-devotional-singing",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Sing, hum, or repeat devotional phrases with heartful presence.",
        "benefit_synopsis": "Opens the heart and shifts emotional energy through sound.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "bell-singing-bowl-listening",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Focus on the sound of a bell or bowl, allowing it to anchor attention.",
        "benefit_synopsis": "Promotes stillness and opens auditory awareness.",
        "recommended_durations": [
          { "duration_label": "5 minutes" }
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
        "slug": "humming-for-calm",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Hum softly on the exhale, letting the vibration soothe your nervous system.",
        "benefit_synopsis": "Downregulates stress and stimulates the vagus nerve.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "breath-linked-mantra",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Mentally link a short mantra to your inhale and exhale.",
        "benefit_synopsis": "Combines rhythm, breath, and intention into a cohesive practice.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "vocal-toning",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Sustain a single tone (like 'Aaaah' or 'Om') to create internal vibration.",
        "benefit_synopsis": "Stimulates the body through sound and calms internal noise.",
        "recommended_durations": [
          { "duration_label": "3 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "listen-to-sound-bath-or-binaural-track",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Close your eyes and listen to a calming soundscape or frequency-based track.",
        "benefit_synopsis": "Induces deep relaxation and entrains brainwaves.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
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
        "slug": "affirmation-based-mantra",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Repeat a positive phrase silently or aloud to reinforce desired qualities.",
        "benefit_synopsis": "Builds self-trust and shifts internal dialogue.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "create-your-own-mantra",
        "category": "spirituality-mindfulness",
        "subcategory": "mantra-sound",
        "description": "Choose a word or phrase that resonates with you and repeat it with breath or rhythm.",
        "benefit_synopsis": "Personalizes intention and builds emotional resonance.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
    
    # PRACTICE SUBCATEGORY
    "moving-mindfulness": [
      {
        "name": "Walking Meditation",
        "slug": "walking-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Walk slowly and mindfully, placing attention on the sensation of each step.",
        "benefit_synopsis": "Brings awareness into motion and transitions.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "qi-gong-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "A practice of slow, flowing movements with relaxed breathing and attention on building energy.",
        "benefit_synopsis": "Circulates and builds energy, Cultivates relaxed focus",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
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
        "slug": "nei-gong-practice",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "A practice of slow, deliberate flows and postures that train alignment, mobility, and internal strength.",
        "benefit_synopsis": "Improves posture, builds body awareness, and strengthens foundational movement patterns.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
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
        "slug": "mindful-stretching",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Stretch gently while focusing on the sensations in your body.",
        "benefit_synopsis": "Releases tension and anchors awareness in movement.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "intuitive-movement-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Let your body move freely and slowly, following internal cues rather than form.",
        "benefit_synopsis": "Encourages embodied presence and emotional release.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "posture-based-breath-synchronization",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Match slow breath with simple body movements like raising arms or shifting stance.",
        "benefit_synopsis": "Unites breath, awareness, and action in rhythmic alignment.",
        "recommended_durations": [
          { "duration_label": "3 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "tai-chi-restorative-flow",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Practice slow, flowing Tai Chi movements to calm the mind and balance the body.",
        "benefit_synopsis": "Enhances balance, body awareness, and inner calm.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
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
        "slug": "dao-yin-flow",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Move through breath-guided stretches and rotations to stimulate energy flow.",
        "benefit_synopsis": "Opens the body, releases tension, and supports energy alignment.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "shaking-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Let your body gently shake or bounce to release tension and re-regulate your system.",
        "benefit_synopsis": "Relieves stress and resets the nervous system.",
        "recommended_durations": [
          { "duration_label": "2 minutes" },
          { "duration_label": "5 minutes" }
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
        "slug": "gentle-dance-flow",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Move intuitively with soft rhythm and breath, letting music or inner feeling guide you.",
        "benefit_synopsis": "Invites playfulness, freedom, and embodied presence.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "walking-labyrinth-meditation",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Walk in a simple circular or spiraling path as a symbolic journey inward and outward.",
        "benefit_synopsis": "Focuses attention and invites reflection through movement.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "10 minutes" }
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
        "slug": "breath-gesture-flow",
        "category": "spirituality-mindfulness",
        "subcategory": "walking-movement",
        "description": "Link simple breath cycles with hand or body gestures to center yourself.",
        "benefit_synopsis": "Combines intention, rhythm, and movement for deepened presence.",
        "recommended_durations": [
          { "duration_label": "3 minutes" },
          { "duration_label": "5 minutes" }
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
    ],
  },

  # PRACTICE CATEGORY
  # "recreation-creativity": {
  #   #  PRACTICE SUBCATEGORY
  #     "Visual & Craft-Based Creativity (Art, Crafts, Photography)": [
  #         {
  #           "name": "Draw, Sketch, Paint For Fun",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Doodle, sketch, or throw down some color — no rules, just creative play.",
  #           "benefit_synopsis": "Reduces stress and encourages free expression.",
  #           "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "20 minutes"}],
  #           "impact_rating_id": 3,
  #           "difficulty_level_id": 1,
  #           "frequency": "Optional or daily",
  #           "is_common": True,
  #           "notes": "Use whatever tools you have — pencil, pen, markers, or watercolor. It’s not about the result, just the act of making marks.",
  #           "objectives": ["express_creatively", "reduce_mental_pressure", "stimulate_flow"]
  #         },
  #         {
  #           "name": "Practice an Art Skill",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Spend time practicing a technique like shading, proportions, or brushwork.",
  #           "benefit_synopsis": "Improves focus and builds creative confidence.",
  #           "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
  #           "impact_rating_id": 4,
  #           "difficulty_level_id": 2,
  #           "frequency": "Optional or weekly",
  #           "is_common": True,
  #           "notes": "Pick one element of technique to explore. Keep it casual — it’s about the reps, not perfection.",
  #           "objectives": ["develop_skills", "build_focus", "gain_artistic_confidence"]
  #         },
  #         {
  #           "name": "Pottery for Fun",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Get your hands into clay and shape something — a bowl, a creature, or just texture.",
  #           "benefit_synopsis": "Deepens tactile engagement and grounds awareness.",
  #           "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
  #           "impact_rating_id": 4,
  #           "difficulty_level_id": 2,
  #           "frequency": "Optional or recreational",
  #           "is_common": False,
  #           "notes": "No wheel needed — try pinch pots or hand-building with air-dry clay or real ceramic clay at a studio.",
  #           "objectives": ["engage_senses", "slow_down", "explore_shape_and_form"]
  #         },
  #         {
  #           "name": "Art Inspiration Adventure",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Go out and explore art in the world — murals, galleries, or public sculpture.",
  #           "benefit_synopsis": "Refuels creative vision and sparks new ideas.",
  #           "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "1 hour"}],
  #           "impact_rating_id": 3,
  #           "difficulty_level_id": 1,
  #           "frequency": "Optional or when creatively dry",
  #           "is_common": False,
  #           "notes": "Take photos, sketch what you see, or just soak it in. Visit a museum, check out local art, or browse unique design stores.",
  #           "objectives": ["stimulate_inspiration", "expand_visual_language", "refill_creative_well"]
  #         },
  #         {
  #           "name": "Photography Nature Walk",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Take a slow walk through nature and capture moments that move you.",
  #           "benefit_synopsis": "Builds connection to environment and quiet visual mindfulness.",
  #           "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
  #           "impact_rating_id": 3,
  #           "difficulty_level_id": 1,
  #           "frequency": "Optional or calming reset",
  #           "is_common": True,
  #           "notes": "Don’t worry about gear — your phone works fine. Look for light, shadows, shapes, or subtle motion.",
  #           "objectives": ["ground_in_nature", "train_visual_awareness", "reduce_stress"]
  #         },
  #         {
  #           "name": "Art Walk with a Theme",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Choose a visual theme and go find it out in the world.",
  #           "benefit_synopsis": "Turns everyday walks into creative missions.",
  #           "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
  #           "impact_rating_id": 3,
  #           "difficulty_level_id": 1,
  #           "frequency": "Optional or weekly",
  #           "is_common": True,
  #           "notes": "Themes can be color-based (like 'blue'), shape-driven ('circles'), or mood-based ('abandoned'). Document what you find however you like.",
  #           "objectives": ["engage_with_environment", "practice_observational_focus", "spark_playful_exploration"]
  #         }
  #     ],

  #   #  PRACTICE SUBCATEGORY
  #     "Writing & Storytelling (Journaling, Poetry, Fiction)": [],

  #   #  PRACTICE SUBCATEGORY
  #     "Music & Rhythm (Instruments, Drumming, Dance)": [
  #         {
  #           "name": "Practice an Instrument",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Spend focused time refining chords, scales, or pieces on your instrument of choice.",
  #           "benefit_synopsis": "Builds discipline and deepens musical fluency.",
  #           "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
  #           "impact_rating_id": 4,
  #           "difficulty_level_id": 2,
  #           "frequency": "Optional or consistent",
  #           "is_common": True,
  #           "notes": "Try a practice ritual that works for you — metronome drills, ear training, or scales. Track progress over time.",
  #           "objectives": ["develop_skill", "enhance_focus", "build_musical_fluency"]
  #         },
  #         {
  #           "name": "Play Music (Jam Sesh)",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Let go and just play — improvise, mess around, or find your groove.",
  #           "benefit_synopsis": "Releases creative energy and boosts mood.",
  #           "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
  #           "impact_rating_id": 4,
  #           "difficulty_level_id": 1,
  #           "frequency": "Optional or energizing",
  #           "is_common": True,
  #           "notes": "Alone or with others, unplugged or electric, acoustic or digital. Just play.",
  #           "objectives": ["have_fun_creating", "release_energy", "get_into_flow"]
  #         },
  #         {
  #           "name": "Practice with the Band",
  #           "category": "Recreation, Play & Creative Hobbies",
  #           "subcategory": "Visual & Craft-Based Creativity (Art, Crafts, Photography)",
  #           "description": "Join your band or group and run through songs, riffs, or rhythms together.",
  #           "benefit_synopsis": "Strengthens coordination, timing, and connection.",
  #           "recommended_durations": [{"duration_label": "20 minutes"}, {"duration_label": "45 minutes"}],
  #           "impact_rating_id": 5,
  #           "difficulty_level_id": 3,
  #           "frequency": "Scheduled or recurring",
  #           "is_common": False,
  #           "notes": "Even one shared practice locks in musical chemistry and shared focus. Practice dynamics, transitions, and listening.",
  #           "objectives": ["enhance_collaboration", "train_listening", "refine_timing"]
  #         },
  #     ],

  #   #  PRACTICE SUBCATEGORY
  #     "Games & Puzzles (Board Games, Video Games, Strategy)": [],

  #   #  PRACTICE SUBCATEGORY
  #     "Tactile & Mindful Hobbies (Knitting, Coloring, Sculpting)": [],

  #   #  PRACTICE SUBCATEGORY
  #     "DIY, Gardening & Home Projects (Gardening, Repairs, Woodworking)": [],

  #   #  PRACTICE SUBCATEGORY
  #     "Food & Flavor (Cooking, Baking, Ferments, Plating)": [],

  #   #  PRACTICE SUBCATEGORY
  #     "Collections & Curated Interests (Cards, Coins, etc.)": [],

  #   #  PRACTICE SUBCATEGORY
  #     "Social Activities & Sports (Recreational Movement & Group Games)": [],

  #   #  PRACTICE SUBCATEGORY
  #     "Exploration & Experience (Outdoor Activities, Travel, Culture)": []
  # },

  # # PRACTICE CATEGORY
  # "Restoration, Relaxation & Self-Care": {},

  # # PRACTICE CATEGORY
  # "Mental Clarity & Cognitive Priming": {},

    # PRACTICE CATEGORY
  "movement-sports": {
    
    # PRACTICE SUBCATEGORY
    "aerobic-conditioning": [
      {
          "name": "Brisk Walk",
          "slug": "brisk-walk",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Walk at a steady, energetic pace indoors or outdoors to elevate heart rate.",
          "benefit_synopsis": "Boosts cardiovascular health and supports mental clarity.",
          "recommended_durations": [{"duration_label": "20 minutes"}, {"duration_label": "45 minutes"}],
          "impact_rating_id": 4,
          "difficulty_level_id": 2,
          "frequency": "Daily or several times per week",
          "is_common": True,
          "notes": "Works well as a standalone routine or as a primer before more intense training.",
          "objectives": ["increase_circulation", "enhance_mood", "improve_daily_energy"]
      },
      {
          "name": "Jogging",
          "slug": "jogging",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Run at a comfortable, steady pace to build cardiovascular endurance.",
          "benefit_synopsis": "Improves aerobic efficiency and builds mental resilience.",
          "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
          "impact_rating_id": 5,
          "difficulty_level_id": 3,
          "frequency": "2–4 times per week",
          "is_common": True,
          "notes": "Maintain a pace that allows for conversation without strain.",
          "objectives": ["build_endurance", "enhance_stamina", "boost_mood"]
      },
      {
          "name": "Running",
          "slug": "running",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Run at a more vigorous pace to train aerobic and muscular endurance.",
          "benefit_synopsis": "Strengthens heart, lungs, and legs under sustained effort.",
          "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
          "impact_rating_id": 5,
          "difficulty_level_id": 4,
          "frequency": "2–3 times per week",
          "is_common": True,
          "notes": "Progress slowly if you're building intensity. Stay mindful of joint recovery.",
          "objectives": ["improve_cardiovascular_capacity", "build_resilience", "enhance_fatigue_tolerance"]
      },
      {
          "name": "Hiking",
          "slug": "hiking",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Walk trails or terrain with elevation to build aerobic and leg strength.",
          "benefit_synopsis": "Combines cardio with the restorative power of nature.",
          "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "90 minutes"}],
          "impact_rating_id": 5,
          "difficulty_level_id": 3,
          "frequency": "Weekly or bi-weekly",
          "is_common": False,
          "notes": "Choose terrain based on fitness level. Bring water and sun protection.",
          "objectives": ["enhance_endurance", "reduce_stress", "strengthen_lower_body"]
      },
      {
          "name": "Stair Climbing",
          "slug": "stair-climbing",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Climb stairs or use a stair machine to build explosive endurance and cardio capacity.",
          "benefit_synopsis": "Engages major muscle groups while elevating heart rate quickly.",
          "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "20 minutes"}],
          "impact_rating_id": 5,
          "difficulty_level_id": 4,
          "frequency": "1–3 times per week",
          "is_common": True,
          "notes": "Pace yourself and use intervals to build stamina gradually.",
          "objectives": ["train_glutes_and_quads", "increase_heart_rate", "build_explosive_strength"]
      },
      {
          "name": "Jump Rope",
          "slug": "jump-rope",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Jump rope continuously to build speed, coordination, and aerobic power.",
          "benefit_synopsis": "High-efficiency cardio with a focus on agility and rhythm.",
          "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "15 minutes"}],
          "impact_rating_id": 5,
          "difficulty_level_id": 4,
          "frequency": "1–3 times per week",
          "is_common": True,
          "notes": "Use intervals or freestyle. Double unders and crossovers increase intensity.",
          "objectives": ["boost_cardiovascular_endurance", "refine_coordination", "build_speed"]
      },
      {
          "name": "Cycling",
          "slug": "cycling",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Ride a bike indoors or outdoors to build lower body strength and endurance.",
          "benefit_synopsis": "Low-impact way to enhance heart and lung function.",
          "recommended_durations": [{"duration_label": "25 minutes"}, {"duration_label": "60 minutes"}],
          "impact_rating_id": 4,
          "difficulty_level_id": 3,
          "frequency": "2–5 times per week",
          "is_common": True,
          "notes": "Adjust resistance or terrain to scale difficulty.",
          "objectives": ["increase_endurance", "build_leg_power", "support_cardiovascular_health"]
      },
      {
          "name": "Rowing",
          "slug": "rowing",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Use a rowing machine or row in open water for full-body aerobic conditioning.",
          "benefit_synopsis": "Develops stamina, power, and rhythm in a joint-friendly format.",
          "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
          "impact_rating_id": 4,
          "difficulty_level_id": 3,
          "frequency": "2–4 times per week",
          "is_common": True,
          "notes": "Focus on posture and breathing. Great for efficient full-body work.",
          "objectives": ["build_aerobic_capacity", "enhance_core_and_leg_strength", "improve_coordination"]
      },
      {
          "name": "Elliptical",
          "slug": "elliptical",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Use an elliptical trainer for low-impact cardio that mimics running or skiing.",
          "benefit_synopsis": "Protects joints while improving endurance and caloric output.",
          "recommended_durations": [{"duration_label": "20 minutes"}, {"duration_label": "45 minutes"}],
          "impact_rating_id": 3,
          "difficulty_level_id": 2,
          "frequency": "2–5 times per week",
          "is_common": True,
          "notes": "Track time and heart rate. Adjust incline for more challenge.",
          "objectives": ["support_joint_health", "increase_cardio_output", "train_full_body_coordination"]
      },
      {
          "name": "Swimming",
          "slug": "swimming",
          "category": "movement-sport",
          "subcategory": "aerobic-conditioning",
          "description": "Swim laps or freestyle in water for full-body aerobic endurance.",
          "benefit_synopsis": "Combines resistance with joint-safe movement for full-body stamina.",
          "recommended_durations": [{"duration_label": "20 minutes"}, {"duration_label": "40 minutes"}],
          "impact_rating_id": 5,
          "difficulty_level_id": 4,
          "frequency": "1–3 times per week",
          "is_common": True,
          "notes": "Alternate strokes and use intervals to vary stimulus.",
          "objectives": ["build_full_body_endurance", "enhance_lung_capacity", "support_joint_recovery"]
      },
      # {
      #     "name": "Low Impact Cardio",
      #     "slug": "low-impact-cardio",
      #     "category": "movement-sport",
      #     "subcategory": "aerobic-conditioning",
      #     "description": "A gentler approach to cardio designed to be accessible for all levels and joint-sensitive users.",
      #     "benefit_synopsis": "Encourages movement without strain or intensity.",
      #     "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "25 minutes"}],
      #     "impact_rating_id": 3,
      # }
    ],

    # PRACTICE SUBCATEGORY
    "intervals-circuits": [
      {
        "name": "CrossFit Class",
        "slug": "crossfit-conditioning",
        "category": "movement-sport",
        "subcategory": "intervals-circuits",
        "description": "Perform high-intensity functional movements in a timed or round-based workout format.",
        "benefit_synopsis": "Combines strength, cardio, and mobility under fatigue to build total conditioning.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "40 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "Scalable to fitness level. May include barbell, bodyweight, and mixed modal drills.",
        "objectives": ["improve_work_capacity", "train_adaptability", "increase_mental_toughness"]
      },
      {
        "name": "P90X Workout",
        "slug": "p90x-intervals",
        "category": "movement-sport",
        "subcategory": "intervals-circuits",
        "description": "Follow structured interval workouts combining strength and cardio in a home-friendly format.",
        "benefit_synopsis": "Delivers full-body results using bodyweight or minimal equipment.",
        "recommended_durations": [
          { "duration_label": "25 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Often uses supersets and active rest. Can be video-guided or self-paced.",
        "objectives": ["build_total_body_fitness", "enhance_aerobic_power", "train_efficiency"]
      },
      {
        "name": "F45 Intervals",
        "slug": "f45-intervals",
        "category": "movement-sport",
        "subcategory": "intervals-circuits",
        "description": "Perform high-intensity stations in short rounds combining resistance, cardio, and agility.",
        "benefit_synopsis": "Maximizes intensity and variety to build cardio-resistance endurance.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "Fast-paced, class-style format. Great for motivation and variety.",
        "objectives": ["boost_metabolic_output", "train_energy_systems", "improve_durability"]
      },
      {
        "name": "Running Intervals",
        "slug": "running-intervals",
        "category": "movement-sport",
        "subcategory": "intervals-circuits",
        "description": "Alternate between sprinting and recovery to build speed and stamina.",
        "benefit_synopsis": "Builds aerobic and anaerobic capacity while sharpening mental grit.",
        "recommended_durations": [
          { "duration_label": "15 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Can be done outdoors, on a track, or treadmill. Vary intensity to progress.",
        "objectives": ["build_speed", "improve_cardio_efficiency", "enhance_mental_resilience"]
      },
      {
        "name": "Cycling Intervals",
        "slug": "cycling-intervals",
        "category": "movement-sport",
        "subcategory": "intervals-circuits",
        "description": "Use alternating efforts on a bike or spin setup to increase cardiovascular and muscular endurance.",
        "benefit_synopsis": "Improves leg power and aerobic conditioning without joint stress.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "40 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "Adjust resistance and cadence for optimal interval adaptation.",
        "objectives": ["increase_lactate_threshold", "build_leg_endurance", "support_joint_health"]
      },
      {
        "name": "HIIT Workout",
        "slug": "hiit-workout",
        "category": "movement-sport",
        "subcategory": "intervals-circuits",
        "description": "Alternate between short bursts of intense effort and brief recovery periods.",
        "benefit_synopsis": "Triggers fat loss, increases endurance, and improves metabolic function.",
        "recommended_durations": [
          { "duration_label": "15 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "No equipment needed — great for quick, effective workouts at any level.",
        "objectives": ["increase_vo2_max", "burn_calories", "improve_recovery_time"]
      },
      {
        "name": "Interval Training",
        "slug": "interval-training",
        "category": "movement-sport",
        "subcategory": "intervals-circuits",
        "description": "Perform any form of cardio or bodyweight movement in structured work-rest intervals.",
        "benefit_synopsis": "Boosts cardiovascular efficiency and trains recovery between efforts.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "35 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Use a timer app to structure intervals. Pairs well with walking, jumping, or stairs.",
        "objectives": ["build_endurance", "train_heart_rate_variability", "improve_energy_system_flexibility"]
      }
    ],

    # PRACTICE SUBCATEGORY
    "strength-training": [
      {
        "name": "Strength Training Circuit",
        "slug": "strength-training-circuit",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Cycle through multiple strength exercises with minimal rest to build strength and endurance.",
        "benefit_synopsis": "Efficiently builds total-body strength and conditioning.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "40 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "Can include bodyweight, dumbbells, or machines. Adjust weight to match effort.",
        "objectives": ["build_general_strength", "improve_work_capacity", "increase_muscle_endurance"]
      },
      {
        "name": "Functional Strength Training",
        "slug": "functional-strength-training",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Train core lifts and movement-based strength patterns like carries, lunges, and twists.",
        "benefit_synopsis": "Builds stability and resilience for real-world movement.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "2–3 times per week",
        "is_common": True,
        "notes": "Emphasize control and posture over heavy loading.",
        "objectives": ["train_integrated_movement", "build_core_and_joint_strength", "enhance_postural_control"]
      },
      {
        "name": "Olympic Lifting Basics",
        "slug": "olympic-lifting-basics",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Work on snatch and clean & jerk fundamentals using barbell technique drills.",
        "benefit_synopsis": "Develops explosive power, coordination, and timing.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–3 times per week",
        "is_common": False,
        "notes": "Use a coach or video feedback for safety and skill progression.",
        "objectives": ["build_explosiveness", "enhance_lift_technique", "develop_motor_control"]
      },
      {
        "name": "Powerlifting Set",
        "slug": "powerlifting-set",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Focus on maximal strength in the squat, bench press, and deadlift.",
        "benefit_synopsis": "Builds raw strength, confidence under load, and muscle mass.",
        "recommended_durations": [
          { "duration_label": "45 minutes" },
          { "duration_label": "75 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "2–3 times per week",
        "is_common": True,
        "notes": "Work in lower rep ranges with longer rest periods.",
        "objectives": ["build_max_strength", "develop_lift_efficiency", "enhance_neural_drive"]
      },
      {
        "name": "Resistance Band Strength",
        "slug": "resistance-band-strength",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Use resistance bands to build strength, especially for joints and stabilizers.",
        "benefit_synopsis": "Improves joint integrity and active control with low risk.",
        "recommended_durations": [
          { "duration_label": "15 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Ideal for beginners, warmups, or injury-prevention routines.",
        "objectives": ["activate_support_muscles", "enhance_joint_stability", "build_controlled_strength"]
      },
      {
        "name": "TRX / Suspension Trainer",
        "slug": "suspension-trainer-workout",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Train full-body strength using a suspension system that emphasizes stability and core engagement.",
        "benefit_synopsis": "Improves functional strength with minimal equipment.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "40 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "Scales easily — adjust angle and stance to change intensity.",
        "objectives": ["build_stabilizer_strength", "improve_body_control", "train_core_alignment"]
      },
      {
        "name": "Calisthenics Strength Training",
        "slug": "calisthenic-strength-training",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Use advanced bodyweight exercises like push-ups, pull-ups, and holds to build raw strength and control.",
        "benefit_synopsis": "Builds relative strength and neuromuscular coordination.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 4,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Best results come from focused rep control and progressive overload.",
        "objectives": ["increase_relative_strength", "train_core_stability", "build_joint_toughness"]
      },
      {
        "name": "Kettlebell Strength Training",
        "slug": "kettlebell-strength-training",
        "category": "movement-sport",
        "subcategory": "strength-training",
        "description": "Use kettlebell lifts like swings, cleans, and get-ups to develop power and functional control.",
        "benefit_synopsis": "Combines strength, mobility, and coordination into one tool.",
        "recommended_durations": [
          { "duration_label": "15 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "2–3 times per week",
        "is_common": True,
        "notes": "Use lighter weights for flow, heavier for strength sets.",
        "objectives": ["improve_hip_power", "develop_motor_precision", "enhance_mobility_under_load"]
      }
    ],

    # PRACTICE SUBCATEGORY
    "martial-calisthenics": [
      {
        "name": "Karate Practice",
        "slug": "karate-practice",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Practice traditional Karate forms, strikes, and footwork to build coordination, focus, and discipline.",
        "benefit_synopsis": "Develops control, reaction time, and mental clarity through structured repetition.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Works well in both class and solo form practice settings.",
        "objectives": ["enhance_focus", "build_reaction_time", "train_discipline"]
      },
      {
        "name": "Taekwondo Practice",
        "slug": "taekwondo-practice",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Use traditional Taekwondo drills and kicking forms to build explosive power and lower-body agility.",
        "benefit_synopsis": "Improves balance, flexibility, and mental sharpness.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Focus on control over height in kicking progressions.",
        "objectives": ["train_kicking_precision", "develop_leg_strength", "increase_balance"]
      },
      {
        "name": "Boxing Training",
        "slug": "boxing-training",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Drill footwork, striking combos, and head movement for cardio conditioning and rhythm.",
        "benefit_synopsis": "Boosts agility, power, and endurance through dynamic movement.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "40 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "Shadowboxing, mitt work, or heavy bag all apply.",
        "objectives": ["build_cardio_endurance", "sharpen_timing", "develop_power"]
      },
      {
        "name": "Kickboxing",
        "slug": "kickboxing",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Combine punches, kicks, and movement in rhythmic sequences to improve full-body coordination.",
        "benefit_synopsis": "Blends power and flow into an accessible cardio-martial fusion.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Works great as a guided class or shadow routine.",
        "objectives": ["train_combination_fluidity", "build_agility", "increase_explosiveness"]
      },
      {
        "name": "Muay Thai Drills",
        "slug": "muay-thai-drills",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Practice elbows, knees, clinch, and striking from Muay Thai fundamentals.",
        "benefit_synopsis": "Trains close-range strength, flexibility, and core power.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "40 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Great for building confidence and body control.",
        "objectives": ["improve_core_strength", "develop_range_control", "build_total_body_tension"]
      },
      {
        "name": "Brazilian Jiu-Jitsu",
        "slug": "brazilian-jiu-jitsu",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Practice grappling, transitions, and submissions from the ground to build strength, awareness, and control.",
        "benefit_synopsis": "Enhances coordination, leverage, and calm under pressure.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Focus on flow and breath rather than force, especially as a beginner.",
        "objectives": ["develop_ground_control", "train_adaptive_response", "enhance_body_awareness"]
      },
      {
        "name": "Mixed Martial Arts Training",
        "slug": "mma-training",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Combine striking, grappling, and movement drills to build hybrid martial skill and conditioning.",
        "benefit_synopsis": "Integrates diverse movement patterns into a single high-output discipline.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Can include pad work, drills, or solo flow combinations.",
        "objectives": ["train_cross_discipline", "improve_combination_timing", "build_full_body_resilience"]
      },
      {
        "name": "Kung Fu Forms Practice",
        "slug": "kung-fu-forms-practice",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Flow through traditional Kung Fu forms that blend grace, force, and breath control.",
        "benefit_synopsis": "Enhances proprioception, flexibility, and inner discipline.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Practice with intention — each movement contains both art and purpose.",
        "objectives": ["refine_movement_precision", "develop_internal_focus", "increase_controlled_power"]
      },
      {
        "name": "Shadow Sparring",
        "slug": "shadow-sparring",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Visualize and respond to imaginary opponents using striking, footwork, and defense.",
        "benefit_synopsis": "Builds reflexes and spatial awareness while honing form.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Can be freestyle or patterned — keep movement continuous and intentional.",
        "objectives": ["improve_reaction_speed", "sharpen_form", "train_visualization"]
      },
      {
        "name": "Capoeira Flow",
        "slug": "capoeira-flow",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Practice the flowing, acrobatic movement style of Capoeira with music, rhythm, and awareness.",
        "benefit_synopsis": "Develops flexibility, agility, and expressive control through martial play.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Even basic Capoeira patterns promote core stability and rhythm.",
        "objectives": ["train_body_awareness", "enhance_fluidity", "build_core_and_leg_control"]
      },
      {
        "name": "Aikido Fundamentals",
        "slug": "aikido-fundamentals",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Practice circular movement, joint locks, and partner flow techniques from Aikido.",
        "benefit_synopsis": "Refines balance, non-resistance, and directional control.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 3,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Requires patience and refinement — best learned slowly with repetition.",
        "objectives": ["enhance_spatial_awareness", "cultivate_centering", "train_joint_sensitivity"]
      },
      {
        "name": "Judo Drills",
        "slug": "judo-drills",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Work on throws, grip control, and ground transitions from Judo fundamentals.",
        "benefit_synopsis": "Improves leverage, hip mobility, and full-body balance.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "40 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Solo reps or partner flow can both reinforce key mechanics.",
        "objectives": ["develop_leverage_mechanics", "train_fall_recovery", "build_hip_and_leg_power"]
      },
      {
        "name": "Krav Maga Conditioning",
        "slug": "krav-maga-conditioning",
        "category": "movement-sport",
        "subcategory": "martial-calisthenics",
        "description": "Drill simple, high-intensity striking and defense techniques from Krav Maga.",
        "benefit_synopsis": "Prioritizes self-defense skills, reaction speed, and explosive effort.",
        "recommended_durations": [
          { "duration_label": "15 minutes" },
          { "duration_label": "30 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Focus on effort, assertiveness, and clean mechanics under pressure.",
        "objectives": ["build_explosive_response", "improve_stress_resilience", "train_close_range_defense"]
      }

    ],

    # PRACTICE SUBCATEGORY
    "mobility-flexibility": [
      {
        "name": "Daily Mobility Routine",
        "slug": "daily-mobility",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "A full-body routine using dynamic joint movements to improve range and reduce stiffness.",
        "benefit_synopsis": "Supports overall movement quality and keeps joints healthy.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily or as needed",
        "is_common": True,
        "notes": "A go-to warmup or standalone reset.",
        "objectives": ["maintain_joint_health", "reduce_stiffness", "enhance_movement_quality"]
      },
      {
        "name": "Lower Body Mobility",
        "slug": "lower-body-mobility",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Target hips, knees, and ankles with movements that restore range and build control.",
        "benefit_synopsis": "Improves squat depth, gait, and injury prevention.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "25 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Focus especially after leg days or long sitting periods.",
        "objectives": ["unlock_hip_range", "improve_joint_alignment", "reduce_lower_body_tension"]
      },
      {
        "name": "Upper Body Mobility",
        "slug": "upper-body-mobility",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Relieve tension and improve motion in shoulders, neck, and thoracic spine.",
        "benefit_synopsis": "Enhances posture and relieves common desk-driven stiffness.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Pairs well with breathwork or upper-body strength training.",
        "objectives": ["increase_t_spine_mobility", "release_neck_tension", "enhance_posture"]
      },
      {
        "name": "Dynamic Stretch Flow",
        "slug": "dynamic-stretch-flow",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Move through controlled, rhythmic stretches that activate and lengthen key muscle groups.",
        "benefit_synopsis": "Primes muscles and joints for movement or performance.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "15 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Pre-workout or movement days",
        "is_common": True,
        "notes": "Use before strength, cardio, or sports. Keep transitions smooth.",
        "objectives": ["activate_movement_patterns", "increase_blood_flow", "reduce_risk_of_strain"]
      },
      {
        "name": "Post-Workout Stretch",
        "slug": "post-workout-stretch",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Cool down with static stretches that lengthen and decompress the body.",
        "benefit_synopsis": "Aids recovery and helps transition the nervous system post-effort.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "After workouts or on recovery days",
        "is_common": True,
        "notes": "Hold each position 20–60 seconds. Focus on breath.",
        "objectives": ["reduce_muscle_tension", "increase_flexibility", "support_nervous_system_recovery"]
      },
      {
        "name": "Hip Opener Sequence",
        "slug": "hip-opener-sequence",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Use deep and active hip stretches to unlock tightness and improve posture.",
        "benefit_synopsis": "Relieves tight hips and supports fluid lower body mechanics.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "2–3 times per week",
        "is_common": True,
        "notes": "Great before or after long sitting periods or leg workouts.",
        "objectives": ["release_hip_flexors", "restore_glute_activation", "enhance_pelvic_mobility"]
      },
      {
        "name": "Spinal Mobility Flow",
        "slug": "spinal-mobility-flow",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Practice flexion, extension, and rotation drills to keep your spine supple and supported.",
        "benefit_synopsis": "Supports posture, core control, and healthy movement mechanics.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "2–4 times per week",
        "is_common": True,
        "notes": "Can be gentle or active depending on flow pace.",
        "objectives": ["improve_spinal_mobility", "release_back_tension", "support_neural_flexibility"]
      },
      {
        "name": "Ankle & Foot Mobility",
        "slug": "ankle-foot-mobility",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Strengthen and mobilize your foot and ankle complex to improve balance and performance.",
        "benefit_synopsis": "Restores movement at the foundation of all upright activity.",
        "recommended_durations": [
          { "duration_label": "5 minutes" },
          { "duration_label": "15 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "1–3 times per week",
        "is_common": False,
        "notes": "Excellent for runners, lifters, or anyone dealing with stiff arches.",
        "objectives": ["enhance_balance", "improve_dorsiflexion", "reduce_risk_of_injury"]
      },
      {
        "name": "Shoulder Opener Series",
        "slug": "shoulder-opener-series",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Open up your chest and shoulders using banded or bodyweight stretches.",
        "benefit_synopsis": "Restores overhead motion and relieves upper body compression.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "15 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Pairs well with upper body strength training or postural reset work.",
        "objectives": ["open_chest", "restore_overhead_range", "enhance_postural_support"]
      },
      {
        "name": "Mobility Stick Routine",
        "slug": "mobility-stick-routine",
        "category": "movement-sport",
        "subcategory": "mobility-flexibility",
        "description": "Use a dowel or mobility stick to guide range of motion and create tension while moving through planes.",
        "benefit_synopsis": "Adds feedback and control to mobility training.",
        "recommended_durations": [
          { "duration_label": "10 minutes" },
          { "duration_label": "20 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": False,
        "notes": "Especially useful for shoulder, spine, and hamstring mobility.",
        "objectives": ["improve_motor_control", "train_under_tension", "increase_joint_integrity"]
      }
    ],

    # PRACTICE SUBCATEGORY
    "movement-classes-flows": [
      {
        "name": "Gentle Yoga Flow",
        "slug": "gentle-yoga-flow",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Move slowly through foundational yoga postures with an emphasis on breath and relaxation.",
        "benefit_synopsis": "Supports nervous system downregulation and physical release.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "1–5 times per week",
        "is_common": True,
        "notes": "Ideal for winding down, recovery days, or mental reset.",
        "objectives": ["reduce_tension", "improve_flexibility", "foster_emotional_balance"]
      },
      {
        "name": "Vinyasa Yoga Flow",
        "slug": "vinyasa-yoga-flow",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Flow through continuous yoga postures synchronized with breath for strength and awareness.",
        "benefit_synopsis": "Builds presence, endurance, and fluid strength.",
        "recommended_durations": [{"duration_label": "20 minutes"}, {"duration_label": "45 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Common format in studio classes — pace can vary.",
        "objectives": ["develop_breath_body_connection", "increase_stamina", "enhance_grace"]
      },
      {
        "name": "Morning Sun Salutations",
        "slug": "morning-sun-salutations",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Perform repeated rounds of the Surya Namaskar sequence to awaken body and mind.",
        "benefit_synopsis": "Energizes the body while grounding the mind.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "Daily or as morning ritual",
        "is_common": True,
        "notes": "Can be used as a standalone ritual or a warmup for deeper practice.",
        "objectives": ["stimulate_morning_energy", "sync_with_breath", "enhance_mobility"]
      },
      {
        "name": "Mobility Flow with Breath",
        "slug": "mobility-breath-flow",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Move through gentle mobility drills guided by deep breathing.",
        "benefit_synopsis": "Improves flexibility and calms the nervous system.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "20 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "2–5 times per week",
        "is_common": True,
        "notes": "Combine circular joint motions with long nasal exhales.",
        "objectives": ["increase_joint_freedom", "support_recovery", "downregulate_stress"]
      },
      {
        "name": "Qi Gong Practice",
        "slug": "qi-gong-practice",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Engage in slow, deliberate movements to cultivate internal energy and awareness.",
        "benefit_synopsis": "Promotes vitality, breath coordination, and calm.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–4 times per week",
        "is_common": False,
        "notes": "Practice barefoot if possible for grounding.",
        "objectives": ["cultivate_energy", "calm_the_mind", "improve_breath_flow"]
      },
      {
        "name": "Tai Chi",
        "slug": "tai-chi",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Move slowly and intentionally through simple Tai Chi forms for balance and internal awareness.",
        "benefit_synopsis": "Improves coordination, breath awareness, and emotional steadiness.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "25 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Ideal for older adults, stress relief, or grounding practice.",
        "objectives": ["enhance_centering", "cultivate_balance", "slow_down_nervous_system"]
      },
      {
        "name": "Nei Gong",
        "slug": "nei-gong",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Introductory practice of internal martial movement focused on tension release and breath.",
        "benefit_synopsis": "Trains internal coordination, subtle breath-body awareness.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Often done in stillness, then in slow transition-based flow.",
        "objectives": ["cultivate_subtle_awareness", "build_inner_strength", "harmonize_energy_flow"]
      },
      {
        "name": "Somatic Movement Reset",
        "slug": "somatic-movement-reset",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Use small, conscious movements to release chronic tension and increase felt sense.",
        "benefit_synopsis": "Deeply restorative practice that promotes interoception and relaxation.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "20 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "1–4 times per week",
        "is_common": False,
        "notes": "Often performed on the floor with eyes closed.",
        "objectives": ["release_habitual_tension", "restore_sensory_awareness", "deepen_relaxation"]
      },
      {
        "name": "Breath-Led Movement",
        "slug": "breath-led-movement",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Guide movement entirely through breath rhythms, creating a moving meditation.",
        "benefit_synopsis": "Supports nervous system balance and physical presence.",
        "recommended_durations": [{"duration_label": "5 minutes"}, {"duration_label": "15 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Anytime, especially transitions",
        "is_common": False,
        "notes": "Can be done seated, standing, or lying down.",
        "objectives": ["sync_breath_with_motion", "induce_calm", "build_body_awareness"]
      },
      {
        "name": "Intuitive Flow Practice",
        "slug": "intuitive-flow-practice",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Allow your body to guide the session with organic movement shaped by mood, breath, and instinct.",
        "benefit_synopsis": "Enhances connection to self and cultivates expressive movement.",
        "recommended_durations": [{"duration_label": "10 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "As needed",
        "is_common": False,
        "notes": "Put on music if desired. Let go of performance or structure.",
        "objectives": ["enhance_embodiment", "express_emotion_through_motion", "reconnect_with_sensation"]
      },
      {
        "name": "Pilates Mat Class",
        "slug": "pilates-mat-class",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Strengthen your core, alignment, and flexibility with a guided floor-based Pilates routine.",
        "benefit_synopsis": "Improves posture, core stability, and muscular control.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–4 times per week",
        "is_common": True,
        "notes": "Can be done with just a mat or using props like bands and balls.",
        "objectives": ["build_core_strength", "enhance_alignment", "increase_body_control"]
      },
      {
        "name": "Nia Class",
        "slug": "nia-class",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Blend dance, martial arts, and somatic movement for expressive, low-impact conditioning.",
        "benefit_synopsis": "Improves coordination, joy, and embodied awareness.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–3 times per week",
        "is_common": False,
        "notes": "Barefoot and expressive — combines music with full-body movement.",
        "objectives": ["cultivate_joy", "release_tension", "build_body_awareness"]
      },
      {
        "name": "Barre Fitness Class",
        "slug": "barre-fitness-class",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Use ballet-inspired movement and holds to train endurance, control, and joint stability.",
        "benefit_synopsis": "Enhances muscle tone and improves postural strength.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Often includes small weights, high reps, and balance work.",
        "objectives": ["improve_postural_control", "develop_endurance", "enhance_leg_and_core_strength"]
      },
      {
        "name": "Dance Fitness Class",
        "slug": "dance-fitness-class",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Follow guided dance routines for fun, cardio, and rhythm-based fitness.",
        "benefit_synopsis": "Improves coordination, mood, and cardiovascular health.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–5 times per week",
        "is_common": True,
        "notes": "Includes formats like Zumba, Afrobeat, or freestyle dance-based cardio.",
        "objectives": ["boost_energy", "enhance_coordination", "increase_cardio_output"]
      },
      {
        "name": "Classic Step Aerobics",
        "slug": "classic-step-aerobics",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Perform rhythmic, choreographed cardio routines using a raised platform.",
        "benefit_synopsis": "Strengthens legs, improves rhythm, and boosts aerobic output.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–4 times per week",
        "is_common": True,
        "notes": "Can be adapted for beginner or advanced routines.",
        "objectives": ["build_cardio_endurance", "train_footwork", "support_lower_body_strength"]
      },
      {
        "name": "Aerial Silks Practice",
        "slug": "aerial-silks-practice",
        "category": "movement-sport",
        "subcategory": "mindful-movement-flows",
        "description": "Climb, wrap, and balance using silks suspended from above to build strength and grace.",
        "benefit_synopsis": "Improves upper body strength, flexibility, and body awareness.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Requires access to silks and instructor for safety and technique.",
        "objectives": ["develop_grip_strength", "enhance_spatial_awareness", "build_confidence_through_movement"]
      }
    ],

    # PRACTICE SUBCATEGORY
    "sport-skill-training": [
      {
        "name": "Play Basketball",
        "slug": "play-basketball",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Shoot hoops solo or join a game to improve endurance, coordination, and agility.",
        "benefit_synopsis": "Combines cardio, fast decision-making, and teamwork.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Adjust intensity and structure based on solo play or group games.",
        "objectives": ["build_endurance", "improve_reaction_time", "enhance_coordination"]
      },
      {
        "name": "Play Soccer",
        "slug": "play-soccer",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Run, pass, and shoot to build speed, endurance, and leg strength.",
        "benefit_synopsis": "Develops cardiovascular fitness and footwork through continuous motion.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "90 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–2 times per week",
        "is_common": True,
        "notes": "Flexible structure — scrimmage, drills, or full matches.",
        "objectives": ["increase_leg_power", "enhance_team_dynamics", "boost_cardio"]
      },
      {
        "name": "Play Tennis",
        "slug": "play-tennis",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Work on rallies or matches to improve hand-eye coordination and lateral movement.",
        "benefit_synopsis": "Combines technical skill with quick reflexes and cardio.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Works well as a casual rally or competitive match.",
        "objectives": ["sharpen_focus", "improve_agility", "enhance_coordination"]
      },
      {
        "name": "Play Football",
        "slug": "play-football",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Play casual or competitive football to build power, agility, and strategy.",
        "benefit_synopsis": "Trains sprint endurance, teamwork, and explosive coordination.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 4,
        "frequency": "1–2 times per week",
        "is_common": True,
        "notes": "Touch, flag, or tackle formats — adapt based on environment.",
        "objectives": ["develop_speed", "enhance_teamwork", "improve_power_output"]
      },
      {
        "name": "Play Volleyball",
        "slug": "play-volleyball",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Serve, set, and spike in a fun volleyball match to train reflexes and coordination.",
        "benefit_synopsis": "Enhances timing, jumping power, and social connection.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Indoor, beach, or grass — adjust intensity as needed.",
        "objectives": ["improve_reaction_time", "build_leg_power", "foster_community"]
      },
      {
        "name": "Play Lacrosse",
        "slug": "play-lacrosse",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Run, pass, and shoot in lacrosse to develop coordination and total-body conditioning.",
        "benefit_synopsis": "Fast-paced sport that builds agility, cardio, and upper-body accuracy.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 4,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Requires stick and ball handling — great for high-speed movement practice.",
        "objectives": ["build_hand_eye_coordination", "improve_agility", "develop_cardio_capacity"]
      },
      {
        "name": "Play Water Polo",
        "slug": "play-water-polo",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Engage in a match or training session of water polo for full-body endurance and coordination.",
        "benefit_synopsis": "Combines swim conditioning with game-based movement strategy.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Requires pool and team setup. Demanding but rewarding.",
        "objectives": ["develop_swim_endurance", "improve_game_strategy", "increase_upper_body_control"]
      },
      {
        "name": "Play Baseball or Softball",
        "slug": "play-baseball-softball",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Play catch, join a game, or hit the batting cage for skill-based physical activity.",
        "benefit_synopsis": "Enhances timing, coordination, and sprint intervals.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "90 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–2 times per week",
        "is_common": True,
        "notes": "Good mix of intensity and downtime. Suitable for all ages.",
        "objectives": ["build_kinesthetic_awareness", "train_focus", "develop_rotational_strength"]
      },
      {
        "name": "Play Pickleball",
        "slug": "play-pickleball",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Play singles or doubles pickleball for fun, fast-paced rallies and social fitness.",
        "benefit_synopsis": "Improves hand-eye coordination, agility, and light cardio.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–4 times per week",
        "is_common": True,
        "notes": "Easy to learn, fun to play — great for all ages and fitness levels.",
        "objectives": ["enhance_coordination", "promote_social_connection", "build_cardio_endurance"]
      },
      {
        "name": "Play Racquetball",
        "slug": "play-racquetball",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Play against a wall or in a match to challenge reaction time and rotational power.",
        "benefit_synopsis": "Fast-paced indoor game that develops quickness and hand speed.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "60 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Great indoor option. Intense and highly reactive sport.",
        "objectives": ["increase_reaction_speed", "develop_rotation", "improve_stamina"]
      },
      {
        "name": "Play Table Tennis",
        "slug": "play-table-tennis",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Play ping pong to sharpen your reflexes, coordination, and focus.",
        "benefit_synopsis": "Improves precision, timing, and mental engagement.",
        "recommended_durations": [
          { "duration_label": "15 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "1–5 times per week",
        "is_common": True,
        "notes": "Can be recreational or competitive. Great for indoor fun.",
        "objectives": ["train_hand_eye_coordination", "boost_focus", "enhance_reaction_time"]
      },
      {
        "name": "Play Badminton",
        "slug": "play-badminton",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Smash, serve, and volley in a fast-paced court game that challenges agility and control.",
        "benefit_synopsis": "Improves footwork, coordination, and light aerobic conditioning.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Light gear, low barrier — high-speed movement in short bursts.",
        "objectives": ["enhance_reaction_speed", "train_controlled_power", "improve_mobility"]
      },
      {
        "name": "Play Squash",
        "slug": "play-squash",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Use agility and angles in a high-intensity match that blends cardio and strategy.",
        "benefit_synopsis": "Trains quick footwork, anticipation, and anaerobic conditioning.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "1–2 times per week",
        "is_common": False,
        "notes": "Very physically demanding — ideal for small indoor courts.",
        "objectives": ["develop_footwork", "boost_strategy", "maximize_cardio_output"]
      },
      {
        "name": "Swim",
        "slug": "swim",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Swim laps or float with intention to train endurance and support joint health.",
        "benefit_synopsis": "Low-impact strength and cardiovascular training.",
        "recommended_durations": [
          { "duration_label": "20 minutes" },
          { "duration_label": "45 minutes" }
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "1–3 times per week",
        "is_common": True,
        "notes": "Can be relaxing or high intensity — adaptable to your goals.",
        "objectives": ["increase_aerobic_capacity", "build_muscular_balance", "promote_joint_health"]
      },
      {
        "name": "Go for a Hike",
        "slug": "go-for-a-hike",
        "category": "movement-sport",
        "subcategory": "recreation-sport",
        "description": "Walk on trails in nature to improve mood, leg strength, and aerobic conditioning.",
        "benefit_synopsis": "Builds endurance while reducing stress and enhancing mental clarity.",
        "recommended_durations": [
          { "duration_label": "30 minutes" },
          { "duration_label": "90 minutes" }
        ],
        "impact_rating_id": 3,
        "difficulty_level_id": 2,
        "frequency": "1–4 times per week",
        "is_common": True,
        "notes": "Choose flat or hilly terrain to match effort and recovery needs.",
        "objectives": ["connect_with_nature", "improve_endurance", "elevate_mood"]
      }
    ]
  }

  #   # PRACTICE CATEGORY
  # "Digital Boundaries & Dopamine Regulation": {},

  #   # PRACTICE CATEGORY
  # "Nutrition & Fuel": {},

  #   # PRACTICE CATEGORY
  # "Purpose, Planning, and Deep Work": {},

  #   # PRACTICE CATEGORY
  # "Building Connections": {},

}


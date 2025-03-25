practice_data = {
# Health & Wellness Practices

# TODO: ADD Column for 'environmental queue', allowing users to select or create queues or prompts to remind them of practices.

# These will shift toward "categorical recommendations", from which users will select 
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
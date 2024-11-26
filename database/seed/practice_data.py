practice_data = {
# Health & Wellness Practices
'General Health': [
    {
        "name": "Morning Hydration",
        "description": "Drink a glass of water to kickstart your metabolism and hydration.",
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
        "recommended_durations": [{"duration_label": "1 minute"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "As needed",
        "is_common": True,
        "notes": "Adjust your chair, desk, and screen height to maintain an ergonomic setup.",
        "objectives": ["reduce_muscle_tension", "enhance_mobility", "promote_energy_efficiency"]
    },
    {
        "name": "Digital Detox Period",
        "description": "Spend time away from screens to reset your mind and reduce strain.",
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
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Twice daily",
        "is_common": True,
        "notes": "Consider preparing your breakfast the night before if mornings are rushed. Avoid high-sugar options like pastries or sugary cereals.",
        "objectives": ["promote_healthy_aging", "enhance_mood_stability", "increase_energy_levels"]
    },
    {
        "name": "Take Supplements",
        "description": "Take any necessary morning supplements (e.g., vitamins, minerals).",
        "recommended_durations": [{"duration_label": "2 minutes"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Please ensure supplements are checked by a healthcare professional. Oversupplementation can be more harmful than good and supplements should complement, not replace, a healthy diet.",
        "objectives": ["boost_immune_system", "promote_healthy_aging", "improve_mental_clarity"]
    },
    {
        "name": "Balanced Macronutrient Choices",
        "description": "Aim to balance macronutrients in each meal, including a source of protein, complex carbohydrates, and healthy fats.",
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
        "name": "General Workout",
        "description": "Engage in a workout of your choice, including strength training, cardio, or a mix of both.",
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
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "45 minutes"}, {"duration_label": "60 minutes"}, {"duration_label": "90 minutes"}, {"duration_label": "2 hours"}],
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
        "name": "Vipassana Meditation",
        "description": "Engage in a focused meditation practice aimed at gaining insight into the nature of reality.",
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
        "recommended_durations": [
            {"duration_label": "15 minutes"}
        ],
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
        "recommended_durations": [
            {"duration_label": "15 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": False,
        "notes": "This practice is especially helpful for long-term planning and goal setting.",
        "objectives": ["enhance_focus", "increase_optimism", "promote_goal_alignment"]
    },
    {
        "name": "Sensory Grounding (5-4-3-2-1 Technique)",
        "description": "Engage the five senses to bring yourself to the present moment.",
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
        'name': 'Aromatherapy', 
        'description': 'Use essential oils to activate your sense of smell and promote calm.', 
        'recommended_durations': [{'duration_label': '5 minutes'}], 
        'impact_rating_id': 4, 
        'difficulty_level_id': 1,
        'frequency': 'Twice daily',  
        'is_common': True,
        'objectives': ['reduce_stress', 'enhance_mood_stability', 'improve_focus']
    },
    {
        'name': 'Nature Walk', 
        'description': 'Take a walk in a park or forest to connect with nature.', 
        'recommended_durations': [{'duration_label': '30 minutes'}], 
        'impact_rating_id': 5, 
        'difficulty_level_id': 2,
        'frequency': 'Daily',  
        'is_common': True,
        'objectives': ['reduce_stress', 'enhance_mood_stability', 'increase_optimism']
    },
    {
        'name': 'Grounding Exercise', 
        'description': 'Walk barefoot on grass or sand to reconnect with the earth.', 
        'recommended_durations': [{'duration_label': '15 minutes'}], 
        'impact_rating_id': 4, 
        'difficulty_level_id': 2,
        'frequency': 'Twice daily',  
        'is_common': True,
        'objectives': ['reduce_stress', 'enhance_emotional_regulation', 'improve_balance']
    },
],

"Spiritual Connection & Gratitude": [
    {
        'name': 'Gratitude Practice', 
        'description': 'List three things you are grateful for to foster a positive mindset.', 
        'recommended_durations': [{'duration_label': '5 minutes'}], 
        'impact_rating_id': 4, 
        'difficulty_level_id': 1,
        'frequency': 'Twice daily',  
        'is_common': True,
        'objectives': ['cultivate_gratitude', 'increase_optimism', 'reduce_stress']
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
        "name": "Gratitude Letters",
        "description": "Write a letter to someone you’re grateful for, expressing your appreciation.",
        "recommended_durations": [
            {"duration_label": "10 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": False,
        "notes": "Consider delivering the letter in person or reading it aloud to deepen the connection.",
        "objectives": ["strengthen_relationships", "increase_empathy", "enhance_mood_stability"]
    },
    {
        'name': 'Prayer',
        'description': 'Engage in personal or traditional prayer to connect spiritually.',
        'recommended_durations': [{'duration_label': '10 minutes'}],
        'impact_rating_id': 5,
        'difficulty_level_id': 2,
        'frequency': 'Twice daily',
        'is_common': True,
        'objectives': ['develop_spiritual_resilience', 'enhance_self-awareness', 'reduce_stress']
    },
    {
        'name': 'Devotional reading',
        'description': 'Read passages from sacred texts to gain insight and reflect on purpose.',
        'recommended_durations': [{'duration_label': '15 minutes'}],
        'impact_rating_id': 5,
        'difficulty_level_id': 3,
        'frequency': 'Twice daily',
        'is_common': True,
        'objectives': ['increase_clarity', 'cultivate_a_sense_of_wonder', 'develop_patience']
    },
    {
        "name": "Loving-Kindness Meditation",
        "description": "Send kindness and compassion to yourself and others.",
        "recommended_durations": [
            {"duration_label": "10 minutes"},
            {"duration_label": "15 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Repeat phrases like 'May I be happy, may I be healthy' for yourself and extend them to others.",
        "objectives": ["increase_empathy", "enhance_mood_stability", "reduce_stress"]
    },
    {
        "name": "Nature Immersion",
        "description": "Spend time in nature to recharge and reduce stress.",
        "recommended_durations": [
            {"duration_label": "15 minutes"},
            {"duration_label": "30 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Take a walk in the park, hike in the woods, or simply sit outdoors and appreciate your surroundings.",
        "objectives": ["enhance_mood_stability", "reduce_stress", "promote_mind-body_connection"]
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
        "objectives": ["enhance_spiritual_connection", "increase_optimism", "promote_emotional_resilience"]
    },
    {
        "name": "Ritual of Intention",
        "description": "Set a daily intention or affirmation to align your actions with your values and goals.",
        "recommended_durations": [
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Pair this ritual with prayer, journaling, or quiet reflection for added meaning.",
        "objectives": ["improve_focus", "enhance_spiritual_connection", "promote_goal_alignment"]
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
        "objectives": ["increase_self-confidence", "enhance_focus", "reduce_negative_self-talk"]
    },
    {
        "name": "Mantra Meditation",
        "description": "Focus on repeating a calming word, phrase, or sound to settle the mind.",
        "recommended_durations": [
            {"duration_label": "10 minutes"},
            {"duration_label": "15 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Mantras like 'Om' or personal phrases can promote clarity and a sense of peace.",
        "objectives": ["enhance_spiritual_connection", "reduce_stress", "improve_focus"]
    },
    {
        "name": "Call to Purpose Affirmation",
        "description": "Recite affirmations that align with your higher purpose or core values.",
        "recommended_durations": [
            {"duration_label": "5 minutes"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use affirmations like 'I am here to contribute to the well-being of others' or 'I act in alignment with my values.'",
        "objectives": ["enhance_spiritual_connection", "improve_goal_alignment", "increase_focus"]
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
        "objectives": ["increase_self-confidence", "reduce_negative_self-talk", "promote_goal_alignment"]
    }
],

'Cold Exposure': [
    {
        'name': 'Cold Shower', 
        'description': 'Take a cold shower to invigorate the body and improve circulation.', 
        'recommended_durations': [{'duration_label': '5 minutes'}], 
        'impact_rating_id': 4, 
        'difficulty_level_id': 3,
        'frequency': 'Twice daily',  
        'is_common': True,
        'objectives': ['increase_stress_resilience', 'improve_emotional_regulation', 'enhance_mood_stability']
    },
    {
        'name': 'Cold Face Rinse', 
        'description': 'Splash cold water on your face to awaken your senses and reduce puffiness.', 
        'recommended_durations': [{'duration_label': '1 minute'}], 
        'impact_rating_id': 4, 
        'difficulty_level_id': 4,
        'frequency': 'Twice daily',  
        'is_common': True,
        'objectives': ['increase_alertness', 'improve_emotional_regulation', 'reduce_inflammation']
    },
    {
        'name': 'Cold Plunge', 
        'description': 'Immerse yourself in cold water to boost circulation and mental toughness.', 
        'recommended_durations': [{'duration_label': '10 minutes'}], 
        'impact_rating_id': 5, 
        'difficulty_level_id': 5,
        'frequency': 'Daily',  
        'is_common': True,
        'objectives': ['increase_stress_resilience', 'reduce_inflammation', 'enhance_mood_stability']
    },
],

'Focused Value Time': [
    {
        'name': 'Deep Work Session',
        'description': 'Dedicate time to focused, undistracted work on a high-value task.',
        'recommended_durations': [{'duration_label': '20 minutes'}],
        'impact_rating_id': 5,
        'difficulty_level_id': 2,
        'frequency': 'Twice daily',
        'is_common': True,
        'objectives': ['increase_productivity', 'enhance_focus', 'reduce_stress']
    },
    {
        'name': 'Value Alignment Journaling',
        'description': 'Reflect on your goals and values to ensure alignment with your actions.',
        'recommended_durations': [{'duration_label': '30 minutes'}],
        'impact_rating_id': 5,
        'difficulty_level_id': 3,
        'frequency': 'Three times daily',
        'is_common': True,
        'objectives': ['clarity', 'increase_self-awareness', 'enhance_motivation']
    },
],
'Skill Learning': [
    {
        'name': 'Language Practice',
        'description': 'Practice a new language using an app or flashcards.',
        'recommended_durations': [{'duration_label': '20 minutes'}],
        'impact_rating_id': 5,
        'difficulty_level_id': 3,
        'frequency': 'Twice daily',
        'is_common': True,
        'objectives': ['improve_language_skills', 'enhance_memory', 'develop_cognitive_resilience']
    },
    {
        'name': 'Instrument Practice',
        'description': 'Learn or practice a musical instrument to enhance coordination and memory.',
        'recommended_durations': [{'duration_label': '30 minutes'}],
        'impact_rating_id': 5,
        'difficulty_level_id': 3,
        'frequency': 'Three times daily',
        'is_common': True,
        'objectives': ['improve_coordination', 'enhance_creative_thinking', 'reduce_stress']
    },
],
'Creative Flow Time': [
    {
        'name': 'Free Writing', 
        'description': 'Spend time writing whatever comes to mind to unleash creativity.', 
        'recommended_durations': [{'duration_label': '30 minutes'}], 
        'impact_rating_id': 5, 
        'difficulty_level_id': 3,
        'frequency': 'Daily',  
        'is_common': True,
        'objectives': ['enhance_creative_thinking', 'improve_language_skills', 'reduce_stress']
    },
    {
        'name': 'Sketching', 
        'description': 'Draw or doodle to foster creative expression and mindfulness.', 
        'recommended_durations': [{'duration_label': '20 minutes'}], 
        'impact_rating_id': 4, 
        'difficulty_level_id': 3,
        'frequency': 'Twice daily',  
        'is_common': True,
        'objectives': ['develop_artistic_skills', 'enhance_pattern_recognition', 'reduce_stress']
    },
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
        "notes": "Apps like Duolingo or flashcard systems like Anki can help. Practicing with a language partner is highly effective.",
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
        "notes": "Focus on consistent, deliberate practice. Consider online tutorials or lessons for guidance.",
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
        "notes": "Choose topics that interest you or align with your goals, such as self-help, fiction, or technical books.",
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
        "notes": "Consider using prompts to get started, such as 'Write about a memorable day' or 'Create a fictional character.'",
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
        "notes": "Use platforms like Codecademy, freeCodeCamp, or LeetCode for structured learning.",
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
        "notes": "Try Toastmasters, recording yourself, or practicing speeches in front of friends for feedback.",
        "objectives": ["improve_communication", "increase_self-confidence", "reduce_speaking_anxiety"]
    },
    {
        "name": "Art Practice",
        "description": "Engage in drawing, painting, or other artistic practices to enhance creativity and mindfulness.",
        "recommended_durations": [
            {"duration_label": "20 minutes"},
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Experiment with different mediums such as watercolor, acrylics, or digital art tools.",
        "objectives": ["enhance_creative_thinking", "reduce_stress", "promote_mindfulness"]
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
        "notes": "Apps like Lumosity or traditional puzzles are great tools. Focus on challenging but enjoyable puzzles.",
        "objectives": ["enhance_memory", "develop_cognitive_resilience", "improve_problem_solving"]
    },
    {
        "name": "Debate Practice",
        "description": "Engage in friendly debates to improve critical thinking and communication skills.",
        "recommended_durations": [
            {"duration_label": "30 minutes"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Choose topics you're passionate about and practice articulating arguments clearly and calmly.",
        "objectives": ["improve_communication", "enhance_critical_thinking", "increase_self-confidence"]
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
        "notes": "Projects like building furniture, crafting, or home repairs can be both rewarding and practical.",
        "objectives": ["enhance_creative_thinking", "improve_problem_solving", "increase_self-confidence"]
    },
    {
        "name": "Gardening",
        "description": "Spend time gardening to connect with nature and build patience and responsibility.",
        "recommended_durations": [
            {"duration_label": "30 minutes"},
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Start with herbs, flowers, or vegetables. Gardening can also improve mood and physical health.",
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
        "notes": "Use platforms like LinkedIn Learning, Coursera, or Skillshare for structured lessons tailored to your field. Focus on skills that directly contribute to your career growth.",
        "objectives": ["improve_professional_skills", "increase_confidence", "enhance_career_progression"]
    },
    {
        "name": "Networking",
        "description": "Engage with industry professionals to exchange ideas and opportunities.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Attend virtual or in-person events, join LinkedIn groups, or connect with colleagues. Networking is a long-term investment in professional relationships.",
        "objectives": ["build_professional_network", "gain_new_opportunities", "enhance_communication_skills"]
    },
    {
        "name": "Certification Preparation",
        "description": "Study for a professional certification, such as PMP, CPA, or AWS.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Follow official prep courses or community resources. Break learning into manageable sessions and set deadlines to stay on track.",
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
        "notes": "Tailor resumes to specific roles. Include measurable achievements for greater impact.",
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
        "notes": "Experiment with different settings, compositions, and lighting. Explore editing tools like Lightroom or Photoshop to enhance your photos.",
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
        "notes": "Look for local theater groups or online classes for beginners. Improv exercises are particularly effective for thinking on your feet and improving public speaking skills.",
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
        "notes": "Read resources on communication strategies and active listening. Role-playing scenarios can help apply new skills effectively.",
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
        "notes": "Reflect weekly on what worked and adjust your approach for better results. Tools like Trello or Notion can be helpful.",
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
        "notes": "Use kits like Arduino or Raspberry Pi to get started with programming and electronics.",
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
        "notes": "Platforms like Kaggle or TensorFlow tutorials provide hands-on learning opportunities.",
        "objectives": ["enhance_career_skills", "develop_problem_solving", "increase_knowledge"]
    },
    {
        "name": "Cooking or Baking",
        "description": "Experiment with new recipes or techniques to improve culinary skills.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Consider themed challenges (e.g., vegan cooking) or specialty baking like sourdough bread.",
        "objectives": ["enhance_creative_thinking", "develop_practical_skills", "reduce_stress"]
    },
    {
        "name": "First Aid Training",
        "description": "Learn or refresh basic first aid and CPR skills.",
        "recommended_durations": [{"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Annually",
        "is_common": False,
        "notes": "Look for Red Cross or local community workshops. Skills include wound care and emergency response.",
        "objectives": ["enhance_safety_awareness", "increase_confidence", "reduce_emergency_risk"]
    },
    {
        "name": "Esports Practice",
        "description": "Dedicate time to improving competitive gaming skills for esports or tournaments.",
        "recommended_durations": [
            {"duration_label": "1 hour"},
            {"duration_label": "2 hours"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on practicing mechanics, game strategies, and teamwork for specific games. Join online communities or scrims to enhance skills.",
        "objectives": ["develop_strategic_thinking", "improve_reaction_time", "enhance_teamwork"]
    },
    {
        "name": "Game Design Practice",
        "description": "Learn or practice game design concepts, including level creation, mechanics, and storytelling.",
        "recommended_durations": [
            {"duration_label": "1 hour"},
            {"duration_label": "2 hours"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Weekly",
        "is_common": False,
        "notes": "Tools like Unity, Unreal Engine, or RPG Maker are great for developing games. Focus on creativity and usability in design.",
        "objectives": ["enhance_creative_thinking", "develop_technical_skills", "improve_problem_solving"]
    },
    {
        "name": "Streaming Content Creation",
        "description": "Stream gameplay and create gaming content for platforms like Twitch or YouTube.",
        "recommended_durations": [
            {"duration_label": "2 hours"},
            {"duration_label": "4 hours"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Focus on engaging with your audience and improving video/audio quality. Explore editing software for highlight videos.",
        "objectives": ["develop_communication_skills", "build_online_presence", "enhance_creative_expression"]
    },
    {
        "name": "Speedrunning Practice",
        "description": "Refine skills for completing games as quickly as possible, optimizing routes and techniques.",
        "recommended_durations": [
            {"duration_label": "1 hour"},
            {"duration_label": "3 hours"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": False,
        "notes": "Join speedrunning communities to learn advanced techniques and share strategies for specific games.",
        "objectives": ["enhance_focus", "improve_reaction_time", "develop_problem_solving"]
    },
    {
        "name": "Game Strategy Research",
        "description": "Study strategies, meta-analysis, or guides to improve your understanding of specific games.",
        "recommended_durations": [
            {"duration_label": "30 minutes"},
            {"duration_label": "1 hour"}
        ],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Browse forums, watch professional players, or read strategy guides to improve your gameplay knowledge.",
        "objectives": ["develop_strategic_thinking", "improve_knowledge", "enhance_focus"]
    }
],

'Social Connection': [
    {
        "name": "Morning Check-In",
        "description": "Call or message a loved one to connect and start the day positively.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Consider asking open-ended questions like 'How are you really feeling today?' to deepen your connection.",
        "objectives": ["enhance_relationships", "develop_empathy", "boost_optimism"]
    },
    {
        "name": "Coffee Chat",
        "description": "Meet a friend or colleague for coffee to foster meaningful interaction.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Use this time to share updates, offer support, or brainstorm ideas. Avoid distractions like checking your phone.",
        "objectives": ["enhance_relationships", "improve_communication_skills", "develop_empathy"]
    },
    {
        "name": "Book Club",
        "description": "Join or start a book club to discuss literature and connect with others.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Monthly",
        "is_common": True,
        "notes": "Select books that challenge or inspire, and focus on creating an inclusive, welcoming environment.",
        "objectives": ["develop_critical_thinking", "enhance_relationships", "promote_emotional_resilience"]
    },
    {
        "name": "Men’s/Women’s Group",
        "description": "Participate in a supportive group tailored to shared life experiences or goals.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "90 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "These groups can provide a safe space to discuss challenges, celebrate wins, and share resources.",
        "objectives": ["build_emotional_resilience", "enhance_support_systems", "develop_empathy"]
    },
    {
        "name": "Community Service",
        "description": "Volunteer in your community to connect with others while contributing to a cause.",
        "recommended_durations": [{"duration_label": "2 hours"}, {"duration_label": "4 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": True,
        "notes": "Options include food banks, animal shelters, or local clean-up events. Choose causes aligned with your values.",
        "objectives": ["enhance_relationships", "boost_community_engagement", "increase_self-worth"]
    },
    {
        "name": "Interest-Specific Groups",
        "description": "Join a group that aligns with your hobbies or interests, such as hiking, gaming, or knitting.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Search for local meetups or online communities. Activities like D&D groups or running clubs foster both fun and connection.",
        "objectives": ["enhance_social_skills", "develop_common_interests", "reduce_social_isolation"]
    },
    {
        "name": "Game Night with Friends",
        "description": "Host or join a game night to enjoy time with friends and strengthen connections.",
        "recommended_durations": [{"duration_label": "2 hours"}, {"duration_label": "3 hours"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Monthly",
        "is_common": True,
        "notes": "Board games, card games, or even video games work well. Focus on creating a light-hearted, inclusive atmosphere.",
        "objectives": ["enhance_relationships", "develop_teamwork", "reduce_stress"]
    },
    {
        "name": "Outdoor Activities with Friends",
        "description": "Plan activities like hiking, kayaking, or picnics to enjoy nature and bond with friends.",
        "recommended_durations": [{"duration_label": "2 hours"}, {"duration_label": "Half day"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Monthly",
        "is_common": True,
        "notes": "Choose activities that match everyone’s fitness level and preferences for maximum enjoyment.",
        "objectives": ["reduce_stress", "enhance_relationships", "promote_healthy_lifestyles"]
    },
    {
        "name": "Weekly Dinner with Friends or Family",
        "description": "Schedule a regular meal to connect with loved ones and share your week.",
        "recommended_durations": [{"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Make it a potluck or rotate hosts to keep things fun and stress-free.",
        "objectives": ["enhance_relationships", "reduce_stress", "build_emotional_resilience"]
    },
    {
        "name": "Support Group Participation",
        "description": "Join a support group for shared experiences, such as parenting, recovery, or grief support.",
        "recommended_durations": [{"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Support groups can provide emotional connection and practical advice for navigating challenges.",
        "objectives": ["develop_empathy", "enhance_emotional_resilience", "build_support_networks"]
    },
    {
        "name": "Lunch Break Socializing",
        "description": "Use your lunch break to catch up with a coworker or friend.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 3,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Keep the conversation light and enjoyable. This can strengthen workplace relationships or friendships.",
        "objectives": ["enhance_relationships", "reduce_stress", "boost_optimism"]
    }
],

'Productivity Anchors': [
    {
        "name": "Daily Prioritization",
        "description": "Write down the top 3 tasks to accomplish today.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on tasks that align with your larger goals and tackle them in order of priority.",
        "objectives": ["improve_focus", "increase_productivity", "reduce_stress"]
    },
    {
        "name": "Goal Visualization",
        "description": "Visualize achieving your long-term goals to stay motivated.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use visualization techniques like imagining the steps to achieve your goals and the emotions tied to success.",
        "objectives": ["clarity", "increase_motivation", "reduce_stress"]
    },
    {
        "name": "Pomodoro Technique",
        "description": "Work in focused intervals with short breaks in between to maintain energy and focus.",
        "recommended_durations": [{"duration_label": "25 minutes work, 5 minutes break"}, {"duration_label": "4 cycles of 25/5 minutes with a 15-minute break"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "This technique helps break tasks into manageable chunks and prevents burnout. Use a timer for accuracy.",
        "objectives": ["enhance_focus", "increase_productivity", "reduce_stress"]
    },
    {
        "name": "Deep Work Blocks",
        "description": "Dedicate uninterrupted time to work on cognitively demanding tasks.",
        "recommended_durations": [{"duration_label": "1 hour"}, {"duration_label": "2 hours"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 4,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Eliminate distractions such as phone notifications and emails. Use this time for critical, high-value work.",
        "objectives": ["improve_focus", "enhance_problem_solving", "increase_productivity"]
    },
    {
        "name": "Time Blocking",
        "description": "Schedule your day into specific blocks of time for focused work, breaks, and relaxation.",
        "recommended_durations": [
            {"duration_label": "10 minutes (planning)"},
            {"duration_label": "1-2 hours (morning routine block)"},
            {"duration_label": "1-3 hours (deep work block)"},
            {"duration_label": "30 minutes (break/transition block)"},
            {"duration_label": "1-2 hours (administrative block)"},
            {"duration_label": "8 hours (daily schedule)"},
            {"duration_label": "1-2 hours (evening routine block)"}
        ],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Include buffer time between tasks to avoid feeling rushed. Review your time blocks at the end of the day.",
        "objectives": ["enhance_time_management", "increase_productivity", "reduce_decision_fatigue"]
    },
    {
        "name": "Batch Tasking",
        "description": "Group similar tasks together to maximize efficiency and minimize context switching.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Examples include responding to emails at a set time or doing all errands in one trip.",
        "objectives": ["increase_efficiency", "reduce_context_switching", "enhance_focus"]
    },
    {
        "name": "Morning Review",
        "description": "Spend time reviewing your goals and priorities for the day before starting work.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "This practice helps align your actions with your overall objectives and ensures clarity.",
        "objectives": ["clarity", "improve_focus", "reduce_stress"]
    },
    {
        "name": "Evening Reflection",
        "description": "Reflect on the day's accomplishments and plan for tomorrow.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use a journal or app to track progress and identify areas for improvement.",
        "objectives": ["enhance_self-awareness", "reduce_stress", "increase_motivation"]
    },
    {
        "name": "Two-Minute Rule",
        "description": "Complete tasks immediately if they take two minutes or less.",
        "recommended_durations": [{"duration_label": "Throughout the day"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "This helps prevent small tasks from piling up. Use this rule for quick emails, tidying, or simple errands.",
        "objectives": ["increase_efficiency", "reduce_procrastination", "enhance_focus"]
    },
    {
        "name": "Eisenhower Matrix",
        "description": "Organize tasks into categories based on urgency and importance to prioritize effectively.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Quadrants include: Urgent & Important, Not Urgent & Important, Urgent & Not Important, and Not Urgent & Not Important.",
        "objectives": ["enhance_decision_making", "improve_time_management", "reduce_overwhelm"]
    },
    {
        "name": "Weekly Goal Review",
        "description": "Evaluate progress on weekly goals and set priorities for the next week.",
        "recommended_durations": [{"duration_label": "30 minutes"}, {"duration_label": "1 hour"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Use a journal or goal-tracking app to monitor progress and adjust strategies as needed.",
        "objectives": ["increase_productivity", "enhance_motivation", "clarity"]
    },
    {
        "name": "Focus Sprints",
        "description": "Work in short, high-intensity bursts on specific tasks to maximize productivity.",
        "recommended_durations": [{"duration_label": "15 minutes"}, {"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Use a timer to keep yourself accountable. Adjust sprint length based on task complexity and your energy levels.",
        "objectives": ["enhance_focus", "increase_efficiency", "reduce_procrastination"]
    },
    {
        "name": "Energy Mapping",
        "description": "Align tasks with your natural energy levels throughout the day.",
        "recommended_durations": [{"duration_label": "15 minutes (planning)"}, {"duration_label": "Throughout the day"}, {"duration_label": "4-6 cycles of 90 minutes (ultradian rhythm blocks)"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 3,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Schedule demanding tasks during peak energy times and less-intensive tasks during low-energy periods.",
        "objectives": ["enhance_time_management", "increase_efficiency", "reduce_burnout"]
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
        "objectives": ["reduce_stress", "enhance_mood_stability", "promote_relaxation"]
    },
    {
        "name": "Gentle Crafting",
        "description": "Engage in crafting activities like knitting, crocheting, or scrapbooking to relax and unwind.",
        "recommended_durations": [{"duration_label": "30 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 2,
        "frequency": "Weekly",
        "is_common": True,
        "notes": "Focus on crafts that you enjoy and that don’t require high stress or precision.",
        "objectives": ["enhance_creativity", "reduce_stress", "promote_mindfulness"]
    },
    {
        "name": "Pet Time",
        "description": "Spend time bonding with a pet to relax and enhance mood.",
        "recommended_durations": [{"duration_label": "15 minutes"}],
        "impact_rating_id": 5,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Activities like walking a dog, playing, or simply cuddling can reduce stress and increase joy.",
        "objectives": ["reduce_stress", "enhance_mood_stability", "promote_connection"]
    },
    {
        "name": "Visualization for Relaxation",
        "description": "Close your eyes and visualize a peaceful scene or memory to calm your mind.",
        "recommended_durations": [{"duration_label": "10 minutes"}],
        "impact_rating_id": 4,
        "difficulty_level_id": 1,
        "frequency": "Daily",
        "is_common": True,
        "notes": "Focus on details such as colors, sounds, and sensations to make the visualization vivid.",
        "objectives": ["reduce_stress", "enhance_focus", "improve_mood_stability"]
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
        "objectives": ["enhance_mood_stability", "reduce_stress", "promote_positivity"]
    }
],
# Addiction and substance related abstinence
}


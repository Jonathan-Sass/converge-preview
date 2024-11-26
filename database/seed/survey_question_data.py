# ADD QUESTIONS ABOUT SCREEN TIME AND DOPAMINE RELATED DESIRES/DRIVERS/RESPONSES
survey_question_data = [
        {
            'topic_slug': 'getting-to-know-you', 
            'questions': [
                {
                    'question_slug': 'overall-well-being-self-assessment', 
                    'question_text': "How would you describe your overall well-being?", 
                    'type': 'guided-choice',
                    'answers': [
                        {'answer_text': 'I feel great physically and mentally', 'answer_value': 6},
                        {'answer_text': 'I feel good overall, with some room for improvement.', 'answer_value': 5},
                        {'answer_text': 'I feel okay, but there are areas I want to work on.', 'answer_value': 4},
                        {'answer_text': 'My mental health is generally good, but my physical health could be better.', 'answer_value': 3},
                        {'answer_text': 'My physical health is generally good, but I would like to improve my mental health.', 'answer_value': 2},
                        {'answer_text': 'I often feel tired, stressed, or unwell.', 'answer_value': 1},
                        {'answer_text': 'My physical and/or mental well-being is a constant struggle', 'answer_value': 0}
                    ]
                }, 
                {
                    'question_slug': 'life-balance-satisfaction', 
                    'question_text': "How balanced do you feel across different areas of your life, like work, personal time, and leisure?", 
                    'type': 'satisfaction-balance'
                }, 
                {
                    'question_slug': 'energy-levels-general', 
                    'question_text': "How would you describe your energy levels throughout a typical day?", 
                    'type': 'guided-choice',
                    'answers': [
                        {'answer_text': "Consistent energy throughout the day", 'answer_value': 7},
                        {'answer_text': "Good energy in the morning, but it fades in the afternoon", 'answer_value': 6},
                        {'answer_text': "Low energy in the morning, improves later in the day", 'answer_value': 5},
                        {'answer_text': "I have energy, but it often feels buzzy or hyperactive", 'answer_value': 4},
                        {'answer_text': "I have energy when I am active, but can easily get tired or fall asleep when inactive.", 'answer_value': 3},
                        {'answer_text': "High at night with difficulty going to sleep when I need", 'answer_value': 2},
                        {'answer_text': "Varies day to day", 'answer_value': 1},
                        {'answer_text': "Frequently low energy all day", 'answer_value': 0}
                    ]
                },
                {
                    'question_slug': 'sleep-wake-rested', 
                    'question_text': "Do you wake up feeling refreshed most mornings?", 
                    'type': 'frequency-day'
                },
                {
                    'question_slug': 'sleep-average-nightly', 
                    'question_text': "On average, how many hours of sleep do you get each night?", 
                    'type': 'range-hours-sleep',
                },
                {
                    'question_slug': 'stress-responsibility-management', 
                    'question_text': "How would you describe your daily workload - are you able to keep up with what's on your plate?", 
                    'type': 'frequency',
                    'answers': [
                        {'answer_text': 'Yes, I keep up well', 'answer_value': 4},
                        {'answer_text': 'Mostly, but it can be a challenge', 'answer_value': 3},
                        {'answer_text': "I manage, but sometimes it's too much", 'answer_value': 2},
                        {'answer_text': 'I often fall behind', 'answer_value': 1},
                        {'answer_text': 'I am unsure or inconsistent', 'answer_value': 0}
                    ]
                },
                {
                    'question_slug': 'stress-frequency-overburdened', 
                    'question_text': "How often do you feel overburdened by your to-dos and responsibilities?", 
                    'type': 'frequency'
                },
                {
                    'question_slug': 'stress-resilience-self-assessment', 
                    'question_text': "When it comes to handling stress, do you feel resilient and able to manage it effectively?", 
                    'type': 'scale-stress-resilience',
                },
                {
                    'question_slug': 'stress-resilience-beliefs', 
                    'question_text': "Do you believe that you can change your resilience to stress?", 
                    'type': 'yes-no-alittle',
                },
                {
                    'question_slug': 'stress-resilience-satisfaction', 
                    'question_text': "How satisfied are you with your level of resilience to stress?", 
                    'type': 'satisfaction'
                },
                
                {
                    'question_slug': 'satisfaction-current-fitness', 
                    'question_text': "How satisfied are you with your current fitness level?", 
                    'type': 'satisfaction'
                },
                {
                    'question_slug': 'satisfaction-work-situation', 
                    'question_text': "How would you rate your satisfaction with your current work situation?", 
                    'type': 'satisfaction'
                },
                {
                    'question_slug': 'satisfaction-relationships', 
                    'question_text': "How satisfied are you with your current relationships (friends, family, partners)?", 
                    'type': 'satisfaction'
                },
                # {
                #     'question_slug': 'satisfaction-current-energy', 
                #     'question_text': "How satisfied are you with your typical energy level?", 
                #     'type': 'satisfaction'
                # },
                {
                    'question_slug': 'adhd-self-assessment', 
                    'question_text': "Have you been diagnosed with ADHD, or do you feel you might exhibit ADHD-related behaviors? Examples can include, but are not limited to: difficulty maintaining focus, easily distracted, procrastination, difficulty with organization and time management, forgetfulness, impulsive behavior, restlessness or fidgeting, difficulty completing tasks, hyperfocus on certain activities, low frustration tolerance, emotional sensitivity and mood swings, poor working memory, interrupting or speaking out of turn, struggling to listen fully, zoning out easily, forgetting social commitments or details, challenges in group dynamics, difficulty with emotional regulation, low self-esteem or social anxiety, avoidance of social situations, difficulty building or maintaining friendships", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "Yes, I have been diagnosed.", 'answer_value': 3},
                        {'answer_text': "I think ADHD might be a factor in some of the issues I experience", 'answer_value': 2},
                        {'answer_text': "I'm not sure/haven't explored this", 'answer_value': 1},
                        {'answer_text': "I don't think I exhibit symptoms of ADHD", 'answer_value': 0},
                    ]
                },
                


                
                # {
                #     'question_slug': 'energy-type', 
                #     'question_text': "How would you describe your energy patterns?", 
                #     'type': 'guided-choice',
                #     'answers': [
                #         {'answer_text': "I have the energy I need most times, most days.", 'answer_value': 0},
                #         {'answer_text': "I have energy when I am active, but am tired when sedentary.", 'answer_value': 1},
                #         {'answer_text': "I feel like I have mental energy, but my body can't keep up.", 'answer_value': 2},
                #         {'answer_text': "I am mentally fatigued, but my body want to move.", 'answer_value': 3},
                #         {'answer_text': "Both my mind and my body are fatigued.", 'answer_value': 4},
                #         {'answer_text': "I can feel fatigued in the situations where I am overwhelmed or stressed.", 'answer_value': 5},
                #         {'answer_text': "I am tired unless I am engaged in something of interest.", 'answer_value': 6},
                #         {'answer_text': "None of the above.", 'answer_value': 7}
                #     ]
                # },
                
            ]
        },
        {
            'topic_slug': 'current-habits-patterns', 
            'questions': [
                {
                    'question_slug': 'am-self-care-time-current', 
                    'question_text': "Do you currently have a morning routine for personal time or self-care? If so, how much time do you set aside for it?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "No, none", 'answer_value': 0}, 
                        {'answer_text': "Less than 10 minutes", 'answer_value': 1}, 
                        {'answer_text': "10-20 minutes", 'answer_value': 2}, 
                        {'answer_text': "20-40 minutes", 'answer_value': 3}, 
                        {'answer_text': "40-60 minutes", 'answer_value': 4}, 
                        {'answer_text': "More than an hour", 'answer_value': 5}, 
                    ]
                },
                {
                    'question_slug': 'am-self-care-desire-more', 
                    'question_text': "Do you wish you had more of this time in your morning?", 
                    'type': 'yes-no'
                }, 
                {
                    'question_slug': 'am-self-care-ideal-morning', 
                    'question_text': "In your ideal world, how much morning personal/self-care time would you have?", 
                    'type': 'guided-choice',
                    'answers': [
                        {'answer_text': "I am not interested in morning self-care", 'answer_value': 0},
                        {'answer_text': "Less than 10 minutes", 'answer_value': 1},
                        {'answer_text': "10-20 minutes", 'answer_value': 2},
                        {'answer_text': "20-40 minutes", 'answer_value': 3},
                        {'answer_text': "40-60 minutes", 'answer_value': 4},
                        {'answer_text': "More than an hour", 'answer_value': 5}
                    ]
                }, 
                {
                    'question_slug': 'am-self-care-barriers', 
                    'question_text': "What are your barriers to having more morning self-care time?", 
                    'type': 'guided-choice',
                    'answers': [
                        {'answer_text': "None, I make the time I need.", 'answer_value': None},
                        {'answer_text': "Inconsistent Bedtime/Difficulty Falling Asleep", 'answer_value': None}, 
                        {'answer_text': "Poor Sleep Quality", 'answer_value': None},
                        {'answer_text': "Late-Night Responsibilities", 'answer_value': None},
                        {'answer_text': "Difficulty Waking Up", 'answer_value': None},
                        {'answer_text': "Early Work/Obligations", 'answer_value': None},
                        {'answer_text': "Overcommitted Schedule", 'answer_value': None},
                        {'answer_text': "Stress or Anxiety", 'answer_value': None},
                        {'answer_text': "Lack of Motivation in the Morning", 'answer_value': None},
                        {'answer_text': "Evening Screen Time", 'answer_value': None},
                        {'answer_text': "Household Responsibilities", 'answer_value': None},
                        {'answer_text': "Busy or Unpredictable Work Schedule", 'answer_value': None},
                        {'answer_text': "Long Commute", 'answer_value': None},
                        {'answer_text': "Difficulty Prioritizing Self-Care", 'answer_value': None},
                        {'answer_text': "Unpredictable Sleep Schedule", 'answer_value': None},
                        {'answer_text': "Need More Quiet or Private Space", 'answer_value': None},
                        {'answer_text': "Fatigue or Health Issues", 'answer_value': None},
                        {'answer_text': "Family Disruptions", 'answer_value': None}
                    ]
                }, 
                
                {
                    'question_slug': 'daily-habits-aspirations', 
                    'question_text': "Are there any positive daily habits you would like to implement into your day? (Select all that apply)", 
                    'type': 'select-any-add', 
                    'answers': [
                        {'answer_text': "Healthier food choices", 'answer_value': None},
                        {'answer_text': "Improved sleep schedule/hygiene", 'answer_value': None},
                        {'answer_text': "Building an exercise regimen", 'answer_value': None},
                        {'answer_text': "Spending more time outdoors", 'answer_value': None},
                        {'answer_text': "Practicing mindfulness, meditation or something similar", 'answer_value': None},
                        {'answer_text': "Daily prayer, journaling, and/or reflection", 'answer_value': None},
                        {'answer_text': "Staying more hydrated", 'answer_value': None},
                        {'answer_text': "Creating a space to set clear intentions for the day", 'answer_value': None},
                        {'answer_text': "Practicing gratitude", 'answer_value': None},
                        {'answer_text': "Spending more time reading or learning", 'answer_value': None},
                        {'answer_text': "Being more present with family or friends", 'answer_value': None},
                        {'answer_text': "Spending more quality time with family or friends", 'answer_value': None},
                        {'answer_text': "Decluttering or organizing my space", 'answer_value': None},
                        {'answer_text': "Positive self-talk and affirmations", 'answer_value': None},
                        {'answer_text': "Learning new skills or hobbies", 'answer_value': None},
                        {'answer_text': "Creating a budget or tracking finances", 'answer_value': None},
                        {'answer_text': "Volunteering or giving back", 'answer_value': None},
                        {'answer_text': "None of the above", 'answer_value': None},
                    ]
                },
                {
                    'question_slug': 'daily-habits-vices-to-change', 
                    'question_text': "Are there any daily habits(vices) you'd like to improve upon or change? (Select all that apply)", 
                    'type': 'select-any-add', 
                    'answers': [
                        {'answer_text': "Less screen time", 'answer_value': None},
                        {'answer_text': "Less social media", 'answer_value': None},
                        {'answer_text': "Healthier food choices", 'answer_value': None},
                        {'answer_text': "Improving regulation of procrastination", 'answer_value': None},
                        {'answer_text': "Cutting back on drinking, smoking or other substances", 'answer_value': None},
                        {'answer_text': "Reduce caffeine intake", 'answer_value': None},
                        {'answer_text': "Reduce impulse spending", 'answer_value': None},
                        {'answer_text': "Negative self-talk or self-criticism", 'answer_value': None},
                        {'answer_text': "Skip fewer meals", 'answer_value': None},
                        {'answer_text': "Multitask less or finish tasks before starting new ones", 'answer_value': None},
                        {'answer_text': "None of the above", 'answer_value': None}
                    ]
                },
                {
                    'question_slug': 'daily-habits-biggest-change', 
                    'question_text': "What is the one change that you feel would make the biggest positive impact in your life right now?", 
                    'type': 'select-any-add', 
                    'answers': [
                        {'answer_text': "To be populated from selected habits", 'answer_value': None}
                    ]
                },
                {
                    'question_slug': 'headspace-presence', 
                    'question_text': "How often do you find yourself thinking about the past and/or future?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "Very little, I tend to stay present in the moment", 'answer_value': 4},
                        {'answer_text': "I am often dwelling in the past", 'answer_value': 3},
                        {'answer_text': "I often find myself daydreaming about the future", 'answer_value': 2},
                        {'answer_text': "It varies day-to-day", 'answer_value': 1},
                        {'answer_text': "I am very often lost in thought/daydreaming in general", 'answer_value': 0},
                    ]
                },
                {
                    'question_slug': 'headspace-focus', 
                    'question_text': "How would you describe your ability to stay focused and free from distractions?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "I have rock solid focus", 'answer_value': 5},
                        {'answer_text': "I am not easily distracted but it does happen", 'answer_value': 4},
                        {'answer_text': "My focus is decent, but I sometimes experience inertia in getting started", 'answer_value': 3},
                        {'answer_text': "I can find myself hyperfocused on something I really enjoy", 'answer_value': 2},
                        {'answer_text': "I am easily distracted", 'answer_value': 1},
                        {'answer_text': "I have a difficult time motivating to do things I need or want to do", 'answer_value': 0}
                    ]
                },
                {
                    'question_slug': 'headspace-responsibility-sources', 
                    'question_text': "How many of your responsibilities are optional?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "My schedule is set in stone, non-negotiable", 'answer_value': 0},
                        {'answer_text': "I have some wiggle room in my day", 'answer_value': 1},
                        {'answer_text': "My schedule is fairly flexible", 'answer_value': 2},
                        {'answer_text': "I can move just about anything I want in my day", 'answer_value': 3}
                    ]
                },
                
            ]
        },
                    {
            'topic_slug': 'social-support-accountability', 
            'questions': [
                # Do you have a friend or friends who have might have similar goals or be similarly interested in personal growth based daily practices who could help you form an accountability team?
                {
                    'question_slug': 'support-system-status', 
                    'question_text': "How would you describe your support system?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "I have a very strong network of multiple people I can rely on unconditionally for support", 'answer_value': 4},
                        {'answer_text': "I have a few close individuals or groups who are there for me in most situations", 'answer_value': 3},
                        {'answer_text': "I have a mix of friends, family or acquaintanaces who can lend a hand or ear in specific circumstances and/or may not be consistently available", 'answer_value': 2},
                        {'answer_text': "I have one or two people I can turn to occasionally, and they may have limited availability or resources", 'answer_value': 1},
                        {'answer_text': "I currently have no one I feel comfortable relying on for support or assistance", 'answer_value': 0}
                    ]
                },
                {
                    'question_slug': 'support-system-desired-expansion', 
                    'question_text': "Are you content with your support system in its current state, or are you interested in expanding you social network/support system?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "I am content with the level of connections and support in my life and am not currently looking to expand", 'answer_value': 5},
                        {'answer_text': "I am mostly content with my current support system but would welcome new connections if they align with my interests", 'answer_value': 4},
                        {'answer_text': "I am actively looking to meet new people with aligned interests and values who I can integrate into my social circle", 'answer_value': 3},
                        {'answer_text': "I am open to meeting new people, but am not quite sure where to start", 'answer_value': 2},
                        {'answer_text': "I feel that I could use more of a support system but meeting new people can be daunting, uncomfortable or otherwise challenging", 'answer_value': 1}
                    ]
                },
                {
                    'question_slug': 'support-system-growth-strats', 
                    'question_text': "Identify individuals or groups in your current support network. If you’d like to broaden your support, select any of the listed potential avenues for support-seeking that most interest you", 
                    'type': 'select-any-add', 
                    'answers': [
                        {'answer_text': "Immediate or extended family members", 'answer_value': None},
                        {'answer_text': "Friends you trust and who will show up for you", 'answer_value': None},
                        {'answer_text': "Respected coworkers or professional contacts", 'answer_value': None},
                        {'answer_text': "Online or local community and social groups, hobby groups, sport and activity-based clubs", 'answer_value': None},
                        {'answer_text': "Friends from real life or video games", 'answer_value': None},
                        {'answer_text': "A mentor or coach", 'answer_value': None},
                        {'answer_text': "Classes or skill-building groups", 'answer_value': None},
                        {'answer_text': "A mental health professional, therapist or counselor, or support group", 'answer_value': None},
                        {'answer_text': "Groups within a temple, church, mosque, meditation center, or other spiritual gathering space", 'answer_value': None},
                        {'answer_text': "Pet groups or animal-related communities", 'answer_value': None},
                        {'answer_text': "Interest-based online communities", 'answer_value': None},
                        {'answer_text': "I'm not sure at the moment", 'answer_value': None},
                        {'answer_text': "I prefer to keep to myself", 'answer_value': None}
                        
                    ]
                },
                {
                    'question_slug': 'support-system-preferred-type', 
                    'question_text': "What type of support do you find most helpful?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "Emotional support (listening, empathy, encouragement)", 'answer_value': 0},
                        {'answer_text': "Practical support (help with tasks, planning, logistics)", 'answer_value': 1},
                        {'answer_text': "Accountability (checking in, helping me stay on track)", 'answer_value': 2},
                        {'answer_text': "Social engagement (companionship, spending time together)", 'answer_value': 3},
                        {'answer_text': "Advice or mentorship (guidance, problem-solving, feedback)", 'answer_value': 4},
                    ]
                },
                {
                    'question_slug': 'support-system-comfort-asking', 
                    'question_text': "How comfortable do you feel reaching out to others for help?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "I am very comfortable reaching out for help when I need it", 'answer_value': 3},
                        {'answer_text': "I am comfortable, though I don't do it often", 'answer_value': 2},
                        {'answer_text': "Somewhat uncomfortable but open to it if necessary", 'answer_value': 1},
                        {'answer_text': "Very uncomfortable, I rarely ask for help", 'answer_value': 0}
                        
                    ]
                },
                {
                    'question_slug': 'support-system-goal-understanding', 
                    'question_text': "Do you feel that your support system understands your personal goals and challenges?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "Yes, they fully understand my goals and challenges", 'answer_value': 5},
                        {'answer_text': "The understand some of my goals, but not all", 'answer_value': 4},
                        {'answer_text': "They know my goals but don't fully grasp my challenges", 'answer_value': 3},
                        {'answer_text': "They know my challenges but don't know about my goals/vision", 'answer_value': 2},
                        {'answer_text': "No, I don't feel they understand my goals or challenges", 'answer_value': 1},
                        {'answer_text': "I haven't discussed my goals and challenges with my network", 'answer_value': 0},
                    ]
                }
            ]
        },
        {
            'topic_slug': 'reflecting-purpose-motivation', 
            'questions': [
                {
                    'question_slug': 'personal-landscape-purpose', 
                    'question_text': "The following are things that inspire and motivate me, or otherwise bring joy or purpose into my life. (Select all that apply)", 
                    'type': 'select-all-add', 
                    'answers': [
                        {'answer_text': "Building a sense of community, both locally and online, gives me motivation and belonging", 'answer_value': None},
                        {'answer_text': "My relationships with family and close friends give meaning and motivation to my life", 'answer_value': None},
                        {'answer_text': "My spiritual or religious beliefs provide me with guidance, purpose, and motivation", 'answer_value': None},
                        {'answer_text': "Finding peace, contentment, and balance in daily life is important to me", 'answer_value': None},
                        {'answer_text': "The process of growth and learning in life brings me joy, regardless of specific outcomes", 'answer_value': None},
                        {'answer_text': "I am motivated by self-improvement, learning new skills, or gaining knowledge", 'answer_value': None},
                        {'answer_text': "Self-discovery and growing through adversity give me purpose", 'answer_value': None},
                        {'answer_text': "Exploring philosophy, existential questions, or life perspectives gives me purpose", 'answer_value': None},
                        {'answer_text': "Mindfulness, emotional resilience, or mental clarity help me stay centered and focused", 'answer_value': None},
                        {'answer_text': "Helping others or making a positive impact, whether through work, volunteering, or kindness, is important to me", 'answer_value': None},
                        {'answer_text': "Being a positive role model for my family or community motivates me", 'answer_value': None},
                        {'answer_text': "Professional growth, career development, or achieving my goals motivates me", 'answer_value': None},
                        {'answer_text': "Achieving financial stability and working toward financial goals gives me direction", 'answer_value': None},
                        {'answer_text': "Problem-solving, innovation, and finding creative solutions energize me", 'answer_value': None},
                        {'answer_text': "Creative activities like art, music, writing, or crafting bring me a sense of purpose", 'answer_value': None},
                        {'answer_text': "Expressing my personality through fashion, makeup, or personal style builds my confidence", 'answer_value': None},
                        {'answer_text': "Engaging in sports, dance, or physical activities keeps me energized", 'answer_value': None},
                        {'answer_text': "I’m inspired by new experiences, exploration, or connecting with different cultures and ideas", 'answer_value': None},
                        {'answer_text': "Spending time in nature, whether through outdoor activities or quiet reflection, inspires me", 'answer_value': None},
                        {'answer_text': "Video games, online communities, or esports give me a sense of connection and accomplishment", 'answer_value': None},
                        {'answer_text': "Connecting with my cultural heritage or traditions brings me joy and a sense of identity", 'answer_value': None},
                        {'answer_text': "Advocating for social identities or social justice (e.g., LGBTQIA+, indigenous rights) is meaningful to me", 'answer_value': None},
                        {'answer_text': "Advocating for causes like social justice, environmental sustainability, or animal welfare gives me purpose", 'answer_value': None},
                        {'answer_text': "Environmental connection and stewardship bring me purpose", 'answer_value': None},
                        {'answer_text': "Discovering and understanding my purpose brings me meaning", 'answer_value': None},
                    ]
                },
                {
                    'question_slug': 'personal-landscape-current-strengths', 
                    'question_text': "What are some personal strengths or qualities that you feel help you succeed through challenges?", 
                    'type': 'select-all-add', 
                    'answers': [
                        {'answer_text': "Patience", 'answer_value': None},
                        {'answer_text': "Discipline", 'answer_value': None},
                        {'answer_text': "Creativity", 'answer_value': None},
                        {'answer_text': "Focus", 'answer_value': None},
                        {'answer_text': "Positivity", 'answer_value': None},
                        {'answer_text': "Resilience", 'answer_value': None},
                        {'answer_text': "Confidence", 'answer_value': None},
                        {'answer_text': "Empathy", 'answer_value': None},
                        {'answer_text': "Adaptability", 'answer_value': None},
                        {'answer_text': "Emotional Intelligence", 'answer_value': None},
                        {'answer_text': "Mindfulness", 'answer_value': None},
                        {'answer_text': "Gratitude", 'answer_value': None},
                        {'answer_text': "Problem-Solving", 'answer_value': None},
                        {'answer_text': "Optimism", 'answer_value': None},
                        {'answer_text': "Assertiveness", 'answer_value': None},
                        {'answer_text': "Self-Compassion", 'answer_value': None}
                    ]
                },
                {
                    'question_slug': 'personal-landscape-desired-strengths', 
                    'question_text': "What are personal strengths or qualities that you would like to cultivate in yourself?", 
                    'type': 'select-all-add', 
                    'answers': [
                        {'answer_text': "Patience", 'answer_value': None},
                        {'answer_text': "Discipline", 'answer_value': None},
                        {'answer_text': "Creativity", 'answer_value': None},
                        {'answer_text': "Focus", 'answer_value': None},
                        {'answer_text': "Positivity", 'answer_value': None},
                        {'answer_text': "Resilience", 'answer_value': None},
                        {'answer_text': "Confidence", 'answer_value': None},
                        {'answer_text': "Empathy", 'answer_value': None},
                        {'answer_text': "Adaptability", 'answer_value': None},
                        {'answer_text': "Emotional Intelligence", 'answer_value': None},
                        {'answer_text': "Mindfulness", 'answer_value': None},
                        {'answer_text': "Gratitude", 'answer_value': None},
                        {'answer_text': "Problem-Solving", 'answer_value': None},
                        {'answer_text': "Optimism", 'answer_value': None},
                        {'answer_text': "Assertiveness", 'answer_value': None},
                        {'answer_text': "Self-Compassion", 'answer_value': None}

                    ]
                },
                {
                    'question_slug': 'personal-landscape-barriers', 
                    'question_text': "Are there potential barriers that might make reaching your goals challenging?", 
                    'type': 'select-all-add', 
                    'answers': [
                        {'answer_text': "Limited time", 'answer_value': None},
                        {'answer_text': "Financial limitations", 'answer_value': None},
                        {'answer_text': "Health challenges", 'answer_value': None},
                        {'answer_text': "Limited support system", 'answer_value': None},
                        {'answer_text': "Difficulty staying motivated", 'answer_value': None},
                        {'answer_text': "Unclear goals or vision", 'answer_value': None}
                    ]
                },
                
                {
                    'question_slug': 'personal-landscape-adhd-type', 
                    'question_text': "If you think you might have ADHD symptoms, which of the following patterns best describes your typcial experiences with attention, activitiy levels, and focus?", 
                    'type': 'guided-choice', 
                    'answers': [
                        {'answer_text': "Inattentive - I often struggle with focus, organization, and following through on tasks.  I may get easily distracted, lose track of details, or feel overwhelmed by organizing information", 'answer_value': 5},
                        {'answer_text': "Hyperactive-Impulsive - I tend to feel restless or fidgey, often acting without thinking things through.  I may talk frequently, interrupt others, or find it difficult to stay still for long", 'answer_value': 4},
                        {'answer_text': "Combined Inattentive and Hyperactive-Impulsive - I experience a mix of attention issues and hyperactivity-impulsivity.  I find it challenging to stay organized and focused and often feel a need to be active or act on impulse", 'answer_value': 3},
                        {'answer_text': "Situational or Contextual Challenges - My attention, focus, or impulse control varies significantly depending on the situation (e.g., work, social gatherings, or high-interest activities). I may hyperfocus in some areas while struffling with others", 'answer_value': 2},
                        {'answer_text': "Emotional Dysregulation - I experience intense emotions or mood swings that affect my realtionships and focus. I may struggle with frustration, motivation, or self-esteem, especially in social or high-pressure situations", 'answer_value': 1},
                        {'answer_text': "None of these patterns resonate with me", 'answer_value': 0}
                    ]
                }
            ]
        },
        # DEFINING YOUR WHY
        {

            # TODO: CHANGE QUESTION TYPES TO MATCH NEW TYPES
            'topic_slug': 'define-your-purpose',
            'questions': [
                {
                    'question_text': "What gets you up in the morning? What keeps you motivated?",
                    'type': 'select-any-add', 
                    'question_slug': 'what-motivates-you',
                    'answers': [
                        {'answer_text': "I want to provide a better life for my family.", 'answer_value': None},
                        {'answer_text': "I feel motivated by helping others and making a positive impact in my community.", 'answer_value': None},
                        {'answer_text': "I want to leave a lasting legacy for future generations, something meaningful that will outlive me.", 'answer_value': None},
                        {'answer_text': "My faith gives me purpose and guides the decisions I make everyday.", 'answer_value': None},
                        {'answer_text': "I'm committed to staying healthy so I can enjoy a long, active life with the people I love.", 'answer_value': None},
                        {'answer_text': "I am driven by a desire to constantly improve myself and grow into the best version of me.", 'answer_value': None},
                        {'answer_text': "My passion for work drives me, especially when I'm making a difference in people's lives.", 'answer_value': None},
                        {'answer_text': "I feel most alive when I'm exploring the world, experiencing new cultures, and seeking adventure.", 'answer_value': None},
                        {'answer_text': "Overcoming challenges in my life has shaped me, and now I feel driven to use my experiences to help others do the same.", 'answer_value': None},
                        {'answer_text': "I'm in survival mode, I get up because I have to.", 'answer_value': None},

                    ]
                },
                {
                    'question_text': "Who or what do you feel deeply connected to?",
                    'type': 'select-any-add', 
                    'question_slug': 'deep-connections',
                    'answers': [
                        {'answer_text': "My community - helping others brings me a sense of purpose and fulfillment.", 'answer_value': None},
                        {'answer_text': "I feel a profound connection to nature and find peace in protecting the environment.", 'answer_value': None},
                        {'answer_text': "My creative work feels like a unique contribution to the world, expressing who I am.", 'answer_value': None},
                        {'answer_text': "Mentoring others gives me a sense of legacy, knowing I'm making a lasting impact.", 'answer_value': None},
                        {'answer_text': "I'm driven by my family connections — they are my foundation and a source of deep pride.", 'answer_value': None},
                        {'answer_text': "I feel at my best when connecting with friends, sharing life’s journey together.", 'answer_value': None},
                        {'answer_text': "Learning something new invigorates me; it keeps my mind sharp and curiosity alive.", 'answer_value': None},
                        {'answer_text': "My faith or spiritual beliefs provide a sense of purpose and connection to something greater.", 'answer_value': None},
                        {'answer_text': "Being in a team setting, working toward a common goal, makes me feel a strong sense of unity.", 'answer_value': None},
                    ]
                },
                {
                    'question_text': "Do you feel like you have uncovered your purpose in life, or are you still searching?",
                    'type': 'guided-choice', 
                    'question_slug': 'have-you-uncovered-purpose',
                    'answers': [
                        {'answer_text': "I know one or more of my purposes in life.", 'answer_value': None},
                        {'answer_text': "I think I have identified my purpose.", 'answer_value': None},
                        {'answer_text': "I think I am starting to uncover it, but I have more exploring to do.", 'answer_value': None},
                        {'answer_text': "I am still searching.", 'answer_value': None},
                    ]
                },
                {
                    'question_text': "When do you feel most like yourself? What activities bring you the greatest sense of authenticity?",
                    'type': 'guided-choice', 
                    'question_slug': 'activities-greatest-authenticity',
                    'answers': [
                        {'answer_text': "When I'm creating or building something that excites me.", 'answer_value': None},
                        {'answer_text': "When I’m working out, I feel like I’m building both my body and my mental resilience.", 'answer_value': None},
                        {'answer_text': "When I'm spending quality time with the people I care about.", 'answer_value': None},
                        {'answer_text': "I’m at my best when I’m mentoring others, passing on my knowledge feels like I'm creating a legacy.", 'answer_value': None},
                        {'answer_text': "I’m most energized when I’m learning something new because it keeps me curious and engaged.", 'answer_value': None},
                    ]
                },
                {
                    'question_text': "What current activities in your life give you a sense of purpose and fulfillment?",
                    'type': 'guided-choice', 
                    'question_slug': 'current-activities-purpose-fulfillment',
                    'answers': [
                        {'answer_text': "When I am spending quality time with my loved ones, I feel like I am truly myself", 'answer_value': None},
                        {'answer_text': "When I am working on something creative, like painting, writing, or designing.", 'answer_value': None},
                        {'answer_text': "I feel most fulfilled when I am helping others, whether through volunteering or supporting a friend.", 'answer_value': None},
                        {'answer_text': "When I'm immersed in nature, hiking or just being outside, I feel grounded and at peace.", 'answer_value': None},
                        {'answer_text': "When I'm pursuing personal growth - learning new skills or challenging myself.", 'answer_value': None},
                        {'answer_text': "When I am engaging in deep conversations with people I care about.", 'answer_value': None},
                        {'answer_text': "When I am fully present in the moment, like during meditation or mindfulness exercises.", 'answer_value': None},
                        {'answer_text': "When I am exercising, especially in activities like yoga, running or strength training.", 'answer_value': None},
                        {'answer_text': "When I am working on a project that aligns with my values and passions.", 'answer_value': None},
                        {'answer_text': "When I'm exploring new places or experiencing different cultures.", 'answer_value': None},
                    ]
                },
                {
                    'question_text': "Are there things you haven't yet explored that you think might be part of your vision of a fulfilled life?",
                    'type': 'guided-choice', 
                    'question_slug': 'unexplored-activities-fulfillment',
                    'answers': [
                        {'answer_text': "Yes, I can think of one or more.", 'answer_value': None},
                        {'answer_text': "I'm not sure, I need to think more.", 'answer_value': None},
                        {'answer_text': "Perhaps, but I currently have many activities I enjoy that are fulfilling to me.", 'answer_value': None},
                        {'answer_text': "I'm all set, if anything I could take on less in my day.", 'answer_value': None},
                    ]
                },
                {
                    'question_text': "What small steps could you take today to start exploring your sense of purpose?", 
                    'type': 'guided-choice', 
                    'question_slug': 'small-steps-toward-purpose',
                    'answers': [
                        {'answer_text': "I could reflect on what truly makes me happy and aligned with my values.", 'answer_value': None},
                        {'answer_text': "I could start writing or journaling about the things I'm passionate and energetic about to see what comes up.", 'answer_value': None},
                        {'answer_text': "I could try a new activity or hobby to see if it clicks with me.", 'answer_value': None},
                        {'answer_text': "I am not sure I can take on any new activities at the moment.", 'answer_value': None}
                    ]
                },
                {
                    'question_text': "What personal strengths or traits help you navigate difficulties?",
                    'type': 'guided-choice', 
                    'question_slug': 'personal-strengths-navigate-difficulties',
                    'answers': [
                        {'answer_text': "I am resilient and always find a way through challenges.", 'answer_value': None},
                        {'answer_text': "I am adaptable.", 'answer_value': None},
                        {'answer_text': "My creativity helps me think outside the box in difficult situations.", 'answer_value': None},
                        {'answer_text': "My resourcefulness helps me think outside the box in difficult tuations.", 'answer_value': None},
                        {'answer_text': "I am good at letting go of the little things and focusing on the big picture.", 'answer_value': None},
                    ]
                },
            ]
        },
        {
            'topic_slug': 'define-your-values',
            'questions': [
                {
                    'question_text': "What values do you hold most dear in life?",
                    'type': 'guided-choice', 
                    'question_slug': 'values-most-dear',
                    'answers': [
                        {'answer_text': "Integrity and honesty are my highest values.", 'answer_value': None},
                        {'answer_text': "Treating others with respect, kindness and compassion.", 'answer_value': None},
                        {'answer_text': "Family - prioritizing family connections, care and support.", 'answer_value': None},
                        {'answer_text': "Personal growth or professional development.", 'answer_value': None},
                        {'answer_text': "Autonomy, independence, personal freedom.", 'answer_value': None},
                        {'answer_text': "Accountability for my actions", 'answer_value': None},
                        {'answer_text': "Courage - having the strength to face my fears, adversity, uncertainty.", 'answer_value': None},
                        {'answer_text': "Maintaining balance between work, family, and personal life.", 'answer_value': None},
                        {'answer_text': "Creativity.", 'answer_value': None},
                        {'answer_text': "Health - prioritizing physical and mental well-being.", 'answer_value': None},
                        {'answer_text': "Justice - fairness, equality, a desire to do what is morally right.", 'answer_value': None},
                        {'answer_text': "Perseverance - commitment to pursuing goals and dreams despite challenges or setbacks.", 'answer_value': None},
                        {'answer_text': "Adventure - seeking new experiences.", 'answer_value': None},
                        {'answer_text': "Service - helping others, contributing to the well-being of the community.", 'answer_value': None}
                    ]
                }
            ]
        },
        
# TODO: POSSIBLE DATA STRUCTURE UPDATE TO UTILIZE MANY-TO-MANY TABLE, POSSIBLY ATTAINABLE WITH ONLY CHANGES TO survey_custom_answer_seed()

        # RECREATION AND TRAVEL
        {
            'topic_slug': 'frequent-hobbies-activities',
            'questions': [
                {
                    'question_text': "How often do you think about engaging in new hobbies or activities?",
                    'question_slug': 'new-hobby-activity-interest',
                    'type': 'frequency'
                },
                {
                    "question_text": "How much time do you spend considering your personal interests, such as traveling or exploring new hobbies?",
                    'question_slug': 'time-exploring-new-interests',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "What is your interest level in local or international travel?",
                    'question_slug': 'interest-local-international-travel',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "How interested are you in pursuing hobbies like crafting or DIY projects on a daily basis?",
                    'question_slug': 'interest-crafts-projects',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "How interested are you in participating in events, competitions, or skill-based activities?",
                    'question_slug': 'interest-competitive-skill-based',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "How spontaneous are you when it comes to trying random new activities or experiences?",
                    'question_slug': 'spontaneity-new-experiences',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "How often do you currently engage in hobbies or activities that bring you joy?",
                    'question_slug': 'frequency-joyful-activities',
                    'type': 'frequency'
                },
                {
                    "question_text": "How much time per week do you currently dedicate to activities like traveling, crafting, sports, or other personal hobbies?",
                    'question_slug': 'time-dedicated-various-activities',
                    'type': 'range-hours-0-10'
                },
                {
                    "question_text": "Are you interested in setting specific goals to prioritize hobbies or activities?",
                    'question_slug': 'interest-goals-prioritizing-hobbies',
                    'type': 'yes-no'
                },
                {
                    "question_text": "Do you feel motivated to make time for hobbies or activities that you haven’t yet explored?",
                    'question_slug': 'interest-make-time-new-activities',
                    'type': 'yes-no'
                },
                # {
                #     "question_text": "Describe an activity or hobby you’ve always wanted to explore but haven’t yet started.",
                #     'slug': 'describe-unexplored-activity',
                #     'type': 'open-ended'
                # },
                # {
                #     "question_text": "What barriers, if any, prevent you from engaging in your preferred hobbies or activities?",
                #     'slug': 'barriers-to-hobbies',
                #     'type': 'open-ended'
                # }
            ]
        },
        {
            'topic_slug': 'adventure-travel',
            'questions': [
                {
                    "question_text": "How interested are you in traveling to remote or adventurous locations?",
                    'question_slug': 'interest-remote-travel',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "How often do you participate in outdoor adventure activities like hiking, camping, or mountain climbing?",
                    'question_slug': 'frequency-adventure-activities',
                    'type': 'frequency'
                },
                {
                    "question_text": "Are you interested in trying extreme sports or adventure travel?",
                    'question_slug': 'interest-extreme-sports',
                    'type': 'yes-no'
                }
            ]
        },
        {
            'topic_slug': 'family-group-events',
            'questions': [
                {
                    "question_text": "How often do you plan events or activities with family or friends?",
                    'question_slug': 'frequency-family-friend-events',
                    'type': 'frequency'
                },
                {
                    "question_text": "What is your interest level in organizing group activities such as reunions or community events?",
                    'question_slug': 'interest-group-activities-community-events',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "Do you enjoy being part of group activities or social gatherings?",
                    'question_slug': 'enjoyment-group-social-activities',
                    'type': 'yes-no'
                }
            ]
        },
        {
            'topic_slug': 'cultural-exploration',
            'questions': [
                {
                    "question_text": "How often do you seek out new cultural experiences (e.g., art exhibits, music, cuisine)?",
                    'question_slug': 'frequency-new-cultural-experiences',
                    'type': 'frequency'
                },
                {
                    "question_text": "How interested are you in learning about different cultures or traditions?",
                    'question_slug': 'interest-cultures-traditions',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "Are you open to trying new foods, art forms, or cultural events?",
                    'question_slug': 'interest-new-foods-events',
                    'type': 'yes-no'
                }
            ]
        },
        {
            'topic_slug': 'special-events',
            'questions': [
                {
                    "question_text": "How often do you plan or attend special events (e.g., weddings, concerts, parties)?",
                    'question_slug': 'frequency-plan-attend-special-events',
                    'type': 'frequency'
                },
                {
                    "question_text": "How much do you enjoy organizing or hosting special events?",
                    'question_slug': 'enjoyment-organizing-hosting-special-events',
                    'type': 'scale-agree-disagree'
                }
            ]
        },
        {
            'topic_slug': 'competitive-events',
            'questions': [
                {
                    "question_text": "How often do you participate in competitive events such as races or tournaments?",
                    'question_slug': 'frequency-competitions',
                    'type': 'frequency'
                },
                {
                    "question_text": "How interested are you in training for or competing in an event?",
                    'question_slug': 'interest-training-competitive-events',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "Do you have specific competitive goals you would like to achieve?",
                    'question_slug': 'specific-competitive-goals',
                    'type': 'yes-no'
                }
            ]
        },
        {
            'topic_slug': 'bucket-list',
            'questions': [
                {
                    "question_text": "How often do you think about your bucket list goals or dreams?",
                    'question_slug': 'frequency-thinking-goals-dreams',
                    'type': 'frequency'
                },
                {
                    "question_text": "How interested are you in working towards checking off items from your bucket list?",
                    'question_slug': 'interest-checking-off-bucket-list',
                    'type': 'scale-agree-disagree'
                },
                {
                    "question_text": "Do you feel motivated to take steps towards achieving your bucket list dreams?",
                    'question_slug': 'motivation-bucket-list-dreams',
                    'type': 'yes-no'
                }
            ]
        }
    ]
# Documentation for survey_question_data Structure

"""
This file contains the structure and guidelines for populating survey_question_data 
used in the database seeding process. Below is an overview of the structure, supported 
question types, and guidelines for reusable answer sets.

### Structure Overview:
- **subcategory_slug**: Must match a corresponding `subcategory_slug` in the `subcategories` table.
- **questions**: A list of dictionaries, each representing a single survey question.

### Question Fields:
1. **question_slug**: Unique identifier for the question.
2. **question_text**: Text displayed to the user for the question.
3. **type**: Defines the answer format. Supported types are:
   - **guided-choice**: User selects one answer from the provided options.
   - **select-any**: User selects any number of answers from the provided options.
   - **select-any-add**: User selects any number of answers and can add custom open-text answers.
   - **open-answer** (optional for future use): User provides an entirely custom text answer.
4. **answers** (optional): Required for `guided-choice`, `select-any`, and `select-any-add`. 
   - A list of dictionaries with the following keys:
       - **answer_text**: Text of the answer displayed to the user.
       - **answer_value**: Numeric representation of the answer, used for tracking or scoring.

### Guidelines:
- Reusable answer sets:
  - Use `generic_survey_answer_data.py` for pre-defined sets of answers.
  - Set the `type` field in your question to match the `answer_type` in the reusable set.
- Custom answer sets:
  - Provide an `answers` key with a list of dictionaries for `guided-choice`, `select-any`, or `select-any-add`.
- Ensure proper alignment of `subcategory_slug`, `question_slug`, and `type` to maintain data integrity.

### TODOs:
- Implement open-answer functionality for `select-any-add` questions.
- Consider adding a `guided-choice-add` type for guided-choice questions with optional open-text input.
- Refactor `survey_generic_answer_seed()` into its own file for modularity.
"""

# ADD QUESTIONS ABOUT SCREEN TIME AND DOPAMINE RELATED DESIRES/DRIVERS/RESPONSES
survey_question_data = [
    {
      "subcategory_slug": "user-objectives",
      "questions": [
            {
              "question_slug": "big-picture-intentions",
              "question_text": "What broader life goals or focus areas matter most to you right now? (Select any that apply)",
              "type": "select-any",
              "answers": [
                {"answer_text": "Longevity & healthy aging", "answer_value": 0},
                {"answer_text": "Mental health & resilience", "answer_value": 1},
                {"answer_text": "Cognitive sharpness & performance", "answer_value": 2},
                {"answer_text": "Physical vitality & fitness", "answer_value": 3},
                {"answer_text": "Work-life balance", "answer_value": 4},
                {"answer_text": "Strong relationships & social connection", "answer_value": 5},
                {"answer_text": "Increased energy & motivation", "answer_value": 6},
                {"answer_text": "More consistent daily routines", "answer_value": 7},
                {"answer_text": "More clarity and focus on what matters", "answer_value": 8}
              ]
            },
            # {
            #     "question_slug": "objectives-top-5",
            #     "question_text": "Ok, if you had more than 5 selected, can you pare it down to your top 5?.",
            #     "type": "select-5"
            # },
            {
              "question_slug": "objectives-top-3",
              "question_text": "Ok great, now please identify the 3 areas most important to you.",
              "type": "select-3"
            },
            {
              "question_slug": "objectives-top-1",
              "question_text": "Fantastic, and your number one?",
              "type": "select-1"
            },
            # {
            #   "question_slug": "converge-idea",
            #   "question_text": "The idea for Converge began in the clinic, seeing the often overwhelming complexity for patients trying to apply the wealth of modern health recommendations ",
            #   "type": "prompt"
            # },
            {
              "question_slug": "wellness-shifts",
              "question_text": "Which health or wellness shifts would you most benefit from right now? (Select any that apply)",
              "type": "select-any",
              "answers": [
                {"answer_text": "Increased energy levels", "answer_value": 0},
                {"answer_text": "Reduced physical discomfort or pain", "answer_value": 1},
                {"answer_text": "Better sleep quality", "answer_value": 2},
                {"answer_text": "Stronger social connections", "answer_value": 3},
                {"answer_text": "Reduced anxiety", "answer_value": 4},
                {"answer_text": "Lower stress", "answer_value": 5},
                {"answer_text": "Improved mood", "answer_value": 7},
                {"answer_text": "Improved fitness", "answer_value": 8},
                {"answer_text": "Improved work-life balance", "answer_value": 9}
              ]
            },
            {
              "question_slug": "shifts-top-3",
              "question_text": "Ok great, now please identify your top 3 from the list.",
              "type": "select-3"
            },
            {
              "question_slug": "shifts-top-1",
              "question_text": "Excellent, now please select the single shift you think would improve your life the most.",
              "type": "select-1"
            },
            # {
            #   "question_slug": "human-malleability",
            #   "question_text": "One of the most beautiful things about life is its adaptability",
            #   "type": "prompt"
            # },
            {
              "question_slug": "trait-skill-focus",
              "question_text": "Which personal traits or skills would benefit you the most, if intentionally developed? (Select any that apply)",
              "type": "select-any",
              "answers": [ 
                {"answer_text": "Self-discipline & follow-through", "answer_value": 0},
                {"answer_text": "Time management & prioritization", "answer_value": 1},
                {"answer_text": "Consistency in routines", "answer_value": 2},
                {"answer_text": "Focus & mental clarity", "answer_value": 3},
                {"answer_text": "Productivity & better systems", "answer_value": 4},
                {"answer_text": "Creative or flexible thinking", "answer_value": 5},
                {"answer_text": "Growth mindset & adaptability", "answer_value": 6},
                {"answer_text": "Decision-making & problem-solving", "answer_value": 7},

                {"answer_text": "Self-awareness & reflection", "answer_value": 8},
                {"answer_text": "Impulse control & emotional regulation", "answer_value": 9},
                {"answer_text": "Confidence & self-esteem", "answer_value": 10},
                {"answer_text": "Resilience under stress", "answer_value": 11},
                {"answer_text": "Self-compassion during setbacks", "answer_value": 12},

                {"answer_text": "Assertiveness & boundary-setting", "answer_value": 13},
                {"answer_text": "Empathy & emotional intelligence", "answer_value": 14},
                {"answer_text": "Active listening & connection skills", "answer_value": 15},
                {"answer_text": "Navigating conflict constructively", "answer_value": 16},
                {"answer_text": "Living with purpose & values", "answer_value": 17}
              ]
            },


            # {
            #   "question_slug": "self-esteem-musings",
            #   "question_text": "What is self-esteem? Well, it's how highly you esteem yourself, right? Why do you or do you not think highly of yourself? Is it because of something you aren't doing you've always wanted to and are putting energy into making that happen? We all have to ask ourselves, is it because of an external image or persona that has been placed in our minds by advertising or filtered culture? Are any of us beautiful enough, exciting enough, virtuous enough?",
            #   "type": "prompt"
            # },
            {
              "question_slug": "skill-trait-top-5",
              "question_text": "I know that was a lot, let's do top 5 this time...",
              "type": "select-5"
            },
            {
              "question_slug": "skill-trait-top-3",
              "question_text": "Ok great, now please identify your top 3 from the list.",
              "type": "select-3"
            },
            {
              "question_slug": "skill-trait-top-1",
              "question_text": "Excellent, now please select the single shift you think would improve your life the most.",
              "type": "select-1"
            },
            # {
            #   "question_slug": "user-preferred-features",
            #   "question_text": "Which features of Converge would be most helpful to you?",
            #   "type": "select-any",
            #   "answers": [
            #     {"answer_text": "Goal tracking", "answer_value": 0},
            #     {"answer_text": "Daily reminders", "answer_value": 1},
            #     {"answer_text": "Progress visualization", "answer_value": 2},
            #     {"answer_text": "Guided practices", "answer_value": 3},
            #     {"answer_text": "Social groups (common interests, book clubs, etc.)", "answer_value": 4},
            #     {"answer_text": "Pairing with accountability partner(s)", "answer_value": 5},
            #     {"answer_text": "Personalized insights", "answer_value": 6},
            #     {"answer_text": "Streak tracking for practices", "answer_value": 7},
            #     {"answer_text": "Integrated scheduling", "answer_value": 8},
            #     {"answer_text": "Gamification elements", "answer_value": 9},
            #     {"answer_text": "Personalized, flexible routine templates", "answer_value": 10},
            #     {"answer_text": "Strategies personalized to your patterns and barriers.", "answer_value": 10}
            #   ]
            # },
            # {
            #     "question_slug": "user-preferred-3-features",
            #     "question_text": "Ok, from those, will you identify up to 3 features that that you think will be most helpful to you?",
            #     "type": "select-3"
            # },
            # 
            # {
            #     "question_slug": "user-feedback-preference",
            #     "question_text": "How would you like Converge to provide support or encouragement?",
            #     "type": "select-any",
            #     "answers": [
            #         {"answer_text": "Daily notifications", "answer_value": 0},
            #         {"answer_text": "Weekly summaries", "answer_value": 1},
            #         {"answer_text": "Encouraging messages", "answer_value": 2},
            #         {"answer_text": "Badges/achievements", "answer_value": 3},
            #         {"answer_text": "Milestone celebrations", "answer_value": 4},
            #         {"answer_text": "Peer feedback", "answer_value": 5},
            #         {"answer_text": "Visual progress charts", "answer_value": 6},
            #         {"answer_text": "Check-in prompts", "answer_value": 7},
            #         {"answer_text": "Self-assessment tools", "answer_value": 8}
            #     ]
            # },
            {
                "question_slug": "motivation-level-check",
                "question_text": "How motivated do you feel to improve your routines and habits right now?",
                "type": "scale-1-5"
            },
          
            # {
            #     "question_slug": "social-engagement-preference",
            #     "question_text": "How would you like to engage with other users in Converge?",
            #     "type": "select-any",
            #     "answers": [
            #         {"answer_text": "I prefer a private, solo experience.", "answer_value": 0},
            #         {"answer_text": "I'd like an accountability partner.", "answer_value": 1},
            #         {"answer_text": "I'd like small group challenges.", "answer_value": 2},
            #         {"answer_text": "I’d like a social feed to see others’ progress.", "answer_value": 3},
            #         {"answer_text": "I’d like occasional check-ins from Converge.", "answer_value": 4}
            #     ]
            # }
        ]
    },
    {
      "subcategory_slug": "digital-disconnect-map",
      "questions": [
        {
          "question_slug": "tech-use-and-attitude",
          "question_text": "How would you describe your current relationship with technology and screen time?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "I use devices constantly and don’t really try to limit it", "answer_value": 0 },
            { "answer_text": "I use tech a lot, and I know it’s too much — I’d like to change it", "answer_value": 1 },
            { "answer_text": "I try to set limits, but it’s a struggle to follow through", "answer_value": 2 },
            { "answer_text": "I’ve started building some boundaries, but there’s room to improve", "answer_value": 3 },
            { "answer_text": "I have strong digital boundaries and a healthy rhythm with screens", "answer_value": 4 }
          ]
        },
        {
          "question_slug": "intro-digital-environment",
          "type": "prompt",
          "question_text": "The way we use technology each day shapes more than our schedule — it affects our focus, mood, energy, and even how connected we feel to ourselves."
        },
        {
          "question_slug": "impulsive-phone-checks",
          "question_text": "How often do you find yourself checking your phone without really meaning to?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Rarely — it’s a conscious choice", "answer_value": 0 },
            { "answer_text": "A few times a day", "answer_value": 1 },
            { "answer_text": "Often — it’s a reflex", "answer_value": 2 },
            { "answer_text": "Constantly — I barely notice I’m doing it", "answer_value": 3 }
          ]
        },
        {
          "question_slug": "prompt-brain-on-screens",
          "type": "prompt",
          "question_text": "Apps and platforms are designed to grab your attention. Each ping or swipe can trigger a tiny hit of dopamine — your brain’s reward signal. Over time, this can shift how we experience boredom, focus, or rest."
        },
        {
          "question_slug": "screen-fatigue-awareness",
          "question_text": "After spending a lot of time online, how do you usually feel?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Refreshed and focused", "answer_value": 0 },
            { "answer_text": "A bit tired or scattered", "answer_value": 1 },
            { "answer_text": "Mentally foggy or overstimulated", "answer_value": 2 },
            { "answer_text": "Exhausted, anxious, or drained", "answer_value": 3 },
            { "answer_text": "No real difference", "answer_value": 4 }
          ]
        },
        {
          "question_slug": "prompt-digital-fatigue-explained",
          "type": "prompt",
          "question_text": "When we’re constantly switching focus or taking in rapid information, our nervous system can stay in a low-grade overdrive. That’s why even passive scrolling can leave us feeling more drained than relaxed."
        },
        {
          "question_slug": "pain-point-identification",
          "question_text": "Which of these screen-related challenges have shown up in your life?",
          "type": "select-any",
          "answers": [
            { "answer_text": "Doom-scrolling news or social media", "answer_value": 0 },
            { "answer_text": "Picking up my phone without meaning to", "answer_value": 1 },
            { "answer_text": "Feeling drained after screen time", "answer_value": 2 },
            { "answer_text": "Trouble winding down or sleeping", "answer_value": 3 },
            { "answer_text": "Feeling anxious when I don’t have my phone", "answer_value": 4 },
            { "answer_text": "None of these apply to me", "answer_value": 5 }
          ]
        },
        {
          "question_slug": "pain-point-top-2",
          "question_text": "Which two feel like the biggest stressors or obstacles for you right now?",
          "type": "select-2"
        },
        {
          "question_slug": "prompt-relationship-reset",
          "type": "prompt",
          "question_text": "Digital boundaries aren’t about quitting tech — they’re about being more intentional. Even small changes, like screen-free mornings or app time limits, can free up attention and energy for the things that matter most."
        },
        {
          "question_slug": "digital-boundary-check",
          "question_text": "Which of these shifts feels most helpful or doable for you right now?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Screen-free first hour of the day", "answer_value": 0 },
            { "answer_text": "No social media after a set time", "answer_value": 1 },
            { "answer_text": "Intentional phone-free time blocks", "answer_value": 2 },
            { "answer_text": "Limits or breaks from social media", "answer_value": 3 },
            { "answer_text": "Limits or breaks from news", "answer_value": 4 },
            { "answer_text": "App usage limits or time tracking", "answer_value": 5 },
            { "answer_text": "I’m not ready to make a change right now", "answer_value": 6 }
          ]
        }
      ]
    },
    {
      "subcategory_slug": "core-primer-map",
      "questions": [
        {
          "question_slug": "core-primer-intro",
          "type": "prompt",
          "question_text": "Core primers are short, science-backed morning routines built around hydration, cold exposure, and natural light or movement. They're designed to wake up your brain and body in about 5 minutes."
        },
        {
          "question_slug": "core-primer-prompt-sun-walk",
          "type": "prompt",
          "question_text": "Getting outside within the first hour or two of waking can dramatically shift your energy, alertness, and sleep quality. Natural light — especially sunlight in your eyes — helps reset your internal clock, boosting morning wakefulness and supporting melatonin release later that night. And when you add movement — even just a short walk — it amplifies the effect. Forward motion and optic flow (what your eyes see as you move through space) also signal to your brain that it’s time to engage. This simple combo of sunlight + walking is one of the most powerful, overlooked ways to improve mood, metabolism, and mental clarity."
        },
        {
          "question_slug": "core-primer-cold-readiness",
          "type": "guided-choice",
          "question_text": "Which best describes your comfort with cold exposure in the morning?",
          "answers": [
            { "answer_text": "I’ve never tried it or want to start gently", "answer_value": 0 },
            { "answer_text": "I’m up for a cold rinse or shower", "answer_value": 1 },
            { "answer_text": "Cold plunges or full showers are already part of my routine", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "core-primer-light-movement-style",
          "type": "guided-choice",
          "question_text": "What feels most appealing after your cold exposure?",
          "answers": [
            { "answer_text": "A calm moment with a warm drink and morning light", "answer_value": 0 },
            { "answer_text": "A short outdoor walk in the sun", "answer_value": 1 },
            { "answer_text": "A quick jog, workout, or run in the morning light", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "core-primer-light-benefits",
          "type": "prompt",
          "question_text": "Getting morning sunlight (especially within the first hour or two of waking) helps reset your internal clock. This improves sleep quality, energy levels, and mood — and the benefits increase when you add forward movement like walking or running."
        },
        {
          "question_slug": "core-primer-hydration-check",
          "type": "guided-choice",
          "question_text": "Do you usually drink water within 30 minutes of waking?",
          "answers": [
            { "answer_text": "Rarely", "answer_value": 0 },
            { "answer_text": "Sometimes", "answer_value": 1 },
            { "answer_text": "Most days", "answer_value": 2 },
            { "answer_text": "Always — it’s a habit", "answer_value": 3 }
          ]
        }
      ]
    },
    {
      "subcategory_slug": "core-builder-map",
      "questions": [
        {
          "question_slug": "meditation-introduction",
          "question_text": "Meditation is widely studied for its ability to reduce stress, improve focus, and enhance emotional well-being. When you meditate, you activate your parasympathetic nervous system, which helps lower your heart rate, reduce stress hormones like cortisol, and promote a sense of calm. Over time, meditation has been shown to improve attention, emotional regulation, and even brain function. Regular practice can also increase gray matter in areas of the brain involved in memory, learning, and emotional control. Which meditation style resonates most with you for your morning routine?",
          "type": "prompt"
        },
        {
          "question_slug": "meditation-preference",
          "question_text": "Which meditation style do you prefer to start your day with?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Stillness and Focus", "answer_value": 0 },
            { "answer_text": "Movement with Focus", "answer_value": 1 },
            { "answer_text": "Breath-Based Calm", "answer_value": 2 },
            { "answer_text": "Gratitude and Presence", "answer_value": 3 }
          ]
        },
        {
          "question_slug": "movement-introduction",
          "question_text": "Movement in the morning has profound effects on both the body and mind. When you engage in physical activity, you increase blood flow, boost circulation, and enhance oxygen delivery to the muscles and brain. This stimulates the release of endorphins, which are natural mood-boosting chemicals that can enhance feelings of happiness and reduce anxiety. Movement also activates the sympathetic nervous system, preparing your body for the day by increasing your heart rate and energy levels. Whether you choose high-intensity exercises for a quick burst of energy or gentle stretches to improve flexibility, movement supports both your physical and mental health. What type of movement would you prefer to start your day?",
          "type": "prompt"
        },
        {
          "question_slug": "movement-preference",
          "question_text": "What type of movement resonates most with you for your morning routine?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "High-Intensity, Quick Energizer", "answer_value": 0 },
            { "answer_text": "Gentle Flow for Flexibility", "answer_value": 1 },
            { "answer_text": "Strength Training for Resilience", "answer_value": 2 },
            { "answer_text": "Mindful Movement with Focus", "answer_value": 3 }
          ]
        },
        {
          "question_slug": "calm-or-energy-introduction",
          "question_text": "Your morning routine can either focus on calming your mind and body or boosting your energy and strength. Calming practices, like meditation, activate your parasympathetic nervous system, which slows down heart rate and promotes relaxation. On the other hand, energy-boosting exercises like HIIT or strength training stimulate your sympathetic nervous system, increasing your heart rate and adrenaline to give you that feeling of readiness and alertness. Deciding what type of energy you want to bring into your morning will shape the focus of your practice. How would you like to begin your day?",
          "type": "prompt"
        },
        {
          "question_slug": "calm-or-energy",
          "question_text": "Would you prefer to begin your day with a focus on calming the nervous system, or boosting your energy and strength?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Calming and Grounding", "answer_value": 0 },
            { "answer_text": "Energy-Boosting Movement", "answer_value": 1 },
            { "answer_text": "Balanced Movement and Calm", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "strength-vs-mobility-introduction",
          "question_text": "Strength and mobility are both crucial for maintaining a healthy body. Strength training helps build muscle, improve metabolism, and enhance physical resilience. It works by putting stress on the muscles, which causes micro-tears that then rebuild stronger, increasing both muscle mass and strength over time. On the other hand, mobility exercises improve joint health, flexibility, and range of motion, which reduces the risk of injury and improves overall movement efficiency. A combination of both is ideal, but you may want to prioritize one depending on your goals. How would you like to structure your morning routine?",
          "type": "prompt"
        },
        {
          "question_slug": "strength-vs-mobility",
          "question_text": "How important is improving your strength or mobility in your morning routine?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Focus on Strength Building", "answer_value": 0 },
            { "answer_text": "Mobility and Flexibility First", "answer_value": 1 },
            { "answer_text": "Balance of Strength and Mobility", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "mental-clarity-introduction",
          "question_text": "Mental clarity and focus are essential for navigating a busy day. Techniques like breathwork and visualization have been shown to increase cognitive performance by improving oxygen flow to the brain, which enhances focus and mental acuity. Breathwork, specifically, can influence the autonomic nervous system, lowering stress and anxiety while improving mental clarity. Visualization, on the other hand, helps activate areas of the brain related to creativity and problem-solving. Would you like to integrate any of these techniques into your morning routine?",
          "type": "prompt"
        },
        {
          "question_slug": "mental-clarity-focus",
          "question_text": "To enhance mental clarity and focus, some routines integrate visualization and other techniques. Would you like to incorporate any of the following?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Focus through Breathwork", "answer_value": 0 },
            { "answer_text": "Creative Energy and Visualization", "answer_value": 1 },
            { "answer_text": "Mindful Presence and Stillness", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "intensity-introduction",
          "question_text": "The intensity of your morning routine can influence your body and mind throughout the day. High-intensity workouts, like HIIT, release endorphins, which are natural mood boosters, while also improving cardiovascular health and stamina. On the other hand, gentler routines, like yoga or meditation, focus on reducing stress, increasing flexibility, and enhancing mindfulness. The intensity level you choose can significantly impact your mood, focus, and energy for the rest of the day. How intense would you like your morning practice to be?",
          "type": "prompt"
        },
        {
          "question_slug": "desired-intensity",
          "question_text": "How intense would you like your morning practice to be? This will determine the balance between relaxation and physical effort.",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Low-Intensity, Grounding", "answer_value": 0 },
            { "answer_text": "High-Intensity, Full Body Workout", "answer_value": 1 },
            { "answer_text": "Balanced, with Movement and Stillness", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "mobility-vs-strength-need-introduction",
          "question_text": "For long-term health, it’s important to balance strength with mobility. Strength training improves muscle mass, which supports metabolic function, increases stamina, and enhances overall physical performance. Mobility exercises focus on joint health and flexibility, reducing the risk of injury and improving posture. Maintaining both strength and mobility ensures a resilient body. Which would you prefer to prioritize in your morning routine?",
          "type": "prompt"
        },
        {
          "question_slug": "mobility-vs-strength-need",
          "question_text": "In your routine, how would you prioritize mobility versus strength?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Prioritize Strength Training", "answer_value": 0 },
            { "answer_text": "Prioritize Mobility and Flexibility", "answer_value": 1 },
            { "answer_text": "Equal Focus on Both Strength and Mobility", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "reflection-introduction",
          "question_text": "Reflection practices, such as mindfulness and gratitude, help you process emotions, reduce stress, and improve mental well-being. Mindfulness encourages present-moment awareness, which can reduce anxiety and promote clarity, while gratitude practices activate areas of the brain related to happiness and positivity. Including these practices in your routine can set a positive tone for the day. Would you like to include a reflective practice?",
          "type": "prompt"
        },
        {
          "question_slug": "reflection-practice",
          "question_text": "Some routines include moments of reflection to help integrate the body and mind. Would you like to include a reflective practice in your morning routine?",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Yes, a Mindful Walking Reflection", "answer_value": 0 },
            { "answer_text": "Yes, a Gratitude Practice", "answer_value": 1 },
            { "answer_text": "No, I prefer to stay focused on movement", "answer_value": 2 }
          ]
        },
        {
          "question_slug": "routine-focus-introduction",
          "question_text": "Having a clear focus for your morning routine is essential for setting intentions and achieving your goals. Whether you’re looking to reset after a stressful day or challenge yourself with a high-energy routine, your focus will guide the type of practices you include. Resetting and restoring energy helps you start the day with a clear mind, while strength-based routines build resilience and stamina. What is your primary focus for the morning?",
          "type": "prompt"
        },
        {
          "question_slug": "routine-focus",
          "question_text": "What is the overall focus you want for your morning routine? This will guide the template recommendation.",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "Reset and Restore", "answer_value": 0 },
            { "answer_text": "Strength and Resilience", "answer_value": 1 },
            { "answer_text": "High-Energy, Full-Body Challenge", "answer_value": 2 },
            { "answer_text": "Focused, Mindful Movement", "answer_value": 3 }
          ]
        }
      ]
    },
    {
      "subcategory_slug": "daily-activity-map",
      "questions": [
            {
              "question_slug": "morning-routine-check",
              "question_text": "Do you currently have an established morning routine?",
              "type": "guided-choice",
              "answers": [
                {"answer_text": "No, because I have very little time in my mornings.", "answer_value": 0},
                {"answer_text": "No, but I would like to.", "answer_value": 1},
                {"answer_text": "No, and I like my mornings as they are.", "answer_value": 2},
                {"answer_text": "Yes, but I could use some help.", "answer_value": 3},
                {"answer_text": "Yes, and I like it as it is.", "answer_value": 4}
              ]
            },
            {
                "question_slug": "habit-adoption-pattern",
                "question_text": "How would you describe your experience with adopting new routines or habits?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "Very easy, I can pick up new habits and be consistent with minimal effort.", "answer_value": 0},
                    {"answer_text": "Easy, new habits come easily, but sometimes take a bit of effort to maintain consistency", "answer_value": 1},
                    {"answer_text": "Neutral, with some effort I can generally stick to new habits.", "answer_value": 2},
                    {"answer_text": "Difficult, it takes preparation and effort to adopt new habits, consistency is challenging.", "answer_value": 3},
                    {"answer_text": "Very difficult, even with significant effort and planning, adopting a new habit feels like a long shot.", "answer_value": 4}
                ]
            },
            {
              "question_slug": "am-energy-pattern",
              "question_text": "How do you usually feel when waking up?",
              "type": "guided-choice",
              "answers": [
                {"answer_text": "Slow and painful", "answer_value": 0},
                {"answer_text": "It takes me an hour or so to get going.", "answer_value": 2},
                {"answer_text": "I perk up after a few minutes.", "answer_value": 3},
                {"answer_text": "I wake energized and ready to go.", "answer_value": 4}
              ]
            },
            {
                "question_slug": "am-routine-time-availability",
                "question_text": "How much time do you typically have for a morning routine beyond the essentials?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "Less than 5 minutes", "answer_value": 0},
                    {"answer_text": "5-15 minutes", "answer_value": 1},
                    {"answer_text": "15-30 minutes", "answer_value": 2},
                    {"answer_text": "30+ minutes", "answer_value": 3}
                ]
            },
            {
                "question_slug": "daily-movement-check",
                "question_text": "How would you describe your exercise regimen?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "Exercise is not a priority for me.", "answer_value": 0},
                    {"answer_text": "I work a physically demanding job.", "answer_value": 1},
                    {"answer_text": "I mostly walk or engage in low intensity movement.", "answer_value": 2},
                    {"answer_text": "I am active regularly.", "answer_value": 3},
                    {"answer_text": "I am an athlete with a structured plan.", "answer_value": 4}
                ]
            },
            {
                "question_slug": "exercise-timing",
                "question_text": "When in the day do you typically exercise?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "Rarely or never", "answer_value": 0},
                    {"answer_text": "Morning", "answer_value": 1},
                    {"answer_text": "Later in the day", "answer_value": 2},
                    {"answer_text": "Flexible", "answer_value": 3}

                ]
            },
            {
                "question_slug": "am-focus-block-check",
                "question_text": "Do you make a block of time in your morning for hobbies, productivity, etc.?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "No", "answer_value": 0},
                    {"answer_text": "No, but I would like to", "answer_value": 1},
                    {"answer_text": "Yes, less than 15 minutes", "answer_value": 2},
                    {"answer_text": "15 - 30 minutes", "answer_value": 3},
                    {"answer_text": "30 - 45 minutes", "answer_value": 4},
                    {"answer_text": "45 - 60 minutes", "answer_value": 5},
                    {"answer_text": "60+ minutes", "answer_value": 6}

                ]
            },

            # MOVE TO INTEREST MAP IF NOT REDUNDANT?
            # {
            #     "question_slug": "hobbies-types",
            #     "question_text": "Which of these hobbies or personal interests do you engage in regularly?",
            #     "type": "select-any",
            #     "answers": [
            #         {"answer_text": "Reading", "answer_value": 0},
            #         {"answer_text": "Writing or journaling", "answer_value": 1},
            #         {"answer_text": "Art, music, or creative work", "answer_value": 2},
            #         {"answer_text": "Sports or physical activities", "answer_value": 3},
            #         {"answer_text": "Meditation or mindfulness", "answer_value": 4},
            #         {"answer_text": "Outdoor activities", "answer_value": 5},
            #         {"answer_text": "Gaming or digital hobbies", "answer_value": 6},
            #         {"answer_text": "Social/community activities", "answer_value": 7}
            #     ]
            # },
            {
                "question_slug": "work-schedule-flexibility",
                "question_text": "How flexible is your schedule?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "Rigid — same hours every day", "answer_value": 0},
                    {"answer_text": "Somewhat flexible", "answer_value": 1},
                    {"answer_text": "Mostly flexible — I have a lot of say in my schedule", "answer_value": 2},
                    {"answer_text": "I do what I want when I want.", "answer_value": 3}
                ]
            },
            # {
            #     "question_slug": "evening-routine-check",
            #     "question_text": "Do you have a structured evening or wind-down routine?",
            #     "type": "yes-no"
            # },
            # # TODO: Branching questions? Specifically, asking user if they want an evening routine? Do we even give them the option? Can skip
            # {
            #     "question_slug": "existing-pm-routines-satisfaction",
            #     "question_text": "How satisfied are you with your current evening routine?",
            #     "type": "satisfaction"
            # },
            # {
            #     "question_slug": "pm-routine-time-availability-prompt",
            #     "question_text": "Evenings before bed can be one of the most potent times for reflection and gratitude about our day, and for many people are an essential wind-down time they need to get quality sleep.",
            #     "type": "prompt"
            # },
            # {
            #     "question_slug": "pm-routine-time-availability",
            #     "question_text": "How much time do you or would you like to set aside for an evening routine?",
            #     "type": "guided-choice",
            #     "answers": [
            #         {"answer_text": "None", "answer_value": 0},
            #         {"answer_text": "Less than 10 minutes", "answer_value": 1},
            #         {"answer_text": "10 - 20 minutes", "answer_value": 2},
            #         {"answer_text": "20 - 30 minutes", "answer_value": 3},
            #         {"answer_text": "30+ minutes", "answer_value": 4}
            #     ]
            # },
            # {
            #     "question_slug": "social-wellness-check",
            #     "question_text": "Rate your satisfaction with your current social activity and connections",
            #     "type": "satisfaction",
            # },
        ]
    },
    {
      "subcategory_slug": "pm-routine-map",
      "questions": [
          {
          "question_slug": "sleep-hygiene",
          "question_text": "How consistent is your sleep schedule and pre-bedtime routine? (bedtime routine might include: reading, meditation, journaling, stretching, no screens, low lights, etc.)",
          "type": "guided-choice",
          "answers": [
            { "answer_text": "My bedtime can vary significantly; no wind-down ritual", "answer_value": 0 },
            { "answer_text": "I go to bed at similar times but don’t unwind systematically", "answer_value": 1 },
            { "answer_text": "I keep an inconsistent sleep schedule but do some winding down", "answer_value": 2 },
            { "answer_text": "I keep a regular schedule and have a basic wind-down ritual", "answer_value": 3},
            { "answer_text": "I follow a structured bedtime ritual", "answer_value": 4 }
          ]
        },
      ]
    },
    {
      "subcategory_slug": "goal-starter-map",
      "questions": [
        {
          "question_slug": "life-position",
          "question_text": "Which statement best describes where you are in life right now?",
          "type": "select-one",
          "answers": [
            { "answer_text": "Still figuring out what I want to do.",          "answer_value": 0 },
            { "answer_text": "Content with where I am; no big goals at the moment.", "answer_value": 1 },
            { "answer_text": "Career‑focused and advancing on a path I love.",   "answer_value": 2 },
            { "answer_text": "In one field but exploring something new.",        "answer_value": 3 },
            { "answer_text": "I’ve achieved my big dreams; looking for the next chapter.", "answer_value": 4 },
            { "answer_text": "I’m in discovery mode—seeking direction and meaning.",      "answer_value": 5 }
          ]
        },
        {
          "question_slug": "interest-areas",
          "question_text": "What areas are you most interested in pursuing goals around? (Select up to 3)",
          "type": "select-any",
          "answers": [
            { "answer_text": "Career & Professional Growth",              "answer_value": 0 },
            { "answer_text": "Health & Fitness",                           "answer_value": 1 },
            { "answer_text": "Personal Growth & Learning",                 "answer_value": 2 },
            { "answer_text": "Financial Stability & Wealth Building",      "answer_value": 3 },
            { "answer_text": "Family & Relationships",                     "answer_value": 4 },
            { "answer_text": "Mental & Emotional Well‑Being",              "answer_value": 5 },
            { "answer_text": "Spiritual Growth & Mindfulness",             "answer_value": 6 },
            { "answer_text": "Creativity & Hobbies",                       "answer_value": 7 },
            { "answer_text": "Community & Social Impact",                  "answer_value": 8 },
            { "answer_text": "Adventure & New Experiences",                "answer_value": 9 },
            { "answer_text": "Time Management & Productivity",             "answer_value": 10 },
            { "answer_text": "Self‑Discipline & Habit Building",           "answer_value": 11 }
          ]
        },
        {
            "question_slug": "interest-areas-top-3",
            "question_text": "From your previously selected interests, select your top 5.",
            "type": "select-3"
        },
        {
            "question_slug": "interest-areas-top-1",
            "question_text": "From your previously selected interests, select your top 5.",
            "type": "select-1"
        },
      ]
    },
    {
      "subcategory_slug": "career-professional-development-map",
      "questions": [
        {
          "question_slug": "career-path",
          "question_text": "Describe your current place in your career path.",
          "type": "guided-choice",
          "answers": [
            {"answer_text": "I am completely content in my professional life.", "answer_value": 0},
            {"answer_text": "I plan on staying in my field, and would like to work toward a management position.", "answer_value": 1},
            {"answer_text": "I plan on staying in my field, and and seek advancement through professional development.", "answer_value": 2},
            {"answer_text": "I am planning or currently transitioning out of my current position or field.", "answer_value": 3},
            {"answer_text": "I am pursuing training or credentials toward desired roles/fields.", "answer_value": 4},

            {"answer_text": "I am not certain .", "answer_value": 3},
            {"answer_text": "I am looking .....", "answer_value": 5}
          ]
        },
      ]
    },

    {
      "subcategory_slug": "discipline-motivation-focus-map",
      "questions": [
            {
                "question_slug": "barriers-to-change-check",
                "question_text": "What challenges have prevented you from building or maintaining habits in the past?",
                "type": "select-any",
                "answers": [
                    {"answer_text": "Lack of time or a busy schedule", "answer_value": 0},
                    {"answer_text": "Lack of motivation or drive", "answer_value": 1},
                    {"answer_text": "Not knowing where to start", "answer_value": 2},
                    {"answer_text": "Difficulty sticking to routines", "answer_value": 3},
                    {"answer_text": "No system for tracking or staying accountable", "answer_value": 4},
                    {"answer_text": "I tend to lose interest over time", "answer_value": 5},
                    {"answer_text": "Low energy or burnout", "answer_value": 6},
                    {"answer_text": "Distractions or poor focus", "answer_value": 7},
                    {"answer_text": "Negative self-talk or doubt", "answer_value": 8},
                    {"answer_text": "Inconsistent environment or lack of support", "answer_value": 9},
                    {"answer_text": "Other (open text input)", "answer_value": 10}
                ]
            },
            {
                "question_slug": "motivation-type-check",
                "question_text": "What motivates you most to take action?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "Internal motivation (personal growth, self-improvement)", "answer_value": 0},
                    {"answer_text": "External rewards (recognition, success, material benefits)", "answer_value": 1},
                    {"answer_text": "Social accountability (teamwork, peer expectations)", "answer_value": 2},
                    {"answer_text": "Urgency or deadlines (pressure fuels productivity)", "answer_value": 3}
                ]
            },
            {
                "question_slug": "focus-difficulty-check",
                "question_text": "How often do you struggle to maintain focus on tasks that do not immediately interest you?",
                "type": "frequency-often"
            },
            {
                "question_slug": "task-initiation-check",
                "question_text": "How often do you find it difficult to start important tasks, even if you know they need to be done?",
                "type": "frequency"
            },
            {
                "question_slug": "time-management-check",
                "question_text": "Which of the following time-related challenges do you frequently experience? Select all that apply",
                "type": "select-any",
                "answers": [
                    {"answer_text": "Difficulty estimating how long tasks will take", "answer_value": 4},
                    {"answer_text": "Frequently running late or missing deadlines", "answer_value": 3},
                    {"answer_text": "Getting 'stuck' on a task for much longer than expected", "answer_value": 2},
                    {"answer_text": "Underestimating or overestimating available time", "answer_value": 1},
                    {"answer_text": "None of the above", "answer_value": 0}
                ]
            },
            {
                "question_slug": "discipline-struggle-check",
                "question_text": "Do you struggle with maintaining discipline and consistency over time?",
                "type": "yes-no"
            },
            {
                "question_slug": "biggest-discipline-challenge",
                "question_text": "What is your biggest challenge when it comes to discipline?",
                "type": "select-any",
                "answers": [
                    {"answer_text": "Getting started on tasks", "answer_value": 0},
                    {"answer_text": "Following through consistently", "answer_value": 1},
                    {"answer_text": "Balancing discipline with flexibility", "answer_value": 2},
                    {"answer_text": "Not feeling motivated to stay consistent", "answer_value": 3}
                ]
            },
            {
                "question_slug": "willpower-fluctuation-check",
                "question_text": "How does your willpower change throughout the day?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "Strongest in the morning", "answer_value": 0},
                    {"answer_text": "Stronger in the afternoon", "answer_value": 1},
                    {"answer_text": "Strongest at night", "answer_value": 2},
                    {"answer_text": "Fluctuates unpredictably", "answer_value": 3}
                ]
            },
            {
                "question_slug": "resilience-check",
                "question_text": "How do you usually handle setbacks or failures?",
                "type": "guided-choice",
                "answers": [
                    {"answer_text": "I bounce back quickly and stay focused", "answer_value": 0},
                    {"answer_text": "I struggle initially but get back on track", "answer_value": 1},
                    {"answer_text": "I feel discouraged and lose momentum", "answer_value": 2},
                    {"answer_text": "I avoid thinking about failures and move on", "answer_value": 3},
                    {"answer_text": "I learn from my failures and move on", "answer_value": 4}
                ]
            },
            {
                "question_slug": "focus-support-strategies",
                "question_text": "What strategies help you focus best?",
                "type": "select-any",
                "answers": [
                    {"answer_text": "Timers or Pomodoro technique", "answer_value": 0},
                    {"answer_text": "Body doubling (working alongside someone)", "answer_value": 1},
                    {"answer_text": "Background music or white noise", "answer_value": 2},
                    {"answer_text": "Physical movement breaks", "answer_value": 3},
                    {"answer_text": "Visual to-do lists", "answer_value": 4},
                    {"answer_text": "Clear external deadlines", "answer_value": 5}
                ]
            }
        ]
    },
    {
      "subcategory_slug": "value-map",
      "questions": [
        {
          "question_slug": "core-values-selection",
          "question_text": "Which of these values resonate most with you? (Select 7-10)",
          "type": "select-any",
          "answers": [
            {"answer_text": "Authenticity – Being true to yourself and your beliefs", "answer_value": 0},
            {"answer_text": "Achievement – Striving for excellence and reaching goals", "answer_value": 1},
            {"answer_text": "Adventure – Seeking new experiences and excitement", "answer_value": 2},
            {"answer_text": "Altruism – Helping others without expecting anything in return", "answer_value": 3},
            {"answer_text": "Balance – Maintaining harmony between different aspects of life", "answer_value": 4},
            {"answer_text": "Compassion – Showing kindness and empathy to others", "answer_value": 5},
            {"answer_text": "Community – Valuing social connections and collective well-being", "answer_value": 6},
            {"answer_text": "Creativity – Expressing originality and new ideas", "answer_value": 7},
            {"answer_text": "Curiosity – Seeking knowledge and exploring new ideas", "answer_value": 8},
            {"answer_text": "Discipline – Staying focused and committed to your goals", "answer_value": 9},
            {"answer_text": "Fairness – Treating everyone with justice and equality", "answer_value": 10},
            {"answer_text": "Family – Prioritizing close relationships with loved ones", "answer_value": 11},
            {"answer_text": "Freedom – Having the ability to make choices independently", "answer_value": 12},
            {"answer_text": "Friendship – Valuing meaningful and supportive relationships", "answer_value": 13},
            {"answer_text": "Growth – Constantly improving and developing yourself", "answer_value": 14},
            {"answer_text": "Health & Well-being – Taking care of your physical and mental health", "answer_value": 15},
            {"answer_text": "Honesty – Being truthful and transparent in all situations", "answer_value": 16},
            {"answer_text": "Humility – Staying modest and open to learning", "answer_value": 17},
            {"answer_text": "Independence – Valuing self-reliance and autonomy", "answer_value": 18},
            {"answer_text": "Integrity – Acting according to strong moral and ethical principles", "answer_value": 19},
            {"answer_text": "Justice – Standing up for fairness and equal treatment", "answer_value": 20},
            {"answer_text": "Kindness – Treating others with warmth and generosity", "answer_value": 21},
            {"answer_text": "Knowledge – Pursuing education and understanding", "answer_value": 22},
            {"answer_text": "Leadership – Inspiring and guiding others toward success", "answer_value": 23},
            {"answer_text": "Learning – Gaining new skills and knowledge throughout life", "answer_value": 24},
            {"answer_text": "Love – Fostering deep affection and care for others", "answer_value": 25},
            {"answer_text": "Loyalty – Staying faithful and committed to people and values", "answer_value": 26},
            {"answer_text": "Mindfulness – Being present and aware in the moment", "answer_value": 27},
            {"answer_text": "Openness – Being receptive to different perspectives and ideas", "answer_value": 28},
            {"answer_text": "Optimism – Maintaining a hopeful and positive outlook", "answer_value": 29},
            {"answer_text": "Passion – Bringing energy and enthusiasm to what you do", "answer_value": 30},
            {"answer_text": "Peace – Seeking inner calm and harmony", "answer_value": 31},
            {"answer_text": "Perseverance – Pushing through challenges without giving up", "answer_value": 32},
            {"answer_text": "Personal Development – Focusing on self-improvement", "answer_value": 33},
            {"answer_text": "Respect – Treating others with dignity and consideration", "answer_value": 34},
            {"answer_text": "Responsibility – Being accountable for your actions", "answer_value": 35},
            {"answer_text": "Security – Ensuring stability and safety in life", "answer_value": 36},
            {"answer_text": "Self-Discipline – Practicing control and consistency", "answer_value": 37},
            {"answer_text": "Spirituality – Connecting with something greater than yourself", "answer_value": 38},
            {"answer_text": "Success – Achieving meaningful goals and accomplishments", "answer_value": 39}
          ]
        },
        {
            "question_slug": "values-top-3",
            "question_text": "From your previous list, select up to 3 that you feel are most important to you.",
            "type": "select-4"
        },
        # {
        #     "question_slug": "select-2-values",
        #     "question_text": "From your previous list, select the 2 that you feel are most important to you.",
        #     "type": "select-2"
        # },
        {
            "question_slug": "values-top-1",
            "question_text": "From your previous list, the one that is most important to you.",
            "type": "select-1"
        }
      ]
    },
    {
      "subcategory_slug": "interest-map",
      "questions": [
        {
          "question_slug": "personal-interests",
          "question_text": "Which topics or activities interest you the most? (Select any that apply)",
          "type": "select-any",
          "answers": [
            {"answer_text": "Physical Fitness & Exercise", "answer_value": 0},
            {"answer_text": "Mental Wellness & Self-Care", "answer_value": 1},
            {"answer_text": "Nutrition & Healthy Eating", "answer_value": 2},
            {"answer_text": "Creative Arts & Expression", "answer_value": 3},
            {"answer_text": "Reading & Learning", "answer_value": 4},
            {"answer_text": "Outdoor Activities & Adventure", "answer_value": 5},
            {"answer_text": "Spirituality & Mindfulness", "answer_value": 6},
            {"answer_text": "Skill Building & Personal Development", "answer_value": 7},
            {"answer_text": "Career Advancement & Productivity", "answer_value": 8},
            {"answer_text": "Music & Performing Arts", "answer_value": 9},
            {"answer_text": "Technology & Innovation", "answer_value": 10},
            {"answer_text": "Gaming & Digital Entertainment", "answer_value": 11},
            {"answer_text": "Social & Community Engagement", "answer_value": 12},
            {"answer_text": "Travel & Cultural Exploration", "answer_value": 13},
            {"answer_text": "Home & Interior Design", "answer_value": 14},
            {"answer_text": "Sustainability & Environmentalism", "answer_value": 15},
            {"answer_text": "DIY & Crafting", "answer_value": 16},
            {"answer_text": "Entrepreneurship & Business", "answer_value": 17},
            {"answer_text": "Finance & Investing", "answer_value": 18},
            {"answer_text": "Parenting & Family Dynamics", "answer_value": 19},
            {"answer_text": "Science & Discovery", "answer_value": 20},
            {"answer_text": "Public Speaking & Communication", "answer_value": 21},
            {"answer_text": "Fashion & Personal Style", "answer_value": 22},
            {"answer_text": "Cooking & Culinary Arts", "answer_value": 23},
            {"answer_text": "Martial Arts & Self-Defense", "answer_value": 24},
            {"answer_text": "Content Creation & Digital Media",   "answer_value": 25},
            {"answer_text": "Photography & Videography",         "answer_value": 26},
            {"answer_text": "Podcasting & Audio Production",     "answer_value": 27},
            {"answer_text": "Gardening & Horticulture",          "answer_value": 28},
            {"answer_text": "Language Learning & Linguistics",    "answer_value": 29}
          ]
        },
        {
            "question_slug": "personal-interests-top-5",
            "question_text": "From your previously selected interests, select your top 5.",
            "type": "select-5"
        },
        {
            "question_slug": "personal-interests-top-3",
            "question_text": "From those selected, select your top 3?",
            "type": "select-3"
        },
        {
            "question_slug": "personal-interests-top-1",
            "question_text": "From those selected, select your top 3?",
            "type": "select-3"
        },
        {
          "question_slug": "new-skills-interest",
          "question_text": "Are there any new skills or habits you’d like to learn? (Select any that apply)",
          "type": "select-any",
          "answers": [
            {"answer_text": "Learning a new language", "answer_value": 0},
            {"answer_text": "Developing better time management", "answer_value": 1},
            {"answer_text": "Practicing meditation or mindfulness", "answer_value": 2},
            {"answer_text": "Improving public speaking skills", "answer_value": 3},
            {"answer_text": "Mastering a musical instrument", "answer_value": 4},
            {"answer_text": "Building coding & programming skills", "answer_value": 5},
            {"answer_text": "Enhancing leadership & management abilities", "answer_value": 6},
            {"answer_text": "Developing financial literacy & investing habits", "answer_value": 7},
            {"answer_text": "Strengthening writing & storytelling skills", "answer_value": 8},
            {"answer_text": "Learning photography or videography", "answer_value": 9},
            {"answer_text": "Cooking more diverse & nutritious meals", "answer_value": 10},
            {"answer_text": "Starting a fitness or workout routine", "answer_value": 11},
            {"answer_text": "Engaging in regular journaling or self-reflection", "answer_value": 12},
            {"answer_text": "Exploring creative arts & painting", "answer_value": 13},
            {"answer_text": "Practicing social skills & networking", "answer_value": 14},
            {"answer_text": "Improving focus & productivity habits", "answer_value": 15},
            {"answer_text": "Adopting better sleep habits", "answer_value": 16},
            {"answer_text": "Becoming more sustainable & eco-conscious", "answer_value": 17},
            {"answer_text": "Training for endurance sports (e.g., running, cycling)", "answer_value": 18},
            {"answer_text": "Becoming skilled in negotiation & persuasion", "answer_value": 19},
            {"answer_text": "Developing DIY home improvement skills", "answer_value": 20},
            {"answer_text": "Learning self-defense & martial arts", "answer_value": 21},
            {"answer_text": "Starting a side business or freelance career", "answer_value": 22},
            {"answer_text": "Enhancing critical thinking & problem-solving", "answer_value": 23},
            {"answer_text": "Learning effective stress management techniques", "answer_value": 24}
          ]
        }
      ]
    },
    {
      "subcategory_slug": "current-priority-map",
      "questions": [
        {
          "question_slug": "current-life-priorities",
          "question_text": "Which of these areas are your biggest priorities right now? (Select up to 3)",
          "type": "select-any",
          "answers": [
              {"answer_text": "Career & Professional Growth", "answer_value": 0},
              {"answer_text": "Personal Growth & Education", "answer_value": 1},
              {"answer_text": "Health & Fitness", "answer_value": 2},
              {"answer_text": "Financial Stability & Wealth Building", "answer_value": 3},
              {"answer_text": "Family & Relationships", "answer_value": 4},
              {"answer_text": "Mental & Emotional Well-being", "answer_value": 5},
              {"answer_text": "Spiritual Growth & Inner Peace", "answer_value": 6},
              {"answer_text": "Leisure & Hobbies", "answer_value": 7},
              {"answer_text": "Community & Social Impact", "answer_value": 8},
              {"answer_text": "Travel & Exploration", "answer_value": 9},
              {"answer_text": "Creativity & Artistic Expression", "answer_value": 10},
              {"answer_text": "Reducing Stress & Simplifying Life", "answer_value": 11},
              {"answer_text": "Time Management & Productivity", "answer_value": 12},
              {"answer_text": "Work-Life Balance", "answer_value": 13},
              {"answer_text": "Building Stronger Friendships & Social Networks", "answer_value": 14},
              {"answer_text": "Developing Leadership & Influence", "answer_value": 15},
              {"answer_text": "Mindfulness & Presence", "answer_value": 16},
              {"answer_text": "Parenting & Family Development", "answer_value": 17},
              {"answer_text": "Volunteering & Philanthropy", "answer_value": 18},
              {"answer_text": "Self-Discipline & Habit Building", "answer_value": 19},
              {"answer_text": "Personal Freedom & Independence", "answer_value": 20},
              {"answer_text": "Environmental Consciousness & Sustainability", "answer_value": 21},
              {"answer_text": "Skill Building & Lifelong Learning", "answer_value": 22},
              {"answer_text": "Confidence & Self-Esteem", "answer_value": 23},
              {"answer_text": "Adventure & New Experiences", "answer_value": 24}
          ]
        },
        {
            "question_slug": "current-priority-alignment",
            "question_text": "Do you feel like your time and energy currently reflect these priorities?",
            "type": "yes-no"
        }
      ]
    },
    {
        "subcategory_slug": "envisioned-priority-map",
        "questions": [
            {
                "question_slug": "ideal-life-priorities",
                "question_text": "Which areas would you like to prioritize more in your life? (Select up to 3)",
                "type": "select-any",
                "answers": [
                    {"answer_text": "Career & Professional Growth", "answer_value": 0},
                    {"answer_text": "Personal Growth & Education", "answer_value": 1},
                    {"answer_text": "Health & Fitness", "answer_value": 2},
                    {"answer_text": "Financial Stability & Wealth Building", "answer_value": 3},
                    {"answer_text": "Family & Relationships", "answer_value": 4},
                    {"answer_text": "Mental & Emotional Well-being", "answer_value": 5},
                    {"answer_text": "Spiritual Growth & Inner Peace", "answer_value": 6},
                    {"answer_text": "Leisure & Hobbies", "answer_value": 7},
                    {"answer_text": "Community & Social Impact", "answer_value": 8},
                    {"answer_text": "Travel & Exploration", "answer_value": 9},
                    {"answer_text": "Creativity & Artistic Expression", "answer_value": 10},
                    {"answer_text": "Reducing Stress & Simplifying Life", "answer_value": 11},
                    {"answer_text": "Time Management & Productivity", "answer_value": 12},
                    {"answer_text": "Work-Life Balance", "answer_value": 13},
                    {"answer_text": "Building Stronger Friendships & Social Networks", "answer_value": 14},
                    {"answer_text": "Developing Leadership & Influence", "answer_value": 15},
                    {"answer_text": "Mindfulness & Presence", "answer_value": 16},
                    {"answer_text": "Parenting & Family Development", "answer_value": 17},
                    {"answer_text": "Volunteering & Philanthropy", "answer_value": 18},
                    {"answer_text": "Self-Discipline & Habit Building", "answer_value": 19},
                    {"answer_text": "Personal Freedom & Independence", "answer_value": 20},
                    {"answer_text": "Environmental Consciousness & Sustainability", "answer_value": 21},
                    {"answer_text": "Skill Building & Lifelong Learning", "answer_value": 22},
                    {"answer_text": "Confidence & Self-Esteem", "answer_value": 23},
                    {"answer_text": "Adventure & New Experiences", "answer_value": 24}
                ]

            },
            {
                "question_slug": "priority-shift-interest",
                "question_text": "Are you ready to take steps to shift towards these priorities?",
                "type": "yes-no"
            }
        ]
    },
]

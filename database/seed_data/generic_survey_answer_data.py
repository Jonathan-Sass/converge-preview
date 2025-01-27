generic_survey_answer_data = [
        # SELECT ANY/ALL, OPEN ANSWER, and GUIDED CHOICE ANSWERS - DEPRECATED?
        # {
        #     'answer_type': 'open-answer',
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # {
        #     'answer_type': 'select-any',
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # {
        #     'answer_type': 'select-any-add',
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # {
        #     'answer_type': 'guided-choice',
        #     'answers': [
        #         {'answer_text': None, "answer_value": 0}
        #     ]
        # },
        # YES/NO and ANSWERS
        {
            "answer_type": "yes-no",
            "answers": [
                {"answer_text": "Yes", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0},
            ],
        },
        {
            "answer_type": "yes-no-sometimes",
            "answers": [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "Sometimes", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0},
            ],
        },
        {
            "answer_type": "yes-no-unsure",
            "answers": [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "I am not sure", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0},
            ],
        },
        {
            "answer_type": "yes-no-alittle",
            "answers": [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "Maybe a little", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0},
            ],
        },
        {
            "answer_type": "yes-no-inconsistent",
            "answers": [
                {"answer_text": "Yes", "answer_value": 2},
                {"answer_text": "Yes, but it's inconsistent", "answer_value": 1},
                {"answer_text": "No", "answer_value": 0},
            ],
        },
        {
            "answer_type": "true-false",
            "answers": [
                {"answer_text": "True", "answer_value": 1},
                {"answer_text": "False", "answer_value": 0},
            ],
        },
        #  SCALE ANSWER SETS
        # Scale 1-5 Answers
        {
            "answer_type": "scale-agree-disagree",
            "answers": [
                {"answer_text": "Strongly Agree", "answer_value": 4},
                {"answer_text": "Agree", "answer_value": 3},
                {"answer_text": "Neutral", "answer_value": 2},
                {"answer_text": "Disagree", "answer_value": 1},
                {"answer_text": "Strongly Disagree", "answer_value": 0},
            ],
        },
        {
            "answer_type": "scale-interest",
            "answers": [
                {"answer_text": "Very Interested", "answer_value": 4},
                {"answer_text": "Interested", "answer_value": 3},
                {"answer_text": "Neutral", "answer_value": 2},
                {"answer_text": "Not Interested", "answer_value": 1},
                {"answer_text": "Not at All Interested", "answer_value": 0},
            ],
        },
        {
            "answer_type": "scale-stress-resilience",
            "answers": [
                {
                    "answer_text": "Yes, very resilient, I can handle just about anything.",
                    "answer_value": 4,
                },
                {
                    "answer_text": "Mostly resilient, I have a relatively high tolerance to stress",
                    "answer_value": 3,
                },
                {
                    "answer_text": "Moderate, sometimes it is difficult to roll with the punches.",
                    "answer_value": 2,
                },
                {"answer_text": "Not very resilient", "answer_value": 1},
                {
                    "answer_text": "I am easily be overwhelmed by stress",
                    "answer_value": 0,
                },
            ],
        },
        # FREQUENCY ANSWER SETS
        {
            "answer_type": "frequency",
            "answers": [
                {"answer_text": "Always/Almost Always", "answer_value": 4},
                {"answer_text": "Frequently", "answer_value": 3},
                {"answer_text": "Sometimes", "answer_value": 2},
                {"answer_text": "Rarely", "answer_value": 1},
                {"answer_text": "Never/Almost Never", "answer_value": 0},
            ],
        },
        {
            "answer_type": "frequency-often",
            "answers": [
                {"answer_text": "Very Often", "answer_value": 4},
                {"answer_text": "Often", "answer_value": 3},
                {"answer_text": "Sometimes", "answer_value": 2},
                {"answer_text": "Rarely", "answer_value": 1},
                {"answer_text": "Never", "answer_value": 0},
            ],
        },
        {
            "answer_type": "frequency-day",
            "answers": [
                {"answer_text": "Almost every day", "answer_value": 4},
                {"answer_text": "Most days", "answer_value": 3},
                {"answer_text": "Sometimes", "answer_value": 2},
                {"answer_text": "Rarely", "answer_value": 1},
                {"answer_text": "Never/Almost Never", "answer_value": 0},
            ],
        },
        # Opinion-Importance Scale
        {
            "answer_type": "opinion-importance-scale",
            "answers": [
                {"answer_text": "Extremely important", "answer_value": 4},
                {"answer_text": "Very important", "answer_value": 3},
                {"answer_text": "Moderately important", "answer_value": 2},
                {"answer_text": "Slightly important", "answer_value": 1},
                {"answer_text": "Not at all important", "answer_value": 0},
            ],
        },
        # RANGE ANSWER SETS
        {
            "answer_type": "range-mins-hours-10-2",
            "answers": [
                {"answer_text": "10 minutes", "answer_value": 0},
                {"answer_text": "20 minutes", "answer_value": 1},
                {"answer_text": "30 minutes", "answer_value": 2},
                {"answer_text": "45 minutes", "answer_value": 3},
                {"answer_text": "1 hour", "answer_value": 4},
                {"answer_text": "90 minutes", "answer_value": 5},
                {"answer_text": "2 hours", "answer_value": 6},
            ],
        },
        {
            "answer_type": "range-hours-0-10+",
            "answers": [
                {"answer_text": "0-1 hour", "answer_value": 0},
                {"answer_text": "1-5 hours", "answer_value": 1},
                {"answer_text": "5-10 hours", "answer_value": 2},
                {"answer_text": "10+ hours", "answer_value": 3},
            ],
        },
        {
            "answer_type": "range-hours-0-20+",
            "answers": [
                {"answer_text": "0-1 hour", "answer_value": 0},
                {"answer_text": "1-5 hours", "answer_value": 1},
                {"answer_text": "5-10 hours", "answer_value": 2},
                {"answer_text": "10-20 hours", "answer_value": 3},
                {"answer_text": "20+ hours", "answer_value": 3},
            ],
        },
        # Range Less 5, Greater 8 Hours
        {
            "answer_type": "range-hours-L5-G8",
            "answers": [
                {"answer_text": "Less than 5 hours", "answer_value": 1},
                {"answer_text": "5-6 hours", "answer_value": 2},
                {"answer_text": "7-8 hours", "answer_value": 3},
                {"answer_text": "More than 8 hours", "answer_value": 4},
            ],
        },
        {
            "answer_type": "range-hours-sleep",
            "answers": [
                {"answer_text": "Less than 5 hours", "answer_value": 1},
                {"answer_text": "5-7 hours", "answer_value": 2},
                {"answer_text": "7-8 hours", "answer_value": 3},
                {"answer_text": "8-10 hours", "answer_value": 4},
                {"answer_text": "More than 10 hours", "answer_value": 5},
            ],
        },
        # SATISFACTION ANSWERS
        {
            "answer_type": "satisfaction",
            "answers": [
                {"answer_text": "Very satisfied", "answer_value": 4},
                {"answer_text": "Mostly satisfied", "answer_value": 3},
                {"answer_text": "Neutral", "answer_value": 2},
                {"answer_text": "Not very satisfied", "answer_value": 1},
                {"answer_text": "Dissatisfied", "answer_value": 0},
            ],
        },
        {
            "answer_type": "satisfaction-balance",
            "answers": [
                {"answer_text": "Very balanced", "answer_value": 4},
                {"answer_text": "Mostly balanced", "answer_value": 3},
                {"answer_text": "Could be better", "answer_value": 2},
                {"answer_text": "Not very balanced", "answer_value": 1},
                {"answer_text": "Overwhelmed or unbalanced", "answer_value": 0},
            ],
        },
        # SUPPORT SYSTEM
        # MULTIPLE CHOICE
        # Multiple Choice
        {
            "answer_type": "multiple-choice-travel-cat",
            "answers": [
                {"answer_text": "Adventure Travel", "answer_value": 1},
                {"answer_text": "Relaxation and Leisure", "answer_value": 2},
                {"answer_text": "Cultural Exploration", "answer_value": 3},
                {"answer_text": "Family-Friendly", "answer_value": 4},
                {"answer_text": "Luxury Travel", "answer_value": 5},
            ],
        },
    ]
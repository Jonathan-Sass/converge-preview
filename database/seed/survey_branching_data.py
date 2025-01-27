# In the event that a given answer should terminate the survey, "answer_text": "end_survey"

survey_branching_data = [
  
  # Survey_topic: Getting started
  {
    "survey_question_slug": "existing_routines_check",
    "answer_text": "no",
    "next_question_slug": "assistance-building-routines-check"
  },
  {
    "survey_question_slug": "existing-routines-comparison-check",
    "answer_text": "yes",
    "next_question_slug": "routine-types-interest-check"
  },
  {
    "survey_question_slug": "existing-routines-comparison-check",
    "answer_text": "no",
    "next_question_slug": "build-your-own-routine-check"
  },
  {
    "survey_question_slug": "assistance-building-routines-check",
    "answer_text": "yes",
    "next_question_slug": "routine-types-interest-check"
  },
  {
    "survey_question_slug": "assistance-building-routines-check",
    "answer_text": "no",
    "next_question_slug": "build-your-own-routine-check"
  },

]


# {
#     "survey_question_slug": "",
#     "answer_text": "",
#     "next_question_slug": ""
#   },
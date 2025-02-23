# In the event that a given answer should terminate the survey, "answer_text": "end_survey"

survey_branching_data = [
  
  # Subcategory: Getting started
  {
    "survey_question_slug": "existing-routines-check",
    "answer_text": "No",
    "next_question_slug": "wellness-survey-check"
  },
  {
    "survey_question_slug": "wellness-survey-check",
    "answer_text": "Yes",
    "next_question_slug": "routine-types-interest-check"
  },
  {
    "survey_question_slug": "wellness-survey-check",
    "answer_text": "No",
    "next_question_slug": "build-your-own-routine-check"
  },
  {
    "survey_question_slug": "assistance-building-routines-check",
    "answer_text": "Yes",
    "next_question_slug": "routine-types-interest-check"
  },
  {
    "survey_question_slug": "assistance-building-routines-check",
    "answer_text": "No",
    "next_question_slug": "build-your-own-routine-check"
  },

]


# {
#     "survey_question_slug": "",
#     "answer_text": "",
#     "next_question_slug": ""
#   },
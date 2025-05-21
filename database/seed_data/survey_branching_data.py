# In the event that a given answer should terminate the survey, "next_question_slug": "end_survey"

survey_branching_data = [
  # Subcategory: Day Map
  {
    "survey_question_slug": "morning-routine-check",
    "answer_text": "No",
    "next_question_slug": "habit-adoption-pattern"
  },
  {
    "survey_question_slug": "evening-routine-check",
    "answer_text": "No",
    "next_question_slug": "pm-routine-time-availability-prompt"
  },

# Subcategory: confirm-goal-category
  {
    "survey_question_slug": "goal-category-confirmation",
    "answer_text": "Yes, that sounds good.",
    "next_question_slug": "end_survey"
  },
  # {
  #   "survey_question_slug": "existing-routines-check",
  #   "answer_text": "No",
  #   "next_question_slug": "wellness-survey-check"
  # },

  # Subcategory: Getting started
  # {
  #   "survey_question_slug": "existing-routines-check",
  #   "answer_text": "No",
  #   "next_question_slug": "wellness-survey-check"
  # },
  # {
  #   "survey_question_slug": "wellness-survey-check",
  #   "answer_text": "Yes",
  #   "next_question_slug": "routine-types-interest-check"
  # },
  # {
  #   "survey_question_slug": "wellness-survey-check",
  #   "answer_text": "No",
  #   "next_question_slug": "build-your-own-routine-check"
  # },
  # {
  #   "survey_question_slug": "assistance-building-routines-check",
  #   "answer_text": "Yes",
  #   "next_question_slug": "routine-types-interest-check"
  # },
  # {
  #   "survey_question_slug": "assistance-building-routines-check",
  #   "answer_text": "No",
  #   "next_question_slug": "build-your-own-routine-check"
  # },

]


# {
#     "survey_question_slug": "",
#     "answer_text": "",
#     "next_question_slug": ""
#   },
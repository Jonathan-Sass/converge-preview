// TODO: Consider refactoring, numerous processes can likely be condensed
// selectAnswer and subsequent answer processing handles all types of questions concurrently.
// render functions should attach eventlisteners to processing functions for each question type rather than using conditionals throughout to determine question-types

document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('start-btn')
    const nextButton = document.getElementById('next-btn')
    const finishButton = document.getElementById('finish-btn')
    const questionContainer = document.getElementById('question-container')
    const questionElement = document.getElementById('question')
    const quizForm = document.getElementById('quiz-form')
    const quizInput = document.getElementById('quiz-input')
    const answerButtons = document.getElementById('answer-buttons')
    const checkboxContainer = document.getElementById('answer-checkboxes')
    const surveyIntro = document.getElementById('survey-intro')
    const nextSectionButton = document.getElementById('next-section-btn')
    
    let currentQuestion = [];
    let currentQuestionSet = [];
    let surveyBranches = [];
    let currentQuestionIndex = 0;
    let selectedButton = null;
    let selectedAnswers = [];
    let answerData = {}
    let collectedAnswers = [];
    let selectLimit;


// EVENT LISTENERS FOR SURVEYS
startButton.addEventListener('click', async (event) => {
    event.preventDefault();
    startSurvey();
});

nextButton.addEventListener('click', (event) => {
    event.preventDefault();

    if (currentQuestionSet[currentQuestionIndex]['type'] != 'prompt') {
        // Check if any answer has been selected
        if (selectedAnswers.length === 0 && !selectedButton) {
          alert('Please select an answer before proceeding.');
          return; // Exit if no answer is selected
        }
    }

    // IF OPEN TEXT, answer.open_answer_text = text
    // ETC

    // TODO: SEPARATE INTO collectAnswerData()
    // For multiple-choice (select-any) questions, use the selectedAnswers array
    if (selectedAnswers.length > 0) {
        selectedAnswers.forEach(answerData => {
            // Check if the question is already answered
            const existingAnswerIndex = collectedAnswers.findIndex(answer => 
                answer.question_id === answerData.question_id &&
                answer.answer_id === answerData.answer_id &&
                answer.answer_text === answerData.answer_text
            );
            if (existingAnswerIndex > -1) {
                // Update existing answer
                collectedAnswers[existingAnswerIndex] = answerData;
            } else {
                // Add new answer
                collectedAnswers.push(answerData);
            }
        });
    } else if (selectedButton) {
        // For single-choice questions, use selectedButton
        // answerData = {
        //     question_id: selectedButton.getAttribute('data-question-id'),
        //     answer_id: selectedButton.getAttribute('data-answer-id'),
        //     answer_text: selectedButton.answer_text
        // };

        const existingAnswerIndex = collectedAnswers.findIndex(answer => answer.question_id === answerData.question_id);
        if (existingAnswerIndex > -1) {
            collectedAnswers[existingAnswerIndex] = answerData;
        } else {
            collectedAnswers.push(answerData);
        }
    }

    // Reset selectedAnswers and selectedButton for the next question
    selectedAnswers = [];
    selectedButton = null;

    console.log('Collected Answers:', collectedAnswers);

    updateCurrentQuestionIndex()
    setNextQuestion();
  });
  
  finishButton.addEventListener('click', async (event) => {
    const category = getCategory();
    
    try {
      // Send the collected answers to the backend as a single request
      console.log('Posting to: /surveys/' + category + '/answers')
      const response = await fetch(`/surveys/${category}/answers`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(collectedAnswers),  // Send the stored answers as JSON
      });
      
      if (response.ok) {
        alert('Quiz submitted successfully!');
        // Optionally, navigate to a results page or reset the form
      } else {
        alert('Failed to submit the quiz.');
      }
    } catch (error) {
      alert('Error: ' + error.message);
    }
    finishButton.classList.add('d-none')
    nextSectionButton.classList.remove('d-none')
    // window.location.href = '/goals/health/select';
  });
  
  
  // LOGIC FOR SURVEY MECHANICS
  
  async function startSurvey() {
    resetState()
      startButton.classList.add('d-none');
      if (surveyIntro) {
        surveyIntro.classList.add('d-none');
      }
      
      // QUERY DB TO FETCH QUESTIONS
      await fetchSurveyQuestions();
      
      // console.log('***STARTING GAME*****')
      currentQuestionIndex = 0;
      questionContainer.classList.remove('d-none');
  }
      
  // This function queries the DB to fetch survey questions
  async function fetchSurveyQuestions() {
    const category = getCategory()
    const subcategory = getSubcategory()
    
    try {
      // Sending a POST request to retrieve survey questions
      const response = await fetch('/surveys/questions/retrieve', {
        method: 'POST',  // Using POST method for sending data
        headers: {
          'Content-Type': 'application/json'  // Specifying the content type
        },
        body: JSON.stringify({
          'category': category, 
          'subcategory': subcategory
        })
      });
      
      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`An error occurred: ${response.statusText}`);
      }
      
      const jsonResponse = await response.json();
      console.log("Response JSON:", jsonResponse);
      // Parsing the response as JSON
      ({currentQuestionSet, surveyBranches } = jsonResponse);
      
      
      // console.log('*****Current Question Set in fetchSurveyQuestions*****')
      // console.log(currentQuestionSet)
      
      // Send question data to be rendered on the page
      renderSurveyQuestion(currentQuestionSet); 
      
    } catch (error) {
      console.error('Error fetching survey questions:', error);
    }
  }
      
  function updateCurrentQuestionIndex() {
    let indexUpdated = false; 
    // Move to the next question by following survey branching or incrementing the index
    console.log("AnswerData: ")
    console.log(answerData)
  
    console.log("currentQuestion")
    console.log(currentQuestionSet[currentQuestionIndex])
    // console.log("surveyBranches: ")
    // console.log(surveyBranches)
  
      for (const questionBranch of surveyBranches) {
        
        // Check current questionId for survey_branch with matching questionId
        if (questionBranch["questionId"] === currentQuestionSet[currentQuestionIndex]["questionId"]) {
         console.log("matching question in surveyBranches.forEach: ", questionBranch)
          console.log("Branch detected!")
          // IF answer_text matches survey_branch answer_text, update currentQuestionIndex to matching index for next_question_slug
          //  FAULTY - question["questionText"] does not exist, see above
          if (answerData.answer_text === questionBranch["answerText"]) {
          console.log("Answer Texts match: ", questionBranch)
          const targetIndex = currentQuestionSet.findIndex(q => q["questionSlug"] === questionBranch["nextQuestionSlug"])
          currentQuestionIndex = targetIndex !== -1 ? targetIndex : currentQuestionIndex + 1;
          indexUpdated = true;
          break;
        }
      }
    }
    if (!indexUpdated) {
      console.log("Branch not detected!")
      currentQuestionIndex++;
    }
    console.log(`currentQuestionIndex: ${currentQuestionIndex}`)
    console.log("****************************************************")
  }
      
  // Function to render survey questions on the page
  function renderSurveyQuestion(currentQuestionSet) {
    // resetState()

    // Example: Show the first question as in showQuestion function
    currentQuestion = currentQuestionSet[currentQuestionIndex]; 
    questionElement.innerText = currentQuestion.question;  // Display the question text
    
    if (currentQuestion.type === 'prompt') {
      renderPrompt(currentQuestion);
    } else if (currentQuestion.type === 'open-answer') {
      renderOpenAnswerWithExamples(currentQuestion);
    } else if (currentQuestion.type === 'guided-choice') {
      renderGuidedChoice(currentQuestion);
    } else if (currentQuestion.type === 'select-any') {
      renderSelectAny(currentQuestion);
    } else if (currentQuestion.type === 'select-any-add') {
      renderSelectAnyAddOpenAnswer(currentQuestion);
    } else if (currentQuestion.type.match(/^select-(\d+)$/)) {
      renderSelectWithLimit(currentQuestion)
    } else {
      renderGenericAnswers(currentQuestion);
    }
  }
      
  function renderPrompt(currentQuestion) {
    nextButton.classList.remove("d-none")
  }

  function renderGenericAnswers(currentQuestion) {
      // Create buttons for each answer
      currentQuestion.answers.forEach(answer => {
          const button = document.createElement('button');
          button.innerText = answer.answerText;
          button.setAttribute('data-question-id', currentQuestion.questionId);
          button.setAttribute('data-answer-id', answer.answerId);
          button.value = answer.answerValue;
          button.classList.add('btn', 'btn-outline-dark', 'col', 'm-3');
          button.addEventListener('click', selectAnswer);  // Attach event listener
          answerButtons.appendChild(button);
      });
  }

  function renderGuidedChoice(currentQuestion) {
      // const answerButtons = document.getElementById('answer-buttons');
      // answerButtons.innerHTML = ''; // Clear previous answers
      console.log(currentQuestion)
      
      answerButtons.classList.remove('d-flex')

      currentQuestion.answers.forEach(answer => {
          const button = document.createElement('button');
          button.innerText = answer.answerText;
          button.setAttribute('data-question-id', currentQuestion.questionId);
          button.setAttribute('data-answer-id', answer.answerId);
          button.value = answer.answerValue;
          button.classList.add('btn', 'btn-outline-dark', 'd-block', 'm-auto', 'my-3', 'guided-choice-answer');
          button.addEventListener('click', selectAnswer);
          answerButtons.appendChild(button);
      });
  }

  function renderSelectAny(currentQuestion) {
      // const answerContainer = document.getElementById('answer-buttons');
      // answerContainer.innerHTML = ''; // Clear previous answers

      console.log('*****currentQuestion in renderSelectAny()*****')
      console.log(currentQuestion)

      populateAnswerCheckboxes(currentQuestion);

      nextButton.classList.remove('d-none');
      answerButtons.classList.remove('d-flex');
  };

  function renderSelectAnyAddOpenAnswer(currentQuestion) {
    // const answerContainer = document.getElementById('answer-buttons');
    // answerContainer.innerHTML = ''; // Clear previous answers
    
    console.log('*****currentQuestion in renderSelectAny()*****')
    console.log(currentQuestion)
    
    populateAnswerCheckboxes(currentQuestion);
    // TODO: ADD OPEN ANSWER FUNCTIONALITY
    // createOpenAnswerInput()
    
    nextButton.classList.remove('d-none');
    answerButtons.classList.remove('d-flex')
    
  }

  function populateAnswerCheckboxes(currentQuestion) {
    currentQuestion.answers.forEach((answer, index) => {
      const label = document.createElement('label');
      
      label.classList.add('btn', 'btn-outline-dark', 'mb-1','form-check-label');
      
      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.classList.add('form-check-input', 'mx-2');
      checkbox.setAttribute('data-question-id', currentQuestion.questionId);
      checkbox.setAttribute('data-answer-id', answer.answerId)
      checkbox.id = answer.answerId;
      checkbox.addEventListener('click', selectAnswer);
      checkbox.value = answer.answerValue;
      
      const checkboxId = `checkbox-${currentQuestion.questionId}-${index}`;
      checkbox.id = checkboxId;
      label.setAttribute('for', checkboxId);
      label.appendChild(document.createTextNode(answer.answerText));
  
      label.prepend(checkbox);
      // label.addEventListener('click', selectAnswer)
      checkboxContainer.appendChild(label);
    });
  };

  function renderSelectWithLimit(currentQuestion) {
    const {previousAnswerIds, questionId} = collectPreviousAnswerIds()
    const previousAnswers = previousAnswersToArray(questionId, previousAnswerIds)
    currentQuestion.answers = previousAnswers;

    populateAnswerCheckboxes(currentQuestion);

    nextButton.classList.remove('d-none');
    answerButtons.classList.remove('d-flex');
  };

  function previousAnswersToArray(questionId, previousAnswerIds) {
    const selectWithLimitAnswers = [];

    currentQuestionSet.forEach(question => {
      if (question.questionId === questionId) {
        question.answers.forEach(answer => {
          if (previousAnswerIds.includes(answer.answerId)) {
            selectWithLimitAnswers.push(answer);
          }
        })
      }
    })
    return selectWithLimitAnswers;
  };

  function collectPreviousAnswerIds() {
    const previousAnswerIds = [];
    let questionId = 0;

    if (collectedAnswers.length > 1) {
      questionId = collectedAnswers[collectedAnswers.length - 1].question_id;
    };
    
    // push 
    collectedAnswers.forEach(answer => {
        if (answer.question_id === questionId) {
          previousAnswerIds.push(answer.answer_id);
        }
    });

    return {previousAnswerIds, questionId};
  }
  
  function createOpenAnswerInput(currentQuestion, placeholder = 'Your answer here...') {
      const openAnswerInput = document.createElement('textarea');
      openAnswerInput.setAttribute('placeholder', placeholder);
      openAnswerInput.setAttribute('data-question-id', currentQuestion.questionId);
      openAnswerInput.setAttribute('data-answer-id', currentQuestion.answerId);

      openAnswerInput.classList.add('form-control', 'my-3', 'w-50', 'm-auto', 'open-answer-input');
      return openAnswerInput;
  }

  function setNextQuestion() {
      resetState();
      if (currentQuestionIndex < currentQuestionSet.length) {
          renderSurveyQuestion(currentQuestionSet);
      } else {
          // alert('Quiz completed!');
          questionContainer.classList.add('d-none');
          finishButton.classList.remove('d-none') 
      }
  }

  function selectAnswer(e) {
      const selectedButton = e.currentTarget || e.target;
      if (!selectedButton) return;

      // checkboxId used as unique ID for compiling answer array
      const checkboxId = selectedButton.id;

      // Check if the question allows multiple selections
      const questionType = currentQuestion.type;
      // const isTypeSelectAny = questionType === 'select-any' || questionType === 'select-any-add'
      answerData = {
          question_id: parseInt(selectedButton.getAttribute('data-question-id'), 10), 
          answer_id: parseInt(selectedButton.getAttribute('data-answer-id'), 10), 
          answer_type: currentQuestion.type
      };
      
      if (questionType === 'select-any' || questionType === 'select-any-add') {
          selectMultipleAnswers(selectedButton, checkboxId);
      
          // Matches any question type with the pattern 'select-#' ('select-' followed by any number)
      } else if (/^select-(\d+)$/.test(questionType)) {
          const match = currentQuestion.type.match(/^select-(\d+)$/)
          selectLimit = parseInt(match[1], 10)  

          const isAlreadySelected = selectedAnswers.some(answer => answer.checkbox_id ===checkboxId)

          if (!isAlreadySelected && selectedAnswers.length >= selectLimit) {
            e.preventDefault();
            alert(`You may only select ${selectLimit} answers.`)
            return
          }  

          selectMultipleAnswers(selectedButton, checkboxId)

      } else {
          selectSingleAnswer(selectedButton, checkboxId);
          
          // Show or hide the Next button based on selection
          const anySelected = document.querySelector('.btn-dark');
          
          if (anySelected) {
              nextButton.classList.remove('d-none');
          } else {
              nextButton.classList.add('d-none');
          };
      };
  };

  function selectMultipleAnswers(selectedButton, checkboxId) {
    answerData.checkbox_id = checkboxId
    // answerData.answer_text = selectedButton.value

    const answerIndex = selectedAnswers.findIndex(
        answer => answer.checkbox_id === checkboxId
    );

    if (answerIndex > -1) {
        selectedAnswers = selectedAnswers.filter(
            answer => answer.checkbox_id !== checkboxId
        );

        selectedButton.classList.remove('btn-dark');
        selectedButton.classList.add('btn-outline-dark');
        // selectedAnswers.splice(answerIndex, 1);

        // console.log('*****selectedAnswers in selectAnswer()*****')
        // console.log('Spliced answerIndex:' + answerIndex);
        // console.log(selectedAnswers)
        // console.log('***************')
        // console.log('   ')
    } else {
        selectedAnswers = [...selectedAnswers, answerData]
        selectedButton.classList.add('btn-dark');
        selectedButton.classList.remove('btn-outline-dark');
        // selectedAnswers.push(answerData)

        // console.log('*****selectedAnswers in selectAnswer()*****')
        // console.log('Pushed answerIndex:' + answerIndex);
        // console.log(selectedAnswers)
        // console.log('***************')
        // console.log('   ')

    }
  }

  function selectSingleAnswer(selectedButton) {
      if(selectedButton.value) {
        answerData.answer_value = parseInt(selectedButton.value)
        answerData.answer_text = selectedButton.innerText
      }
      // if (selectedButton.answerText) {
      // }

      console.log("answerData in selectAnswer: ", answerData)

      // For single choice, deselect all other buttons first
      const allButtons = document.querySelectorAll('#answer-buttons > *');
      allButtons.forEach(button => {
          button.classList.remove('btn-dark');
          button.classList.add('btn-outline-dark');
      });

      // Select the clicked button
      selectedAnswers = [answerData]
      selectedButton.classList.add('btn-dark');
      selectedButton.classList.remove('btn-outline-dark');

      // console.log('*****selectedAnswers in selectAnswer()*****')
      // console.log('selectedAnswers reset to: ');
      // console.log(selectedAnswers)
      // console.log('***************')
      // console.log('   ')
    }

  function resetState() {
      // Remove Next button and Next Section button from page
      nextButton.classList.add('d-none')
      
      // Remove selectable answers from page
      if (checkboxContainer) {
          while (checkboxContainer.firstChild) {
              checkboxContainer.removeChild(checkboxContainer.firstChild);
          }
      }
      
      if (!answerButtons.classList.contains('d-flex')) {
          answerButtons.classList.add('d-flex')
      }
      // Remove answer buttons from page
      while (answerButtons.firstChild) {
          answerButtons.removeChild(answerButtons.firstChild);
      }
      
      scrollToElement(questionElement)
      return
  }

  function scrollToElement(element, offset = 200) {
      if (element) {
          const elementPosition = element.getBoundingClientRect().top + window.scrollY;
          window.scrollTo({ top: elementPosition - offset, behavior: 'smooth' });

      }
  }

  function getCategory() {
    let categoryElement = startButton.closest('[data-category]');
    
    if (categoryElement) {
      let category = categoryElement.dataset.category;
      return category;
    } else {
      return null;
    }
  }

  function getSubcategory() {
    // Get the parent element of the button
    let subcategoryElement = startButton.closest('[data-subcategory]');
    
    if (subcategoryElement) {
      let subcategory = subcategoryElement.dataset.subcategory;
      return subcategory
    } else {
      console.log('No subcategory found in HTML');
      return null;
    }
  }

// CLOSING DOMContentLoaded Wrapper
});
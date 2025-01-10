import { convertTimeframeForDatabase } from "./timeframe-to-date.js";

document.addEventListener("DOMContentLoaded", () => {
  const saveButtons = document.querySelectorAll("button[type='submit']");

  saveButtons.forEach(button => {
    button.addEventListener("click", validateAndProcessGoalData);
    
  });
});

async function submitGoalData(data) {

  console.log("processing and sending goal data...")
  

  try {

    const response = await fetch(`/goals/${subcategorySlug}/save`, {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });

    if (response.ok) {
      alert('Goals saved successfully!');
    } else {
      alert ('Failed to save goals.');
    }
  } catch (error) {
    alert('Error: ' + error.message)
  }
};


function validateAndProcessGoalData(event) {
  const requiredFields = document.querySelectorAll('input[required], select[required], textarea[required]');
  let allFieldsValid = true;

  requiredFields.forEach(field => {
    if (!field.value.trim()) {
      allFieldsValid = false;
      // Display error message or highlight the field
      field.classList.add('error');
      // Optionally, provide a specific error message
      const errorMessage = document.createElement('span');
      errorMessage.textContent = `${field.name} is required.`;
      errorMessage.classList.add('error-message');
      field.parentElement.appendChild(errorMessage);
    } else {
      field.classList.remove('error');
      // Remove existing error message if field is valid
      const existingError = field.parentElement.querySelector('.error-message');
      if (existingError) {
        existingError.remove();
      }
    }
  });

  if (!allFieldsValid) {
    alert('Please fill out all required fields.');
    return; // Prevent further processing
  }


  const subcategorySection = event.target.closest(".subcategory-section")
  const subcategorySlug = subcategorySection.dataset.subcategorySlug
  // const subcategoryGoalsData = processGoalData(subcategorySection)
  
  
  const subcategoryGoalsData = {
    subcategorySlug: "",
    goals: []
  }
  // Loop through all goal sections
  subcategorySection.querySelectorAll(".goal-section").forEach(goalSection => {
    // Set subcategorySlug from goal-section
    const subcategorySlug = goalSection.dataset.subcategorySlug;
    subcategoryGoalsData.subcategorySlug = subcategorySlug;

    // Loop through each goal-card for a subcategory
    goalSection.querySelectorAll(".goal-card").forEach(goalCard => {
      const goalData = {
        name: "",
        description: "", 
        goalType: "",
        priority: "",
        projectedCompletion: null,
        isComplete: false,
        milestones: []
      }
      
      const goalId = goalCard.dataset.goalId;
      goalData.name = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-name`).value;
      goalData.description = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-description`).value;
      goalData.goalType = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-type`).value;
      goalData.priority = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-priority`).value;
      goalData.projectedCompletion = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-date`).value;

      // Select all milestones
      goalCard.querySelectorAll(".milestone-card").forEach(milestoneCard => {
        const milestoneId = goalCard.dataset.milestoneId
        const milestoneData = {
          name: "",
          description: "",
          projectedCompletion: null,
          isComplete: false,
          actionItems: []
        }

        const milestoneNameElement = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-name`)
        if (milestoneNameElement) {
          milestoneData.name = milestoneNameElement.value;
        }
        console.log("Selector: " + milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-name`))
        // milestoneData.name = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-name`).value
        if (milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-description`).value) {
          milestoneData.description = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-description`).value
        }
        
        // timeValue and timeUnit conversion to projectedCompletion date
        if (milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-value`).value && milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-unit`).value) {
          const timeValue = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-value`).value;
          const timeUnit = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-unit`).value;
          milestoneData.projectedCompletion = convertTimeframeForDatabase(timeValue, timeUnit)
        }
        // TODO: REVERSE THE ARRAY BEFORE APPENDING... OR NOT?
      
        milestoneCard.querySelectorAll("action-item-card").forEach(actionItemCard => {
          const actionItemId = actionItemCard.dataset.actionItemId;

          const actionItemData = {
            name: "",
            description: "",
            estimatedTimeValue: null, 
            estimateTimeUnit: "", 
            isCompleted: false,
          }

          actionItemData.name = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-name`).value;
          actionItemData.description = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-description`).value;
          actionItemData.estimatedTimeValue = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-value`).value;
          actionItemData.estimateTimeUnit = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-unit`).value;


          milestoneData.actionItems.append(actionItemData)
          goalData.milestones.append(milestoneData)
          subcategoryGoalsData.goals.append(goalData)
        });
      });
    });
  });
  submitGoalData(subcategoryGoalsData);
  return
};

function sendToBackend(payload) {
  fetch("/api/save-goals", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to save goals");
      }
      return response.json();
    })
    .then((data) => {
      if(data.success) {
        alert("Goals saved successfully!");
        // window.location.href = data.redirect;
        } else {
          console.error("Save failed.  Try again.")
        }
    })
    .catch(error => {
      console.error("Error saving goals:", error);
      alert("There was an error saving your goals. Please try again.");
    });
}

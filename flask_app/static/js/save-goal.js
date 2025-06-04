import { convertTimeframeForDatabase } from "./timeframe-to-date.js";

document.addEventListener("DOMContentLoaded", () => {
  const saveButtons = document.querySelectorAll("button[type='submit']");

  saveButtons.forEach(button => {
    button.addEventListener("click", validateAndProcessGoalData);
    
  });
});

async function submitGoalData(data) {
  console.log("processing and sending goal data...")

  const categorySlug = data.categorySlug

  try {

    const response = await fetch(`/goals/${categorySlug}/save`, {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });

    if (response.ok) {
      alert('Goals saved successfully!');
      hideSaveShowNextButtons(categorySlug);
    } else {
      alert ('Failed to save goals.');
    }
  } catch (error) {
    alert('Error: ' + error.message)
  }
};

function hideSaveShowNextButtons(categorySlug) {
  const saveBtn = document.getElementById(`${categorySlug}-goals-save`);
  const nextBtn = document.getElementById('next-section-btn');

  if (saveBtn) {
    saveBtn.classList.add('d-none');
    nextBtn.classList.remove('d-none');
  }
}

function validateAndProcessGoalData(event) {
  const categoryCard = event.target.closest(".category-card");

  validateAllRequiredFields(categoryCard);
  processGoalData(categoryCard);
}


function processGoalData(categoryCard) {
  
  const categoryGoalsData = {
    categorySlug: "",
    goals: []
  }
  // Loop through all goal sections
  categoryCard.querySelectorAll(".goal-section").forEach(goalSection => {
    // Set categorySlug from goal-section
    const categorySlug = goalSection.dataset.categorySlug;
    categoryGoalsData.categorySlug = categorySlug;

    // Loop through each goal-card for a category
    goalSection.querySelectorAll(".goal-card").forEach(goalCard => {
      const goalData = {
        name: "",
        description: "", 
        goalType: "",
        priority: null,
        isActive: true,
        projectedCompletion: null,
        isComplete: false,
        milestones: []
      }
      
      const goalId = goalCard.dataset.goalId;
      goalData.name = goalCard.querySelector(`#${categorySlug}-goal-${goalId}-name`).value;
      const goalDescriptionElement = goalCard.querySelector(`#${categorySlug}-goal-${goalId}-description`)
      goalData.description = goalDescriptionElement ? goalDescriptionElement.value.trim() : "";
      goalData.goalType = goalCard.querySelector(`#${categorySlug}-goal-${goalId}-type`).value;
      goalData.priority = goalCard.querySelector(`#${categorySlug}-goal-${goalId}-priority`).value;
      // Defaulting isActive to True when saving a goal the first time, this may be subject to change depending on upcoming features
      goalData.isActive = true;
      goalData.projectedCompletion = goalCard.querySelector(`#${categorySlug}-goal-${goalId}-date`).value;

      // Select all milestones
      goalCard.querySelectorAll(".milestone-card").forEach(milestoneCard => {
        const milestoneId = milestoneCard.dataset.milestoneId
        const milestoneData = {
          name: "",
          description: "",
          projectedCompletion: null,
          isComplete: false,
          actionItems: []
        }
        // console.log(`Looking for: #${categorySlug}-goal-${goalId}-milestone-${milestoneId}-name`)
        milestoneData.name = milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-name`).value;
        // console.log("Selector: " + milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-name`))
        // milestoneData.name = milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-name`).value
        
        const milestoneDescriptionElement = milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-description`)
        milestoneData.description = milestoneDescriptionElement ? milestoneDescriptionElement.value.trim() : "";
        
        // timeValue and timeUnit conversion to projectedCompletion date
        if (milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-value`).value && milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-unit`).value) {
          const timeValue = milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-value`).value;
          const timeUnit = milestoneCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-unit`).value;
          milestoneData.projectedCompletion = convertTimeframeForDatabase(timeValue, timeUnit)
        }
        // TODO: REVERSE THE ARRAY BEFORE APPENDING... OR NOT?
        milestoneCard.querySelectorAll(".action-item-card").forEach((actionItemCard, index) => {
          const actionItemId = actionItemCard.dataset.actionItemId;

          const actionItemData = {
            name: "",
            description: "",
            actionItemOrder: null,
            estimatedTimeValue: null, 
            estimatedTimeUnit: "", 
            isComplete: false,
          }

          actionItemData.name = actionItemCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-name`).value;
          const actionItemDescriptionElement = actionItemCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-description`);
          actionItemData.description = actionItemDescriptionElement ? actionItemDescriptionElement.value : "";
          actionItemData.actionItemOrder = index + 1;
          const actionItemEstimatedTimeValue = actionItemCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-value`);
          actionItemData.estimatedTimeValue = actionItemEstimatedTimeValue ? parseInt(actionItemEstimatedTimeValue.value) : null;
          const actionItemEstimatedTimeUnit = actionItemCard.querySelector(`#${categorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-unit`);
          actionItemData.estimatedTimeUnit = actionItemEstimatedTimeUnit ? actionItemEstimatedTimeUnit.value : "";

          milestoneData.actionItems.push(actionItemData);
        });
        goalData.milestones.push(milestoneData);
      });
      console.log(goalData)
      categoryGoalsData.goals.push(goalData);
      console.log(categoryGoalsData.goals)
    });
    submitGoalData(categoryGoalsData);
  });
  return
};

function validateAllRequiredFields(categoryCard) {
  const requiredFields = categoryCard.querySelectorAll('input[required], select[required], textarea[required]');
  let allFieldsValid = true;

  requiredFields.forEach(field => {
    if (!field.value.trim()) {
      allFieldsValid = false;
      // Display error message or highlight the field
      field.classList.add('is-invalid');

    } else {
      field.classList.remove('is-invalid');
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

}

// function sendToBackend(payload) {
//   fetch("/api/save-goals", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(payload),
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("Failed to save goals");
//       }
//       return response.json();
//     })
//     .then((data) => {
//       if(data.success) {
//         alert("Goals saved successfully!");
//         // window.location.href = data.redirect;
//         } else {
//           console.error("Save failed.  Try again.")
//         }
//     })
//     .catch(error => {
//       console.error("Error saving goals:", error);
//       alert("There was an error saving your goals. Please try again.");
//     });
// }

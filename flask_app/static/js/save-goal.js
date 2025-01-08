import { convertTimeframeForDatabase } from "./timeframe-to-date";

document.addEventListener("DOMContentLoaded", () => {
  const saveButtons = document.querySelectorAll("button[type='submit']");

  saveButtons.forEach(button => {
    button.addEventListener("click", processAndSendGoalData);
  });
});

async function processAndSendGoalData(event) {
  const subcategorySection = event.closest(".subcategory-section")
  const subcategorySlug = subcategorySection.dataset.subcategorySlug
  const subcategoryGoalsData = processGoalData(subcategorySection)

  try {

    const response = await fetch(`/goals/${subcategorySlug}/save`, {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(subcategoryGoalsData)
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


function processGoalData(subcategorySection) {
  const subcategoryGoalsData = []
  // Loop through all goal sections
  subcategorySection.querySelectorAll(".goal-section").forEach(goalSection => {
    // Set subcategorySlug from goal-section
    const subcategorySlug = goalSection.dataset.subcategorySlug;

    // Loop through each goal-card for a subcategory
    goalSection.querySelectorAll(".goal-card").forEach(goalCard => {
      const goalData = {
        name: "",
        description: "", 
        goal_type: "",
        priority: "",
        projectedCompletion: null,
        isComplete: false,
        milestones: []
      }
      
      const goalId = goalCard.dataset.goalId;
      goalData.name = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-name`).value;
      goalData.description = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-description`).value;
      goalData.goal_type = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-goal-type`).value;
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

        milestoneData.name = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-name`).value
        milestoneData.description = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-description`).value
        
        // timeValue and timeUnit conversion to projectedCompletion date
        const timeValue = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-value`).value;
        const timeUnit = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-unit`).value;
        milestoneData.projectedCompletion = convertTimeframeForDatabase(timeValue, timeUnit)
        // TODO: REVERSE THE ARRAY BEFORE APPENDING... OR NOT?
      
        milestoneCard.querySelectorAll("action-item-card").forEach(actionItemCard => {
          const actionItemId = actionItemCard.dataset.actionItemId;

          const actionItemData = {
            name: "",
            description: "",
            estimated_time_value: null, 
            estimate_time_unit: "", 
            isCompleted: false,
          }

          actionItemData.name = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-name`).value;
          actionItemData.description = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-description`).value;
          actionItemData.estimated_time_value = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-value`).value;
          actionItemData.estimate_time_unit = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-unit`).value;


          milestoneData.actionItems.append(actionItemData)
          goalData.milestones.append(milestoneData)
          subcategoryGoalsData.append(goalData)
        });
      });
    });
  });
  return subcategoryGoalsData
};

function sendToBackend(payload) {
  fetch("/api/save-goals", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to save goals");
      }
      return response.json();
    })
    .then(data => {
      alert("Goals saved successfully!");
    })
    .catch(error => {
      console.error("Error saving goals:", error);
      alert("There was an error saving your goals. Please try again.");
    });
}

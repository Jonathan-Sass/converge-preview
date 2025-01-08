import { convertTimeframeForDatabase } from "./timeframe-to-date";

document.addEventListener("DOMContentLoaded", () => {
  const saveButtons = document.querySelectorAll("button[type='submit']");

  saveButtons.forEach(button => {
    button.addEventListener("click", processGoalData);
  });
});

function processGoalData() {
  const subcategoryGoalsData = []
  // Loop through all goal sections
  document.querySelectorAll(".goal-section").forEach(goalSection => {
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
      goal.name = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-name`).value;
      goal.description = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-description`).value;
      goal.goal_type = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-goal-type`)
      goal.priority = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-priority`).value;
      goal.projectedCompletion = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-date`).value;

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

        milestone.name = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-name`).value
        milestone.description = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-description`).value
        
        // timeValue and timeUnit conversion to projectedCompletion date
        const timeValue = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-value`).value
        const timeUnit = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-completion-unit`).value
        milestone.projectedCompletion = convertTimeframeForDatabase(timeValue, timeUnit)
        // TODO: REVERSE THE ARRAY BEFORE APPENDING... OR NOT?
      
        milestoneCard.querySelectorAll("action-item-card").forEach(actionItemCard => {
          const actionItemId = actionItemCard.dataset.actionItemId

          const actionItem = {
            name: "",
            description: "",
            estimated_time_value: null, 
            estimate_time_unit: "", 
            isCompleted: false,
          }

          actionItem.name = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-name`).value;
          actionItem.description = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-description`).value;
          actionItem.estimated_time_value = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-value`).value;
          actionItem.estimate_time_unit = actionItemCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemId}-estimated-time-unit`).value;


          milestoneData.actionItems.append(actionItem)
          goalData.milestones.append(milestone)
          subcategoryGoalsData.append(goal)
        });
      });
    });
  });
  return subcategoryGoalsData
};
  
const goalsData = Array.from(goalCards).map(goalCard => {


    const milestones = Array.from(goalCard.querySelectorAll(".milestone-card")).map(milestoneCard => {
      const milestoneId = milestoneCard.dataset.milestoneId;
      const completionValue = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-completion-value`).value;
      const completionUnit = milestoneCard.querySelector(`#${subcategorySlug}-goal-${goalId}-completion-unit`).value;
      const description = milestoneCard.querySelector(`#${subcategorySlug}-milestone-description-${milestoneId}`).value;

      return {
        milestoneId,
        completionValue,
        completionUnit,
        description,
      };
    });

    const actionItem = goalCard.querySelector(`#${subcategorySlug}-action-item-goal-${goalId}`).value;

    return {
      goalId,
      goalName,
      timeValue,
      timeUnit,
      milestones,
      actionItem,
    };
  });

  const payload = {
    subcategorySlug,
    goals: goalsData,
  };

  sendToBackend(payload);
}

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

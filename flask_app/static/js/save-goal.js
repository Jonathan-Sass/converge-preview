// save-goals.js

document.addEventListener("DOMContentLoaded", () => {
  const saveButtons = document.querySelectorAll("button[type='submit']");

  saveButtons.forEach(button => {
    button.addEventListener("click", processGoalData);
  });
});

function processGoalData() {
  // Loop through all goal sections
  document.querySelectorAll(".goal-section").forEach(goalSection => {
    // Set subcategorySlug from goal-section
    const subcategorySlug = goalSection.dataset.subcategorySlug;
    const subcategoryGoals = []

    // Loop through each goal-card for a subcategory
    goalSection.querySelectorAll(".goal-card").forEach(goalCard => {
      const goal = {
        name: "",
        description: "", 
        priority: "",
        date: "",
        projectedCompletion: null,
        isComplete: false,
        milestones: []
      }
      
      const goalId = goalCard.dataset.goalId;
      goal.name = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-name`).value;
      goal.description = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-description`).value;
      goal.priority = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-priority`).value;
      goal.projectedCompletion = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-date`).value;

      // Select all milestones
      goalCard.querySelectorAll(".milestone-card").forEach(milestoneCard => {
        const milestoneId = goalCard.dataset.milestoneId
        const milestone = {
          name: "",
          description: "",
          projectedCompletion: null,
          isComplete: false,
          actionItems: []
        }

        milestone.name = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-name`).value
        milestone.description = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-description`).value
        
        // Needs conversion to a date
        milestone.projectedCompletion = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-projected-completion`).value

        // TODO: REVERSE THE ARRAY BEFORE APPENDING... OR NOT?
      
        milestoneCard.querySelectorAll("action-item-card").forEach(actionItemCard => {
          const actionItem = {
            name: "",
            description: "",
            actionItemOrder: "",
            isCompleted: false,
            target_date: null, 
            estimatedTimeCommitment: ""
          }


          milestone.actionItems.append(actionItem)
          goal.milestones.append(milestone)
          subcategoryGoals.append(goal)
        });
      });
    });
  });


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

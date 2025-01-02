// save-goals.js

document.addEventListener("DOMContentLoaded", () => {
  const saveButtons = document.querySelectorAll("button[type='submit']");

  saveButtons.forEach(button => {
    button.addEventListener("click", handleSaveGoals);
  });
});

function handleSaveGoals(event) {
  event.preventDefault();

  const subcategorySlug = event.target.closest(".accordion-item").querySelector(".goal-section").id.split("goals-container-")[1];
  const goalCards = document.querySelectorAll(`#goals-container-${subcategorySlug} .goal-card`);

  const goalsData = Array.from(goalCards).map(goalCard => {
    const goalId = goalCard.dataset.goalId;

    const goalName = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-name`).value;
    const timeValue = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-time-interval-value`).value;
    const timeUnit = goalCard.querySelector(`#${subcategorySlug}-goal-${goalId}-time-interval-unit`).value;

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

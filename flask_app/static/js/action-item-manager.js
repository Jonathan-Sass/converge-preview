document.addEventListener("DOMContentLoaded", () => {
  initializeSeparateActionItemsListeners();
  initializeAddActionItemListeners();
  applyInitialActionItemVisibility();
});

export function initializeSeparateActionItemsListeners() {
  document.querySelectorAll(".separate-action-items-checkbox").forEach(checkbox => {
    checkbox.addEventListener("change", toggleActionItemSection)
  })
}

function applyInitialActionItemVisibility() {
  document.querySelectorAll(".separate-action-items-checkbox").forEach(checkbox => {
    toggleActionItemSection({ target: checkbox });
  });
}


function toggleActionItemSection(event) {
  const checkbox = event.target;
  const milestoneCard = checkbox.closest(".milestone-card")
  const actionItemSection = milestoneCard.querySelector(".action-item-section")
  
  if (checkbox.checked) {
      actionItemSection.classList.remove("d-none")
    } else {
      actionItemSection.classList.add("d-none")
    }
}

export function initializeAddActionItemListeners() {
  // Add event listener for adding action items
  document.querySelectorAll('.add-action-item-btn').forEach(button => {
    button.removeEventListener("click", handleAddActionItem)
    button.addEventListener("click", handleAddActionItem)
  })
}

export function initializeRemoveActionItemListeners() {
  // Add event listener for removing action items
  document.querySelectorAll('.remove-action-item-btn').forEach(button => {
    button.removeEventListener('click', handleRemoveActionItem)
    button.addEventListener('click', handleRemoveActionItem)
    });
  }



function handleAddActionItem() {
  const milestoneCard = this.closest(".milestone-card")
  const componentSlug = milestoneCard.dataset.componentSlug;
  const goalId = milestoneCard.dataset.goalId;
  console.log(milestoneCard)
  console.log("milestoneCard goalId for new action-item: ", goalId)
  const milestoneId = milestoneCard.dataset.milestoneId;
  const actionItemSection = this.closest('.action-item-section')
  const actionItemCount = actionItemSection.querySelectorAll(".action-item-card").length + 1;
  const actionItemCard = document.createElement("div");
  actionItemCard.classList.add("card", "shadow", "p-2", "mb-3", "action-item-card");
  actionItemCard.dataset.actionItemId = actionItemCount;

  actionItemCard.innerHTML = `
    <div class="card shadow p-1 m-auto mb-1">
      <div class="mb-3 form-floating">
        <input type="text" class="form-control action-item-name"
          id="${componentSlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemCount}-name"
          placeholder="Action Name"
          required>
        <label
          for="${componentSlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemCount}-name">Action
          Name</label>
      </div>
      <div class="invalid-feedback">Name is required.</div>
      <div class="mb-3 form-floating">
        <textarea class="form-control action-item-description"
          id="${componentSlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemCount}-description"
          placeholder="Description (optional)"></textarea>
        <label
          for="${componentSlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemCount}-description">Description
          (optional)</label>
      </div>
      
      <h6 class="card-title mb-2">Estimated time required:</h6>
      <div class="d-flex gap-2 mb-3 projected-completion-card">
        <input type="number" class="form-control" name="time_value"
          id="${componentSlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemCount}-estimated-time-value"
          placeholder="0" min="1">

        <select class="form-select" name="time_unit"
          id="${componentSlug}-goal-${goalId}-milestone-${milestoneId}-action-item-${actionItemCount}-estimated-time-unit"
          required>
          <option value=" " selected disabled hidden>Time Unit</option>
          <option value="day">Day(s)</option>
          <option value="week">Week(s)</option>
          <option value="month">Month(s)</option>
          <option value="year">Year(s)</option>
        </select>      
      </div>
      <button class="btn btn-danger btn-sm remove-action-item-btn w-50 mb-2 m-auto">
        Remove action item
      </button>
    </div>`;

  actionItemSection.insertBefore(actionItemCard, actionItemSection.querySelector(".add-action-item-btn"));

  initializeRemoveActionItemListeners();
}

function handleRemoveActionItem() {
  const actionItemCard = this.closest('.action-item-card')
  actionItemCard.remove();
}


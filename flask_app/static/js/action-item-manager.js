document.addEventListener("DOMContentLoaded", () => {
  initializeSeparateActionItemsListeners();
  initializeAddActionItemListeners();
});

export function initializeSeparateActionItemsListeners() {
  document.querySelectorAll(".separate-action-items-checkbox").forEach(checkbox => {
    checkbox.addEventListener("change", toggleActionItemSection)
  })
}

function toggleActionItemSection(event) {
  const checkbox = event.target;
  const milestoneCard = checkbox.closest(".milestone-card")
  const actionItemSection = milestoneCard.querySelector(".action-item-section")
  
  console.log("separate-action-items-checkbox clicked")
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
  const subcategorySlug = this.dataset.subcategorySlug;
  const goalId = this.dataset.goalId;
  const milestoneId = this.dataset.milestoneId;
  const actionItemSection = this.closest('.action-item-section')
  const actionItemCount = actionItemSection.querySelectorAll(".action-item-card").length + 1;
  const actionItemCard = document.createElement("div");
  actionItemCard.classList.add("action-item-card", "card", "p-3", "mb-3", "shadow", "text-bg-secondary");
  actionItemCard.dataset.actionItemId = actionItemCount;

  actionItemCard.innerHTML = `
    <div class="mb-3 form-floating">
      <input type="text" class="form-control action-item-name"
        id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-${actionItemCount}-name"
        placeholder="Action Name">
      <label for="${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-${actionItemCount}-name">Action Name</label>
    </div>
    <div class="mb-3 form-floating">
      <textarea class="form-control action-item-description"
        id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-${actionItemCount}-description"
        placeholder="Description (optional)"></textarea>
      <label for="${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-${actionItemCount}-description">Description (optional)</label>
    </div>
    <h6 class="card-title mb-2 projected-completion-card">Est. time required:</h6>
    <div class="d-flex gap-2 mb-3">
      <input type="number" class="form-control" name="time_value"
        id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-${actionItemCount}-completion-value"
        placeholder="0" min="1" required>
      <select class="form-select" name="time_unit"
        id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneId}-action-${actionItemCount}-completion-unit"
        required>
        <option value=" " selected disabled hidden>Unit</option>
        <option value="day">Day(s)</option>
        <option value="week">Week(s)</option>
        <option value="month">Month(s)</option>
        <option value="year">Year(s)</option>
      </select>
    </div>
    <button class="btn btn-danger btn-sm remove-action-item-btn w-50 m-auto">
      Remove action item
    </button>`;

  actionItemSection.insertBefore(actionItemCard, actionItemSection.querySelector(".add-action-item-btn"));

  initializeRemoveActionItemListeners();
}

function handleRemoveActionItem() {
  const actionItemCard = this.closest('.action-item-card')
  actionItemCard.remove();
}


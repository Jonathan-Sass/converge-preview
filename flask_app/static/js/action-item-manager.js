document.addEventListener("DOMContentLoaded", () => {
  initializeSeparateActionItemsListeners();
  // addFirstActionItem();
  initializeAddActionItemListeners();
  initializeRemoveActionItemListeners();
});

function initializeSeparateActionItemsListeners() {
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

function toggleEditActionItemsButton(milestoneCard, isChecked) {
  let editButton = milestoneCard.querySelector(".edit-action-items");
  const lastChild = milestoneCard.lastElementChild;
  const subcategorySlug = milestoneCard.dataset.subcategorySlug;
  const goalId = milestoneCard.dataset.goalId;
  const milestoneId = milestoneCard.dataset.milestoneId

  if (isChecked) {
    // If the button doesn't already exist, create it
    if (!editButton) {
      editButton = document.createElement("button");
      editButton.classList.add("btn", "btn-primary", "btn-sm", "edit-action-items", "mb-3");
      editButton.textContent = "Edit Action Items";
      editButton.setAttribute("type", "button");
      editButton.setAttribute("data-bs-toggle", "modal");
      editButton.setAttribute("data-bs-target", "#actionItemsModal");
      editButton.setAttribute("data-goal-id", goalId);
      editButton.setAttribute("data-milestone-id", milestoneId);
      editButton.setAttribute("data-subcategory-slug", subcategorySlug)

      milestoneCard.insertBefore(editButton, lastChild);
    }
  } else {
    // If unchecked, remove the button
    if (editButton) {
      editButton.remove();
    }
  }
}

function handleAddActionItem() {
  const subcategorySlug = this.dataset.subcategorySlug;
  const goalId = this.dataset.goalId;
  const milestoneId = this.dataset.milestoneId;
  const actionItemSection = this.closest('.action-item-section')
  const actionItemCount = actionItemSection.querySelectorAll(".action-item-card").length + 1;
  const actionItemCard = document.createElement("div");
  actionItemCard.classList.add("action-item-card", "card", "p-3", "mb-3", "shadow");
  actionItemCard.dataset.actionItemId = actionItemCount;

  actionItemCard.innerHTML = `
    <div class="mb-3 form-floating">
      <input type="text" class="form-control action-item-name"
        placeholder="Action Name">
      <label>Action Name</label>
    </div>
    <div class="mb-3 form-floating">
      <textarea class="form-control action-item-description"
        placeholder="Description (optional)"></textarea>
      <label>Description (optional)</label>
    </div>
    <div class="mb-3">
      <label>Target Date</label>
      <input type="date" class="form-control action-item-target-date">
    </div>
    <h6 class="card-title mb-2">Est. time required:</h6>
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


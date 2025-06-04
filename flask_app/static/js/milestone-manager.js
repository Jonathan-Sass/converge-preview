import { initializeRemoveActionItemListeners } from "./action-item-manager.js";
import { initializeAddActionItemListeners } from "./action-item-manager.js";
import { initializeSeparateActionItemsListeners } from "./action-item-manager.js";
import { updateCardOrder } from "./sortable-containers.js";

document.addEventListener("DOMContentLoaded", () => {
  initializeAddMilestoneListeners();
  initializeRemoveMilestoneListeners();
});
  
// Listen for clicks on the "Add Milestone" button
export function initializeAddMilestoneListeners() {
  document.querySelectorAll(".add-milestone-btn").forEach(button => {
    button.removeEventListener("click", handleAddMilestone); // Avoid duplicate listeners
    button.addEventListener("click", handleAddMilestone); // Attach the event listener
  });
}

export function initializeRemoveMilestoneListeners() {
  document.querySelectorAll(".remove-milestone-btn").forEach(button => {
    button.removeEventListener("click", handleRemoveMilestone)
    button.addEventListener("click", handleRemoveMilestone)

    })
  }

function handleAddMilestone() {
  const componentSlug = this.dataset.componentSlug; // Subcategory slug
  const goalId = this.dataset.goalId; // Goal ID
  console.log("goal-id from add-milestone-btn?: ", goalId)
  const containerId = `${componentSlug}-goal-${goalId}-milestones`; // Milestone container ID
  const milestonesContainer = document.getElementById(`${componentSlug}-goal-${goalId}-milestones`);
  const milestoneCount = milestonesContainer.querySelectorAll(".milestone-card").length + 1;
  
  if (!milestonesContainer) return; // Exit if container is not found

  // Build the milestone HTML
  const milestoneHtml = `
    <!-- Example Milestone Slide -->
    <div class="card shadow d-flex flex-column p-2 milestone-card position-relative sortable-card mb-2"
      id="${componentSlug}-goal-${goalId}-milestone-${milestoneCount}"
      data-component-slug="${componentSlug}" data-milestone-id="1"
      data-order="1" data-goal-id="${goalId}">
      <!-- Milestone order number -->
      <div class="card-title">
        <h5 class="fs-5 card-order text-primary">1</h5>
        <hr class="w-25 m-auto mb-2">
      </div>
      <!-- Milestone name input -->
      <div class="mb-3 form-floating">
        <input type="text" class="form-control"
          id="${componentSlug}-goal-${goalId}-milestone-${milestoneCount}-name" placeholder=" "
          required>
        <label for="${componentSlug}-goal-${goalId}-milestone-${milestoneCount}-name"
          class="form-label">
          Milestone Name
        </label>
        <div class="invalid-feedback">Milestone name is required.</div>
      </div>
      <h5 class="card-title mb-2">Target completion:</h5>
      <div class="d-flex gap-2 mb-3 projected-completion-card">
        <div class="mb-3 w-50">
          <input type="number" class="form-control" name="time_value"
            id="${componentSlug}-goal-${goalId}-milestone-${milestoneCount}-completion-value"
            placeholder="0" min="1" required>
          <div class="invalid-feedback">Value required</div>
        </div>
        <div class="mb-3 w-50">
          <select class="form-select" name="time_unit"
            id="${componentSlug}-goal-${goalId}-milestone-${milestoneCount}-completion-unit"
            required>
            <option value=" " selected disabled hidden>Time Unit</option>
            <option value="day">Day(s)</option>
            <option value="week">Week(s)</option>
            <option value="month">Month(s)</option>
            <option value="year">Year(s)</option>
          </select>
          <div class="invalid-feedback">Unit required</div>
        </div>
      </div>
      <div class="form-floating mb-3">
        <textarea class="form-control mb-2"
          name="${componentSlug}-milestone-${milestoneCount}-description"
          id="${componentSlug}-goal-${goalId}-milestone-${milestoneCount}-description" rows="3"
          placeholder=" ">
          </textarea>
        <label for="${componentSlug}-goal-${goalId}-milestone-${milestoneCount}-description"
          class="form-label">Description (optional)</label>
      </div>
      <!-- Separate Into Action Items Checkbox -->
      <div class="form-check form-switch mb-3">
        <input class="form-check-input toggle-panels separate-action-items-checkbox"
          type="checkbox"
          id="separate-action-items-${componentSlug}-goal-${goalId}-milestone-${milestoneCount}">
        <label class="form-check-label"
          for="separate-action-items-${componentSlug}-goal-${goalId}-milestone-${milestoneCount}">
          Separate into action items
        </label>
      </div>
      <button class="btn btn-danger btn-sm w-50 m-auto mb-3 remove-milestone-btn">
        Remove milestone
      </button>
      <!-- Action Items Section for Milestone -->
      <div
      class="card shadow p-1 d-none action-item-section position-absolute text-bg-light mt-1">
        <h5 class="text-primary fs-4">Action Items</h5>
        <hr class="w-25 m-auto mb-3">
        <button class="btn btn-primary btn-sm add-action-item-btn w-75 m-auto my-2">Add
          Action Item
        </button>
      </div>
    </div>
    `;
  
  // Append the new milestone to the container
  milestonesContainer.insertAdjacentHTML("afterbegin", milestoneHtml);

    // Update Swiper instance (if Swiper is in use)
  if (window.myswiper) {
    myswiper.update();
  }
  // Reinitialize event listeners for remove milestone and action-item buttons
  initializeRemoveMilestoneListeners();
  initializeAddActionItemListeners();
  initializeRemoveActionItemListeners();
  initializeSeparateActionItemsListeners();
  updateCardOrder(milestonesContainer);
};

function handleRemoveMilestone() {
  console.log("Remove milestone clicked");
  const milestoneCard = this.closest('.milestone-card');
  milestoneCard.remove();
}


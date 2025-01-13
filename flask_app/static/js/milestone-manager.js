import { initializeRemoveActionItemListeners } from "./action-item-manager.js";
import { initializeAddActionItemListeners } from "./action-item-manager.js";
import { initializeSeparateActionItemsListeners } from "./action-item-manager.js";

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
  const subcategorySlug = this.dataset.subcategorySlug; // Subcategory slug
  const goalId = this.dataset.goalId; // Goal ID
  const containerId = `${subcategorySlug}-goal-${goalId}-milestones`; // Milestone container ID
  const milestonesContainer = document.getElementById(`${subcategorySlug}-goal-${goalId}-milestones`);
  const milestoneCount = milestonesContainer.querySelectorAll(".milestone-card").length + 1;
  
  if (!milestonesContainer) return; // Exit if container is not found

  // Build the milestone HTML
  const milestoneHtml = `
    <div class="card shadow p-3 milestone-card position-relative sortable-card"
      id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}" data-subcategory-slug="${subcategorySlug}" data-milestone-id="${milestoneCount}" data-goal-id="${goalId}">
      
      <!-- Milestone order number -->
      <div class="card-title">
        <h5 class="card-order">{{ loop.index }}.</h5>
      </div>
      
      <!-- Milestone name input -->
      <div class="mb-3 form-floating">
        <input type="text" class="form-control"
          id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-name" placeholder=" "
          required>
        <label for="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-name"
          class="form-label">Milestone
          Name</label>
      </div>
      <h5 class="card-title mb-2">Target completion:</h5>
      <div class="d-flex gap-2 mb-3">
        <input type="number" class="form-control" name="time_value"
          id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-completion-value" placeholder="0"
          min="1" required>
        <select class="form-select" name="time_unit"
          id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-completion-unit" required>
          <option value=" " selected disabled hidden>Time Unit</option>
          <option value="day">Day(s)</option>
          <option value="week">Week(s)</option>
          <option value="month">Month(s)</option>
          <option value="year">Year(s)</option>
        </select>
      </div>
      <hr class="w-75 m-auto mb-3">
      <textarea class="form-control mb-2"
        name="${subcategorySlug}-goal-${goalId}-milestone_description[${milestoneCount}]"
        id="${subcategorySlug}-goal-${goalId}-milestone-description-${milestoneCount}" rows="3"
        placeholder="Description (optional)" required>
      </textarea>

      <!-- Separate Into Action Items Checkbox -->
      <div class="form-check form-switch mb-3">
        <input class="form-check-input separate-action-items-checkbox" type="checkbox"
          id="separate-action-items-${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}">
        <label class="form-check-label"
          for="separate-action-items-${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}">Separate
          into action items</label>
      </div>
      <!-- Action Items Section for Milestone -->
      <div class="card shadow d-none action-item-section position-absolute">
        <h5 class="text-primary fs-4">Action Items</h5>
        <!-- Example action item card -->
        <div class="card shadow p-3 mb-3 action-item-card text-bg-secondary">
          <div class="mb-3 form-floating">
            <input type="text" class="form-control action-item-name" id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-action-1-name"
              placeholder="Action Name">
            <label for="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-action-1-name">Action Name</label>
          </div>
          <div class="mb-3 form-floating">
            <textarea class="form-control action-item-description" id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-action-1-description"
              placeholder="Description (optional)"></textarea>
            <labelfor ="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-action-1-description">Description (optional)</label>
          </div>
          <h6 class="card-title mb-2">Est. time required:</h6>
          <div class="d-flex gap-2 mb-3">
            <input type="number" class="form-control" name="time_value"
              id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-action-1-completion-value"
              placeholder="0" min="1" required>
            <select class="form-select" name="time_unit"
              id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}-action-1-completion-unit"
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
          </button>
        </div>
        <button class="btn btn-primary btn-sm add-action-item-btn w-75 m-auto mb-3">Add
          Action Item
        </button>
        <hr class="w-25 m-auto mb-3">
      </div>
      <button class="btn btn-danger btn-sm w-50 m-auto remove-milestone-btn">Remove
        milestone</button>
    </div>`;
  
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
};

function handleRemoveMilestone() {
  console.log("Remove milestone clicked");
  const milestoneCard = this.closest('.milestone-card');
  milestoneCard.remove();
}


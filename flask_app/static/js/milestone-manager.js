import { initializeRemoveActionItemListeners } from "./action-item-manager.js";

document.addEventListener("DOMContentLoaded", () => {
  initializeAddMilestoneListeners();
  initializeRemoveMilestoneListeners();
});
  
// Listen for clicks on the "Add Milestone" button
export function initializeAddMilestoneListeners() {
  document.querySelectorAll(".add-milestone-btn").forEach(button => {
    button.removeEventListener("click", handleAddMilestone); // Avoid duplicate listeners
    button.addEventListener("click", handleAddMilestone); // Attach the event listener
    console.log("***Initializing add-milestone-btn Event Listeners***")
  });
}

export function initializeRemoveMilestoneListeners() {
  document.querySelectorAll(".remove-milestone-btn").forEach(button => {
    button.removeEventListener("click", handleRemoveMilestone)
    button.addEventListener("click", handleRemoveMilestone)

    })
  }

function handleAddMilestone(event) {
  const subcategorySlug = this.dataset.subcategorySlug; // Subcategory slug
  const goalId = this.dataset.goalId; // Goal ID
  const containerId = `${subcategorySlug}-goal-${goalId}-milestones`; // Milestone container ID
  console.log(containerId)
  const milestonesContainer = document.getElementById(`${subcategorySlug}-goal-${goalId}-milestones`);

  
  const milestoneCount = milestonesContainer.querySelectorAll(".milestone-card").length + 1;
  
  // const container = document.getElementById(containerId);

  console.log("***Running handleAddMilestone***")
  console.log("***Looking for: " + subcategorySlug + "-goal-" + goalId + "-milestones")
  if (!milestonesContainer) return; // Exit if container is not found
  console.log("***Adding Milestone!***")

  // Create a unique milestone ID
  // const milestoneCount = container.children.length + 1; // Increment based on existing milestones

  // Build the milestone HTML

  const milestoneHtml = `
    <div class="card shadow p-3 milestone-card"
      id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}" data-milestone-id="${milestoneCount}">
      <h5 class="card-title mb-2">Target completion:</h5>
      <div class="d-flex gap-2 mb-3">
        <input type="number" class="form-control" name="time_value"
          id="${subcategorySlug}-goal-${goalId}-completion-value" placeholder="0"
          min="1" required>
        <select class="form-select" name="time_unit"
          id="${subcategorySlug}-goal-${goalId}-completion-unit" required>
          <option value=" " selected disabled hidden>Time Unit</option>
          <option value="day">Day(s)</option>
          <option value="week">Week(s)</option>
          <option value="month">Month(s)</option>
          <option value="year">Year(s)</option>
        </select>
      </div>
      <hr class="w-75 m-auto mb-3">
      <textarea class="form-control mb-2"
        name="${subcategorySlug}-milestone_description[${milestoneCount}]"
        id="${subcategorySlug}-milestone-description-${milestoneCount}" rows="3"
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
      <button class="btn btn-danger btn-sm w-50 m-auto remove-milestone-btn">Remove
        milestone</button>
    </div>`;
  
  
  // <div class="milestone-card card p-3 shadow"
  // id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}" data-goal-id="${goalId}"
  // data-milestone-id="${milestoneCount}">
  //   <!-- <div class="card-title"> -->
  //   <h5 class="card-title mb-2">Target completion:</h5>
  //   <!-- </div> -->
  //   <div class="d-flex gap-2 mb-3">
  //     <input type="number" class="form-control" name="time_value"
  //       id="{{subcategory.subcategory_slug }}-goal-${goalId}-completion-value" placeholder="0"
  //       min="1" required>
  //     <select class="form-select" name="time_unit"
  //       id="{{subcategory.subcategory_slug }}-goal-${goalId}-completion-unit" required>
  //       <option value=" " selected disabled hidden>Time unit</option>
  //       <option value="day">Day(s)</option>
  //       <option value="week">Week(s)</option>
  //       <option value="month">Month(s)</option>
  //       <option value="year">Year(s)</option>
  //     </select>
  //   </div>
  //   <hr class="w-75 m-auto mb-2">
  //   <textarea class="form-control mt-2"
  //     name="${subcategorySlug}-milestone_description[1]"
  //     id="${subcategorySlug}-milestone-description-1" data-goal-id="${goalId}"
  //     data-milestone-id="${milestoneCount}" rows="3" placeholder="Description" required>
  //   </textarea>
  // </div>
  // `;
  // Append the new milestone to the container
  milestonesContainer.insertAdjacentHTML("afterbegin", milestoneHtml);

    // Update Swiper instance (if Swiper is in use)
  if (window.myswiper) {
    myswiper.update();
  }
  // Reinitialize event listeners for remove milestone and action-item buttons
  initializeRemoveMilestoneListeners();
  initializeRemoveActionItemListeners();
};

function handleRemoveMilestone(event) {
  console.log("Remove milestone clicked");
  const button = event.currentTarget
  const milestoneCard = button.closest('.milestone-card');
  milestoneCard.remove();
}


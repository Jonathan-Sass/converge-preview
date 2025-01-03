document.addEventListener("DOMContentLoaded", () => {
  initializeMilestoneListeners()

  document.querySelectorAll('.remove-milestone-btn').forEach(button => {
    button.addEventListener('click', event => {
      const clickedButton = event.currentTarget
      removeMilestone(clickedButton)
    })
  })
});
  
// Listen for clicks on the "Add Milestone" button
export function initializeMilestoneListeners() {
  document.querySelectorAll(".add-milestone-btn").forEach((button) => {
    button.removeEventListener("click", handleAddMilestone); // Avoid duplicate listeners
    button.addEventListener("click", handleAddMilestone); // Attach the event listener
    console.log("***Initializing add-milestone-btn Event Listeners***")
  });
}

function handleAddMilestone(event) {
  const subcategorySlug = this.dataset.subcategorySlug; // Subcategory slug
  const goalId = this.dataset.goalId; // Goal ID
  const containerId = `${subcategorySlug}-goal-${goalId}-milestones`; // Milestone container ID
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
  <div class="milestone-card card p-3 shadow"
  id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneCount}" data-goal-id="${goalId}"
  data-milestone-id="${milestoneCount}">
    <!-- <div class="card-title"> -->
    <h5 class="card-title mb-2">Target completion:</h5>
    <!-- </div> -->
    <div class="d-flex gap-2 mb-3">
      <input type="number" class="form-control" name="time_value"
        id="{{subcategory.subcategory_slug }}-goal-${goalId}-completion-value" placeholder="0"
        min="1" required>
      <select class="form-select" name="time_unit"
        id="{{subcategory.subcategory_slug }}-goal-${goalId}-completion-unit" required>
        <option value=" " selected disabled hidden>Time unit</option>
        <option value="day">Day(s)</option>
        <option value="week">Week(s)</option>
        <option value="month">Month(s)</option>
        <option value="year">Year(s)</option>
      </select>
    </div>
    <hr class="w-75 m-auto mb-2">
    <textarea class="form-control mt-2"
      name="${subcategorySlug}-milestone_description[1]"
      id="${subcategorySlug}-milestone-description-1" data-goal-id="${goalId}"
      data-milestone-id="1" rows="3" placeholder="Description" required>
    </textarea>
  </div>
  `;
  // Append the new milestone to the container
  milestonesContainer.insertAdjacentHTML("afterbegin", milestoneHtml);

    // Update Swiper instance (if Swiper is in use)
  if (window.myswiper) {
    myswiper.update();
  }
};

function removeMilestone(button) {
  console.log("Remove milestone clicked");
  const milestoneCard = button.closest('.milestone-card');
  milestoneCard.remove();
}


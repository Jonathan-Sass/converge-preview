import { initializeAddMilestoneListeners } from './milestone-manager.js'
import { initializeRemoveMilestoneListeners } from './milestone-manager.js';
import { initializeRemoveActionItemListeners } from './action-item-manager.js';

document.addEventListener("DOMContentLoaded", function () {
  
  // Select and create event listeners for all add-goal buttons
  document.querySelectorAll(".add-goal-btn").forEach (button => {
    button.addEventListener("click", event => {
      const clickedButton = event.currentTarget
      addGoal(clickedButton)
    })
  })
});

function addGoal(button) {
  // Retrieve the category or subcategory from data attributes
  const subcategorySlug = button.dataset.subcategorySlug;

  // Increment a counter for the specific category or subcategory
  const goalsContainer = document.getElementById(`${subcategorySlug}-goals-container`);
  const goalCount = goalsContainer.querySelectorAll(".goal-card").length + 1;
  
  const goalCard = document.createElement("div")
  goalCard.classList.add("card", "shadow", "p-3", "mb-3", "goal-card");
  goalCard.dataset.goalId = goalCount;
  
  // Template for a new goal card
  goalCard.innerHTML = `
    <!-- Goal Name Input -->
    <div class="mb-3 form-floating">
      <input type="text" class="form-control" id="${subcategorySlug}-goal-${goalCount}-name"
        placeholder=" " required>
      <label for="${subcategorySlug}-goal-${goalCount}-name" class="form-label">Goal
        Name</label>
    </div>

    <!-- Goal Description Input -->
    <div class="mb-3 form-floating">
      <textarea class="form-control" id="${subcategorySlug}-goal-${goalCount}-description"
        rows="3" placeholder=" " required></textarea>
      <label for="${subcategorySlug}-goal-${goalCount}-description"
        class="form-label">Description</label>
    </div>

    <!-- Priority Selector -->
    <div class="mb-3">
      <label for="${subcategorySlug}-goal-${goalCount}-priority"
        class="form-label">Priority</label>
      <select class="form-select" id="${subcategorySlug}-goal-${goalCount}-priority" required>
        <option value="" disabled selected>Select priority</option>
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
        <option value="urgent">Urgent</option>
      </select>
    </div>

    <!-- Estimated Goal Completion Input -->
    <div class="mb-3 text-center">
      <p>Estimated Completion</p>
      <div class="d-flex justify-content-around gap-3 align-items-center m-auto">
        <!-- Input for Time Value -->
        <div class="col-4">
          <label for="${subcategorySlug}-goal-${goalCount}-time-value"
            class="form-label">Select a time from now</label>
          <div class="d-flex gap-2 align-items-center">
            <input type="number" class="form-control w-auto"
              id="${subcategorySlug}-goal-${goalCount}-time-value" placeholder="Enter number"
              min="1">
            <select class="form-select w-auto"
              id="${subcategorySlug}-goal-${goalCount}-time-unit">
              <option value="" disabled selected>Time unit</option>
              <option value="day">Day(s)</option>
              <option value="week">Week(s)</option>
              <option value="month">Month(s)</option>
              <option value="year">Year(s)</option>
            </select>
          </div>
        </div>
        <div class="col-1">
          <p>OR</p>
        </div>
        <div class="col-4">
          <label for="${subcategorySlug}-goal-${goalCount}-date" class="form-label">Select a
            date</label>
          <input type="date" class="form-control"
            id="${subcategorySlug}-goal-${goalCount}-date">
        </div>
      </div>
    </div>

    <h4 class="text-center text-primary">Let's break it down.</h4>
    <hr class="mb-3">

    <!-- Goal Milestones -->
    <h3 class="display-6">Major Milestones</h3>
    <p class="lead">Hint: Start with the longest time interval to work your way backwards.</p>
    <div class="container-fluid mb-3">
      <!-- Add Milestone Button -->
      <div class="mb-3">
        <button type="button" id="add-milestone" class="btn btn-primary add-milestone-btn"
          data-subcategory-slug="${subcategorySlug}" data-goal-id="${goalCount}">
          Add Milestone
        </button>
      </div>
      <!-- Swiper Container for Milestones -->
      <div class="swiper-container scroll-wrapper position-relative">
        <!-- Swiper Wrapper -->
        <div class="swiper-wrapper d-flex gap-2 align-items-center">

          <!-- Dynamically Added Milestones -->
          <div class="d-flex swiper-slide gap-2 milestone-section"
            id="${subcategorySlug}-goal-${goalCount}-milestones">

            <!-- Example Milestone Slide -->
            <div class="card shadow p-3 milestone-card "
              id="${subcategorySlug}-goal-${goalCount}-milestone-1" data-milestone-id="1">
              <h5 class="card-title mb-2">Target completion:</h5>
              <div class="d-flex gap-2 mb-3">
                <input type="number" class="form-control" name="time_value"
                  id="${subcategorySlug}-goal-${goalCount}-completion-value" placeholder="0"
                  min="1" required>
                <select class="form-select" name="time_unit"
                  id="${subcategorySlug}-goal-${goalCount}-completion-unit" required>
                  <option value=" " selected disabled hidden>Time Unit</option>
                  <option value="day">Day(s)</option>
                  <option value="week">Week(s)</option>
                  <option value="month">Month(s)</option>
                  <option value="year">Year(s)</option>
                </select>
              </div>
              <hr class="w-75 m-auto mb-3">
              <textarea class="form-control mb-2"
                name="${subcategorySlug}-milestone_description[1]"
                id="${subcategorySlug}-milestone-description-1" rows="3"
                placeholder="Description (optional)" required>
              </textarea>

              <!-- Separate Into Action Items Checkbox -->
              <div class="form-check form-switch mb-3">
                <input class="form-check-input separate-action-items-checkbox" type="checkbox"
                  id="separate-action-items-${subcategorySlug}-goal-${goalCount}-milestone-1">
                <label class="form-check-label"
                  for="separate-action-items-${subcategorySlug}-goal-${goalCount}-milestone-1">Separate
                  into action items</label>
              </div>
              <button class="btn btn-danger btn-sm w-50 m-auto remove-milestone-btn">Remove
                milestone</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    `;
  
// Append the new goal card to the goals container
const addGoalBtn = document.getElementById(`${subcategorySlug}-add-goal-btn`)
goalsContainer.insertBefore(goalCard, addGoalBtn);

// Reinitialize milestone and action item listeners to include new goal's milestones and action-items
initializeAddMilestoneListeners();
initializeRemoveMilestoneListeners();
initializeRemoveActionItemListeners();
}

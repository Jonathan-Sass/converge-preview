import { initializeAddMilestoneListeners } from './milestone-manager.js'
import { initializeRemoveMilestoneListeners } from './milestone-manager.js';
import { initializeRemoveActionItemListeners } from './action-item-manager.js';
import { initializeSeparateActionItemsListeners } from './action-item-manager.js';
import { initializeCompletionTimeEventListeners} from './timeframe-to-date.js';

document.addEventListener("DOMContentLoaded", function () {
  initializeAddGoalListener();
  initializeRemoveGoalListener();
});

function initializeAddGoalListener() {
  document.querySelectorAll(".add-goal-btn").forEach (button => {
    button.addEventListener("click", addGoal)
  })
}

function initializeRemoveGoalListener() {
  document.querySelectorAll(".remove-goal-btn").forEach( button => {
    button.removeEventListener("click", handleRemoveGoal)
    button.addEventListener("click", handleRemoveGoal)
  })
}

function addGoal() {
  // Retrieve the category or subcategory from data attributes
  const subcategorySlug = this.dataset.subcategorySlug;

  // Increment a counter for the specific category or subcategory
  const goalsContainer = document.getElementById(`${subcategorySlug}-goals-container`);
  const goalCount = goalsContainer.querySelectorAll(".goal-card").length + 1;
  
  const goalCard = document.createElement("div")
  goalCard.classList.add("card", "shadow", "p-3", "mb-3", "goal-card");
  goalCard.dataset.goalId = goalCount;
  goalCard.id = `${subcategorySlug}-goal-${goalCount}-card`;
  
  // Template for a new goal card
  goalCard.innerHTML = `
      <!-- Goal Name Input -->
      <div class="mb-3 form-floating">
        <input type="text" class="form-control" id="${subcategorySlug}-goal-${goalCount}-name"
          placeholder=" " name="name" required>
        <label for="${subcategorySlug}-goal-${goalCount}-name" class="form-label">Goal
          Name</label>
        <div class="invalid-feedback">Name is required.</div>
      </div>

      <!-- Goal Description Input -->
      <div class="mb-3 form-floating">
        <textarea class="form-control" id="${subcategorySlug}-goal-${goalCount}-description"
          rows="3" placeholder=" "></textarea>
        <label for="${subcategorySlug}-goal-${goalCount}-description"
          class="form-label">Description (optional)</label>
      </div>

      <!-- Goal Type Input -->
      <div class="mb-3">
        <label for="${subcategorySlug}-goal-${goalCount}-type" class="form-label">Goal
          Type</label>
        <select class="form-select" id="${subcategorySlug}-goal-${goalCount}-type" required>
          <option value="" disabled selected>Select a Type of Goal</option>
          <option value="active">
            Active (goals you intend to pursue currently)
          </option>
          <option value="supportive">
            Supportive (goals that directly support or enable other goals)
          </option>
          <option value="collaborative">
            Collaborative (goals requiring contributions or coordination with others)
          </option>
          <option value="habitual">
            Habitual (goals that involve building or maintaining habits or routine practices)
          </option>
          <option value="experimental">
            Experimental (goals being explored without full commitment, to gauge interest or
            feasability)
          </option>
          <option value="self-care">
            Self-Care (goals focusing on personal well-being, mental health, or stress management)
          </option>
          <option value="archived">
            Archived (goals to be pursued later, possibly those that follow other goals or steps in
            life)
          </option>
        </select>
        <div class="invalid-feedback">Please select a goal type.</div>
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
        <div class="invalid-feedback">Please assign a priority.</div>
      </div>

      <!-- Estimated Goal Completion Input -->
      <div class="mb-3 text-center">
        <p>Projected Completion</p>
        <div
          class="d-flex justify-content-around gap-3 align-items-center m-auto projected-completion-card">
          <!-- Input for Time Value -->
          <div class="col-4">
            <label for="${subcategorySlug}-goal-${goalCount}-time-value" class="form-label">
              Select a time from now
            </label>
            <div class="d-flex gap-2 align-items-center">
              <input type="number" class="form-control w-auto"
                id="${subcategorySlug}-goal-${goalCount}-time-value" placeholder="Enter number"
                min="1" data-type="projected-completion-value">
              <select class="form-select w-auto"
                id="${subcategorySlug}-goal-${goalCount}-time-unit"
                data-type="projected-completion-unit">
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
            <label for="${subcategorySlug}-goal-${goalCount}-date" class="form-label">
              Select a date
            </label>
            <input type="date" class="form-control"
              id="${subcategorySlug}-goal-${goalCount}-date"
              data-type="projected-completion-date" required>
            <div class="invalid-feedback">Please enter a projected completion date.</div>
          </div>
        </div>
      </div>

      <h4 class="text-center text-primary">Break it down!</h4>
      <hr class="mb-3">

      <!-- Goal Milestones -->
      <h3 class="display-6">Major Milestones</h3>
      <p class="lead">Hint: Start with the longest time interval to work your way backwards.</p>
      <div class="container-fluid mb-3">
        <!-- Add Milestone Button -->
        <div class="mb-3">
          <button type="button" id="add-milestone" class="btn btn-primary add-milestone-btn"
            data-subcategory-slug="${subcategorySlug}" data-goal-id="${goalCount}>
            Add Milestone
          </button>
        </div>

        <!-- Swiper Container for Milestones, (Swiper functionality in question, may opt for sortable horizonal-scroll) -->
        <div class="swiper-container scroll-wrapper position-relative">
          <div class="card shadow p-3 swiper-wrapper">
            <div class="swiper-slide">
              <!-- Dynamically Added Milestones go here -->
              <div class="d-flex gap-2 milestone-section p-2 sortable-container"
                id="${subcategorySlug}-goal-${goalCount}-milestones">
                <!-- Example Milestone Slide -->
                <div
                  class="card shadow p-2 d-flex flex-wrap milestone-card position-relative sortable-card"
                  id="${subcategorySlug}-goal-${goalCount}-milestone-1"
                  data-subcategory-slug="${subcategorySlug}" data-milestone-id="1"
                  data-order="1" data-goal-id="1">
                  <!-- Milestone order number -->
                  <div class="card-title">
                    <h5 class="card-order">1.</h5>
                  </div>
                  <!-- Milestone name input -->
                  <div class="mb-3 form-floating">
                    <input type="text" class="form-control"
                      id="${subcategorySlug}-goal-${goalCount}-milestone-1-name" placeholder=" "
                      required>
                    <label for="${subcategorySlug}-goal-${goalCount}-milestone-1-name"
                      class="form-label">
                      Milestone Name
                    </label>
                    <div class="invalid-feedback">Milestone name is required.</div>
                  </div>
                  <h5 class="card-title mb-2">Target completion:</h5>
                  <div class="d-flex gap-2 mb-3 projected-completion-card">
                    <div class="mb-3 w-50">
                      <input type="number" class="form-control" name="time_value"
                        id="${subcategorySlug}-goal-${goalCount}-milestone-1-completion-value"
                        placeholder="0" min="1" required>
                      <div class="invalid-feedback">Value required</div>
                    </div>
                    <div class="mb-3 w-50">
                      <select class="form-select" name="time_unit"
                        id="${subcategorySlug}-goal-${goalCount}-milestone-1-completion-unit"
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
                  <hr class="w-75 m-auto mb-3">
                  <div class="form-floating mb-3">
                    <textarea class="form-control mb-2"
                      name="${subcategorySlug}-milestone[1]_description"
                      id="${subcategorySlug}-goal-${goalCount}-milestone-1-description" rows="3"
                      placeholder=" ">
                      </textarea>
                    <label for="${subcategorySlug}-goal-${goalCount}-milestone-1-description"
                      class="form-label">Description (optional)</label>
                  </div>
                  <!-- Separate Into Action Items Checkbox -->
                  <div class="form-check form-switch mb-3">
                    <input class="form-check-input toggle-panels separate-action-items-checkbox"
                      type="checkbox"
                      id="separate-action-items-${subcategorySlug}-goal-${goalCount}-milestone-1">
                    <label class="form-check-label"
                      for="separate-action-items-${subcategorySlug}-goal-${goalCount}-milestone-1">
                      Separate into action items
                    </label>
                  </div>
                  <!-- Action Items Section for Milestone -->
                  <div class=" border rounded p-1 shadow d-none action-item-section position-absolute text-bg-secondary">
                    <h5 class="text-primary fs-4">Action Items</h5>
                    <hr class="w-25 m-auto mb-3">
                    <button class="btn btn-primary btn-sm add-action-item-btn w-75 m-auto mb-3">Add
                      Action Item
                    </button>
                  </div>
                  <button class="btn btn-danger btn-sm w-50 m-auto remove-milestone-btn">
                    Remove milestone
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button class="btn btn-danger btn-sm w-50 m-auto mb-3 remove-goal-btn">Remove
        Goal</button>
    `;
  
// Append the new goal card to the goals container
const addGoalBtn = document.getElementById(`${subcategorySlug}-add-goal-btn`)
goalsContainer.insertBefore(goalCard, addGoalBtn);

// Reinitialize milestone and action item listeners to include new goal's milestones and action-items
initializeAddMilestoneListeners();
initializeRemoveMilestoneListeners();
initializeRemoveActionItemListeners();
initializeRemoveGoalListener();
initializeSeparateActionItemsListeners();
initializeCompletionTimeEventListeners();
}

function handleRemoveGoal() {
  const goalCard = this.closest(".goal-card");
  goalCard.remove();
}

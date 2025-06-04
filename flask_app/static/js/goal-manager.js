import { initializeAddMilestoneListeners } from './milestone-manager.js'
import { initializeRemoveMilestoneListeners } from './milestone-manager.js';
import { initializeCompletionTimeEventListeners} from './timeframe-to-date.js';
import { 
  initializeAddActionItemListeners, 
  initializeRemoveActionItemListeners, 
  initializeSeparateActionItemsListeners
  } from './action-item-manager.js';

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
  const categoryComponentSlug = this.dataset.componentSlug;

  // Increment a counter for the specific category or subcategory
  const goalsContainer = document.getElementById(`${categoryComponentSlug}-goals-container`);
  const goalCount = goalsContainer.querySelectorAll(".goal-card").length + 1;
  
  const goalCard = document.createElement("div")
  goalCard.classList.add("card", "shadow", "p-3", "mb-3", "goal-card");
  goalCard.dataset.goalId = goalCount;
  goalCard.id = `${categoryComponentSlug}-goal-${goalCount}-card`;
  
  // Template for a new goal card
  goalCard.innerHTML = `
    <!-- Accordion container for a goal -->
    <div class="accordion-item goal-card p-3" id="${categoryComponentSlug}-container"
    data-component-slug="${categoryComponentSlug}">
      <h2 class="accordion-header d-flex justify-content-between align-items-center" id="heading-${goalCount}">
        <button class="accordion-button collapsed w-100 text-start goal-accordion-btn" type="button"
          data-bs-toggle="collapse"
          data-bs-target="#collapse-${goalCount}"
          aria-expanded="false"
          aria-controls="collapse-${goalCount}">
          {{ goal.name or "Goal " ~ goal_index }}
          <span class="badge bg-secondary ms-3">
            {{ goal.category_component.name }}
          </span>
        </button>
      </h2>

      <!-- Container for an example goal -->
      <div id="collapse-${goalCount}" class="accordion-collapse collapse"
        aria-labelledby="heading-${goalCount}"
        data-bs-parent="#category-accordion-{{ category_archetype.slug }}">

        <div class="accordion-body p-2 mb-3 solid-white-bg goal-card" id="${categoryComponentSlug}-goal-${goalCount}-card" data-goal-id="${goalCount}">
        
          <div class="card shadow p-3 mb-3 solid-white-bg">
            <h4 class="display-6 text-primary text-center">Goal Details</h4>
            <hr class="w-100 mb-3">
            <div class="mb-3 form-floating">
              <input type="text" class="form-control goal-name" id="${categoryComponentSlug}-goal-${goalCount}-name"
                value="{{ goal.name }}" name="name" autocomplete="on" required>
              <label for="${categoryComponentSlug}-goal-${goalCount}-name" class="form-label">Goal
                Name</label>
              <div class="invalid-feedback">Name is required.</div>
            </div>
            <!-- Goal Description Input -->
            <div class="mb-3 form-floating">
              <textarea class="form-control" id="${categoryComponentSlug}-goal-${goalCount}-description"
                rows="3">{{ goal.description }}</textarea>
              <label for="${categoryComponentSlug}-goal-${goalCount}-description"
                class="form-label">Description (optional)</label>
            </div>
            <!-- Goal Type Input -->
            <div class="mb-3">
              <label for="${categoryComponentSlug}-goal-${goalCount}-type" class="form-label">Goal
                Type</label>
              {% set types = {
                'active': 'Active (goals you intend to pursue currently)',
                'supportive': 'Supportive (goals that directly support or enable other goals)',
                'collaborative': 'Collaborative (goals requiring contributions or coordination with others)',
                'habitual': 'Habitual (goals that involve building or maintaining habits or routine practices)',
                'experimental': 'Experimental (goals being explored without full commitment, to gauge interest or feasibility)',
                'self-care': 'Self-Care (goals focusing on personal well-being, mental health, or stress management)',
                'archived': 'Archived (goals to be pursued later, possibly those that follow other goals or steps in life)'
              } %}
              <select class="form-select" id="${categoryComponentSlug}-goal-${goalCount}-type" required>
                <option value="" disabled {% if not goal.goal_type %}selected{% endif %}>Select a Type of Goal</option>
                {% for type, label in types.items() %}
                  <option value="{{ type }}" {% if goal.goal_type == type %}selected{% endif %}>{{ label }}</option>
                {% endfor %}
              </select>
              <div class="invalid-feedback">Please select a goal type.</div>
            </div>
            <!-- Priority Selector -->
            <div class="mb-3">
              <label for="${categoryComponentSlug}-goal-${goalCount}-priority"
                class="form-label">Priority</label>
              {% set priorities = {
                '4': 'Low',
                '3': 'Medium',
                '2': 'High',
                '1': 'Urgent'
              } %}
              <select class="form-select" id="${categoryComponentSlug}-goal-${goalCount}-priority" required>
                <option value="" disabled {% if not goal.priority %}selected{% endif %}>Select Priority</option>
                {% for priority, label in priorities.items() %}
                  <option value="{{ priority }}" {% if goal.priority == priority %}selected{% endif %}>{{ label }}</option>
                {% endfor %}
              </select>
              <div class="invalid-feedback">Please assign a priority.</div>
            </div>
            <!-- Display as an active goal -->
            <!-- <div class="form-check form-switch mb-3">
              <input class="form-check-input toggle-panels goal-is-active-checkbox" type="checkbox"
                id="${categoryComponentSlug}-goal-${goalCount}-is-active">
              <label class="form-check-label" for="${categoryComponentSlug}-goal-${goalCount}-is-active">
                Display goal and associated milestones/action items on dashboard?
              </label>
            </div> -->
          </div>
          <div class="card shadow p-3 mb-3">
            <!-- Estimated Goal Completion Input -->
            <div class="mb-3 text-center">
              <h4 class="display-6 text-primary">Projected Completion</h4>
              <hr class="w-100 mb-3">
              <div
                class="d-flex justify-content-around gap-3 align-items-center m-auto projected-completion-card">
                <!-- Input for Time Value -->
                <div class="col-4">
                  <label for="${categoryComponentSlug}-goal-${goalCount}-time-value" class="form-label">
                    Select a time from now
                  </label>
                  <div class="d-flex gap-2 align-items-center">
                    <input type="number" class="form-control w-auto"
                      id="${categoryComponentSlug}-goal-${goalCount}-time-value" placeholder="Enter number"
                      min="1" data-type="projected-completion-value" value="{{ goal.estimated_time_value }}">
                    {% set units = {
                      'day': 'Day(s)',
                      'week': 'Week(s)',
                      'month': 'Month(s)',
                      'year': 'Year(s)'
                    } %}
                    <select class="form-select" id="${categoryComponentSlug}-goal-${goalCount}-time-unit" required>
                      <option value="" disabled {% if not goal.estimated_time_unit %}selected{% endif %}>Time Unit</option>
                      {% for unit, label in units.items() %}
                        <option value="{{ unit }}" {% if goal.estimated_time_unit == unit %}selected{% endif %}>{{ label }}</option>
                      {% endfor %}
                    </select>
                  </div>
                </div>
                <div class="col-1">
                  <p>OR</p>
                </div>
                <div class="col-4">
                  <!-- TODO: REVISIT JS FOR AUTOPOPULATE -->
                  <label for="${categoryComponentSlug}-goal-${goalCount}-date" class="form-label">
                    Select a date
                  </label>
                  <input type="date" class="form-control"
                    id="${categoryComponentSlug}-goal-${goalCount}-date"
                    data-type="projected-completion-date" required>
                  <div class="invalid-feedback">Please enter a projected completion date.</div>
                </div>
              </div>
            </div>
          </div>
          <div class="card shadow p-3 mb-3 opaque-white-bg">
            <!-- Goal Milestones -->
            <div class="text-center">
              <h4 class="display-6 text-primary">Milestones</h4>
              <hr class="m-auto my-3 w-100">
              <h4 class="">Let's break it down!</h4>
              <ol>
                <li class="lead">Fill out the card you see with the final goal, the last thing that happens when you're done with all of it.</li>
                <li class="lead"></li>
              </ol>
              <p class="lead">Hint: Milestones add to the left (in front of one another).</p>
        
            </div>
            <div class="container-fluid mb-3 text-center">
              <!-- Add Milestone Button -->
              <div class="mb-3">
                <button type="button" id="add-milestone" class="btn btn-primary add-milestone-btn"
                  data-component-slug="${categoryComponentSlug}" data-goal-id="${goalCount}">
                  Add Milestone
                </button>
              </div>
        
              <!-- Swiper Container for Milestones, (Swiper functionality in question, may opt for sortable horizonal-scroll) -->
              <div class="swiper-container scroll-wrapper position-relative">
                <div class="card shadow swiper-wrapper m-auto">
                  <div class="swiper-slide">
                    <!-- Dynamically Added Milestones go here -->
                    <div
                      class="d-flex justify-content-left m-auto mb-2 gap-2 p-3 milestone-section sortable-container bg-secondary-subtle"
                      id="${categoryComponentSlug}-goal-${goalCount}-milestones">        
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <button
              class="btn btn-danger btn-lg m-auto my-3 remove-goal-btn">
              Remove Goal
            </button>
          </div>
          <div class="text-center mb-3">
            <button type="submit" class="btn btn-primary btn-lg"
              id="${categoryComponentSlug}-goals-save">Save Goal
            </button>
            <a href="/home" class="btn btn-lg btn-primary d-none" id="next-section-btn">Next Section</a>
          </div>
        </div>
      </div>
    </div>


    <!-- 

            </div>
          </div>
        </div>
    </div> -->
    `;
  
// Append the new goal card to the goals container
const addGoalBtn = document.getElementById(`${categoryComponentSlug}-add-goal-btn`)
goalsContainer.insertBefore(goalCard, addGoalBtn);

// Reinitialize milestone and action item listeners to include new goal's milestones and action-items
initializeAddMilestoneListeners();
initializeRemoveMilestoneListeners();
initializeAddActionItemListeners();
initializeRemoveActionItemListeners();
initializeRemoveGoalListener();
initializeSeparateActionItemsListeners();
initializeCompletionTimeEventListeners();
}

function handleRemoveGoal() {
  const goalCard = this.closest(".goal-card");
  goalCard.remove();
}

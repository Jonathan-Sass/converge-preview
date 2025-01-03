import { initializeMilestoneListeners } from './milestone-manager.js'

document.addEventListener("DOMContentLoaded", function () {
  // Select all add-goal buttons
  const addGoalButtons = document.querySelectorAll(".add-goal-button");

  // Loop through each button and add a click event listener
  addGoalButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Retrieve the category or subcategory from data attributes
      const subcategorySlug = this.dataset.subcategorySlug;
      const subcategoryId = this.dataset.subcategoryId;

      console.log(subcategorySlug)
      console.log(subcategoryId)

      // Increment a counter for the specific category or subcategory
      const goalsContainer = document.getElementById(`goals-container-${subcategorySlug}`);
      const goalCount = goalsContainer.querySelectorAll(".goal-card").length + 1;
      // console.log("***Looking for: " + subcategorySlug + "-goal-" + goalCount + "-milestones ")
      // const milestonesContainer = document.getElementById(`${subcategorySlug}-goal-${goalCount}-milestones`);
      // const milestoneCount = milestonesContainer.querySelectorAll(".milestone-card").length + 1;

      console.log("****goalCount: " + goalCount + "****")
    // Template for a new goal card
      const newGoalHTML = `
      <div class="card shadow p-3 mb-3 goal-card" id="${subcategorySlug}-goal-${goalCount}-card"
                        data-goal-id="${goalCount}" data-subcategory-slug="${subcategorySlug}">

                        <!-- Goal Name Input -->
                        <div class=" mb-3 form-floating">
                          <input type="text" class="form-control" id="${subcategorySlug}-goal-${goalCount}-name"
                            placeholder=" " required>
                          <label for="${subcategorySlug}-goal-${goalCount}-name" class="form-label">Goal
                            Name</label>
                        </div>

                        <!-- Estimated Goal Completion Input -->
                        <div class="mb-3 text-start">
                          <p>Estimated Completion:</p>
                          <div class="d-flex gap-2 align-items-center">
                            <!-- Input for Time Value -->
                            <input type="number" class="form-control w-auto" name="time_value"
                              id="{{ subcategory.subcategory_slug }}-goal-${goalCount}-time-interval-value"
                              placeholder="Enter number" min="1" required>
                            <!-- Dropdown for Time Unit -->
                            <select class="form-select w-auto" name="time_unit"
                              id="{{ subcategory.subcategory_slug }}-goal-${goalCount}-time-interval-unit" required>
                              <option value="" disabled selected>Time unit</option>
                              <option value="day">Day(s)</option>
                              <option value="week">Week(s)</option>
                              <option value="month">Month(s)</option>
                              <option value="year">Year(s)</option>
                            </select>
                          </div>
                        </div>

                        <h4 class="text-center text-primary">Let's break it down.</h4>
                        <hr class="mb-3">

                        <!-- Goal Milestones Container -->
                        <h3 class="display-6">Major Milestones</h3>
                        <p class="lead">Hint: Start with the longest time interval to work your way backwards.</p>
                        <div class="container-fluid mb-3">
                          <!-- Add Milestone Button -->
                          <div class="mb-3">
                            <button type="button" id="add-milestone" class="btn btn-outline-primary add-milestone-btn"
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
                                <div class="milestone-card card p-3 shadow"
                                  id="${subcategorySlug}-goal-${goalCount}-milestone-1" data-goal-id="${goalCount}"
                                  data-milestone-id="last">
                                  <!-- <div class="card-title"> -->
                                  <h5 class="card-title mb-2">Target completion:</h5>
                                  <!-- </div> -->
                                  <div class="d-flex gap-2 mb-3">
                                    <input type="number" class="form-control" name="time_value"
                                      id="{{subcategory.subcategory_slug }}-goal-${goalCount}-completion-value" placeholder="0"
                                      min="1" required>
                                    <!-- <label for="{{subcategory.subcategory_slug }}-goal-${goalCount}-completion-value"
                                      class="form-label">Enter Number</label> -->
                                    <select class="form-select" name="time_unit"
                                      id="{{subcategory.subcategory_slug }}-goal-${goalCount}-completion-unit" required>
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
                                    id="${subcategorySlug}-milestone-description-1" data-goal-id="${goalCount}"
                                    data-milestone-id="1" rows="3" placeholder="Description" required>
                                  </textarea>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <p class="lead text-start">Enter an action you can take immediately to progress toward this
                          goal.
                        </p>
                        <div class="form-floating mb-3">
                          <input type="text" class="form-control" name="action_item"
                            id="${subcategorySlug}-action-item-goal-${goalCount}" value="{{ action_item }}"
                            placeholder=" ">
                          <label for="action_item" class="form-label">Current action item</label>
                        </div>
                      </div>`;

    // Append the new goal card to the goals container
    goalsContainer.insertAdjacentHTML("beforeend", newGoalHTML);

    // Reinitialize milestone listeners to include the new goal's add-milestone-btn
    initializeMilestoneListeners();
    });
  });
});

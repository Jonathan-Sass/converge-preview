import { initializeMilestoneListeners } from './add-milestone.js'

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
    const newGoalHTMLDeprecated = `
      <div class="card shadow p-3 mb-3" id="goal-card-${goalCount}">
        <div class="mb-3 form-floating">
          <input type="text" class="form-control" id="goal${goalCount}" placeholder=" " required>
          <label for="goal${goalCount}" class="form-label">Goal Name</label>
        </div>
        <div class="mb-3 text-start">
          <label for="time-interval-${goalCount}" class="form-label">Estimated Completion:</label>
          <div class="d-flex gap-2 align-items-center">
            <input type="number" class="form-control w-25" name="time_value" id="time-interval-value-${goalCount}"
              placeholder="Enter number" min="1" required>
            <select class="form-select w-25" name="time_unit" id="time-interval-unit-${goalCount}" required>
              <option value="" disabled selected>Select unit</option>
              <option value="day">Day(s)</option>
              <option value="week">Week(s)</option>
              <option value="month">Month(s)</option>
              <option value="year">Year(s)</option>
            </select>
          </div>
        </div>
        <h4 class="text-center text-primary">Let's break it down.</h4>
        <hr class="mb-3">
        <h3 class="display-6">Milestones</h3>
        <div class="container-fluid mb-3">
          <div class="mb-3">
            <button type="button" id="add-milestone-${goalCount}" class="btn btn-outline-primary add-milestone-btn"
              data-goal-id="${goalCount}">
              Add Milestone
            </button>
          </div>
          <div class="swiper-container scroll-wrapper position-relative">
            <div class="swiper-wrapper d-flex gap-2 align-items-center" id="goal-${goalCount}-milestones">
              <!-- Milestone content will be dynamically added here -->
              <!-- Example Milestone Slide -->
              <div class="milestone-card card p-3 shadow"
                id="${subcategorySlug}-milestone-last" data-milestone-id="last">
                <div class="card-title">
                  <h5 class="time-interval-title">Target completion:</h5>
                </div>
                <div class="d-flex gap-2 mb-3">
                  <input type="number" class="form-control w-25" name="time_value"
                    id="time-interval-value" placeholder="0" min="1" required>
                  <select class="form-select w-75" name="time_unit" id="time-interval-unit" required>
                    <option value="" disabled selected>Timeframe</option>
                    <option value="day">Day(s)</option>
                    <option value="week">Week(s)</option>
                    <option value="month">Month(s)</option>
                    <option value="year">Year(s)</option>
                  </select>
                </div>
                <hr class="w-75 m-auto mb-2">
                <textarea class="form-control mt-2"
                  name="${subcategorySlug}-milestone_description[1]"
                  id="${subcategorySlug}-milestone-description-1" rows="3"
                  placeholder="Description" required></textarea>
              </div>
            </div>
          </div>
        </div>
        <p class="lead text-start">Enter an action you can take immediately to progress toward this goal.</p>
        <div class="form-floating mb-3">
          <input type="text" class="form-control" name="action_item"
            id="action-item-${goalCount}" placeholder=" ">
          <label for="action-item-${goalCount}" class="form-label">Current action item</label>
        </div>
      </div>`;

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
                            <input type="number" class="form-control w-25" name="time_value"
                              id="${subcategorySlug}-goal-${goalCount}-time-interval-value"
                              placeholder="Enter number" min="1" required>
                            <!-- Dropdown for Time Unit -->
                            <select class="form-select w-25" name="time_unit"
                              id="${subcategorySlug}-goal-${goalCount}-time-interval-unit" required>
                              <option value="" disabled selected>Select unit</option>
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
                                  id="${subcategorySlug}-goal-${goalCount}-milestone-last" data-goal-id="${goalCount}"
                                  data-milestone-id="last">
                                  <!-- <div class="card-title"> -->
                                  <h5 class="card-title mb-2">Target completion:</h5>
                                  <!-- </div> -->
                                  <div class="d-flex gap-2 mb-3">
                                    <div class="form-floating w-50">
                                      <input type="number" class="form-control" name="time_value"
                                        id="${subcategorySlug}-goal-${goalCount}-completion-value" placeholder="0"
                                        min="1" required>
                                      <label for="${subcategorySlug}-goal-${goalCount}-completion-value"
                                        class="form-label">Enter Number</label>
                                    </div>
                                    <div class="form-floating w-50">
                                      <select class="form-select" name="time_unit"
                                        id="${subcategorySlug}-goal-${goalCount}-completion-unit" required>
                                        <option value="day">Day(s)</option>
                                        <option value="week">Week(s)</option>
                                        <option value="month">Month(s)</option>
                                        <option value="year">Year(s)</option>
                                      </select>
                                      <label
                                        for="${subcategorySlug}-goal-${goalCount}-completion-unit">Timeframe</label>
                                    </div>
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

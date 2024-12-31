document.addEventListener("DOMContentLoaded", function () {
  // Select all add-goal buttons
  const addGoalButtons = document.querySelectorAll(".add-goal-button");

  // Loop through each button and add a click event listener
  addGoalButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Retrieve the category or subcategory from data attributes
      const categorySlug = this.dataset.subcategorySlug;
      const subcategoryId = this.dataset.subcategoryId;

      console.log(categorySlug)
      console.log(subcategoryId)

      // Increment a counter for the specific category or subcategory
      const goalsContainer = document.getElementById(`goals-container-${categorySlug}`);
      const goalCount = goalsContainer.querySelectorAll(".goal-section").length + 1;

    // Template for a new goal card
    const newGoalHTML = `
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
                id="{{ subcategory.subcategory_slug }}-milestone-last" data-milestone-id="last">
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
                  name="{{ subcategory.subcategory_slug }}-milestone_description[1]"
                  id="{{ subcategory.subcategory_slug }}-milestone-description-1" rows="3"
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

    // Append the new goal card to the goals container
    goalsContainer.insertAdjacentHTML("beforeend", newGoalHTML);
    });
  });
});

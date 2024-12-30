document.addEventListener("DOMContentLoaded", () => {
  // Listen for clicks on the "Add Milestone" button
  document.querySelectorAll(".add-milestone-btn").forEach((button) => {
      button.addEventListener("click", function () {
          const subcategorySlug = this.dataset.subcategory; // Subcategory slug
          const goalId = this.dataset.goalId; // Goal ID
          const containerId = `${subcategorySlug}-goal-${goalId}-milestones`; // Milestone container ID
          const container = document.getElementById(containerId);

          if (!container) return; // Exit if container is not found

          // Create a unique milestone ID
          const milestoneIndex = container.children.length + 1; // Increment based on existing milestones

          // Build the milestone HTML
          const milestoneHtml = `
              <div class="swiper-slide milestone-card card p-3 border shadow" 
                   id="${subcategorySlug}-goal-${goalId}-milestone-${milestoneIndex}" 
                   data-milestone-id="${milestoneIndex}">
                  <div class="card-title">
                      <h5 class="time-interval-title">Target completion:</h5>
                  </div>
                  <div class="d-flex gap-2 mb-3">
                      <input type="number" class="form-control w-50" name="time_value" 
                             id="time-interval-value-${milestoneIndex}" 
                             placeholder="Enter number" min="1" required>
                      <select class="form-select w-50" name="time_unit" id="time-interval-unit-${milestoneIndex}" required>
                          <option value="" disabled selected>Select unit</option>
                          <option value="day">Day(s)</option>
                          <option value="week">Week(s)</option>
                          <option value="month">Month(s)</option>
                          <option value="year">Year(s)</option>
                      </select>
                  </div>
                  <hr class="w-75 m-auto mb-3">
                  <textarea class="form-control mt-2" name="${subcategorySlug}-milestone-description-${milestoneIndex}" 
                            id="${subcategorySlug}-milestone-description-${milestoneIndex}" 
                            rows="3" placeholder="Description" required></textarea>
              </div>
          `;

          // Append the new milestone to the container
          container.insertAdjacentHTML("beforeend", milestoneHtml);
      });
  });
});

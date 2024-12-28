// Select all "Add Another Goal" buttons and attach event listeners
document.querySelectorAll('.add-goal').forEach(button => {
    button.addEventListener('click', function () {
        const goalId = this.getAttribute('data-goal-id'); // Get the goal's unique ID
        const container = document.getElementById(`additional-goals-${goalId}`); // Locate the container for extra goals
        const newGoal = `
            <div class="goal-section">
                <div class="mb-3">
                    <label for="goal1" class="form-label">Goal Name</label>
                    <input type="text" class="form-control" id="goal1"
                        placeholder="Enter your goal">
                </div>
                <div class="mb-3">
                    <label for="time-interval-{{ subcategory.id }}"
                        class="form-label">Estimated Completion:</label>
                    <select class="form-select" name="timeframe" id="timeframe">
                        <option value="" selected>Select a timeframe</option>
                        <option value="1_month">1 Month</option>
                        <option value="2_month">2 Months</option>
                        <option value="3_month">3 Months</option>
                        <option value="6_month">6 Months</option>
                        <option value="9_month">9 Months</option>
                        <option value="1_year">1 Year</option>
                        <option value="2_year">2 Years</option>
                        <option value="3_year">3 Years</option>
                        <option value="5_year">5 Years</option>
                        <option value="10_year">10 Years</option>
                        <option value="15_year">15 Years</option>
                        <option value="20_year">20 Years</option>
                        <option value="30_year">30 Years</option>
                    </select>
                </div>
            </div>`;
        container.insertAdjacentHTML('beforeend', newGoal); // Append the new goal form
    });
});

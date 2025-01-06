document.addEventListener("DOMContentLoaded", () => {
  initializeCompletionTimeEventListeners();
});

export function initializeCompletionTimeEventListeners() {
  document.querySelectorAll('[data-type="timeframe-value"]').forEach(input => {
    input.addEventListener("input", processTimeframeToDateConversion)
  })

  document.querySelectorAll('[data-type="timeframe-unit"]').forEach(input => {
    input.addEventListener("input", processTimeframeToDateConversion)
  })
}


function processTimeframeToDateConversion(event) {
  const projectedCompletionCard = event.target.closest(".projected-completion-card")

  const valueInput = projectedCompletionCard.querySelector('[data-type="projected-completion-value]')
  const valueUnit = projectedCompletionCard.querySelector('[data-type="projected-completion-unit"]')
  const completionDateInput = projectedCompletionCard.querySelector('[data-type="projected-completion-date"]')

  const value = valueInput.value;
  const unit = unitInput.value;

  if (value && unit) {
    const currentDate = new Date();
    let projectedDate;
  }
}

  function updateCompletionDate() {
    const timeValue = parseInt(timeValueInput.value, 10);
    const timeUnit = timeUnitSelect.value;

    if (timeValue > 0 && timeUnit) {
      const now = new Date();
      switch (timeUnit) {
        case "day":
          now.setDate(now.getDate() + timeValue);
          break;
        case "week":
          now.setDate(now.getDate() + timeValue * 7);
          break;
        case "month":
          now.setMonth(now.getMonth() + timeValue);
          break;
        case "year":
          now.setFullYear(now.getFullYear() + timeValue);
          break;
      }
      completionDateInput.value = now.toISOString().split("T")[0]; // Format as YYYY-MM-DD
    }
  }

  function clearTimeFromNow() {
    if (completionDateInput.value) {
      timeValueInput.value = "";
      timeUnitSelect.value = "";
    }
  }

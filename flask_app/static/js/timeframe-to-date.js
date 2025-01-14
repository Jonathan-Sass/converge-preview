document.addEventListener("DOMContentLoaded", () => {
  initializeCompletionTimeEventListeners();
});

export function initializeCompletionTimeEventListeners() {
  document.querySelectorAll('[data-type="projected-completion-value"]').forEach(input => {
    input.addEventListener("input", convertTimeframeToCompletionDate);
  })

  document.querySelectorAll('[data-type="projected-completion-unit"]').forEach(input => {
    input.addEventListener("change", convertTimeframeToCompletionDate);
  })
}

function convertTimeframeToCompletionDate(event) {
  const projectedCompletionCard = event.target.closest(".projected-completion-card")
  if (!projectedCompletionCard) return;

  const valueInput = projectedCompletionCard.querySelector('[data-type="projected-completion-value"]')
  const unitInput = projectedCompletionCard.querySelector('[data-type="projected-completion-unit"]')
  const completionDateInput = projectedCompletionCard.querySelector('[data-type="projected-completion-date"]')

  if (!valueInput || !unitInput || !completionDateInput) return;

  const timeValue = parseInt(valueInput.value, 10);
  const timeUnit = unitInput.value;

  if (timeValue > 0 && timeUnit) {
   
    const projectedDate = processTimeframeToDate(timeValue, timeUnit)

    completionDateInput.value = projectedDate.toISOString().split("T")[0]; // Format as YYYY-MM-DD
  } else {
    completionDateInput.value = "";
  }
}

export function convertTimeframeForDatabase(timeValue, timeUnit) {
  const projectedDateTime = processTimeframeToDate (timeValue, timeUnit)
  const projectedDate = projectedDateTime.toISOString().split("T")[0];
  return projectedDate;
}

function processTimeframeToDate (timeValue, timeUnit) {
  const currentDate = new Date();
    let projectedDate = new Date();

    if (timeValue > 0 && timeUnit) {
    switch (timeUnit) {
      case "day": 
        projectedDate.setDate(currentDate.getDate() + timeValue);
        break;
      case "week": 
        projectedDate.setDate(currentDate.getDate() + timeValue * 7);
        break;
      case "month":
        projectedDate.setMonth(currentDate.getMonth() + timeValue);
        break;
      case "year": 
        projectedDate.setFullYear(currentDate.getFullYear() + timeValue);
        break;
      default:
        return;
    }
    return projectedDate
  }
}

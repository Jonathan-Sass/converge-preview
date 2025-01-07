document.addEventListener("DOMContentLoaded", () => {
  initializeCompletionTimeEventListeners();
});

export function initializeCompletionTimeEventListeners() {
  document.querySelectorAll('[data-type="projected-completion-value"]').forEach(input => {
    input.addEventListener("input", processTimeframeToDateConversion);
  })

  document.querySelectorAll('[data-type="projected-completion-unit"]').forEach(input => {
    input.addEventListener("change", processTimeframeToDateConversion);
  })
}


function processTimeframeToDateConversion(event) {
  console.log("Triggered processTimeframeToDateConversion");

  
  const projectedCompletionCard = event.target.closest(".projected-completion-card")
  if (!projectedCompletionCard) return;

  const valueInput = projectedCompletionCard.querySelector('[data-type="projected-completion-value"]')
  const unitInput = projectedCompletionCard.querySelector('[data-type="projected-completion-unit"]')
  const completionDateInput = projectedCompletionCard.querySelector('[data-type="projected-completion-date"]')

  if (!valueInput || !unitInput || !completionDateInput) return;

  const timeValue = parseInt(valueInput.value, 10);
  const timeUnit = unitInput.value;

  if (timeValue > 0 && timeUnit) {
    const currentDate = new Date();
    let projectedDate = new Date();

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
    console.log(projectedDate)

    completionDateInput.value = projectedDate.toISOString().split("T")[0]; // Format as YYYY-MM-DD
  } else {
    completionDateInput.value = "";
  }
}

  // function clearTimeFromNow() {
  //   if (completionDateInput.value) {
  //     timeValueInput.value = "";
  //     timeUnitSelect.value = "";
  //   }
  // }

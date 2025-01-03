document.addEventListener("DOMContentLoaded", () => {
  const timeValueInput = document.getElementById("time-value");
  const timeUnitSelect = document.getElementById("time-unit");
  const completionDateInput = document.getElementById("completion-date");

  timeValueInput.addEventListener("input", updateCompletionDate);
  timeUnitSelect.addEventListener("change", updateCompletionDate);
  completionDateInput.addEventListener("input", clearTimeFromNow);

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
});

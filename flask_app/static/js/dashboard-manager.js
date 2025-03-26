document.addEventListener('DOMContentLoaded', () => {

  const flexButtons = document.querySelectorAll('[data-action="add-to-flex"]')

  console.log("Found flex buttons:", flexButtons.length);

  flexButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const goalId = button.getAttribute('data-goal-id');
      const parentElement = `goal-${goalId}`

      addToFlexTasks({goalId, parentElement});
    })
  })

  function addToFlexTasks({goalId, parentElement}) {
    removeRenderedGoal(parentElement)

    if (goalId) {
      saveGoalToFlexTasks(goalId)
    } else {
      console.warn(`There was a problem adding the goal: ${goalId}`)
    }

  };

  function removeRenderedGoal(parentElement) {
    const element = document.getElementById(parentElement)

    if (element) {
      element.classList.add('fade-out');
      setTimeout(() => element.remove(), 300);
    };
  };

  async function saveGoalToFlexTasks(goalId) {
    try {
      const response = await fetch(`/flex-tasks/add-goal/${goalId}`, {
        method: 'POST', 
      });

      if (response.ok) {
        alert(`Goal: ${goalId} added to Flex Tasks`)
      } else {
        alert (`Failed to add Goal: ${goalId}`)
      }
    } catch (error) {
      alert ('Error: ' + error.message)
    }
    
    return
  };

  // CLOSING for DOMContentLoaded
});

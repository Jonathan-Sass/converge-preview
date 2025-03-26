document.addEventListener('DOMContentLoaded', () => {

  const flexButtons = document.querySelectorAll('[data-action="add-to-flex"]')

  flexButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const goalId = button.getAttribute('data-goal-id');
      const parentElementId = `goal-${goalId}`

      addToFlexTasks({goalId, parentElementId});
    })
  })

  function addToFlexTasks({goalId, parentElementId}) {
    if (goalId) {
      saveGoalToFlexTasks(goalId, parentElementId)
    } else {
      console.warn(`There was a problem adding the goal: ${goalId}`)
    }

  };
  
  function moveGoalToFlexTasks(parentElementId) {
    const parentElement = document.getElementById(parentElementId)
    const flexTaskElement = document.getElementById('flex-task-list')

    if (parentElement && flexTaskElement) {
      parentElement.classList.add('fade-out');
      setTimeout(() => flexTaskElement.appendChild(parentElement), 300);
      
    };
  };

  async function saveGoalToFlexTasks(goalId, parentElementId) {
    try {
      const response = await fetch(`/flex-tasks/add-goal/${goalId}`, {
        method: 'POST', 
      });

      if (response.ok) {
        moveGoalToFlexTasks(parentElementId)
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

document.addEventListener('DOMContentLoaded', () => {

  const addFlexButtons = document.querySelectorAll('[data-action="add-to-flex"]');
  const removeFlexButtons = document.querySelectorAll('[data-action="remove-flex"]');

  addFlexButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const goalId = button.getAttribute('data-goal-id');
      const parentElementId = `goal-${goalId}`;

      addToFlexTasks({goalId, parentElementId});
    });
  });

  removeFlexButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const goalId = button.getAttribute('data-goal-id');
      const parentElementId = `goal-${goalId}`;

      deleteGoalFromFlexTasks({goalId, parentElementId})
    })
  });

  function addToFlexTasks({goalId, parentElementId}) {
    if (goalId) {
      saveGoalToFlexTasks(goalId, parentElementId);
    } else {
      console.warn(`There was a problem adding the goal: ${goalId}`);
    };

  };
  
  function moveGoalToFlexTasks(parentElementId) {
    const parentElement = document.getElementById(parentElementId);
    const flexTaskElement = document.getElementById('flex-task-list');

    if (parentElement && flexTaskElement) {
      parentElement.classList.add('fade-out');
      setTimeout(() => flexTaskElement.appendChild(parentElement), 300);
      
    };
  };
  
  function removeFlexTask(parentElementId) {
    const parentElement = document.getElementById(parentElementId)

    if (parentElement) {
      parentElement.classList.add('fade-out');
      setTimeout(() => parentElement.remove(), 300);
    }
  };

  async function saveGoalToFlexTasks(goalId, parentElementId) {
    try {
      const response = await fetch('/flex-tasks', {
        method: 'POST', 
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({goal_id: goalId})
      });

      if (response.ok) {
        moveGoalToFlexTasks(parentElementId);
        alert(`Goal: ${goalId} added to Flex Tasks`);
      } else {
        alert (`Failed to add Goal: ${goalId}`);
      }
    } catch (error) {
      alert ('Error: ' + error.message);
    }
    
    return
  };

  async function deleteGoalFromFlexTasks({goalId, parentElementId}) {
    try {
      const response = await fetch (`/flex-tasks/${goalId}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        removeFlexTask(parentElementId)
        console.log("Goal removed from flex tasks");
      } else {
        throw new Error("Failed to remove goal");
      }

    } catch (error) {
      console.error("Error removing goal:", error);
    }
  };

  // CLOSING for DOMContentLoaded
});

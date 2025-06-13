document.addEventListener('DOMContentLoaded', () => {
  findAndInitializeAddToFlexButtons()
  findAndInitializeRemoveFromFlexButtons()

  function findAndInitializeAddToFlexButtons () {
    const addToFlexButtons = document.querySelectorAll('[data-action="add-to-flex"]');

    addToFlexButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        const goalId = button.getAttribute('data-goal-id');
        const parentElementId = `goal-${goalId}`;
  
        addToFlexTasks({goalId, parentElementId});
      });
    });
  };

  function findAndInitializeRemoveFromFlexButtons () {
    const removeFromFlexButtons = document.querySelectorAll('[data-action="remove-flex"]');

    removeFromFlexButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        const goalId = button.getAttribute('data-goal-id');
        const parentElementId = `goal-${goalId}`;
  
        deleteGoalFromFlexTasks({goalId, parentElementId})
      })
    });
  }




  function addToFlexTasks({goalId, parentElementId}) {
    if (goalId) {
      saveGoalToFlexTasks(goalId, parentElementId);
    } else {
      console.warn(`There was a problem adding the goal: ${goalId}`);
    };

  };
  
  function moveGoalToFlexTasks(goalId, parentElementId) {
    const parentElement = document.getElementById(parentElementId);
    const elementAddToFlexButton = parentElement.querySelector('[data-action="add-to-flex"]')
    const actionableItemHeader = parentElement.querySelector('.actionable-item-header')
    const flexTaskListElement = document.getElementById('flex-task-list');

    if (!actionableItemHeader) {
      console.error(`Could not find .flex-task-header`);
      return;
    }

    const removeFlexTaskButton = `<button class="btn btn-sm btn-outline-primary"
                                    data-action="remove-flex"
                                    data-goal-id="${goalId}">
                                      Remove
                                  </button>`

    if (parentElement && flexTaskListElement) {
      // parentElement.classList.add('fade-out');
      setTimeout(() => flexTaskListElement.appendChild(parentElement), 300);
      actionableItemHeader.insertAdjacentHTML('beforeend', removeFlexTaskButton)
      elementAddToFlexButton.remove()
      findAndInitializeRemoveFromFlexButtons()
    };
  };
  
  function removeFlexTask(parentElementId) {
    const flexTaskElement = document.getElementById(parentElementId)
    
    if (flexTaskElement) {
      flexTaskElement.classList.add('fade-out');
      setTimeout(() => flexTaskElement.remove(), 300);
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
        moveGoalToFlexTasks(goalId, parentElementId);
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

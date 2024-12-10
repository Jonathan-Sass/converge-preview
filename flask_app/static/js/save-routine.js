const collectRoutineData = () => {
    // personalroutine
        // name, routine_type, start_time, end_time, is_active, notes,
        // practices = {practice_id, duration_id, position}

        let personalRoutine = {
            name: document.getElementById('routine-name').innerText,
            description: document.getElementById('routine-description').innerText,
            start_time: document.getElementById('routine-start-time').innerText,
            is_active: true,
            notes: null, 
            practices: []
        };

    const cards = document.querySelectorAll('.practice-card');
    const selectedDuration = document.querySelector('.duration option:checked');

    const practices = Array.from(cards).map((card) => ({
      id: card.dataset.practiceId,
      name: card.querySelector('.practice-name').innerText,
      durationId: selectedDuration.value,
    }));
  
    return {
      userId: currentUserId,
      routineType: 'morning',
      practices,
    };
  };
  
  const saveRoutine = () => {
    const routineData = collectRoutineData();
    fetch('/routines/builder/am/initial/save', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(routineData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Routine saved successfully:', data);
      })
      .catch((error) => {
        console.error('Error saving routine:', error);
      });
  };
  
  document.getElementById('save-button').addEventListener('click', saveRoutine);
  
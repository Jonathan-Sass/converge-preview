import { updateCardOrder } from "./sortable-containers.js";

// // Function to update the data-order attributes
// function updateCardOrder() {
//   const cards = document.querySelectorAll('.practice-card');
//   cards.forEach((card, index) => {
//     card.dataset.order = index + 1; // Update data-order with new position
//   });
//   console.log('Card order updated:', [...cards].map(card => card.dataset.order));
// }

// Function to collect and prepare routine data
const collectRoutineData = () => {
  const startTimeElement = document.getElementById('routine-start-time')
  const startTime = startTimeElement.value === '' ? null : startTimeElement.value;

  let personalRoutineData = {
    name: document.getElementById('routine-name').innerText,
    description: document.getElementById('routine-description').innerText,
    routineType: document.getElementById('practice-container').dataset.routineType,
    startTime: startTime,
    isActive: true,
    notes: null,
    practices: [],
  };
  console.log()
  console.log("PersonalRoutineData")
  console.log(personalRoutineData)

  const cards = document.querySelectorAll('.practice-card');
  const selectedDuration = document.querySelector('.duration option:checked');

  const practices = Array.from(cards).map((card) => ({
    personalRoutineId: null,
    practiceId: card.dataset.practiceId,
    durationId: selectedDuration ? selectedDuration.value : null,
    position: card.dataset.order, // Use the updated data-order
  }));

  personalRoutineData.practices = practices;

  return personalRoutineData;
};

// Function to save the routine
const saveRoutine = () => {
  const routineData = collectRoutineData();

  fetch('/routines/am/builder/initial/save', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(routineData),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to save routine');
      }
      return response.json(); // Parse JSON response
    })    
    .then((data) => {
      if(data.success) {
        console.log('Routine saved successfully:', data);
        window.location.href = data.redirect; 
    } else {
        console.error('Save failed. Redirecting to login...');
        // window.location.href = '/login'; // Redirect to login
      }
    })
    .catch((error) => {
      console.error('Error saving routine:', error);
    });
};

// Event listener for saving the routine
document.getElementById('save-button').addEventListener('click', saveRoutine);

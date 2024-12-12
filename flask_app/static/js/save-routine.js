
// Function to collect and prepare routine data
const collectRoutineData = () => {
  let personalRoutineData = {
    user_id: sessionStorage.getItem('user_id'), // Ensure this is populated server-side
    name: document.getElementById('routine-name').innerText,
    description: document.getElementById('routine-description').innerText,
    routine_type: document.getElementById('practice-container').dataset.routineType,
    start_time: document.getElementById('routine-start-time').innerText,
    is_active: true,
    notes: null,
    practices: [],
  };

  const cards = document.querySelectorAll('.practice-card');
  const selectedDuration = document.querySelector('.duration option:checked');

  const practices = Array.from(cards).map((card) => ({
    personal_routine_id: null,
    practice_id: card.dataset.practiceId,
    duration_id: selectedDuration ? selectedDuration.value : null,
    position: card.dataset.order, // Use the updated data-order
  }));

  personalRoutineData.practices = practices;

  return personalRoutineData;
};

// Function to save the routine
const saveRoutine = () => {
  updateCardOrder(); // Ensure the order is up-to-date
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
      window.location.href = '/next-page'; // Navigate to the next page
    })
    .catch((error) => {
      console.error('Error saving routine:', error);
    });
};

// Event listener for saving the routine
document.getElementById('save-button').addEventListener('click', saveRoutine);


// const saveButton = document.getElementById('save-button')

// // Save the new order when navigating to the next page
// saveButton.addEventListener('click', () => {
//   saveOrder();
//   saveRoutine
//   window.location.href = '/next-page'; // Navigate to the next page
// });

// // Save the updated order to the server
// function saveOrder() {
//   const updatedOrder = [...document.querySelectorAll('.practice-card')].map((card, index) => ({
//       id: card.id.split('-')[1], // Extract the ID
//       position: index + 1        // Use the index as the new position
//   }));

//   fetch('/update-order', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify(updatedOrder)
//   }).then(response => {
//       if (response.ok) {
//           console.log('Order updated successfully in the database!');
//       }
//   });
// }

// const collectRoutineData = () => {

//         let personalRoutineData = {
//           user_id: req.session.user_id,
//           name: document.getElementById('routine-name').innerText,
//           description: document.getElementById('routine-description').innerText,
//           routine_type: document.getElementById('practice-container').dataset.routineType,
//           start_time: document.getElementById('routine-start-time').innerText,
//           is_active: true,
//           notes: null, 
//           practices: []
//         };

//     const cards = document.querySelectorAll('.practice-card');
//     const selectedDuration = document.querySelector('.duration option:checked');

//     const practices = Array.from(cards).map((card) => ({
//       personal_routine_id: null,
//       practice_id: card.dataset.practiceId,
//       duration_id: selectedDuration.value,
//       position: card.dataset.order
//     }));

//     personalRoutineData.practices = practices
  
//     return personalRoutineData
//   };
  
//   const saveRoutine = () => {
//     const routineData = collectRoutineData();
//     fetch('/routines/builder/am/initial/save', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify(routineData),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         console.log('Routine saved successfully:', data);
//       })
//       .catch((error) => {
//         console.error('Error saving routine:', error);
//       });
//   };
  
//   document.getElementById('save-button').addEventListener('click', saveRoutine);
  
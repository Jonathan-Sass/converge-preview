const practiceContainer = document.getElementById('practice-container');

new Sortable(practiceContainer, {
  animation: 150, // Smooth animation
  onEnd: () => {
    updateCardOrder(); // Update data-order attributes after drag-and-drop
  },
});


// let draggedElement = null;
// let placeholder = null;

// // Start dragging
// function drag(event) {
//     draggedElement = event.target;
//     placeholder = document.createElement('div');
//     placeholder.className = 'placeholder';
//     placeholder.style.height = `${draggedElement.offsetHeight}px`; // Match dragged element's height
//     draggedElement.parentNode.insertBefore(placeholder, draggedElement.nextSibling); // Insert the placeholder
//     event.dataTransfer.setData('text/plain', draggedElement.id); // Required for drag API
// }

// // Allow drop and handle dynamic placeholder placement
// function allowDrop(event) {
//     event.preventDefault();

//     const target = event.target.closest('.practice-card');
//     if (target && target !== draggedElement && target !== placeholder) {
//         const container = document.getElementById('practice-container');
//         const targetRect = target.getBoundingClientRect();
//         const offset = event.clientY - targetRect.top;

//         // Place the placeholder based on mouse position
//         if (offset < targetRect.height / 2) {
//             container.insertBefore(placeholder, target);
//         } else {
//             container.insertBefore(placeholder, target.nextSibling);
//         }
//     }
// }

// // Handle drag enter to add visual feedback
// function dragEnter(event) {
//     const target = event.target.closest('.practice-card');
//     if (target && target !== draggedElement) {
//         target.classList.add('drag-over');
//     }
// }

// // Handle drag leave to remove visual feedback
// function dragLeave(event) {
//     const target = event.target.closest('.practice-card');
//     if (target) {
//         target.classList.remove('drag-over');
//     }
// }

// // Finish dragging and update the DOM
// function dragEnd(event) {
//     placeholder.parentNode.insertBefore(draggedElement, placeholder); // Move the dragged element to the placeholder's position
//     placeholder.remove(); // Remove the placeholder
//     placeholder = null;   // Reset placeholder
//     updateOrder();        // Update the DOM order
// }

// // Drop the element
// function drop(event) {
//     event.preventDefault();
//     document.querySelectorAll('.drag-over').forEach(el => el.classList.remove('drag-over')); // Clean up visual effects
// }

// // Update order dynamically
// function updateOrder() {
//     const cards = document.querySelectorAll('.practice-card');
//     cards.forEach((card, index) => {
//         card.dataset.order = index + 1;
//         card.querySelector('h3').innerText = `${index + 1}. ${card.querySelector('h3').innerText.split('. ')[1]}`;
//     });
// }

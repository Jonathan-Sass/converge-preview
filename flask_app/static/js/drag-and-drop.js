let draggedElement = null;

document.getElementById('next-page-button').addEventListener('click', () => {
    saveOrder();
    window.location.href = '/next-page'; // Navigate to the next page
});

function saveOrder() {
    // Collect the new order from the DOM
    const updatedOrder = [...document.querySelectorAll('.practice-card')].map((card, index) => ({
        id: card.id.split('-')[1], // Extract the ID from the card's ID attribute
        position: index + 1 // Use the new index as the position
    }));

    // Send the new order to the server via fetch or AJAX
    fetch('/update-order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedOrder) // Send as JSON
    }).then(response => {
        if (response.ok) {
            console.log('Order updated successfully in the database!');
        }
    });
}

// Called when a drag starts
function drag(event) {
    draggedElement = event.target; // Store the element being dragged
    event.dataTransfer.setData("text", event.target.id); // Pass the ID of the dragged element
}

// Allow drop by preventing the default behavior
function allowDrop(event) {
    event.preventDefault();
    event.target.closest('.practice-card')?.classList.add('drag-over');

}

// Called when an element is dropped
function drop(event) {
    event.preventDefault();
    const droppedOn = event.target.closest('.practice-card');
    droppedOn?.classList.remove('drag-over'); // Remove visual feedback

    if (droppedOn && droppedOn !== draggedElement) {
        const container = document.getElementById('practice-container');

        // Swap positions of draggedElement and droppedOn
        const draggedIndex = [...container.children].indexOf(draggedElement);
        const droppedIndex = [...container.children].indexOf(droppedOn);

        if (draggedIndex > droppedIndex) {
            container.insertBefore(draggedElement, droppedOn);
        } else {
            container.insertBefore(draggedElement, droppedOn.nextSibling);
        }

        // Update the order attribute for all practice cards
        updateOrder();
    }
}

// Update order data after drag-and-drop
function updateOrder() {
    const cards = document.querySelectorAll('.practice-card');
    cards.forEach((card, index) => {
        card.dataset.order = index + 1;
        card.querySelector('h3').innerText = `${index + 1}. ${card.querySelector('h3').innerText.split('. ')[1]}`;
    });
}

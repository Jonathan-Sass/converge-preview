document.addEventListener("DOMContentLoaded", () => {
  initializeSortableContainers();
});


 export function initializeSortableContainers() {
  document.querySelectorAll('.sortable-container').forEach(sortableContainer => {
  // Sortable container must have sortable children (cards or list items)
  // 

    new Sortable(sortableContainer, {
      animation: 150, // Smooth animation
      onEnd: function (event) {
        updateCardOrder(event.to); // Update data-order attributes after drag-and-drop
      }
    });
  });
}

// Update order dynamically
export function updateCardOrder(container) {
  console.log("Selecting sortable-cards:")
  const cards = container.querySelectorAll('.sortable-card');
  console.log("Updating card order text...")
  cards.forEach((card, index) => {
    const cardOrder = index + 1;  
    card.dataset.order = cardOrder;


    const orderElement = card.querySelector('.card-order')
    if (orderElement) {
      console.log("Order element: ", orderElement)
      orderElement.innerText = `${cardOrder}.`;
    } else {
      console.warn("No .card-order element found in card: ", card)
    }
  });
}

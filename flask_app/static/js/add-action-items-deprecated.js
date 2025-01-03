document.addEventListener("DOMContentLoaded", () => {

  // Add event listener for dynamically adding more action items
  document.querySelectorAll('.add-action-item-btn').forEach(button => {
    button.addEventListener('click', event => {
      const clickedButton = event.currentTarget;
      addActionItem(clickedButton)
      console.log("Add action clicked")

    })
  });
});

function addActionItem(button) {
  const actionItemSection = button.closest('.action-item-section')
  const actionItemCount = actionItemSection.querySelectorAll(".action-item-card").length + 1;

  console.log("action-item-section selected:")
  console.log(actionItemSection)
  const actionItemCard = document.createElement("div");
  actionItemCard.classList.add("action-item-card", "card", "p-3", "mb-3", "shadow");
  actionItemCard.dataset.actionItemId = actionItemCount;

  actionItemCard.innerHTML = `
    <div class="mb-3 form-floating">
      <input type="text" class="form-control action-item-name" placeholder="Action Name">
      <label>Action Name</label>
    </div>
    <div class="mb-3 form-floating">
      <textarea class="form-control action-item-description"
        placeholder="Description (optional)"></textarea>
      <label>Description (optional)</label>
    </div>
    <div class="mb-3">
      <label>Target Date</label>
      <input type="date" class="form-control action-item-target-date">
    </div>
    <button class="btn btn-danger btn-sm remove-action-item-btn w-50 m-auto">Remove action
                  item</button>
  `;

  actionItemSection.insertBefore(actionItemCard, actionItemSection.querySelector(".add-action-item-btn"));
}

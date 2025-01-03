document.addEventListener("DOMContentLoaded", () => {
  // Event listener for the checkbox to toggle the button
  document.body.addEventListener("change", function (event) {
    if (event.target.classList.contains("separate-action-items-checkbox")) {
      const milestoneCard = event.target.closest(".milestone-card");
      toggleEditActionItemsButton(milestoneCard, event.target.checked);
    }
  });

  // Add event listener for dynamically adding more action items
  document.querySelectorAll('.add-action-item-btn').forEach(button => {
    button.addEventListener('click', event => {
      const clickedButton = event.currentTarget;
      addActionItem(clickedButton)
      console.log("Add action clicked")

    })
  });

  document.querySelectorAll('.remove-action-item-btn').forEach(button => {
    button.addEventListener('click', event => {
      const clickedButton = event.currentTarget
      removeActionItem(clickedButton)
    });
    
  });
});

function toggleEditActionItemsButton(milestoneCard, isChecked) {
  let editButton = milestoneCard.querySelector(".edit-action-items");

  if (isChecked) {
    // If the button doesn't already exist, create it
    if (!editButton) {
      editButton = document.createElement("button");
      editButton.classList.add("btn", "btn-outline-primary", "btn-sm", "edit-action-items", "mt-2");
      editButton.textContent = "Edit Action Items";
      editButton.setAttribute("type", "button");
      editButton.setAttribute("data-bs-toggle", "modal");
      editButton.setAttribute("data-bs-target", "#actionItemsModal");
      editButton.setAttribute("data-milestone-id", milestoneCard.dataset.milestoneId);

      milestoneCard.appendChild(editButton);
    }
  } else {
    // If unchecked, remove the button
    if (editButton) {
      editButton.remove();
    }
  }
}

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

function removeActionItem(button) {
  const actionItemCard = button.closest('.action-item-card')
  
  if (actionItemCard) {
    actionItemCard.remove();
  }
}


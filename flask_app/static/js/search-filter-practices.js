document.addEventListener("DOMContentLoaded", async function () {
  let practicesByCategory = {}; // Store practices grouped by category

  // Fetch all practices from the backend
  async function fetchPractices() {
      try {
          const response = await fetch('/api/categorized-practices/all'); // Adjust route as needed
          if (!response.ok) throw new Error('Failed to fetch practices');
          return await response.json(); // Returns structured category-practices data
      } catch (error) {
          console.error("Error fetching practices:", error);
          return {}; // Return empty object if there's an error
      }
  }

  // Initialize practices data
  practicesByCategory = await fetchPractices();

  // Elements
  const categoryFilterBtn = document.getElementById("category-filter-btn");
  const categoryListContainer = document.getElementById("category-list");

  // Open modal when filter button is clicked
  categoryFilterBtn.addEventListener("click", function () {
      populateCategoryModal();
      const categoryModal = new bootstrap.Modal(document.getElementById("categoryModal"));
      categoryModal.show();
  });

  // Function to populate the modal with categories and practices
  function populateCategoryModal() {
    categoryListContainer.innerHTML = ""; // Clear previous content

    Object.entries(practicesByCategory).forEach(([category, practices], index) => {
        // Create the main accordion item
        const accordionItem = document.createElement("div");
        accordionItem.classList.add("accordion-item");

        // Create category title (Accordion Header)
        const categoryTitle = document.createElement("h2");
        categoryTitle.classList.add("accordion-header");
        categoryTitle.id = `heading-${index}`;

        categoryTitle.innerHTML = `
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                data-bs-target="#collapse-${index}" aria-expanded="false"
                aria-controls="collapse-${index}">
                ${category}
            </button>
        `;

        // Create the collapsible section (Accordion Body)
        const accordionCollapse = document.createElement("div");
        accordionCollapse.id = `collapse-${index}`;
        accordionCollapse.classList.add("accordion-collapse", "collapse");
        accordionCollapse.setAttribute("aria-labelledby", `heading-${index}`);
        accordionCollapse.setAttribute("data-bs-parent", "#category-list");

        // Create the container for practice cards
        const cardContainer = document.createElement("div");
        cardContainer.classList.add("accordion-body", "d-flex", "flex-wrap", "justify-content-center", "gap-3", "mb-3");

        // Create practice cards
        practices.forEach((practice, practiceIndex) => {
            const card = document.createElement("div");
            card.classList.add("practice-card", "card", "shadow", "p-2", "text-center", "opacity-75", "mb-3", "col-3", "sortable-card");
            card.dataset.practiceId = practice.id;
            card.dataset.order = practiceIndex + 1; // Simulating loop.index
            card.id = `practice-${index}-${practiceIndex + 1}`; // Ensure unique ID

            card.innerHTML = `
                <div class="card-body compact-card d-flex flex-column">
                    <div class="card-header">
                        <h5 class="card-order text-primary">${practiceIndex + 1}. </h5>
                        <h5 class="practice-name text-primary">${practice.name}</h5>
                        <span class="badge difficulty-badge d-block">Difficulty: ${practice.difficulty || "N/A"}</span>
                        <span class="badge impact-badge">${truncateText(practice.impact_rating_description, 30)}</span>
                    </div>
                    <button class="btn btn-sm btn-outline-primary mt-2 add-to-routine" data-id="${practice.id}">Add to Routine</button>
                </div>
            `;

            card.querySelector(".add-to-routine").addEventListener("click", () => addToRoutine(practice, index));

            cardContainer.appendChild(card);
        });

        // Append everything correctly
        accordionCollapse.appendChild(cardContainer);
        accordionItem.appendChild(categoryTitle);
        accordionItem.appendChild(accordionCollapse);
        categoryListContainer.appendChild(accordionItem);
    });
}

  // Function to truncate text (like `truncate(100)` in Jinja)
  function truncateText(text, maxLength) {
      if (!text) return "";
      return text.length > maxLength ? text.substring(0, maxLength) + "..." : text;
  }

  // Function to add a practice to the routine
  function addToRoutine(practice, index) {
    const practiceContainer = document.getElementById("practice-container");

    const existingPracticeCard = practiceContainer.querySelector(`[data-practice-id=${practice.id}]`);

    if (existingPracticeCard) {
      console.warn(`practiceId ${practice.id} already exists. Skipping duplicate.`)
      return;
    }
    // Create the practice card
    const practiceCard = document.createElement("div");
    practiceCard.classList.add("practice-card", "card", "shadow", "p-2", "text-center", "opacity-75", "mb-3", "col-3", "sortable-card");
    practiceCard.dataset.practiceId = practice.id;
    practiceCard.dataset.order = index;
    practiceCard.id = `practice-${index}`;

    // Build the inner HTML structure
    practiceCard.innerHTML = `
        <div class="h5 practice-category">${practice.practice_category || "Uncategorized"}</div>
        <div class="card-body compact-card d-flex flex-column">
            <div class="card-header">
                <h5 class="card-order text-primary">${index}. </h5>
                <h5 class="practice-name text-primary">${practice.name}</h5>
                <span class="badge difficulty-badge d-block">Difficulty: ${practice.difficulty || "N/A"}</span>
                <span class="badge impact-badge">${truncateText(practice.impact_rating_description, 30)}</span>
            </div>
            <p class="short-description">${truncateText(practice.description, 100)}</p>
            <select class="form-select duration" aria-label="Default select example" id="${practice.name}-duration">
                ${practice.durations.map(duration => `
                    <option value="${duration.id}">
                        ${duration.duration_label} ${duration.engagement_level ? `(${duration.engagement_level})` : ""}
                    </option>
                `).join("")}
            </select>
            <div class="card-footer mt-auto">
                <button class="btn btn-link details-button" data-bs-toggle="modal"
                    data-bs-target="#practiceDetails${index}">
                    Learn More
                </button>
            </div>
        </div>
    `;

    // Append to the container
    practiceContainer.appendChild(practiceCard);
}
});

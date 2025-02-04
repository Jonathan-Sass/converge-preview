document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("search-practices");
  const categoryFilter = document.getElementById("category-filter");
  const practiceCards = document.querySelectorAll(".practice-card");

  function filterPractices() {
      const searchQuery = searchInput.value.toLowerCase();
      const selectedCategory = categoryFilter.value;

      practiceCards.forEach(card => {
          const practiceName = card.querySelector(".practice-name").textContent.toLowerCase();
          const practiceCategory = card.querySelector(".practice-category").textContent.trim();

          const matchesSearch = searchQuery === "" || practiceName.includes(searchQuery);
          const matchesCategory = selectedCategory === "" || practiceCategory === selectedCategory;

          if (matchesSearch && matchesCategory) {
              card.style.display = "block";
          } else {
              card.style.display = "none";
          }
      });
  }

  searchInput.addEventListener("input", filterPractices);
  categoryFilter.addEventListener("change", filterPractices);
});
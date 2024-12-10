document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("practice-container");
    const scrollLeftButton = document.getElementById("scroll-left");
    const scrollRightButton = document.getElementById("scroll-right");

    // Scroll left
    scrollLeftButton.addEventListener("click", () => {
        container.scrollBy({ left: -250, behavior: "smooth" }); // Adjust value to card width
    });

    // Scroll right
    scrollRightButton.addEventListener("click", () => {
        container.scrollBy({ left: 250, behavior: "smooth" }); // Adjust value to card width
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("practice-container");
    const scrollLeftButton = document.getElementById("scroll-left");
    const scrollRightButton = document.getElementById("scroll-right");

    // Helper function to find the next scrollable card
    const findNextCard = (direction) => {
        const cards = Array.from(container.querySelectorAll(".practice-card"));
        const containerRect = container.getBoundingClientRect();

        if (direction === "left") {
            for (let i = cards.length - 1; i >= 0; i--) {
                const cardRect = cards[i].getBoundingClientRect();
                if (cardRect.right < containerRect.left) {
                    return cards[i];
                }
            }
        } else if (direction === "right") {
            for (const card of cards) {
                const cardRect = card.getBoundingClientRect();
                if (cardRect.left > containerRect.right) {
                    return card;
                }
            }
        }
        return null;
    };

    // Scroll left
    scrollLeftButton.addEventListener("click", () => {
        const prevCard = findNextCard("left");
        if (prevCard) {
            prevCard.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "start" });
        }
    });

    // Scroll right
    scrollRightButton.addEventListener("click", () => {
        const nextCard = findNextCard("right");
        if (nextCard) {
            nextCard.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "start" });
        }
    });

    // Drag-aware scrolling
    document.addEventListener("dragover", (event) => {
        const containerRect = container.getBoundingClientRect();

        if (event.clientX < containerRect.left + 50) {
            container.scrollBy({ left: -10, behavior: "auto" });
        } else if (event.clientX > containerRect.right - 50) {
            container.scrollBy({ left: 10, behavior: "auto" });
        }
    });
});

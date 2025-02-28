let lastScrollPosition = 0;
let ticking = false;

function applyScrollEffects() {
    lastScrollPosition = window.scrollY;

    if (!ticking) {
        requestAnimationFrame(() => {
            // Move the background smoothly at 75% scroll speed
            document.querySelector(".parallax-bg").style.transform = `translateY(${lastScrollPosition * 0.75}px)`;
            ticking = false;
        });

        ticking = true;
    }
}

// Attach scroll event listener
window.addEventListener("scroll", applyScrollEffects);

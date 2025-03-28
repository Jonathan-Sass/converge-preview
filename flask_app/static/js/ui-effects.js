let lastScrollY = 0;
let parallaxY = 0;
let easeFactor = 1; // Adjust for more or less smoothing

function smoothParallax() {
    // Interpolating between last position and target position for smooth effect
    parallaxY += (lastScrollY * 0.5 - parallaxY) * easeFactor;

    // Apply the transformed value
    document.querySelector(".parallax-bg").style.transform = `translateY(${parallaxY}px)`;

    // Keep updating the animation frame for smooth interpolation
    requestAnimationFrame(smoothParallax);
}

// Attach scroll listener to update `lastScrollY`
window.addEventListener("scroll", () => {
    lastScrollY = window.scrollY;
});

// Start animation loop
smoothParallax();

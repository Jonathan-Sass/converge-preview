document.addEventListener('DOMContentLoaded', () => {
  // Initialize Swiper
  const swiper = new Swiper('.swiper-container', {
    direction: 'horizontal',
    slidesPerView: 'auto',
    spaceBetween: 16,
    centeredSlides: false,
    breakpoints: {
      // Optionally configure for responsiveness
      768: {
          spaceBetween: 24, // Increase gap for larger screens
      }
    },
    navigation: {
      nextEl: '#scroll-right',
      prevEl: '#scroll-left',
    },
    scrollbar: {
      el: '.swiper-scrollbar',
      draggable: true,
    },
  });

  // Export swiper instance for use in other scripts
  window.mySwiper = swiper;
});

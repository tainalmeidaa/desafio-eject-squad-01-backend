function initializeHomeCarousel() {
  const viewport = document.querySelector("#space-section .carousel__viewport");
  const carousel = document.querySelector("#space-section .carousel");
  if (!viewport || !carousel) return;

  const slides = [...viewport.querySelectorAll(".carousel__slide")];
  const dots = [...carousel.querySelectorAll(".carousel__dot")];

  function applySlide(index) {
    const i = Math.max(0, Math.min(index, slides.length - 1));
    dots.forEach((dot, j) => {
      const active = j === i;
      dot.classList.toggle("carousel__dot--active", active);
      if (active) dot.setAttribute("aria-current", "true");
      else dot.removeAttribute("aria-current");
    });
  }

  function goToSlide(index) {
    const w = viewport.clientWidth;
    if (!w) return;
    const i = Math.max(0, Math.min(index, slides.length - 1));
    viewport.scrollTo({ left: i * w, behavior: "smooth" });
  }

  dots.forEach((dot, i) => {
    dot.addEventListener("click", () => goToSlide(i));
  });

  function syncFromScroll() {
    const w = viewport.clientWidth;
    if (!w) return;
    const index = Math.round(viewport.scrollLeft / w);
    applySlide(index);
  }

  let raf = 0;
  function onScroll() {
    if (raf) return;
    raf = requestAnimationFrame(() => {
      raf = 0;
      syncFromScroll();
    });
  }

  viewport.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", syncFromScroll);
  syncFromScroll();
}

initializeHomeCarousel();

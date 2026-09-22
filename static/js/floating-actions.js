document.addEventListener("DOMContentLoaded", function () {
  const fab = document.getElementById("floatingActions");
  const footer = document.querySelector("footer");
  const header = document.querySelector(".site-header");

  if (!fab || !footer) return;

  function updateFabPosition() {
    // Measure from the untransformed position each time, otherwise the
    // previous frame's shift compounds into this one.
    fab.style.transform = "translateY(0)";

    const fabRect = fab.getBoundingClientRect();
    const footerRect = footer.getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    const headerHeight = header ? header.getBoundingClientRect().height : 0;

    const overlap = Math.max(0, viewportHeight - footerRect.top);
    if (overlap <= 0) return;

    // Never push the buttons above the fixed header (or the top of the
    // viewport, if there's no header), no matter how tall the footer is
    // or how far past it you scroll.
    const maxShift = Math.max(0, fabRect.top - headerHeight);
    const shift = Math.min(overlap + 20, maxShift);
    if (shift > 0) fab.style.transform = `translateY(-${shift}px)`;
  }

  window.addEventListener("scroll", updateFabPosition);
  window.addEventListener("resize", updateFabPosition);
  updateFabPosition();
});
document.addEventListener("DOMContentLoaded", function () {
  const fab = document.getElementById("floatingActions");
  const footer = document.querySelector("footer");

  if (!fab || !footer) return;

  function updateFabPosition() {
    const footerRect = footer.getBoundingClientRect();
    const viewportHeight = window.innerHeight;

    if (footerRect.top < viewportHeight) {
      const overlap = viewportHeight - footerRect.top;
      fab.style.transform = `translateY(-${overlap + 20}px)`;
    } else {
      fab.style.transform = "translateY(0)";
    }
  }

  window.addEventListener("scroll", updateFabPosition);
  window.addEventListener("resize", updateFabPosition);
  updateFabPosition();
});
// Reveal-on-scroll (respects prefers-reduced-motion via CSS)
(function () {
  var els = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    els.forEach(function (el) { el.classList.add("in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  els.forEach(function (el) { io.observe(el); });
})();

// Highlight current page in nav
(function () {
  var here = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("nav.main-nav a").forEach(function (a) {
    if (a.getAttribute("href") === here) a.classList.add("active");
  });
})();

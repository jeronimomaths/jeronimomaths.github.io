
(function () {
  const root = document.documentElement;
  const button = document.getElementById("theme-toggle");

  if (!button) return;

  const saved = localStorage.getItem("theme");

  const systemDark = window.matchMedia(
    "(prefers-color-scheme: dark)"
  ).matches;

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);

    button.setAttribute(
      "aria-label",
      theme === "dark"
        ? "Switch to light mode"
        : "Switch to dark mode"
    );
  }

  applyTheme(saved || (systemDark ? "dark" : "light"));

  button.addEventListener("click", function () {
    const next =
      root.getAttribute("data-theme") === "dark"
        ? "light"
        : "dark";

    localStorage.setItem("theme", next);
    applyTheme(next);
  });

  window.matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", function (event) {
      if (!localStorage.getItem("theme")) {
        applyTheme(event.matches ? "dark" : "light");
      }
    });
})();

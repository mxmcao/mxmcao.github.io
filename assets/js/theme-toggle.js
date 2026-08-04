(() => {
  const storageKey = "theme";
  const button = document.querySelector("[data-theme-toggle]");

  if (!button) return;

  const applyTheme = (theme) => {
    document.documentElement.classList.toggle("dark-mode", theme === "dark");
    document.body.classList.toggle("dark-mode", theme === "dark");
    button.setAttribute("aria-pressed", String(theme === "dark"));
    button.setAttribute(
      "aria-label",
      theme === "dark" ? "Use light theme" : "Use dark theme",
    );
  };

  button.addEventListener("click", () => {
    const nextTheme = document.body.classList.contains("dark-mode")
      ? "light"
      : "dark";

    localStorage.setItem(storageKey, nextTheme);
    applyTheme(nextTheme);
  });

  const savedTheme = localStorage.getItem(storageKey);
  const preferredTheme = window.matchMedia("(prefers-color-scheme: dark)")
    .matches
    ? "dark"
    : "light";

  applyTheme(savedTheme || preferredTheme);
})();

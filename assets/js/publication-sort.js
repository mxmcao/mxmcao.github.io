(() => {
  const sorter = document.querySelector("[data-publication-sorter]");

  if (!sorter) return;

  const yearGroups = sorter.querySelector("[data-publication-year-groups]");
  const citationList = sorter.querySelector("[data-publication-citation-list]");
  const buttons = Array.from(sorter.querySelectorAll("[data-publication-sort]"));
  const status = sorter.querySelector("[data-publication-sort-status]");
  const items = Array.from(
    yearGroups.querySelectorAll(".publication-item"),
  );
  const itemsByParent = new Map();

  items.forEach((item, index) => {
    const parent = item.parentElement;

    item.dataset.publicationIndex = String(index);

    if (!itemsByParent.has(parent)) {
      itemsByParent.set(parent, []);
    }

    itemsByParent.get(parent).push(item);
  });

  const citationCount = (item) =>
    Number.parseInt(item.dataset.publicationCitations || "0", 10) || 0;

  const year = (item) =>
    Number.parseInt(item.dataset.publicationYear || "0", 10) || 0;

  const restoreYearOrder = () => {
    itemsByParent.forEach((parentItems, parent) => {
      parentItems.forEach((item) => parent.append(item));
    });
  };

  const sortByCitations = () => {
    items
      .slice()
      .sort(
        (left, right) =>
          citationCount(right) - citationCount(left) ||
          year(right) - year(left) ||
          Number(left.dataset.publicationIndex) -
            Number(right.dataset.publicationIndex),
      )
      .forEach((item) => citationList.append(item));
  };

  const setMode = (mode) => {
    const citations = mode === "citations";

    if (citations) {
      sortByCitations();
    } else {
      restoreYearOrder();
    }

    yearGroups.hidden = citations;
    citationList.hidden = !citations;

    buttons.forEach((button) => {
      const active = button.dataset.publicationSort === mode;

      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });

    status.textContent = citations
      ? "Sorted by citation count."
      : "Sorted by year.";
  };

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      setMode(button.dataset.publicationSort);
    });
  });
})();

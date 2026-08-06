(() => {
  const dialog = document.querySelector("[data-wechat-dialog]");
  const openButtons = document.querySelectorAll("[data-wechat-dialog-open]");
  const closeButton = document.querySelector("[data-wechat-dialog-close]");

  if (!dialog || !openButtons.length || !closeButton) {
    return;
  }

  openButtons.forEach((button) => {
    button.addEventListener("click", () => {
      if (!dialog.open) {
        dialog.showModal();
      }
    });
  });

  closeButton.addEventListener("click", () => dialog.close());

  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) {
      dialog.close();
    }
  });
})();

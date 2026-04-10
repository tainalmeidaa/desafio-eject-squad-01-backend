function initializeToastMessages() {
  const toasts = document.querySelectorAll(".global-messages__item");
  if (!toasts.length) return;

  function closeToast(toast) {
    toast.classList.add("global-messages__item--closing");
    window.setTimeout(() => {
      toast.remove();
      const container = document.querySelector(".global-messages");
      if (container && !container.children.length) {
        container.remove();
      }
    }, 180);
  }

  toasts.forEach((toast) => {
    window.setTimeout(() => closeToast(toast), 10000);
  });
}

initializeToastMessages();

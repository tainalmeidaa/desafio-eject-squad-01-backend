function initializeNavbar() {
  const menuToggle = document.querySelector(".menu-toggle");
  const navbarMenu = document.getElementById("primary-nav");

  if (!menuToggle || !navbarMenu) return;
  if (menuToggle.dataset.bound === "true") return;

  menuToggle.addEventListener("click", function () {
    navbarMenu.classList.toggle("navbar__menu--open");
    menuToggle.classList.toggle(
      "menu-toggle--open",
      navbarMenu.classList.contains("navbar__menu--open"),
    );
  });

  menuToggle.dataset.bound = "true";
}

initializeNavbar();

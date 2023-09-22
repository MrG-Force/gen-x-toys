const MESSAGE_CLASSES =
  "cart-message absolute z-150 top-2 left-1/2 transform -translate-x-1/2 -translate-y-full bg-blue-400 text-slate-900 font-semibold p-4 rounded opacity-0 transition-all duration-700 ease-in-out";

function displayAddedToCartMessage(toyTitle) {
  const newDiv = document.createElement("div");
  newDiv.className = MESSAGE_CLASSES;
  newDiv.textContent = `${toyTitle} was added to your cart`;

  const nav = document.querySelector("nav");
  nav.appendChild(newDiv);

  applyTransitions(newDiv);
}

function applyTransitions(element) {
  setTimeout(() => {
    element.classList.replace("-translate-y-full", "translate-y-0");
    element.classList.replace("opacity-0", "opacity-80");
  }, 50);

  setTimeout(() => {
    element.classList.replace("translate-y-0", "-translate-y-full");
    element.classList.replace("opacity-80", "opacity-0");
    setTimeout(() => {
      element.remove();
    }, 1000);
  }, 3000);
}

function attachCartButtonListeners() {
  const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");
  addToCartButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      const toyTitle = event.target.getAttribute("data-toy-title");
      displayAddedToCartMessage(toyTitle);
    });
  });
}

function attachCategorySelectListener() {
  const categorySelect = document.getElementById("categorySelect");
  const toyGrid = document.getElementById("toyList");

  categorySelect.addEventListener("change", function () {
    const selectedCategory = categorySelect.value;
    const fetchUrl = `/shop/get_toys_by_category?category=${selectedCategory}`;
    fetch(fetchUrl)
      .then((response) => response.text())
      .then((html) => {
        toyGrid.innerHTML = html;
        attachCartButtonListeners();
      });
  });
}

document.addEventListener("DOMContentLoaded", () => {
  attachCartButtonListeners();
  attachCategorySelectListener();
});

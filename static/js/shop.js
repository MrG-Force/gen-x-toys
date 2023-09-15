const MESSAGE_CLASSES = 'cart-message absolute z-150 top-2 left-1/2 transform -translate-x-1/2 -translate-y-full bg-green-500 text-white p-4 rounded opacity-0 transition-all duration-700 ease-in-out';

// Function to display a message when an item is added to the cart
function displayAddedToCartMessage(toyTitle) {
    console.log("displayAddedToCartMessage called");
    // Create a new div element
    const newDiv = document.createElement("nav");
  
    // Set div attributes
    newDiv.className = MESSAGE_CLASSES;
    newDiv.textContent = `${toyTitle} was added to your cart`;

    // Get body element
    const nav = document.querySelector('nav');
  
    // Append the new div to the body
    nav.appendChild(newDiv);
  
    // Add transition classes after appending (for slide-down and fade-in)
    setTimeout(() => {
      newDiv.classList.replace('-translate-y-full', 'translate-y-0');
      newDiv.classList.replace('opacity-0', 'opacity-100');
    }, 50);
  
    // Remove the message after 3 seconds with fade-out effect
    setTimeout(() => {
      newDiv.classList.replace('translate-y-0', '-translate-y-full');
      newDiv.classList.replace('opacity-100', 'opacity-0');
      setTimeout(() => {
        newDiv.remove();
      }, 1000);
    }, 3000);
}
// Add event listeners to 'Add to cart' buttons
document.addEventListener("DOMContentLoaded", () => {
    const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");
  
    addToCartButtons.forEach((button) => {
      button.addEventListener("click", (event) => {
        event.preventDefault();
        const toyTitle = event.target.getAttribute('data-toy-title');
        displayAddedToCartMessage(toyTitle);
      });
    });
  });
  

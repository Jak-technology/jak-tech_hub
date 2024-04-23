const navCloseBtn = document.querySelector(".navCloseBtn");
const checkbox = document.getElementById("chk1");

// Function to close the navigation menu
function closeNavMenu() {
    checkbox.checked = false;
}

// Event listener for the close button
navCloseBtn.addEventListener("click", () => {
    closeNavMenu();
});


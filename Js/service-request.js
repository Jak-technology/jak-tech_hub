async function populateSelectOptions() {
    try {
        const response = await fetch('https://jak-tech-hub.onrender.com/api/choices/');
        const data = await response.json();
        const { contact_choices, service_choices, business_type_choices } = data;

        // Populate Preferred Method of Contact
        const preferredContactSelect = document.getElementById('preferredContact');
        for (const [key, value] of Object.entries(contact_choices)) {
            const option = document.createElement('option');
            option.value = key;
            option.textContent = value;
            preferredContactSelect.appendChild(option);
        }

        // Populate Services Needed
        const servicesNeededSelect = document.getElementById('servicesNeeded');
        for (const [key, value] of Object.entries(service_choices)) {
            const option = document.createElement('option');
            option.value = key;
            option.textContent = value;
            servicesNeededSelect.appendChild(option);
        }

        // Populate Business Type
        const businessTypeSelect = document.getElementById('businessType');
        for (const [key, value] of Object.entries(business_type_choices)) {
            const option = document.createElement('option');
            option.value = key;
            option.textContent = value;
            businessTypeSelect.appendChild(option);
        }
    } catch (error) {
        console.error('Error fetching select options:', error);
    }
}

const loadingImage = document.createElement("img");
loadingImage.setAttribute("src", "../assets/loading3.gif")
loadingImage.setAttribute("id", "loading");
loadingImage.setAttribute("alt", "Loading");

const overlay = document.createElement("div");
overlay.setAttribute("id", "overlay");



function setStyling(elId, propertyObject) {
    el = elId;
    for (var property in propertyObject) {
        el.style[property] = propertyObject[property]
    }
}
setStyling(loadingImage, {
    "display": "none",
    "position": "fixed",
    "top": "50%",
    "left": "50%",
    "transform": "translate(-50%, -50%)",
    "z-index": "1001",
    "width": "90px",
    "height": "90px",
})
setStyling(overlay, {
    "display": "none",
    "position": "fixed",
    "top": "0",
    "left": "0",
    "width": "100%",
    "height": "100%",
    "background": "rgba(0, 0, 0, 0.5)",
    "z-index": "1000",
}) 
document.body.appendChild(loadingImage);
document.body.appendChild(overlay);


// Function to handle form submission
// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission
    loadingImage.style.display = "block";
    overlay.style.display = "block";

    // Get form data
    const formData = new FormData(event.target);

    // Submit form data to the specified URL
    fetch('https://jak-tech-hub.onrender.com/api/services/', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        loadingImage.style.display = "none";
        overlay.style.display = "none";
        if (response.ok) {
            console.log('Form submitted successfully');
            // Redirect to Services page
            event.target.reset()
            // Display success message
            alert('Request Submitted Successfully');
        } else {
            console.error('Form submission failed');
            alert('Request Submission Failed');
            }
        })
        .catch(error => {
            loadingImage.style.display = "none";
            overlay.style.display = "none";
            console.error('Error submitting form:', error);
            alert('Error Submitting Request');
        });
}
// Call the function to populate select options when the page loads
window.onload = populateSelectOptions;

// Add event listener for form submission
document.querySelector('.first-form').addEventListener('submit', handleSubmit);


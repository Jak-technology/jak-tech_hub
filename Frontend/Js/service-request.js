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

// Function to handle form submission
// Function to handle form submission
function handleSubmit(event) {
event.preventDefault(); // Prevent default form submission

// Get form data
const formData = new FormData(event.target);

// Submit form data to the specified URL
fetch('https://jak-tech-hub.onrender.com/api/services/', {
    method: 'POST',
    body: formData,
})
.then(response => {
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
        console.error('Error submitting form:', error);
        alert('Error Submitting Request');
    });
}
// Call the function to populate select options when the page loads
window.onload = populateSelectOptions;

// Add event listener for form submission
document.querySelector('.first-form').addEventListener('submit', handleSubmit);
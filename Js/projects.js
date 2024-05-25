document.getElementById('file').addEventListener('change', function() {
    const selectedFiles = document.getElementById('selectedFiles');
    const addMoreButton = document.getElementById('addMoreButton');

    selectedFiles.innerHTML = '';

    for (const file of this.files) {
      const fileItem = document.createElement('div');
      fileItem.className = 'file-item';

      const fileNameElement = document.createElement('div');
      fileNameElement.textContent = file.name;
      fileItem.appendChild(fileNameElement);

      const removeButton = document.createElement('button');
      removeButton.textContent = 'Remove';
      removeButton.addEventListener('click', function() {
        selectedFiles.removeChild(fileItem);
      });
      fileItem.appendChild(removeButton);

      selectedFiles.appendChild(fileItem);
    }
    // CHANGED "chooseFile" TO "file" BECAUSE I WAS GETTING NULL ERROR
    document.getElementById('file').innerText = this.files.length > 1 ? this.files.length + ' files selected' : 'file selected';

    // Show the "Add More Files" button if files are selected, otherwise hide it
    addMoreButton.style.display = this.files.length > 0 ? 'block' : 'none';
  });

  // Additional check when files are removed manually
  document.getElementById('file').addEventListener('click', function() {
    const addMoreButton = document.getElementById('addMoreButton');
    // Hide the "Add More Files" button when the file input is clicked
    addMoreButton.style.display = 'none';
  });


  document.addEventListener("DOMContentLoaded", function() {
    const newsletterForm = document.getElementById('newsletterForm');

    newsletterForm.addEventListener("submit", event => {
        event.preventDefault();

        const emailInput = newsletterForm.querySelector('input[type="email"]');
        const email = emailInput.value;

        if (!email) {
            alert("Please enter your email address.");
            return;
        }

        const data = {
            email: email
        };

        fetch('https://jak-tech-hub.onrender.com/subscriber/create/', {
            headers: {
                'Content-Type': 'application/json',
            },
            mode: 'cors',
            method: "POST",
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            alert("Subscription successful!"); // You can customize this message
        })
        .catch(error => {
            console.error('Error:', error);
            alert("An error occurred. Please try again later."); // You can customize this message
        });
    });
});

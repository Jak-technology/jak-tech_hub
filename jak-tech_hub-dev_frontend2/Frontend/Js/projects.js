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
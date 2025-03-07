document.addEventListener("DOMContentLoaded", function () {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("file-input");
  const fileNameDisplay = document.getElementById("file-name");
  
  dropArea.addEventListener("click", () => {
      fileInput.click();
  });

  dropArea.addEventListener("dragover", (event) => {
      event.preventDefault();
      dropArea.classList.add("border-blue-500");
  });
  
  dropArea.addEventListener("dragleave", () => {
      dropArea.classList.remove("border-blue-500");
  });
  
  dropArea.addEventListener("drop", (event) => {
      event.preventDefault();
      dropArea.classList.remove("border-blue-500");
      
      if (event.dataTransfer.files.length) {
          fileInput.files = event.dataTransfer.files;
          fileNameDisplay.textContent = event.dataTransfer.files[0].name;
      }
  });

  fileInput.addEventListener("change", (event) => {
      if (event.target.files.length) {
          fileNameDisplay.textContent = event.target.files[0].name;
      }
  });
});
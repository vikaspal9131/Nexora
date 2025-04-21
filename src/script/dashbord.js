const tabs = document.querySelectorAll('#tabs [data-tab]');
const panes = document.querySelectorAll('.tab-pane');
const defaultMsg = document.getElementById('default-msg');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.tab;
    panes.forEach(pane => pane.classList.add('hidden'));
    const activePane = document.getElementById(target);
    if (activePane) {
      activePane.classList.remove('hidden');
      defaultMsg.style.display = 'none';
    }
  });
});

// Drop area file trigger
const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("file-input");
const fileNameDisplay = document.getElementById("file-name");

dropArea.addEventListener("click", () => fileInput.click());

fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  fileNameDisplay.textContent = file ? file.name : "No file selected";
});

// Form submit handler
document.getElementById('resumeForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

  fetch('/analyze/', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      return response.json().then(err => { throw new Error(err.error || "Unknown error"); });
    }
    return response.json();
  })
  .then(data => {
    // Fill each tab with bullet point list
    const fillTab = (id, content) => {
      const el = document.getElementById(id);
      el.innerHTML = Array.isArray(content)
        ? '<ul class="list-disc pl-5 space-y-1">' + content.map(item => `<li>${item}</li>`).join('') + '</ul>'
        : `<p>${content}</p>`;
    };

    fillTab('overall', data.Overall);
    fillTab('gaps', data["Notable Gaps"]);
    fillTab('recommendations', data.Recommendations);
    fillTab('verdict', data["Final Verdict"]);
    fillTab('improvements', data["Areas for Improvement"]);
    fillTab('keywords', data["Keywords Found"]);

    document.getElementById('overall').classList.remove('hidden');
    defaultMsg.style.display = 'none';
  })
  .catch(error => {
    alert("Error: " + error.message);
  });
});
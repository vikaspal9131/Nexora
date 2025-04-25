const tabs = document.querySelectorAll('#tabs [data-tab]');
const panes = document.querySelectorAll('.tab-pane');
const defaultMsg = document.getElementById('default-msg');
const loader = document.getElementById('loader'); // Loader element

// Tab switching
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.tab;
    panes.forEach(p => p.classList.add('hidden'));
    const active = document.getElementById(target);
    if (active) {
      active.classList.remove('hidden');
      defaultMsg.style.display = 'none';
    }
  });
});

// File Upload
const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("file-input");
const fileNameDisplay = document.getElementById("file-name");

dropArea.addEventListener("click", () => fileInput.click());
fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  fileNameDisplay.textContent = file ? file.name : "";
});

// Form Submit
document.getElementById('resumeForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(this);

  // Show loader and hide default message
  loader.classList.remove('hidden');
  defaultMsg.style.display = 'none';
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.add('hidden'));

  fetch('/analyze/', {
    method: 'POST',
    body: formData
  })
  .then(res => {
    if (!res.ok) return res.json().then(err => { throw new Error(err.error || "Unknown error"); });
    return res.json();
  })
  .then(data => {
    console.log('API Response:', data);

    const fillTab = (id, content) => {
      const el = document.getElementById(id);
      if (!el) return;

      if (content === null || content === undefined) {
        el.innerHTML = "<p>Data not available</p>";
        return;
      }

      if (Array.isArray(content)) {
        if (content.length === 0) {
          el.innerHTML = "<p>No items available</p>";
        } else {
          el.innerHTML = '<ul class="list-disc pl-5 space-y-1">' + content.map(item => `<li>${item}</li>`).join('') + '</ul>';
        }
      } else {
        el.innerHTML = `<p>${content || "Not available"}</p>`;
      }
    };

    fillTab('overall', data.Overall);
    fillTab('gaps', data["Notable Gaps"]);
    fillTab('match_percentage', data["Match Percentage"]);
    fillTab('key_strengths', data["Key Strengths"]);
    fillTab('skills_gap', data["Skills Gap"]);
    fillTab('recommendations', data.Recommendations);
    fillTab('keywords', data["Keywords Found"]);
    fillTab('matched_keywords', data["Matched Keywords"]);
    fillTab('missing_keywords', data["Missing Keywords"]);
    fillTab('improvements', data["Areas for Improvement"] || data["Improvements"]);
    fillTab('ats_recommendations', data["ATS Recommendations"]);
    fillTab('final_verdict', data["Final Verdict"]);

    // Show "overall" tab and hide loader
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.add('hidden'));
    document.getElementById('overall').classList.remove('hidden');
    loader.classList.add('hidden');
  })
  .catch(error => {
    loader.classList.add('hidden');
    console.error("Error:", error);
    alert("Error: " + error.message);
  });
});

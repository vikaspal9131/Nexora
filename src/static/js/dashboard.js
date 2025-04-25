const form = document.getElementById("resumeForm");
const tabContents = document.querySelectorAll(".tab-pane");
const tabs = document.querySelectorAll("#tabs p");
const defaultMsg = document.getElementById("default-msg");

let analysisData = {}; // Store API response here

// 👇 Mapping between data-tab and JSON keys
const tabKeyMap = {
  overall: "Overall",
  gaps: "Notable Gaps",
  match_percentage: "Match Percentage",
  key_strengths: "Key Strengths",
  skills_gap: "Skills Gap",
  recommendations: "Recommendations",
  keywords: "Keywords Found",
  matched_keywords: "Matched Keywords",
  missing_keywords: "Missing Keywords",
  improvements: "Areas for Improvement",
  ats_recommendations: "ATS Recommendations",
  final_verdict: "Final Verdict"
};

// Submit Form and Get API Response
form.addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(form);
  const loader = document.getElementById("loader");

  loader.classList.remove("hidden");
  defaultMsg.classList.add("hidden"); // Hide default message when submitting form

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    analysisData = data;

    loader.classList.add("hidden");

    // 👉 Hide the default message when data is loaded
    defaultMsg.classList.add("hidden");

    // 👉 Auto-open first tab after data loads
    const firstTab = tabs[0];
    firstTab.click();
  } catch (err) {
    loader.classList.add("hidden");
    alert("Error analyzing resume.");
  }
});

// Handle Tab Click and Show Related Content
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const selected = tab.getAttribute("data-tab");

    tabContents.forEach((pane) => pane.classList.add("hidden"));

    const selectedPane = document.getElementById(selected);
    selectedPane.classList.remove("hidden");

    const content = analysisData[tabKeyMap[selected]];

    // Show content with the headline (tab title)
    const headline = `<h3 class="font-semibold text-[40px] py-[20px] text-gray-300">${tabKeyMap[selected]}</h3>`;

    if (Array.isArray(content)) {
      selectedPane.innerHTML = headline + "<ul class='list-disc pl-5'>" + content.map(item => `<li>${item}</li>`).join("") + "</ul>";
    } else {
      selectedPane.innerHTML = headline + `<p>${content || 'No data available.'}</p>`;
    }
  });
});
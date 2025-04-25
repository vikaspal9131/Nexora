import google.generativeai as genai
import json
import re
from config import Config

# Configure Gemini API
genai.configure(api_key=Config.GENAI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_resume(job_description, resume_text):
    prompt = f"""
    You are a Senior Technical HR Manager with 10+ years of experience hiring developers.

    The job description for the role is as follows:
    {job_description}

    Evaluate the following candidate's resume. Provide a detailed professional review with real examples from the resume.

    Also, as an ATS (Applicant Tracking System) expert, analyze the resume from an ATS standpoint.

    Structure the JSON response as follows:

    1. **overall**
    2. **key_strengths**
    3. **notable_gaps**
    4. **recommendations**
    5. **final_verdict**
    6. **areas_for_improvement**
    7. **keywords_found**
    8. **match_percentage**
    9. **matched_keywords**
    10. **missing_keywords**
    11. **skills_gap**
    12. **ats_recommendations**

    Resume:
    {resume_text}

    Respond **only** in valid JSON format without any extra explanation or text. Do not add markdown or code blocks.
    """

    # Request to Gemini API
    response = model.generate_content(prompt)

    try:
        cleaned_text = response.text.strip()
        match = re.search(r"\{.*\}", cleaned_text, re.DOTALL)
        json_str = match.group(0) if match else cleaned_text
        full_data = json.loads(json_str)

        return {
            "overall": full_data.get("overall", "Not found"),
            "key_strengths": full_data.get("key_strengths", []),
            "notable_gaps": full_data.get("notable_gaps", []),
            "recommendations": full_data.get("recommendations", []),
            "final_verdict": full_data.get("final_verdict", "Not found"),
            "areas_for_improvement": full_data.get("areas_for_improvement", []),
            "keywords_found": full_data.get("keywords_found", []),
            "match_percentage": full_data.get("match_percentage", "Not found"),
            "matched_keywords": full_data.get("matched_keywords", []),
            "missing_keywords": full_data.get("missing_keywords", []),
            "skills_gap": full_data.get("skills_gap", []),
            "ats_recommendations": full_data.get("ats_recommendations", [])
        }
    except json.JSONDecodeError as e:
        print("❌ JSON Parse Error:", e)
        return {
            "overall": response.text,
            "key_strengths": [],
            "notable_gaps": [],
            "recommendations": [],
            "final_verdict": "Unable to extract",
            "areas_for_improvement": [],
            "keywords_found": [],
            "match_percentage": "Unable to extract",
            "matched_keywords": [],
            "missing_keywords": [],
            "skills_gap": [],
            "ats_recommendations": []
        }

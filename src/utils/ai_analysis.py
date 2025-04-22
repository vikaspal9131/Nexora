import google.generativeai as genai
import json
import re
from config import Config

# Configure Gemini API
genai.configure(api_key=Config.GENAI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_resume(job_role, resume_text):
    prompt = f"""
    You are a Senior Technical HR Manager with 10+ years of experience hiring developers.

    Evaluate the following candidate's resume for the role of **{job_role}**. Provide a **detailed professional review** with real examples from the resume.

    Also, as an ATS (Applicant Tracking System) expert, analyze the resume from an ATS standpoint.

    Structure the JSON response as follows:

    1. **overall**: 
       - Discuss how well the resume aligns with the job role.
       - Highlight match in required tech stack, soft skills, project relevance, and job responsibilities.

    2. **key_strengths**: 
       - List strong technical and non-technical skills backed by resume examples.
       - Mention past project or internship experience that strengthens the candidate’s profile.

    3. **notable_gaps**: 
       - Clearly list missing or underrepresented skills/tools for the job role.
       - Mention any unclear/missing project ownership, deployment, or practical usage gaps.

    4. **recommendations**: 
       - Give actionable suggestions to improve the resume (e.g. “Add quantified metrics for projects”).
       - Help the candidate highlight their most relevant work.

    5. **final_verdict**: 
       - Final recommendation: Suitable or Not Suitable for the role.
       - Or give he adlines like “Needs improvement” or “Good fit with minor tweaks”.

    6. **areas_for_improvement**: 
       - Point out sections that need clarity, more examples, or better structure.

    7. **keywords_found**: 
       - List relevant keywords found from job description (e.g., HTML, Git, REST API).

    8. **match_percentage**: 
       - Overall match percentage between resume and job role (e.g., 82%).

    9. **matched_keywords**: 
       - List of key matching keywords found in the resume.

    10. **missing_keywords**: 
        - Important keywords missing based on job role expectations.

    11. **skills_gap**: 
        - List of skills the candidate lacks or hasn’t clearly demonstrated for the role.

    12. **ats_recommendations**: 
        - Suggestions to improve ATS-friendliness of the resume (e.g., formatting tips, keyword enhancements, structural clarity).

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    try:
        cleaned_text = re.sub(r"```json|```", "", response.text).strip()
        full_data = json.loads(cleaned_text)

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
    except json.JSONDecodeError:
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

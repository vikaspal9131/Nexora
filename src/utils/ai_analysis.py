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
       - Mention if an interview is recommended.

    6. **areas_for_improvement**: 
       - Point out sections that need clarity, more examples, or better structure.

    7. **keywords_found**: 
       - List relevant keywords found from job description (e.g., HTML, Git, REST API).

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    try:
        # Remove formatting if Gemini returns with ```json blocks
        cleaned_text = re.sub(r"```json|```", "", response.text).strip()
        full_data = json.loads(cleaned_text)

        return {
            "overall": full_data.get("overall", "Not found"),
            "key_strengths": full_data.get("key_strengths", []),
            "notable_gaps": full_data.get("notable_gaps", []),
            "recommendations": full_data.get("recommendations", []),
            "final_verdict": full_data.get("final_verdict", "Not found"),
            "areas_for_improvement": full_data.get("areas_for_improvement", []),
            "keywords_found": full_data.get("keywords_found", [])
        }
    except json.JSONDecodeError:
        return {
            "overall": response.text,
            "key_strengths": [],
            "notable_gaps": [],
            "recommendations": [],
            "final_verdict": "Unable to extract",
            "areas_for_improvement": [],
            "keywords_found": []
        }

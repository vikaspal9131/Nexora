import google.generativeai as genai
from config import Config

# Configure Gemini API
genai.configure(api_key=Config.GENAI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_resume(job_role, resume_text):
    prompt = f"""
    As an experienced Technical Human Resource Manager, provide a detailed professional evaluation 
                        of the candidate's resume against the job description. Please analyze:
                        1. Overall alignment with the role
                        2. Key strengths and qualifications that match
                        3. Notable gaps or areas for improvement
                        4. Specific recommendations for enhancing the resume
                        5. Final verdict on suitability for the role
                        
                        Format the response with clear headings and professional language.
    {resume_text}
    """
    response = model.generate_content(prompt)
    return response.text

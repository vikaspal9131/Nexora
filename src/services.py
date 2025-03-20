import os
import google.generativeai as genai
from config import GEMINI_API_KEY, UPLOAD_FOLDER


genai.configure(api_key=GEMINI_API_KEY)


os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if uploaded file is a PDF"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() == "pdf"

def summarize_pdf(file_path):
    """Summarize the uploaded PDF"""
    try:
        uploaded_file = genai.upload_file(path=file_path)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([
            uploaded_file, 
            "Summarize the document with key insights, important facts, and major conclusions."
        ])
        return response.text  
    except Exception as e:
        return f"Error in summarization: {str(e)}"

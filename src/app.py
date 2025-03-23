import os
from flask import Flask, request, jsonify, session
import fitz  # PyMuPDF for PDF parsing
from docx import Document
import google.generativeai as genai
from flask_session import Session

app = Flask(__name__)

# Configure session
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure Gemini API
GENAI_API_KEY = "AIzaSyAH7POcFUh2rVr8oqy5PzAekvXlAebXrYo"
genai.configure(api_key=GENAI_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

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
    response = model.generate_content(prompt)  # Fixed this line
    return response.text

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files or 'job_role' not in request.form:
        return jsonify({"error": "Missing resume file or job role"}), 400

    job_role = request.form['job_role']
    resume_file = request.files['resume']
    
    if resume_file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Extract text based on file type
    if resume_file.filename.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_file.filename.endswith('.docx'):
        resume_text = extract_text_from_docx(resume_file)
    else:
        return jsonify({"error": "Unsupported file format. Upload PDF or DOCX."}), 400
    
    # Analyze resume
    analysis_result = analyze_resume(job_role, resume_text)
    
    # Store result in session
    session['last_analysis'] = analysis_result
    
    return jsonify({"analysis": analysis_result})

@app.route('/last_analysis', methods=['GET'])
def get_last_analysis():
    if 'last_analysis' in session:
        return jsonify({"last_analysis": session['last_analysis']})
    return jsonify({"error": "No previous analysis found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

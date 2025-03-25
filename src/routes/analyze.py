from flask import Blueprint, request, jsonify
from utils.extract_text import extract_text_from_pdf, extract_text_from_docx
from utils.ai_analysis import analyze_resume

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/', methods=['POST'])  # Changed from '/analyze' to '/'
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

    return jsonify({"analysis": analysis_result})

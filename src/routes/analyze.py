from flask import Blueprint, request, jsonify
from utils.extract_text import extract_text_from_pdf, extract_text_from_docx
from utils.ai_analysis import analyze_resume

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/', methods=['POST'])
def analyze():
    
    if 'resume' not in request.files or 'job_description' not in request.form:
        return jsonify({"error": "Missing resume file or job description"}), 400

   
    job_description = request.form['job_description']  
    resume_file = request.files['resume']

    if resume_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    
    if resume_file.filename.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_file)
    elif resume_file.filename.endswith('.docx'):
        resume_text = extract_text_from_docx(resume_file)
    else:
        return jsonify({"error": "Unsupported file format. Upload PDF or DOCX."}), 400

    
    analysis_result = analyze_resume(job_description, resume_text)

 
    response = {
        "Overall": analysis_result.get("overall", ""),
        "Notable Gaps": analysis_result.get("notable_gaps", []),
        "Recommendations": analysis_result.get("recommendations", []),
        "Final Verdict": analysis_result.get("final_verdict", ""),
        "Areas for Improvement": analysis_result.get("areas_for_improvement", []),
        "Keywords Found": analysis_result.get("keywords_found", []),
        "Match Percentage": analysis_result.get("match_percentage", "N/A"),
        "Matched Keywords": analysis_result.get("matched_keywords", []),
        "Missing Keywords": analysis_result.get("missing_keywords", []),
        "Skills Gap": analysis_result.get("skills_gap", []),
        "ATS Recommendations": analysis_result.get("ats_recommendations", []),
        "Key Strengths": analysis_result.get("key_strengths", [])
    }

    return jsonify(response)

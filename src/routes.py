from flask import Blueprint, request, jsonify, render_template, session
import google.generativeai as genai
import os

api = Blueprint("api", __name__)

@api.route("/")
def index():
    return render_template("index.html")

@api.route("/summarize", methods=["POST"])
def summarize_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = f"uploads/{file.filename}"
    file.save(file_path)

   
    session["last_uploaded_file"] = file.filename  

    uploaded_file = genai.upload_file(path=file_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    response = model.generate_content([
        uploaded_file, 
        "Summarize the document with key insights, important facts, and any major conclusions."
    ])

    return jsonify({"filename": file.filename, "summary": response.text})

@api.route("/get-last-file", methods=["GET"])
def get_last_uploaded_file():
    if "last_uploaded_file" in session:
        return jsonify({"last_file": session["last_uploaded_file"]})
    return jsonify({"error": "No file found in session"})

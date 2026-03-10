
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(BASE_DIR, "notes")
QP_DIR = os.path.join(BASE_DIR, "question_papers")
IMP_DIR = os.path.join(BASE_DIR, "important_questions")

@app.route("/")
def home():
    return "EduChat Backend Running"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message","").lower()

    if "notes" in message:
        return jsonify({
            "reply":"Here are DBMS notes",
            "file":"/download/notes/dbms_notes.pdf"
        })

    elif "question paper" in message:
        return jsonify({
            "reply":"Download DBMS Question Paper",
            "file":"/download/question/dbms_qp.pdf"
        })

    elif "important question" in message:
        return jsonify({
            "reply":"Here are DBMS Important Questions",
            "image":"/download/important/dbms_imp.png"
        })

    else:
        if model:
            response = model.generate_content(message)
            return jsonify({"reply":response.text})
        else:
            return jsonify({"reply":"AI not configured. Add GEMINI_API_KEY in .env"})


@app.route("/download/notes/<filename>")
def download_notes(filename):
    return send_from_directory(NOTES_DIR, filename, as_attachment=True)

@app.route("/download/question/<filename>")
def download_qp(filename):
    return send_from_directory(QP_DIR, filename, as_attachment=True)

@app.route("/download/important/<filename>")
def download_imp(filename):
    return send_from_directory(IMP_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)


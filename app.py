from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Folder paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(BASE_DIR, "notes")
QP_DIR = os.path.join(BASE_DIR, "question_papers")
IMP_DIR = os.path.join(BASE_DIR, "important_questions")


# ---------------- HOME ROUTE ----------------


# ---------------- CHAT API ----------------

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message", "")
    return jsonify({
        "reply": "Bot received:"+ message
    })

    # NOTES REQUEST
    if "notes" in message:
        return jsonify({
            "reply": "Here are the DBMS notes",
            "file": "/download/notes/dbms_notes.pdf"
        })

    # QUESTION PAPER
    elif "question paper" in message:
        return jsonify({
            "reply": "Download DBMS Question Paper",
            "file": "/download/question/dbms_qp.pdf"
        })

    # IMPORTANT QUESTIONS
    elif "important question" in message:
        return jsonify({
            "reply": "Here are DBMS Important Questions",
            "image": "/download/important/dbms_imp.png"
        })

    # DEFAULT RESPONSE
    else:
        return jsonify({
            "reply": "Ask for notes, question papers or important questions"
        })


# ---------------- DOWNLOAD NOTES ----------------

@app.route("/download/notes/<filename>")
def download_notes(filename):
    return send_from_directory(NOTES_DIR, filename, as_attachment=True)


# ---------------- DOWNLOAD QUESTION PAPERS ----------------

@app.route("/download/question/<filename>")
def download_qp(filename):
    return send_from_directory(QP_DIR, filename, as_attachment=True)


# ---------------- IMPORTANT QUESTIONS IMAGE ----------------

@app.route("/download/important/<filename>")
def download_imp(filename):
    return send_from_directory(IMP_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    app.run(host="0.0.0.0", port=5000, debug=True)

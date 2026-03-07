from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "EduChat Backend Running"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")

    return jsonify({
        "reply": "Bot received: " + message
    })

if __name__ == "__main__":
    app.run()

    # NOTES
    if "notes" in message:

        return jsonify({
            "reply": "Download DBMS notes",
            "file": "/download/notes/dbms_notes.pdf"
        })


    # QUESTION PAPERS
    elif "question paper" in message:

        return jsonify({
            "reply": "Download DBMS Regulation 2017 Question Paper",
            "file": "/download/question/dbms_reg2017.pdf"
        })


    # IMPORTANT QUESTIONS
    elif "important question" in message:

        return jsonify({
            "reply": "Here are DBMS important questions",
            "image": "/download/important/dbms_imp.png"
        })


    else:

        return jsonify({
            "reply": "Ask for notes, question papers or important questions"
        })


# ---------------- DOWNLOAD NOTES ----------------

@app.route("/download/notes/<filename>")
def download_notes(filename):

    return send_from_directory(NOTES_DIR, filename, as_attachment=True)


# ---------------- DOWNLOAD QUESTION PAPER ----------------

@app.route("/download/question/<filename>")
def download_qp(filename):

    return send_from_directory(QP_DIR, filename, as_attachment=True)


# ---------------- IMPORTANT QUESTIONS IMAGE ----------------

@app.route("/download/important/<filename>")
def download_imp(filename):

    return send_from_directory(IMP_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (resets when container restarts)
notes = []

@app.route("/")
def home():
    return jsonify(message="MicroNotes API is running")

@app.route("/health")
def health():
    return jsonify(status="ok")

# Get all notes
@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

# Create a new note
@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()

    note = {
        "id": len(notes) + 1,
        "title": data.get("title"),
        "content": data.get("content")
    }

    notes.append(note)
    return jsonify(note), 201

# Get a single note
@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if note is None:
        return jsonify(error="Note not found"), 404
    return jsonify(note)

# Update a note
@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.get_json()
    note = next((n for n in notes if n["id"] == note_id), None)

    if note is None:
        return jsonify(error="Note not found"), 404

    note["title"] = data.get("title", note["title"])
    note["content"] = data.get("content", note["content"])

    return jsonify(note)

# Delete a note
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
    return jsonify(message="Deleted"), 200

DEFAULT_NOTES = [
    {"id": 1, "title": "First note", "content": "Deployed via CI/CD!"}
]

DEFAULT_NOTES = [
    {"id": 1, "title": "First note", "content": "Deployed via CI/CD!"}
]

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


import os

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "notes")

conn = psycopg2.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    dbname=DB_NAME
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder where uploaded files will be stored
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route to handle file uploads
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"message": "No selected file"}), 400

    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return jsonify({"message": f"File {file.filename} uploaded successfully!"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000)

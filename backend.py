from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"message": "No selected file"}), 400

    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return jsonify({"message": f"File {file.filename} uploaded successfully!"})

if __name__ == "__main__":
    app.run(debug=True)


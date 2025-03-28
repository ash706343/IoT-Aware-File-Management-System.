from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 5 * 1024 * 1024 * 1024  # 5GB limit

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        if "file" not in request.files:
            return jsonify({"message": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"message": "No selected file"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        # Save the file in chunks
        with open(file_path, "wb") as f:
            while True:
                chunk = file.stream.read(1024 * 1024)  # Read 1MB at a time
                if not chunk:
                    break
                f.write(chunk)

        return jsonify({"message": f"File '{file.filename}' uploaded successfully!"})

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)

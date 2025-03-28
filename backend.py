from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        print("❌ No file part in request")  # Debugging message
        return jsonify({"message": "No file part"}), 400

    file = request.files["file"]
    
    if file.filename == "":
        print("❌ No file selected")  # Debugging message
        return jsonify({"message": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    print(f"✅ File saved at {file_path}")  # Debugging message

    return jsonify({"message": f"File '{file.filename}' uploaded successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)

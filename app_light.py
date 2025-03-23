from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import uuid
import random

app = Flask(__name__)
CORS(app)  # これでCORS対応完了！
UPLOAD_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "🚀 Hello from app_light!"

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    filename = f"{uuid.uuid4()}.jpg"
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image_file.save(image_path)

    result_label = random.choice(["bird", "not_bird"])

    return jsonify({
        "result": result_label,
        "image_url": f"/static/results/{filename}"
    })

@app.route("/static/results/<path:filename>")
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

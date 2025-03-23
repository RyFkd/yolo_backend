from flask import Flask, request, jsonify, send_from_directory
import torch
from PIL import Image
import os
import uuid
import urllib.request

MODEL_PATH = "yolov5s.pt"

# 自動ダウンロード（Renderなどで初回自動取得）
if not os.path.exists(MODEL_PATH):
    print("📥 yolov5s.pt not found. Downloading from official source...")
    os.makedirs(os.path.dirname(MODEL_PATH) or ".", exist_ok=True)
    urllib.request.urlretrieve(
        "https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt",
        MODEL_PATH
    )
    print("✅ Download complete!")

app = Flask(__name__)
model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH, force_reload=True)
OUTPUT_DIR = "static/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    image_bytes = image_file.read()

    temp_filename = f"{uuid.uuid4()}.jpg"
    temp_path = os.path.join(OUTPUT_DIR, temp_filename)

    with open(temp_path, 'wb') as f:
        f.write(image_bytes)

    results = model(temp_path)
    results.save(save_dir=OUTPUT_DIR)

    result_filename = os.listdir(OUTPUT_DIR)[-1]
    image_url = f"/static/results/{result_filename}"

    result_label = next(iter(results.pandas().xyxy[0]['name']), 'none')

    return jsonify({
        'result': result_label,
        'image_url': image_url
    })

@app.route("/static/results/<path:filename>")
def serve_image(filename):
    return send_from_directory(OUTPUT_DIR, filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render uses PORT env variable
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify, send_from_directory
import torch
from PIL import Image
import os
import uuid

MODEL_PATH = "yolov5s.pt"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"{MODEL_PATH} が見つかりません。ローカルで実行する場合はDLしてください")

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

    # 一時ファイル名を作成
    temp_filename = f"{uuid.uuid4()}.jpg"
    temp_path = os.path.join(OUTPUT_DIR, temp_filename)

    # 保存
    with open(temp_path, 'wb') as f:
        f.write(image_bytes)

    # 推論実行
    results = model(temp_path)
    results.save(save_dir=OUTPUT_DIR)

    # バウンディングボックス画像のパス取得
    result_filename = os.listdir(OUTPUT_DIR)[-1]  # 最新のファイルを取得
    image_url = f"/static/results/{result_filename}"

    result_label = next(iter(results.pandas().xyxy[0]['name']), 'none')

    return jsonify({
        'result': result_label,
        'image_url': image_url
    })

# 静的ファイルを返す（Renderでも画像表示できるように）
@app.route("/static/results/<path:filename>")
def serve_image(filename):
    return send_from_directory(OUTPUT_DIR, filename)

# Render用のポート対応
if __name__ == "__main__":
    import os

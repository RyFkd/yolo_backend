import torch
import os
from PIL import Image

def detect_bird(image_path: str, output_dir: str = "output"):
    # モデルロード
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

    # 出力ディレクトリ作成
    os.makedirs(output_dir, exist_ok=True)

    # 推論実行
    results = model(image_path)

    # 結果を画像に描画（バウンディングボックスを重ねる）
    results.render()

    # 画像保存
    for i, im in enumerate(results.ims):
        im = Image.fromarray(im)
        output_path = os.path.join(output_dir, f"result_{i+1}.jpg")
        im.save(output_path)
        print(f"保存完了: {output_path}")

    # ラベル判定
    detected_labels = results.pandas().xyxy[0]['name'].tolist()
    if 'bird' in detected_labels:
        print("🟡 → 鳥を検出！（たぶんひよこ）")
    else:
        print("🔵 → 鳥はいません（たぶんひよこじゃない）")


if __name__ == "__main__":
    # ここにだけパスを書く！
    test_image_path = "test_images/sample.jpg"  # 公開用の相対パス
    detect_bird(test_image_path)

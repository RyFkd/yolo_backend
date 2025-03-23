from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from app_light!"

@app.route("/predict", methods=["POST"])
def predict():
    return jsonify({
        "result": "dummy_bird",
        "image_url": "/static/results/dummy.jpg"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

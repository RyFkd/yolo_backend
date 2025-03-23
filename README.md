
# Hiyoko Kanteishi (Chick Classification System)

---

## Executive Summary

The *Hiyoko Kanteishi* project is a cutting-edge poultry verification solution engineered to deliver deterministic evaluations on the presence or absence of chick-like avian entities in image-based data assets. Leveraging state-of-the-art computer vision infrastructure (YOLOv5), this system serves as a highly scalable framework for visual bird inference and classification workflows.

---

## Key Features

- Advanced object detection using YOLOv5 pre-trained weights
- Dynamic bounding box rendering on visual input
- Heuristic-based binary chick inference model (`bird` detection = "probably a chick")
- RESTful API integration via Flask
- Cross-platform Flutter-based front-end compatibility

---

## Infrastructure Overview

The system is divided into two operational layers:

1. **Front-end Client**  
   Developed in Flutter. Enables users to select image files and receive instant classification feedback via HTTP request-response interactions.

2. **Back-end API (Inference Layer)**  
   Implemented in Python using Flask and PyTorch. Accepts image uploads, performs YOLOv5 inference, and returns JSON-based results with optional annotated image output.

---

## Repository Structure

```
.
├── app.py                # Flask REST API endpoint for inference (/predict)
├── yolo_bird_check.py    # Standalone local test script
├── test_images/
│   └── sample.jpg        # Sample input image (AI-generated; royalty-free)
├── output/               # Rendered output images with bounding boxes
├── requirements.txt      # Python dependencies
└── runtime.txt           # Python runtime specification (Render compatible)
```

---

## Deployment & Execution

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. (Optional) Download YOLOv5 Weights

If not already present, the required model weights (`yolov5s.pt`) will be automatically downloaded via PyTorch Hub.

### 3. Execute Local Test

```bash
python yolo_bird_check.py
```

Annotated images will be exported to the `output/` directory. Console logs will indicate classification verdict.

---

## API Usage (Sample)

**Endpoint**: `POST /predict`  
**Form Data**: `image` (binary file)  
**Response Format**: JSON

```json
{
  "result": "bird",
  "image_url": "/static/output/result_1.jpg"
}
```

---

## License

This project is licensed under the terms of the MIT License.  
See the [LICENSE](LICENSE) file for full text.

---

## Legal Disclaimer

The term “chick” is interpreted loosely within the context of this repository and does not constitute a biological classification nor an agricultural-grade verification standard. All inferences are probabilistic and intended for entertainment and demonstration purposes only.

---

## Contact

For further inquiries, enterprise partnerships, or chick-related collaborations, please contact the repository maintainer through GitHub Issues or Discussions.

# Implementation Guide

## Prerequisites

- Python 3.10+ recommended
- Working webcam for Phase 1 and real-time capture experiments
- Internet access on the first EasyOCR setup if model files need to be downloaded

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Phase 1: Capture Images

```bash
python src/capture_images.py
```

Press **Space** to save a webcam frame and **Q** to quit. Images are written to `captured_images/`.

## Phase 2: Recognize a Plate

Use a captured image:

```bash
python src/plate_recognition.py captured_images/vehicle_001.jpg
```

The script preprocesses the image with OpenCV, sends it through EasyOCR, normalizes the recognized text, and records the result in `data/plates.csv`.

## Phase 3: Verify Access

Add synthetic or authorized test registration numbers to `data/registered_vehicles.csv`, then run:

```bash
python src/access_control.py captured_images/vehicle_001.jpg
```

The output is one of:

- `ACCESS: GRANTED`
- `ACCESS: DENIED`
- `ACCESS: UNVERIFIED`

## Troubleshooting

### Webcam does not open

Check that another application is not using the camera. If your system exposes the camera under another OpenCV index, change `VideoCapture(0)` to the appropriate index.

### EasyOCR setup is slow

EasyOCR may need to initialize/download its model data the first time it runs. Later executions normally reuse the local model cache.

### OCR is inaccurate

OCR quality depends heavily on image resolution, lighting, plate visibility, camera angle, and preprocessing. The current repository deliberately keeps the academic implementation simple rather than claiming universal recognition accuracy.

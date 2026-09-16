# Academic Project Documentation

## Title

**AI-Based Automatic Smart Security Number Plate Detection System**

## Purpose

The project explores an automated approach to vehicle identification and entry verification using image processing and OCR.

## Core Problem

Manual vehicle identification at an institutional entrance can require time and human attention. The proposed approach uses a camera to capture vehicle images, recognizes the registration number, and checks the recognized number against registered vehicle information.

## Objectives

- Capture vehicle images using a camera/webcam.
- Process images using computer vision techniques.
- Extract registration numbers using OCR.
- Store recognized vehicle information.
- Compare a recognized registration number with registered records.
- Provide an access-verification result.

## Technologies

| Technology | Role |
|---|---|
| Python | Main implementation language |
| OpenCV | Image capture and image processing |
| EasyOCR | Optical character recognition |
| CSV | Simple vehicle-data storage |
| Webcam | Image acquisition |

## Methodology

### 1. Image Capture

A webcam captures images of vehicles approaching the entrance. The captured frames can be stored for subsequent processing.

### 2. Image Processing and OCR

OpenCV is used to prepare the image for recognition. EasyOCR processes the image and produces text candidates. The implementation normalizes the recognized text before storing or comparing it.

### 3. Vehicle Verification

The recognized registration number is compared with the registered vehicle dataset. A matching record results in a `GRANTED` verification result; an unmatched or unreadable plate is reported as `DENIED` or `UNVERIFIED` rather than being treated as a successful identification.

## Repository Implementation

- `src/capture_images.py` implements webcam capture.
- `src/plate_recognition.py` implements basic OpenCV preprocessing, EasyOCR recognition, normalization, and CSV logging.
- `src/access_control.py` implements comparison with registered vehicle numbers.
- `data/registered_vehicles.csv` contains a synthetic sample entry for demonstration.

## Important Scope Note

This repository implements the software workflow represented by the documented academic project. It does **not** claim production-grade number-plate detection, guaranteed OCR accuracy, or physical gate-hardware control. Such capabilities require additional engineering, testing, calibration, security controls, privacy safeguards, and hardware integration.

## Evaluation Considerations

A complete academic evaluation should consider recognition accuracy, false recognition, missed recognition, lighting conditions, camera position, vehicle distance, plate visibility, and processing time. Results should be measured from an actual test dataset rather than invented in documentation.

## Privacy and Security

Vehicle registration numbers and images can be sensitive in real deployments. Use synthetic data in public repositories, remove personal information from demonstrations, and apply appropriate access controls and retention policies to real-world data.

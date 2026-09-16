# AI-Based Automatic Smart Security Number Plate Detection System

> An academic computer-vision project for identifying vehicle registration numbers and verifying vehicle access using a camera, OpenCV, EasyOCR, and registered vehicle data.

## 📌 About the Project

Vehicle entry points such as college and institutional gates often depend on security personnel to visually inspect and identify vehicles. This project explores how **computer vision and Optical Character Recognition (OCR)** can be used to make that process more systematic and reduce the need for manual number-plate checking.

The system captures an image of an approaching vehicle, processes the image, reads the visible registration number using OCR, and compares the recognized number with a list of registered vehicles. Based on that comparison, the system produces an access-verification result.

The project was developed as an **academic project** to demonstrate the practical use of image processing, OCR, and simple data management in an automated security application.

---

## 🎯 What Does the System Do?

At a high level, the system follows this process:

1. A camera/webcam captures an image of a vehicle.
2. OpenCV loads and preprocesses the image.
3. EasyOCR analyzes the image and extracts readable text.
4. The recognized text is normalized as a vehicle registration number.
5. Vehicle information can be stored in CSV format.
6. During verification, the recognized registration number is compared with registered vehicle records.
7. The system reports whether the vehicle is **GRANTED**, **DENIED**, or **UNVERIFIED**.

```text
                    VEHICLE APPROACHES
                           │
                           ▼
                    Camera / Webcam
                           │
                           ▼
                    Capture Image
                           │
                           ▼
                Image Processing (OpenCV)
                           │
                           ▼
                   Number Plate / Text
                           │
                           ▼
                      EasyOCR
                           │
                           ▼
               Recognized Registration No.
                           │
                           ▼
                Registered Vehicle Records
                           │
                           ▼
                       Comparison
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           MATCHED      NOT MATCHED   NOT READABLE
              │            │            │
              ▼            ▼            ▼
           GRANTED       DENIED     UNVERIFIED
```

---

## 🧠 Why This Project?

Manual vehicle verification can become repetitive when many vehicles enter an institution. A computer-vision-based system can assist security personnel by automatically extracting a vehicle's registration number from an image and checking it against registered records.

The project therefore combines three practical areas:

- **Computer Vision** — understanding and preparing images.
- **OCR** — converting text visible in an image into machine-readable text.
- **Data Verification** — checking recognized registration numbers against stored records.

The goal is not simply to read text from an image, but to demonstrate how those technologies can be connected into a complete vehicle-verification workflow.

---

## 🔬 Project Implementation

The implementation is divided into three main phases.

### Phase 1 — Vehicle Image Capture

The first phase uses a webcam to capture vehicle images. The captured frames can be saved and used as input for the recognition stage.

Implementation: `src/capture_images.py`

```bash
python src/capture_images.py
```

Press **Space** to capture an image and **Q** to quit.

---

### Phase 2 — Number Plate Recognition

The second phase processes a captured vehicle image.

**OpenCV** is used for basic image processing and preparation. **EasyOCR** is then used to recognize text from the image. The recognized text is normalized and stored in CSV format for later use.

Implementation: `src/plate_recognition.py`

```bash
python src/plate_recognition.py captured_images/vehicle_001.jpg
```

The recognition pipeline is approximately:

```text
Input Image
     ↓
OpenCV
     ↓
Grayscale / Resize
     ↓
EasyOCR
     ↓
Text Candidates
     ↓
Text Normalization
     ↓
Registration Number
     ↓
CSV Storage
```

> **Important:** The current implementation is an academic OCR workflow. It should not be interpreted as a production-grade Automatic Number Plate Recognition system with guaranteed plate localization and recognition accuracy.

---

### Phase 3 — Vehicle Access Verification

The third phase uses the recognized registration number to verify whether the vehicle exists in the registered vehicle dataset.

Implementation: `src/access_control.py`

```bash
python src/access_control.py captured_images/vehicle_001.jpg
```

The system compares the normalized registration number against:

`data/registered_vehicles.csv`

Possible results:

| Result | Meaning |
|---|---|
| **ACCESS: GRANTED** | Recognized registration number exists in the registered dataset. |
| **ACCESS: DENIED** | A registration number was recognized but it does not exist in the registered dataset. |
| **ACCESS: UNVERIFIED** | A usable registration number could not be recognized. |

---

## 🏗️ System Architecture

```text
┌──────────────────────┐
│     Camera/Webcam    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Image Acquisition  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   OpenCV Processing  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       EasyOCR        │
│  Text Recognition    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Registration Number  │
│    Normalization     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Registered Vehicle   │
│       Dataset        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Access Verification │
└──────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **OpenCV** | Image capture and image preprocessing |
| **EasyOCR** | Optical Character Recognition |
| **CSV** | Simple vehicle-record storage |
| **Webcam** | Vehicle image acquisition |

---

## 📂 Project Structure

```text
ai-smart-security-number-plate/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── capture_images.py
│   ├── plate_recognition.py
│   └── access_control.py
│
├── data/
│   ├── registered_vehicles.csv
│   └── README.md
│
├── dataset/
│   └── .gitkeep
│
├── captured_images/
│   └── .gitkeep
│
├── docs/
│   ├── README.md
│   ├── academic-project.md
│   └── implementation.md
│
└── tests/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abhiramk-10/ai-smart-security-number-plate.git
cd ai-smart-security-number-plate
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

EasyOCR may download its model files during its first initialization.

---

## ▶️ Running the Project

### Capture a vehicle image

```bash
python src/capture_images.py
```

### Recognize a registration number

```bash
python src/plate_recognition.py captured_images/vehicle_001.jpg
```

### Verify vehicle access

```bash
python src/access_control.py captured_images/vehicle_001.jpg
```

---

## 📊 Data Format

The verification dataset uses a simple CSV structure:

```csv
registration_number
KL00AA0000
```

The repository contains **synthetic demonstration data only**.

For a real deployment, vehicle records should be handled with appropriate privacy, security, access-control, and retention policies.

---

## ⚠️ Limitations

The current academic implementation has several limitations:

- OCR accuracy depends on image quality.
- Lighting and shadows can affect recognition.
- Camera angle and vehicle distance can affect results.
- A plate that is partially hidden may not be recognized correctly.
- OCR output can contain incorrect characters.
- The current implementation does not guarantee reliable plate localization in every image.
- CSV storage is suitable for demonstration but is not a replacement for a production database.
- Physical gate hardware is outside the scope of the current software implementation.

These limitations are important when distinguishing an academic prototype from a production security system.

---

## 🚀 Future Scope

The project can be extended in several directions:

- Dedicated number-plate detection using an object-detection model.
- Improved preprocessing for different lighting conditions.
- Better OCR post-processing and validation.
- Vehicle type classification.
- Image and vehicle-event logging.
- A proper database instead of CSV storage.
- Real-time monitoring interface.
- Improved handling of multiple vehicles.
- Physical gate-controller integration.
- Authentication and role-based administration.
- Performance and accuracy evaluation using a larger test dataset.

---

## 🎓 Academic Context

This repository is based on the academic project **AI-Based Automatic Smart Security Number Plate Detection System**.

The project demonstrates the integration of image acquisition, computer vision, OCR, data storage, and vehicle verification into an automated security workflow.

It is intended for **academic, educational, and demonstration purposes**. Additional engineering and validation would be required before using such a system in a real security environment.

---

## 🔐 Privacy Note

Vehicle registration numbers and vehicle images may contain sensitive information. Do not upload real vehicle-owner information, private photographs, or credentials to this public repository.

The example vehicle registration number included in this repository is synthetic.

---

## 👨‍💻 Author

**Abhiram K**  
B.Sc. Computer Science  
University of Calicut – NMSM Government College, Kalpetta

---

## 📚 Documentation

Detailed documentation is available in the [`docs/`](docs/) directory:

- [Academic Project Documentation](docs/academic-project.md)
- [Implementation Guide](docs/implementation.md)

---

## 📄 License

This project is currently maintained as an academic project. Add the license required by your institution or project supervisor before distributing it as an open-source project.

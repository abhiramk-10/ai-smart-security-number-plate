# AI-Based Automatic Smart Security Number Plate Detection System

> An academic computer-vision project for identifying vehicle registration numbers and verifying vehicle access using a camera, OpenCV, EasyOCR, and registered vehicle data.

## 📌 About the Project

Vehicle entry points such as college and institutional gates often depend on security personnel to visually inspect and identify vehicles. This project explores how **computer vision and Optical Character Recognition (OCR)** can be used to make that process more systematic and reduce the need for manual number-plate checking.

The system captures an image of an approaching vehicle, processes the image, reads the visible registration number using OCR, and compares the recognized number with a list of registered vehicles. Based on that comparison, the system produces an access-verification result.

The project was developed as an **academic project** to demonstrate the practical use of image processing, OCR, and simple data management in an automated security application.

## 🎯 What Does the System Do?

1. A camera/webcam captures an image of a vehicle.
2. OpenCV loads and preprocesses the image.
3. EasyOCR analyzes the image and extracts readable text.
4. The recognized text is normalized as a vehicle registration number.
5. Vehicle information can be stored in CSV format.
6. During verification, the recognized registration number is compared with registered vehicle records.
7. The system reports whether the vehicle is **GRANTED**, **DENIED**, or **UNVERIFIED**.

```text
Camera/Webcam → Capture Image → OpenCV → EasyOCR
                                      ↓
                           Registration Number
                                      ↓
                         Registered Vehicle Data
                                      ↓
                                Comparison
                           ↙         ↓         ↘
                      GRANTED     DENIED    UNVERIFIED
```

## 🧠 Why This Project?

Manual vehicle verification can become repetitive when many vehicles enter an institution. A computer-vision-based system can assist security personnel by automatically extracting a vehicle's registration number from an image and checking it against registered records.

The project combines three practical areas:

- **Computer Vision** — image capture and preprocessing.
- **OCR** — converting visible text in an image into machine-readable text.
- **Data Verification** — checking recognized registration numbers against stored records.

## 🔬 Project Implementation

### Phase 1 — Vehicle Image Capture

A webcam captures vehicle images. Captured frames can be saved and used as input for the recognition stage.

```bash
python src/capture_images.py
```

Press **Space** to capture an image and **Q** to quit.

### Phase 2 — Number Plate Recognition

OpenCV performs basic image preprocessing and EasyOCR recognizes text from the image. The recognized text is normalized and stored in CSV format.

```bash
python src/plate_recognition.py captured_images/vehicle_001.jpg
```

Pipeline:

```text
Input Image → OpenCV → EasyOCR → Text Normalization → Registration Number → CSV
```

> **Scope:** This is an academic OCR workflow. It is not claimed to be a production-grade ANPR system with guaranteed plate localization or recognition accuracy.

### Phase 3 — Vehicle Access Verification

The recognized registration number is compared with the registered vehicle dataset.

```bash
python src/access_control.py captured_images/vehicle_001.jpg
```

The system compares against `data/registered_vehicles.csv` and produces:

| Result | Meaning |
|---|---|
| **ACCESS: GRANTED** | Registration number exists in the registered dataset. |
| **ACCESS: DENIED** | Registration number was recognized but is not registered. |
| **ACCESS: UNVERIFIED** | A usable registration number could not be recognized. |

## 🏗️ System Architecture

```text
┌──────────────────────┐
│     Camera/Webcam    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Image Acquisition  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   OpenCV Processing  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│       EasyOCR        │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Registration Number  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Registered Vehicles  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Access Verification │
└──────────────────────┘
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **OpenCV** | Image capture and preprocessing |
| **EasyOCR** | Optical Character Recognition |
| **CSV** | Vehicle-record storage |
| **Webcam** | Image acquisition |

## 📂 Project Structure

```text
ai-smart-security-number-plate/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── capture_images.py
│   ├── plate_recognition.py
│   └── access_control.py
├── data/
│   ├── registered_vehicles.csv
│   └── README.md
├── dataset/
│   └── .gitkeep
├── captured_images/
│   └── .gitkeep
├── docs/
│   ├── README.md
│   ├── academic-project.md
│   └── implementation.md
└── tests/
```

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone https://github.com/abhiramk-10/ai-smart-security-number-plate.git
cd ai-smart-security-number-plate
```

## 2. Check Python

Python 3.10+ is recommended.

```bash
python --version
```

## 3. Create a virtual environment

### Windows CMD

```cmd
python -m venv .venv
.venv\Scripts\activate
```

If activation works, you should see `(.venv)` at the beginning of the terminal prompt.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install the required packages

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

EasyOCR may download its model files the first time it is initialized.

## 5. Capture a vehicle image

Connect a webcam and run:

```bash
python src/capture_images.py
```

A camera window will open.

- Press **Space** → capture and save an image.
- Press **Q** → quit.

Captured images are saved in:

```text
captured_images/
```

Example:

```text
captured_images/vehicle_001.jpg
```

## 6. Run number-plate OCR

Use one of the captured images:

```bash
python src/plate_recognition.py captured_images/vehicle_001.jpg
```

The program will:

```text
Image
  ↓
OpenCV preprocessing
  ↓
EasyOCR
  ↓
Recognized text
  ↓
Normalized registration number
  ↓
Saved to data/plates.csv
```

## 7. Run access verification

After you have a test image, run:

```bash
python src/access_control.py captured_images/vehicle_001.jpg
```

The program checks the recognized registration number against:

```text
data/registered_vehicles.csv
```

Example output:

```text
Recognized registration number: KL00AA0000
ACCESS: GRANTED
```

For an unregistered number:

```text
Recognized registration number: KL00XX1234
ACCESS: DENIED
```

If OCR cannot recognize a usable number:

```text
ACCESS: UNVERIFIED — no registration number recognized.
```

## 🧪 Complete Test Flow

For a complete demonstration, run the phases in this order:

```text
1. Start webcam
       ↓
2. Capture vehicle image
       ↓
3. Run OCR recognition
       ↓
4. Check registered vehicle data
       ↓
5. Run access verification
       ↓
6. Observe GRANTED / DENIED / UNVERIFIED
```

Commands:

```bash
python src/capture_images.py
python src/plate_recognition.py captured_images/vehicle_001.jpg
python src/access_control.py captured_images/vehicle_001.jpg
```

## 🔧 Troubleshooting

### `python` is not recognized

Check that Python is installed and available in PATH:

```bash
python --version
```

### Webcam does not open

Check that the webcam is connected and not being used by another application. The current implementation uses camera index `0`.

### EasyOCR installation/model setup takes time

The first EasyOCR run may require model initialization/download. Allow it to finish before testing recognition.

### OCR gives the wrong registration number

Recognition depends on image resolution, lighting, camera angle, plate visibility, and text quality. Try a clearer image with the plate facing the camera.

### Access is denied even though the plate looks correct

Check the normalized registration number stored in `data/registered_vehicles.csv`. The comparison is based on the recognized normalized text.

## 📊 Data Format

The verification dataset uses:

```csv
registration_number
KL00AA0000
```

The repository contains **synthetic demonstration data only**. Do not upload real vehicle-owner information or private vehicle images to this public repository.

## ⚠️ Limitations

- OCR accuracy depends on image quality.
- Lighting, shadows, camera angle, and vehicle distance affect recognition.
- Partially hidden plates may not be recognized correctly.
- OCR can produce incorrect characters.
- The current implementation does not guarantee reliable plate localization in every image.
- CSV storage is suitable for demonstration, not a production database.
- Physical gate hardware is outside the scope of the current software implementation.

## 🚀 Future Scope

- Dedicated number-plate detection using an object-detection model.
- Improved preprocessing for different lighting conditions.
- Better OCR post-processing and validation.
- Vehicle type classification.
- Image and vehicle-event logging.
- Database integration.
- Real-time monitoring interface.
- Multiple-vehicle handling.
- Physical gate-controller integration.
- Authentication and role-based administration.
- Evaluation using a larger test dataset.

## 🎓 Academic Context

This repository is based on the academic project **AI-Based Automatic Smart Security Number Plate Detection System**. It demonstrates the integration of image acquisition, computer vision, OCR, data storage, and vehicle verification into an automated security workflow.

It is intended for **academic, educational, and demonstration purposes**. Additional engineering, testing, privacy safeguards, security controls, and hardware validation would be required for real-world deployment.

## 🔐 Privacy Note

Vehicle registration numbers and vehicle images may contain sensitive information. Do not upload real vehicle-owner information, private photographs, credentials, or other sensitive data to this public repository.

## 👨‍💻 Author

**Abhiram K**  
B.Sc. Computer Science  
University of Calicut – NMSM Government College, Kalpetta

## 📚 Documentation

Detailed documentation is available in [`docs/`](docs/):

- [Academic Project Documentation](docs/academic-project.md)
- [Implementation Guide](docs/implementation.md)

## 📄 License

This project is maintained as an academic project. Add the license required by your institution or project supervisor before distributing it as an open-source project.

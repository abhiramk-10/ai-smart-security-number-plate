"""Phase 2: Recognize a number plate from an image using EasyOCR.

The academic documentation describes OpenCV preprocessing followed by
EasyOCR recognition and CSV storage. This starter implementation keeps
those responsibilities explicit and avoids claiming a detector that is not
present in the documented implementation.
"""

from pathlib import Path
import csv
import re
import sys

import cv2
import easyocr

DATA_FILE = Path("data/plates.csv")


def normalize_plate(text: str) -> str:
    """Keep alphanumeric characters and normalize OCR whitespace."""
    return re.sub(r"[^A-Z0-9]", "", text.upper())


def recognize_plate(image_path: Path, reader: easyocr.Reader) -> str:
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    # Basic OpenCV preprocessing for OCR input.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    results = reader.readtext(gray)
    candidates = [normalize_plate(text) for _, text, confidence in results if confidence > 0.20]
    candidates = [candidate for candidate in candidates if candidate]

    if not candidates:
        return ""

    return max(candidates, key=len)


def save_result(plate: str, image_path: Path) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_exists = DATA_FILE.exists()

    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["registration_number", "image"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"registration_number": plate, "image": str(image_path)})


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python src/plate_recognition.py <image_path>")
        raise SystemExit(2)

    image_path = Path(sys.argv[1])
    reader = easyocr.Reader(["en"], gpu=False)
    plate = recognize_plate(image_path, reader)

    if not plate:
        print("No readable registration number was found.")
        return

    print(f"Recognized registration number: {plate}")
    save_result(plate, image_path)
    print(f"Saved result to: {DATA_FILE}")


if __name__ == "__main__":
    main()

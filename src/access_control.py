"""Phase 3: Verify a recognized plate against registered vehicle data."""

from pathlib import Path
import csv
import sys

from plate_recognition import recognize_plate
import easyocr

DATA_FILE = Path("data/registered_vehicles.csv")


def registered_plates() -> set[str]:
    if not DATA_FILE.exists():
        return set()

    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        return {
            row["registration_number"].strip().upper()
            for row in csv.DictReader(file)
            if row.get("registration_number")
        }


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python src/access_control.py <image_path>")
        raise SystemExit(2)

    reader = easyocr.Reader(["en"], gpu=False)
    image_path = Path(sys.argv[1])
    plate = recognize_plate(image_path, reader)

    if not plate:
        print("ACCESS: UNVERIFIED — no registration number recognized.")
        return

    allowed = plate in registered_plates()
    print(f"Recognized registration number: {plate}")
    print("ACCESS: GRANTED" if allowed else "ACCESS: DENIED")


if __name__ == "__main__":
    main()

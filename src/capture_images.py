"""Phase 1: Capture vehicle images from a webcam.

This module follows the academic project's documented image-capture phase.
Press SPACE to save a frame and Q to quit.
"""

from pathlib import Path
import cv2

OUTPUT_DIR = Path("captured_images")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise RuntimeError("Could not open the default webcam (camera index 0).")

    image_number = 1
    print("Press SPACE to capture an image. Press Q to quit.")

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Unable to read a frame from the webcam.")
                break

            cv2.imshow("Vehicle Image Capture", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
            if key == 32:
                output_path = OUTPUT_DIR / f"vehicle_{image_number:03d}.jpg"
                if cv2.imwrite(str(output_path), frame):
                    print(f"Saved: {output_path}")
                    image_number += 1
                else:
                    print(f"Failed to save: {output_path}")
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

# Home Surveillance — Simple Face Detection

## Project Overview

This small Python project demonstrates a lightweight home-surveillance face-detection script using OpenCV's Haar Cascade classifier. It runs a simple detection routine (via `main.py`) using the provided `haarcascade_frontalface_default.xml` model and example images in the `images/` directory.

**Repository structure**
- `haarcascade_frontalface_default.xml`: Pre-trained Haar cascade classifier for frontal face detection.
- `main.py`: Main script to run detection.
- `images/`: Sample images used for testing and demonstration.
- `.gitignore`: Local files to ignore (e.g., virtual environments).

## Features

- Detects faces in images using Haar cascades.
- Works offline with bundled classifier file.
- Minimal dependencies; suitable as a learning/demo project.

## Requirements

- Python 3.8+ recommended
- OpenCV for Python

You can install the primary dependency with pip:

```bash
pip install opencv-python
```

If you plan to run in a virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install opencv-python
```

## Usage

Run the detection script from the project root:

```bash
python main.py
```

By default `main.py` is expected to load images from `images/` and run the face detector against them. If the script accepts paths or flags, inspect the top of `main.py` for usage notes.

Example workflow:

1. Add or replace photos in the `images/` directory.
2. Ensure the Haar cascade file `haarcascade_frontalface_default.xml` is present in the project root.
3. Run `python main.py` to process images and view detection output.

## How it works (brief)

1. `main.py` loads `haarcascade_frontalface_default.xml` into an OpenCV CascadeClassifier.
2. For each image in `images/`, it converts the image to grayscale and runs `detectMultiScale`.
3. Detected face regions can be drawn to the image and saved or displayed.

## Troubleshooting

- If you see import errors, ensure you installed `opencv-python` into the active Python environment.
- If no faces are detected, try tuning parameters passed to `detectMultiScale` (scaleFactor, minNeighbors, minSize) inside `main.py`.
- If `haarcascade_frontalface_default.xml` cannot be found, verify the file exists in the project root.

## Extending the project

- Add argument parsing to `main.py` to accept input paths and output directories.
- Add webcam/live-stream support using OpenCV's `VideoCapture`.
- Replace or augment Haar cascades with a DNN-based face detector for greater accuracy.



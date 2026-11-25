![Static Badge](https://img.shields.io/badge/Download-VSCode-hsl)
![Static Badge](https://img.shields.io/badge/Download-Python-hsl)
![Static Badge](https://img.shields.io/badge/Download-OpenCV-hsl)



# Real-Time Face, Eye, Mouth & Wrinkle Detection using OpenCV

## Overview

This project implements computer vision applications using Python and OpenCV to detect facial features and analyze facial images. It uses Haar Cascade Classifiers for face, eye, and mouth detection, along with image processing techniques for wrinkle detection.

The project demonstrates real-time object detection using webcam input and image-based analysis using OpenCV.

## Features

### 1. Face & Eye Detection
- Detects human faces in real-time using webcam input.
- Uses Haar Cascade Classifiers for face and eye detection.
- Draws bounding boxes around detected faces and eyes.
- Processes video frames in real-time using OpenCV.

### 2. Mouth Detection
- Detects mouths from live webcam video streams using a Haar Cascade Classifier.
- Applies grayscale conversion and image resizing for efficient processing.
- Identifies potential mouth openings based on detected region dimensions.
- Displays visual indicators for mouth detection.

### 3. Wrinkle Detection
- Detects potential facial wrinkle-like patterns from input images.
- Applies Gaussian Blur to reduce image noise.
- Uses Canny Edge Detection to identify edges and facial texture patterns.
- Applies thresholding and contour detection to identify candidate wrinkle regions.
- Draws bounding boxes around regions matching predefined geometric criteria.

## Technologies Used

- **Programming Language:** Python
- **Computer Vision Library:** OpenCV (cv2)
- **Numerical Computing:** NumPy
- **Object Detection:** Haar Cascade Classifiers
- **Image Processing:** Gaussian Blur, Grayscale Conversion, Canny Edge Detection, Thresholding, Contour Detection

## Project Structure

```text
Face-Detection-OpenCV/
│
├── face_eye_detection.py
├── mouth_detection.py
├── wrinkle_detection.py
│
├── haarcascade_frontalface_default.xml
├── haarcascade_eye_tree_eyeglasses.xml
├── haarcascade_mcs_mouth.xml
│
├── requirements.txt
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Face-Detection-OpenCV
```

### 2. Install Dependencies

```bash
pip install opencv-python numpy
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

### 3. Download Haar Cascade Files

Download the required Haar Cascade XML files and place them in the project directory.

- `haarcascade_frontalface_default.xml`
- `haarcascade_eye_tree_eyeglasses.xml`
- `haarcascade_mcs_mouth.xml`

Update the XML file paths in the Python scripts according to your local project directory.

## Execution

Run each application independently.

**Face & Eye Detection**
```bash
python face_eye_detection.py
```

**Mouth Detection**
```bash
python mouth_detection.py
```

**Wrinkle Detection**
```bash
python wrinkle_detection.py
```

For webcam-based applications, ensure that your webcam is connected and accessible.

Press `q` to exit the real-time detection windows.

## Working Methodology

### Face & Eye Detection
1. Capture video frames using the webcam.
2. Convert each frame into grayscale.
3. Apply Haar Cascade Classifiers to detect faces.
4. Extract facial regions of interest (ROI).
5. Detect eyes within the extracted facial regions.
6. Draw bounding boxes around detected features.

### Mouth Detection
1. Capture live webcam frames.
2. Resize frames to improve processing efficiency.
3. Convert frames into grayscale.
4. Apply the mouth Haar Cascade Classifier.
5. Analyze detected mouth regions using predefined dimensions.
6. Display detection results on the video window.

### Wrinkle Detection
1. Load the input facial image.
2. Convert the image into grayscale.
3. Apply Gaussian Blur to reduce noise.
4. Use Canny Edge Detection to identify facial edges.
5. Apply binary thresholding.
6. Extract contours from the thresholded image.
7. Filter contours using predefined width, height and aspect-ratio conditions.
8. Highlight potential wrinkle regions.

## Key Concepts Demonstrated

- Real-Time Video Processing
- Haar Cascade Object Detection
- Region of Interest (ROI) Extraction
- Image Preprocessing
- Edge Detection and Contour Analysis
- Grayscale Conversion
- Noise Reduction
- Webcam Integration

## Future Enhancements

- Improve mouth detection using facial landmarks.
- Implement more robust wrinkle detection using advanced image processing or deep learning.
- Integrate face, eye and mouth detection into a single application.
- Improve detection accuracy under different lighting conditions.
- Develop a graphical user interface for interactive image and video processing.

## Note

The mouth detection implementation uses detected region dimensions as a basic heuristic for identifying mouth openings. Similarly, wrinkle detection uses contour-based geometric filtering and may identify other facial edges as potential wrinkles. These implementations are intended for computer vision experimentation and learning.


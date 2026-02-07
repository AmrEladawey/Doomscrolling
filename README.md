# Doomscrolling

An nose-tracking application using computer vision to detect and track nose direction to detect Doomscrolling in real-time.

## Features
- **Webcam Integration**: Works with your device's webcam for live tracking
- **YOLOv8 Model Support**: Includes YOLOv8 nano and small pre-trained models for object detection

## Technology Stack
- **MediaPipe**: Face mesh and landmark detection
- **OpenCV**: Image processing and video capture
- **YOLO v8**: Object detection capabilities
- **Python**: Core programming language

## Project Structure
```
Doomscrolling/
├── yolov8n.pt          # YOLOv8 Nano model weights
├── yolov8s.pt          # YOLOv8 Small model weights
├── punishment.mp3      # Audio file
├── punishment.jpg      # Image file
└── README.md           # This file
```

## Installation
```bash
pip install opencv-python mediapipe numpy
```

## Usage
```bash
python Doomscrolling.py
```

The application will:
1. Access your webcam
2. Detect facial landmarks and iris position
3. Display real-time nose tracking visualization
4. Mirror the video horizontally for natural interaction

## How It Works
The application uses MediaPipe's Face Mesh solution with refined landmarks to:
- Identify nose center points (landmarks 468 and 473)
- Provide pixel-coordinate mapping for on-screen interaction

## Future Enhancements
- Add eye movement gesture recognition
- Integrate YOLO models for additional object detection
- Add real-time performance metrics

## License
MIT

## Author
AmrEladawey

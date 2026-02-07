# Doomscrolling

An eye-tracking application using computer vision to detect and track iris movement in real-time.

## Features
- **Iris Detection**: Real-time iris tracking using MediaPipe's face mesh detection
- **Eye Gaze Estimation**: Detects eye position and movement
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
├── IrisTracker.py      # Main iris tracking application
├── yolov8n.pt          # YOLOv8 Nano model weights
├── yolov8s.pt          # YOLOv8 Small model weights
├── video.mp4           # Sample video for testing
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
python IrisTracker.py
```

The application will:
1. Access your webcam
2. Detect facial landmarks and iris position
3. Display real-time iris tracking visualization
4. Mirror the video horizontally for natural interaction

## How It Works
The application uses MediaPipe's Face Mesh solution with refined landmarks to:
- Identify iris center points (landmarks 468 and 473)
- Track iris diameter using multiple detection points
- Calculate eye gaze direction and movement
- Provide pixel-coordinate mapping for on-screen interaction

## Future Enhancements
- Implement gaze-based UI interaction
- Add eye movement gesture recognition
- Integrate YOLO models for additional object detection
- Add real-time performance metrics

## License
MIT

## Author
AmrEladawey

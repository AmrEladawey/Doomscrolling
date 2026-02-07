import cv2
import mediapipe as mp
import numpy as np

# 1. SETUP MEDIAPIPE
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,  # <--- THIS IS KEY: Enables Iris and Lip detail
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# 2. DEFINE IRIS INDICES (From MediaPipe documentation)
# Left Eye
LEFT_IRIS_CENTER = 468
LEFT_IRIS_DIAMETER = [474, 475, 476, 477]

# Right Eye
RIGHT_IRIS_CENTER = 473
RIGHT_IRIS_DIAMETER = [478, 479, 480, 481]

# Open Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip frame horizontally for a mirror-like effect
    frame = cv2.flip(frame, 1)
    
    # Get frame dimensions
    h, w, _ = frame.shape
    
    # Convert BGR to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            
            # Helper function to convert normalized (0-1) to pixel coordinates
            def to_pixel(landmark_idx):
                if landmark_idx >= len(face_landmarks.landmark):
                    return None
                pt = face_landmarks.landmark[landmark_idx]
                return (int(pt.x * w), int(pt.y * h))

            # --- DRAW LEFT IRIS ---
            # Draw Center (Red)
            left_center = to_pixel(LEFT_IRIS_CENTER)
            if left_center:
                cv2.circle(frame, left_center, 3, (0, 0, 255), -1, cv2.LINE_AA)
                # Draw Vision Line (Blue line extending from iris center)
                end_point = (int(left_center[0] + 100), left_center[1])
                cv2.line(frame, left_center, end_point, (255, 0, 0), 2, cv2.LINE_AA)
            
            # Draw Boundary Points (Yellow)
            for idx in LEFT_IRIS_DIAMETER:
                pos = to_pixel(idx)
                if pos:
                    cv2.circle(frame, pos, 2, (0, 255, 255), -1, cv2.LINE_AA)

            # --- DRAW RIGHT IRIS ---
            # Draw Center (Red)
            right_center = to_pixel(RIGHT_IRIS_CENTER)
            if right_center:
                cv2.circle(frame, right_center, 3, (0, 0, 255), -1, cv2.LINE_AA)
                # Draw Vision Line (Blue line extending from iris center)
                end_point = (int(right_center[0] + 100), right_center[1])
                cv2.line(frame, right_center, end_point, (255, 0, 0), 2, cv2.LINE_AA)
            
            # Draw Boundary Points (Yellow)
            for idx in RIGHT_IRIS_DIAMETER:
                pos = to_pixel(idx)
                if pos:
                    cv2.circle(frame, pos, 2, (0, 255, 255), -1, cv2.LINE_AA)

    cv2.imshow('Iris Tracking', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import numpy as np

# Load Hand Template Image
template = cv2.imread('hand_template.png', cv2.IMREAD_UNCHANGED)
template_h, template_w = template.shape[:2]

# Initialize Camera
cap = cv2.VideoCapture(0)

# Mediapipe for Hand Detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7)

# Function to Overlay Transparent Template
def overlay_template(img, img_overlay, pos):
    x, y = pos
    alpha_overlay = img_overlay[:, :, 3] / 255.0
    alpha_background = 1.0 - alpha_overlay

    for c in range(0, 3):
        img[y:y+img_overlay.shape[0], x:x+img_overlay.shape[1], c] = (
            alpha_overlay * img_overlay[:, :, c] +
            alpha_background * img[y:y+img_overlay.shape[0], x:x+img_overlay.shape[1], c]
        )

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip Horizontally for a Mirror Effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Calculate the Center Position of the Screen for the Template Image
    center_x, center_y = w // 2 - template_w // 2, h // 2 - template_h // 2

    # Overlay Hand Template Image
    overlay_template(frame, template, (center_x, center_y))

    # Process Hand Detection
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw Hand Landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get Bounding Box for Hand
            x_coords = [lm.x for lm in hand_landmarks.landmark]
            y_coords = [lm.y for lm in hand_landmarks.landmark]
            x_min, x_max = int(min(x_coords) * w), int(max(x_coords) * w)
            y_min, y_max = int(min(y_coords) * h), int(max(y_coords) * h)

            # Bounding Box Check
            if (center_x < x_min < center_x + template_w and
                center_y < y_min < center_y + template_h and
                center_x < x_max < center_x + template_w and
                center_y < y_max < center_y + template_h):
                # Bounding Box is Within the Template Area
                video = cv2.VideoCapture('vid.mp4')
                while video.isOpened():
                    ret_vid, frame_vid = video.read()
                    if not ret_vid:
                        break
                    cv2.imshow('Hand Detection', frame_vid)
                    if cv2.waitKey(30) & 0xFF == 27:
                        break
                video.release()
    
    cv2.imshow('Hand Detection Overlay', frame)
    if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to Exit
        break

cap.release()
cv2.destroyAllWindows()
import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Variables
WIDTH, HEIGHT = 1280, 720
FOLDER_PATH = "ppt"

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

# Get the list of presentation images
pathImages = sorted(os.listdir(FOLDER_PATH), key=len)

# Project Variables
img_number = 0
hs, ws = int(120 * 1), int(213 * 1)
button_pressed = False
button_counter = 0
button_delay = 20
annotations = [[]]
annotation_number = -1
annotation_start = False
mode = "Slides" # Current mode: "Slides" or "Draw"

# Hand Detector - Increased detection confidence for better accuracy
detector = HandDetector(detectionCon=0.85, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    path_full_image = os.path.join(FOLDER_PATH, pathImages[img_number])
    img_current = cv2.imread(path_full_image)

    hands, img = detector.findHands(img, flipType=False)

    # Add mode display text on the webcam feed
    cv2.putText(img, f'Mode: {mode}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    if hands and not button_pressed:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        lmList = hand['lmList']
        
        # Constrain pointer values for drawing
        xVal = int(np.interp(lmList[8][0], [WIDTH // 2, WIDTH], [0, WIDTH]))
        yVal = int(np.interp(lmList[8][1], [150, HEIGHT - 150], [0, HEIGHT]))
        index_finger = xVal, yVal

        # Gesture: Open Palm (5 fingers) to switch modes
        if fingers == [1, 1, 1, 1, 1]:
            if mode == "Slides":
                mode = "Draw"
            else:
                mode = "Slides"
            button_pressed = True

        # Slide Control Mode Logic
        if mode == "Slides":
            if fingers == [1, 0, 0, 0, 0]: # Left (Thumb)
                if img_number > 0:
                    button_pressed = True
                    annotations = [[]]; annotation_number = -1
                    img_number -= 1
            elif fingers == [0, 0, 0, 0, 1]: # Right (Pinky)
                if img_number < len(pathImages) - 1:
                    button_pressed = True
                    annotations = [[]]; annotation_number = -1
                    img_number += 1
        
        # Drawing Control Mode Logic
        elif mode == "Draw":
            index_up = fingers[1] == 1
            middle_up = fingers[2] == 1
            ring_up = fingers[3] == 1

            if index_up and middle_up and ring_up: # Erase
                if annotations:
                    annotations.pop(-1)
                    if annotation_number >= 0: annotation_number -= 1
                    button_pressed = True
                annotation_start = False
            
            elif index_up and middle_up: # Pointer
                cv2.circle(img_current, index_finger, 12, (0, 0, 255), cv2.FILLED)
                annotation_start = False

            elif index_up: # Drawing
                if not annotation_start:
                    annotation_start = True
                    annotation_number += 1
                    annotations.append([])
                cv2.circle(img_current, index_finger, 12, (0, 0, 255), cv2.FILLED)
                annotations[annotation_number].append(index_finger)
            
            else:
                annotation_start = False

    # Debounce for button presses
    if button_pressed:
        button_counter += 1
        if button_counter > button_delay:
            button_counter = 0
            button_pressed = False

    # Draw annotations
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(img_current, annotations[i][j - 1], annotations[i][j], (0, 0, 200), 12)

    # Add webcam feed to slide
    img_small = cv2.resize(img, (ws, hs))
    h, w, _ = img_current.shape
    img_current[0:hs, w - ws:w] = img_small

    # --- CHANGE MADE HERE ---
    # We only need to show the final slide window
    cv2.imshow("Presentation Slides", img_current)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


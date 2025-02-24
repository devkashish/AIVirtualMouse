import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

index_x, index_y = 0, 0  # Initialize index finger coordinates
thumb_x, thumb_y = 0, 0  # Initialize thumb coordinates

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:  # Index finger
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=-1)
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                if id == 4:  # Thumb
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=-1)
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

        # Right-click detection
        if abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 20:
            pyautogui.rightClick()
            pyautogui.sleep(1)

        # Double-click detection
        elif abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 50:
            pyautogui.doubleClick()
            pyautogui.sleep(1)

        # Move the cursor
        else:
            pyautogui.moveTo(index_x, index_y)

        # Scroll functionality (Swipe up/down)
        if abs(index_y - thumb_y) > 150:
            if index_y < thumb_y:
                pyautogui.scroll(5)  # Scroll up
            else:
                pyautogui.scroll(-5)  # Scroll down

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()

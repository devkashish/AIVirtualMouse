 Virtual Mouse Using Hand Tracking

 Overview
This project implements a **virtual mouse** using **OpenCV**, **MediaPipe**, and **PyAutoGUI**. The program captures real-time video from a webcam, detects hand landmarks, and allows users to control the mouse pointer using hand gestures.

Features
- Hand Tracking: Uses MediaPipe's Hand Tracking module to detect hand landmarks.
- Mouse Movement: Moves the cursor based on the index finger's position.
- Clicking Mechanism: Performs a left-click when the thumb and index finger come close together.

Prerequisites
Ensure you have Python installed on your system. Install the required dependencies using:

```sh
pip install opencv-python mediapipe pyautogui
```

 How It Works
1. The webcam captures video frames.
2. The MediaPipe Hands model processes the frames to detect hand landmarks.
3. The index finger's position controls the cursor movement.
4. If the thumb and index finger are close together, a mouse click is triggered.

 Running the Project
To start the virtual mouse, run the following command:
python main.py


Key Functionalities
- Moving the cursor: Move your index finger in front of the camera.
- Clicking: Bring your thumb and index finger close together to simulate a left-click.
- Stopping the program: Press `Esc` to exit the program.

 Troubleshooting
- If you encounter `ModuleNotFoundError`, ensure all dependencies are installed using the pip command above.
- Make sure your webcam is connected and accessible by OpenCV.

Future Enhancements
- Implementing right-click and double-click gestures.
- Adding gesture-based scrolling functionality.
- Enhancing hand-tracking accuracy for better usability.

Credits
- OpenCV: For image processing and video capture.
- MediaPipe: For hand landmark detection.
- PyAutoGUI: For controlling the mouse pointer programmatically.


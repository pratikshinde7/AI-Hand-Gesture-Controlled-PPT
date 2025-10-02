Gesture-Controlled Presentation Tool 🖐️
This is a Python application that allows you to control a presentation slideshow using hand gestures captured from your webcam. You can navigate slides, draw annotations, and point to specific areas, all without touching your mouse or keyboard.

The project uses OpenCV for computer vision and the CVZone library for easy and accurate hand tracking.

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
</p>

Features
Gesture Navigation: Use simple hand gestures to move to the next or previous slide.

Interactive Drawing Mode: Switch to a drawing mode to annotate your slides in real-time.

Live Pointer: Use a gesture to create a virtual laser pointer to highlight parts of your presentation.

Intuitive Controls: A dedicated "Open Palm" gesture toggles between presentation and drawing modes, making the controls easy to manage.

Clean UI: The webcam feed is neatly overlaid on the corner of the presentation, providing a single, clean window.

How It Works
The application captures the live webcam feed and uses the cvzone library (powered by Google's MediaPipe) to detect a hand and its landmarks in real-time.

The code continuously checks which fingers are raised and uses this information to trigger actions. A mode-switching system, toggled by an open palm gesture, allows the same set of fingers to perform different actions (either controlling slides or drawing), making the system robust and easy to use.

Setup and Installation
Prepare Your Slides:

Create a folder named ppt in the main project directory.

Export your presentation slides as image files (e.g., 1.jpg, 2.png, 3.jpg, etc.) and place them inside the ppt folder.

Create a Virtual Environment:

python -m venv venv

Activate the Environment:

# On Windows
.\venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Run the Application:

python main.py

Gesture Controls
Switch Mode (Open Palm): Toggles between "Slides" and "Draw" mode.

In "Slides" Mode:

Thumb: Previous Slide

Pinky: Next Slide

In "Draw" Mode:

Index + Middle finger: Show Pointer

Index finger only: Draw on the slide

Index + Middle + Ring finger: Erase the last drawing
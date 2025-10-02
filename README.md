# Gesture-Controlled Presentation Tool 🖐️

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/MediaPipe-05A475?style=for-the-badge&logo=mediapipe&logoColor=white" />
</p>

<p align="center">
  <em>Control your presentations with the wave of a hand. This tool uses your webcam to translate hand gestures into presentation controls like navigating slides, pointing, and drawing.</em>
</p>

<p align="center">
  </p>

---

## ✨ Features

* 🖱️ **Mouse-Free Navigation:** Use simple hand gestures to move to the next or previous slide.
* ✍️ **Interactive Drawing Mode:** Switch to a drawing mode to annotate your slides in real-time.
* 🎯 **Live Pointer:** Use a gesture to create a virtual laser pointer to highlight parts of your presentation.
* ✋ **Intuitive Mode Switching:** A dedicated "Open Palm" gesture toggles between presentation and drawing modes.
* 🖼️ **Clean UI:** The webcam feed is neatly overlaid on the corner of the presentation, providing a single, clean window for your audience.

---

## 🛠️ Technology Stack

* **Python:** Core programming language.
* **OpenCV:** For all camera interactions and image/video processing.
* **CVZone:** A helper library to simplify hand tracking implementation.
* **MediaPipe:** The powerful, underlying Google framework that performs the actual hand landmark detection.
* **NumPy:** For fast numerical operations on image data.

---

## 🚀 Setup and Installation

1.  **Prepare Your Slides:**
    * Create a folder named `ppt` in the main project directory.
    * Export your presentation slides as image files (e.g., `1.jpg`, `2.png`) and place them inside the `ppt` folder.

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Environment:**
    ```bash
    # On Windows
    .\venv\Scripts\activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application:**
    ```bash
    python main.py
    ```

---

## ⚙️ How It Works

The application captures the live webcam feed and uses the CVZone library to detect a hand and its landmarks in real-time. The code continuously checks which fingers are raised to trigger actions. A mode-switching system, toggled by an open palm gesture, allows the same set of fingers to perform different actions (either controlling slides or drawing), making the system robust and easy to use.

---

## 🖐️ Gesture Controls

The control system is based on your hand gestures. Use the **Open Palm** gesture to switch between **Slides Mode** and **Draw Mode**.

| Gesture                               | Mode   | Action                  |
| ------------------------------------- | ------ | ----------------------- |
| ✋ Open Palm                           | Any    | Switch Mode             |
| 👍 Thumb                              | Slides | Previous Slide          |
| 🖐️ Pinky                              | Slides | Next Slide              |
| ☝️ Index Finger                       | Draw   | Draw on the slide       |
| ✌️ Index & Middle Fingers              | Draw   | Show Pointer            |
| 🖖 Index, Middle, & Ring Fingers      | Draw   | Erase the last drawing  |
```eof

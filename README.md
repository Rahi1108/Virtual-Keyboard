# 🖐️ Virtual Hand Gesture Keyboard (OpenCV + MediaPipe)

A real-time **virtual keyboard system** that allows you to type using **hand gestures captured via webcam**. This project uses computer vision to detect finger positions and simulate key presses — all displayed directly on the camera screen.

---

## 🚀 Features

* ✋ Hand tracking using MediaPipe
* ⌨️ Fully functional on-screen QWERTY keyboard
* 🤏 Pinch gesture (thumb + index finger) to click keys
* 🖥️ Real-time typing displayed on camera feed
* ⌫ Backspace support
* 🔤 Spacebar support
* 🎯 Smooth interaction with click delay handling

---

## 🧠 How It Works

* The webcam captures live video using OpenCV
* MediaPipe detects hand landmarks (fingers)
* The tip of the **index finger** acts as a cursor
* A **pinch gesture** (index + thumb close together) triggers a key press
* Pressed keys are added to a text string and displayed on screen

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone hhttps://github.com/Rahi1108/Virtual-Keyboard.git
   cd virtual-keyboard
   ```

2. Install dependencies:

   ```bash
   pip install opencv-python mediapipe numpy pynput
   ```

3. Run the program:

   ```bash
   python keyboard.py
   ```

---

## 🎮 Controls

| Gesture               | Action                |
| --------------------- | --------------------- |
| Move index finger     | Move cursor           |
| Pinch (thumb + index) | Click key             |
| Hover over key        | Highlight key         |
| Back button           | Delete last character |
| Space button          | Add space             |

---

## ⚙️ Customization

You can easily modify:

* Keyboard layout
* Button size and spacing
* Gesture sensitivity (pinch distance threshold)
* Screen resolution

---

## ⚠️ Limitations

* Requires good lighting for accurate detection
* May have slight delay depending on system performance
* Gesture precision depends on camera quality

---

## 🔮 Future Improvements

* 🔤 Uppercase/lowercase toggle
* 📱 Predictive text / autocomplete
* 😊 Emoji support
* 🧠 AI-based gesture recognition improvements
* 🎤 Voice + gesture hybrid input

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create your feature branch
3. Commit your changes
4. Open a pull request
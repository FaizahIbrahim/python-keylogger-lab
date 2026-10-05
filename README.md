<div align="center">

# 🔐 Python Keylogger Lab

### Beginner Cybersecurity Project

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Lab-111827?style=for-the-badge&logo=hackthebox&logoColor=9FEF00)
![pynput](https://img.shields.io/badge/pynput-Input%20Monitoring-6C63FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<br>

*A beginner cybersecurity lab exploring keyboard and mouse input monitoring in Python using `pynput`.*

</div>

---

## 🧠 About the Project

This project was created in a controlled environment to understand how keyboard and mouse input monitoring works in Python.

The lab explores how input events can be captured, processed, and stored locally while also examining keylogging techniques from a defensive cybersecurity perspective.

---

## 🎯 Learning Objectives

- Understand how Python handles keyboard and mouse input
- Learn how event listeners work
- Practice Python file handling
- Explore event-driven programming
- Understand how captured input can be stored locally
- Examine the security risks associated with keylogging techniques
- Learn basic defensive considerations for suspicious input-monitoring behaviour

---

## 🛠 Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/Python-Programming-3776AB?style=flat-square&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)

</div>

---

## ⚙️ How It Works

The project uses the `pynput` library to monitor keyboard and mouse events.

### Keyboard Listener

The keyboard listener:

- Detects key presses
- Converts key events into readable strings
- Handles special keys such as `Space`, `Shift`, and `Enter`
- Appends captured input to a local text file
- Runs continuously while the listener is active

### Mouse Listener

The mouse listener:

- Detects mouse movement
- Captures real-time `(x, y)` cursor coordinates
- Uses callback functions to respond to movement events

---

## 📁 Project Structure

```text
python-keylogger-lab/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── keyboard_listener.py
│
├── practice/
│   ├── file_handling.py
│   ├── input_controller.py
│   └── mouse_listener.py
│
└── docs/
    └── keycodes.md

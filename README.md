# Python Keylogger Lab

A beginner cybersecurity project exploring how keyboard input monitoring works in Python using the `pynput` library.

## Purpose

This project was created for educational purposes in a controlled environment to understand how keyboard and mouse event monitoring works and how keylogging techniques can be examined from a defensive cybersecurity perspective.

## Learning Objectives

- Understand how Python handles keyboard and mouse input
- Learn how keyboard event listeners work
- Practice Python file handling and event-driven programming
- Understand how captured input can be stored locally
- Explore the security risks associated with keylogging techniques
- Learn basic defensive considerations for detecting suspicious input-monitoring behaviour

## Technologies

- Python
- `pynput`
- Visual Studio Code
- Git & GitHub

## Project Status

✅ Completed

## How It Works

The project uses the `pynput` library to listen for keyboard events and process captured keystrokes.

The keyboard listener:

- Detects key presses
- Converts key events into readable strings
- Handles special keys such as Space and Enter
- Appends captured input to a local text file
- Runs continuously while the listener is active

Generated log files are excluded from the repository to prevent accidentally publishing captured personal input.

## Progress

### File Handling

- Practiced creating, opening, reading, writing, and appending files in Python
- Used `with open()` for automatic file closing and safer resource management
- Learned how file handling can be used to store captured keyboard events

### Input Control with `pynput`

- Installed and imported the `pynput` library
- Practiced programmatically controlling keyboard and mouse input
- Learned the difference between input controllers and input listeners

### Mouse Listener

- Used `pynput.mouse.Listener` to monitor mouse movement
- Captured real-time cursor coordinates
- Learned how callback functions respond to mouse events
- Used `listener.join()` to keep the listener running

### Keyboard Listener

- Used `pynput.keyboard.Listener` to capture keyboard events
- Converted key events into strings before storing them
- Processed special keys such as Space, Shift, and Enter
- Appended captured keyboard input to a local text file
- Practiced event-driven programming in Python

## Security Perspective

Keylogging demonstrates how software can monitor keyboard input at the user level.

From a defensive cybersecurity perspective, unexpected programs monitoring user input, suspicious background processes, and unexplained log files may be indicators worth investigating.

This project helped me understand both how keyboard monitoring works technically and why unauthorized keylogging presents a serious privacy and security risk.

## References

This project was developed while learning Python-based input monitoring concepts from publicly available educational resources and was expanded with my own documentation and security analysis.

Tutorial reference:
https://www.youtube.com/playlist?list=PLhTjy8cBISEoYoJd-zR8EV0NqDddAjK3m

## Ethical Use

This project is intended only for authorized educational testing and cybersecurity learning.

It should not be used to monitor devices, systems, or users without permission.

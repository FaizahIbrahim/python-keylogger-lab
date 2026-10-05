from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController

# (left to right, top to bottom)
# The top-left of the screen can be treated as (0, 0)

def control_mouse():
    mouse = MouseController()
    mouse.position = (100, 20)

def control_keyboard():
    keyboard = KeyboardController()
    keyboard.type("I am not typing this")

control_keyboard()

# Topics explored:
# - Controlling the mouse
# - Listening to the mouse
# - Controlling the keyboard
# - Listening to the keyboard

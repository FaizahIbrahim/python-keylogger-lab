from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController


def control_mouse():
    mouse = MouseController()
    mouse.position = (100, 20)


def control_keyboard():
    keyboard = KeyboardController()
    keyboard.type("I am not typing this")


control_keyboard()

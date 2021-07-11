import time
from pynput.keyboard import Key, Controller

def discord():
    keyboard = Controller()

    print("Opening Discord in 5 seconds")
    time.sleep(5) # The script starts after 5 seconds
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(0.5)
    keyboard.type("discord") 
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)

discord()
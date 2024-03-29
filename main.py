import threading,Arduino
from pynput import mouse
from pynput import keyboard

switch = False
arduino = Arduino.arduino()
clicks = 0
timer = None

def on_click( x, y, button, pressed):
    global clicks
    if switch and pressed:
        clicks = clicks + 1 

def check():
    global arduino, switch, timer, clicks
    if switch:
        print(clicks)
        if clicks < 6:
            arduino.shock()
        else:
            print("You did good")
        timer = threading.Timer(1.2, check)
        clicks = 0
        timer.start()

def end(key):
    global switch, timer
    if (key==keyboard.Key.f8):
        switch = not switch
        print("pause")
        if not timer.is_alive():
            timer = threading.Timer(2.0, check)
            timer.start()

timer = threading.Timer(1.0, check)


arduino.shock()
key_listener = keyboard.Listener(on_release=end)
key_listener.start()

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
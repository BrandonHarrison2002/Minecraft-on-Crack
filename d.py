import time, threading, random, math
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

button = Button.left
start_stop_key = KeyCode(char='[')
exit_key = KeyCode(char='=')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.trick = 0

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                if self.trick == random.randint(0, 3):
                    self.delay = random.uniform(0.07, 0.13)
                else:
                    self.delay = random.uniform(self.delay-0.005, self.delay+0.005)
                print(self.delay)
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(random.uniform(0.07, 0.13), button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if not click_thread.running:
            click_thread.start_clicking()
            print("Start")
    elif key == exit_key:
        print("Ended")
        click_thread.exit()
        listener.stop()

def on_release(key):
    if key == start_stop_key:
        print("Stoped")
        click_thread.stop_clicking()


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
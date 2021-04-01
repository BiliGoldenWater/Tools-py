from pykeyboard import PyKeyboard
from pymouse import PyMouse

import random
import time

mouse = PyMouse()
keyboard = PyKeyboard()
randint = random.randint


def do_once():
    delays = [1100, 1100, 1100, 1100, 1100, 1100, 1400]
    keyboard.tap_key('f')
    for x in range(7):
        time.sleep((delays[x] + randint(0, 200)) / 1000)
        mouse.click(1780 + randint(-30, 30), 980 + randint(-30, 30))
        # print(delays[x])


def run_sq(times, start_at):
    for x in range(start_at, times):
        do_once()
        print("done once ({}".format(x))
        time.sleep((10000 + randint(0, 300)) / 1000)


time.sleep(3)
run_sq(1000, 9)

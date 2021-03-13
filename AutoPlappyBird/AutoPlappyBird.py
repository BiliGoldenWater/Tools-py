import time
from PIL import ImageGrab

import win32api
import win32con
import win32gui
import win32ui


def window_capture(filename):
    hwnd = win32gui.GetDesktopWindow()
    dc = win32gui.GetDC(hwnd)
    win32gui.CreateCompatibleDC()


id = 0
time_ = []

while id < 50:
    beg = time.time_ns()
    # for i in range(1):
    #     window_capture("haha.jpg")
    image = ImageGrab.grab()
    # time.sleep(1)
    end = time.time_ns()
    # image.show()
    time_.append((end - beg) / 1000 / 1000)
    id += 1

print(time_)

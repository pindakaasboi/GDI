import win32gui
import win32con
import win32api
import random

hdc = win32gui.GetDC(0)
sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

while True:
    win32gui.BitBlt(hdc, random.randint(-20, 9), random.randint(-10, 9), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
    win32gui.BitBlt(hdc, random.randint(-20, 9), random.randint(-10, 9), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
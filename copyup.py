import win32gui
import win32con
import win32api
import time

while True:
    hdc = win32gui.GetDC(0)
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)
    win32gui.BitBlt(hdc, 10, 10, w, h, hdc, 12, 12, win32con.SRCCOPY)
    time.sleep(0.1)
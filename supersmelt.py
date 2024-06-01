import win32api
import win32con
import win32gui
import random

def main():
    while True:
        hdc = win32gui.GetDC(0)
        w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        rx = random.randint(0, w)
        win32gui.BitBlt(hdc, rx, 10, 100, h, hdc, rx, 0, win32con.SRCCOPY)
        win32gui.ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()
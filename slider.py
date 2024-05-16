import win32api
import win32gui
import random
import win32con
from win32gui import * #type: ignore
from win32gui import GetDesktopWindow, GetWindowDC, StretchBlt, BitBlt
from win32api import GetSystemMetrics
from math import * #type: ignore
hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(hwnd)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
x2 = GetSystemMetrics(0)

import math
import time
desktop = GetDesktopWindow()
left, top, right,bottom = GetWindowRect(desktop)

def redraw():
    RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN) #type: ignore

for i in range(100):
    hdc = GetDC(0)
    r = random.randint(0, 1)
    if r == 1:
        for _ in range(10):
            StretchBlt(hdc, 0, -50,x,y,hdc,0, 0, x,y, win32con.SRCCOPY);
            StretchBlt(hdc,0,-y + 50,x,y,hdc,0,0,x,y,win32con.SRCCOPY);

    else:
        for _ in range(10):
            StretchBlt(hdc,0,50,x,y,hdc,0, 0, x,y, win32con.SRCCOPY);
            StretchBlt(hdc, 0, -y + 50,x,y,hdc,0, 0, x,y, win32con.SRCCOPY);
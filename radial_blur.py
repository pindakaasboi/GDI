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
    memdc = CreateCompatibleDC(hdc)
    hbit = CreateCompatibleBitmap(hdc, x, y)
    sel = SelectObject(memdc, hbit) #type: ignore

    val = random.randint(1, 2)
    rateofturning = 30
    if val == 1:
        PlgBlt(memdc, ((left-rateofturning,top+rateofturning) , (right-rateofturning,top-rateofturning) , (left+rateofturning,bottom+rateofturning)) , hdc, 0, 0, x2, y, 0, 0, 0);


    if val == 2:
        PlgBlt(memdc, ((left-rateofturning, top+rateofturning), (right-rateofturning, top-rateofturning), (left+rateofturning, bottom+rateofturning)), hdc, 0, 0, x2, y, 0, 0, 0);


    AlphaBlend(hdc,random.randint(-10,-10), random.randint(-10, -10), x, y, memdc, 0, 0, x, y, (0, 0, 70, 0))

    SelectObject(memdc, sel) #type: ignore
    DeleteObject(sel)
    DeleteObject(hbit)
    DeleteDC(memdc)
    DeleteDC(hdc)


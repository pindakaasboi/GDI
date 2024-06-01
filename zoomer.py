from win32api import *
from win32gui import *
import win32con
import time
import random

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



def zoom_vertical():
    hdc = GetDC(0)


    for i in range(15):

        SetStretchBltMode(hdc, 4)
        StretchBlt(hdc, 0,0-10,x2+20,y,hdc,0,0,x2,y, win32con.SRCINVERT)
        StretchBlt(hdc, 0,0-10,x2+20,y,hdc,0,0,x2,y, win32con.SRCCOPY)
def zoom_horizontal():
    hdc = GetDC(0)


    for i in range(15):

        SetStretchBltMode(hdc, 4)
        StretchBlt(hdc, 0-10, 0, x2, y+20, hdc, 0, 0, x2, y, win32con.SRCINVERT)
        StretchBlt(hdc, 0-10, 0, x2, y+20, hdc, 0, 0, x2, y, win32con.SRCCOPY)


for i in range(100):
    zoom_vertical()
    redraw()
    zoom_horizontal()
    redraw()
import ctypes
import random
import win32api
import win32con
import win32gui

def main():
    while True:
        w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        hdc = win32gui.GetDC(0)
        
        hPen = win32gui.CreatePen(win32con.PS_SOLID, 2, win32api.RGB(255, 0, 0))
        hOldPen = win32gui.SelectObject(hdc, hPen)
        
        hBrush = win32gui.CreateSolidBrush(win32api.RGB(0, 0, 255))
        hOldBrush = win32gui.SelectObject(hdc, hBrush)
        
        vertices = [(random.randint(0, w), random.randint(0, h)) for _ in range(3)]
        win32gui.Polygon(hdc, vertices)
        
        win32gui.SelectObject(hdc, hOldBrush)
        win32gui.DeleteObject(hBrush)
        
        win32gui.SelectObject(hdc, hOldPen)
        win32gui.DeleteObject(hPen)
        
        win32gui.ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()
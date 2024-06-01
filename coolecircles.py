import ctypes
import random
import win32api
import win32con
import win32gui

def ci(x, y, w, h, hdc):
    hrgn = ctypes.windll.gdi32.CreateEllipticRgn(x, y, w+x, h+y)
    ctypes.windll.gdi32.SelectClipRgn(hdc, hrgn)
    ctypes.windll.gdi32.BitBlt(hdc, x, y, w, h, hdc, x, y, win32con.NOTSRCERASE)
    ctypes.windll.gdi32.DeleteObject(hrgn)

def main():
    desktop_hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetDC(desktop_hwnd)
    rect = win32gui.GetWindowRect(desktop_hwnd)
    w = rect[2] - rect[0] - 500
    h = rect[3] - rect[1] - 500
    
    try:
        while True:
            size = 1000
            x = random.randint(-size//2, w + size//2)
            y = random.randint(-size//2, h + size//2)
            
            for i in range(0, size, 100):
                ci(x - i//2, y - i//2, i, i, hdc)
                win32api.Sleep(25)
    finally:
        win32gui.ReleaseDC(desktop_hwnd, hdc)

if __name__ == "__main__":
    main()
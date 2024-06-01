import win32api
import win32con
import win32gui
import time

def main():
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)

    while True:
        hdc = win32gui.GetDC(0)
        
        win32gui.BitBlt(hdc, 0, 0, w, h, hdc, -30, 0, win32con.SRCCOPY)
        win32gui.BitBlt(hdc, 0, 0, w, h, hdc, w - 30, 0, win32con.SRCCOPY)
        win32gui.BitBlt(hdc, 0, 0, w, h, hdc, 0, -30, win32con.SRCCOPY)
        win32gui.BitBlt(hdc, 0, 0, w, h, hdc, 0, h - 30, win32con.SRCCOPY)
        
        win32gui.ReleaseDC(0, hdc)
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()

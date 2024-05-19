import win32api
import win32con
import win32gui
import math
import time
import random

def wavy_screen():
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)

    # Create a bitmap to hold the wavy screen
    hBitmap = win32gui.CreateCompatibleBitmap(hdc, sw, sh)
    memDC = win32gui.CreateCompatibleDC(hdc)
    win32gui.SelectObject(memDC, hBitmap)

    for y in range(sh):
        for x in range(sw):
            # Calculate the displacement of the sine wave for each pixel
            displacement = int(math.sin(x / 10) * 50 + math.cos(y / 10) * 50)
            # Calculate RGB values based on position in the sine wave
            r = int(127 * (1 + math.sin((x + displacement) / 10)) + 128)
            g = int(127 * (1 + math.sin((y + displacement) / 10)) + 128)
            b = int(127 * (1 - math.sin(((x + y) + displacement) / 20)) + 128)
            # Draw the wavy pixel
            win32gui.SetPixel(memDC, x, y, win32api.RGB(r, g, b))

    # Copy the wavy screen bitmap to the desktop
    win32gui.BitBlt(hdc, 0, 0, sw, sh, memDC, 0, 0, win32con.SRCCOPY)

    # Clean up
    win32gui.DeleteObject(hBitmap)
    win32gui.DeleteDC(memDC)
    win32gui.ReleaseDC(desktop, hdc)

def wavy_screen2():
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)

    # Create a bitmap to hold the wavy screen
    hBitmap = win32gui.CreateCompatibleBitmap(hdc, sw, sh)
    memDC = win32gui.CreateCompatibleDC(hdc)
    win32gui.SelectObject(memDC, hBitmap)

    for y in range(sh):
        for x in range(sw):
            # Calculate the displacement of the sine wave for each pixel
            displacement = int(math.sin(x / 10) * 50 + math.cos(y / 10) * 50)
            # Calculate RGB values based on position in the sine wave
            r = int(127 * (1 + math.sin(x / 10)) + 128)
            g = int(127 * (1 + math.sin(y / 10)) + 128)
            b = int(127 * (1 - math.sin((x + y) / 20)) + 128)
            # Draw the wavy pixel
            win32gui.SetPixel(memDC, x, y, win32api.RGB(r, g, b))

    # Copy the wavy screen bitmap to the desktop
    win32gui.BitBlt(hdc, 0, 0, sw, sh, memDC, 0, 0, win32con.SRCCOPY)

    # Clean up
    win32gui.DeleteObject(hBitmap)
    win32gui.DeleteDC(memDC)
    win32gui.ReleaseDC(desktop, hdc)

if __name__ == '__main__':
    while True:
        wavy_screen()
        time.sleep(2)
        wavy_screen2()

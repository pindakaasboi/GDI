import ctypes
import random
import time

user32 = ctypes.WinDLL('user32')
gdi32 = ctypes.WinDLL('gdi32')

GetSystemMetrics = user32.GetSystemMetrics
GetDC = user32.GetDC
ReleaseDC = user32.ReleaseDC
CreateSolidBrush = gdi32.CreateSolidBrush
DeleteObject = gdi32.DeleteObject
Ellipse = gdi32.Ellipse

SM_CXSCREEN = 0
SM_CYSCREEN = 1

def main():
    w = GetSystemMetrics(SM_CXSCREEN)
    h = GetSystemMetrics(SM_CYSCREEN)
    signX = 1
    signY = 1
    incrementor = 10
    x = 10
    y = 10
    while True:
        hdc = GetDC(0)
        x += incrementor * signX
        y += incrementor * signY
        top_x = 0 + x
        top_y = 0 + y
        bottom_x = 100 + x
        bottom_y = 100 + y
        brush = CreateSolidBrush(((random.randint(0, 255) << 16) | (random.randint(0, 255) << 8) | random.randint(0, 255)))
        Ellipse(hdc, top_x, top_y, bottom_x, bottom_y)
        if y >= GetSystemMetrics(SM_CYSCREEN):
            signY = -1
        if x >= GetSystemMetrics(SM_CXSCREEN):
            signX = -1
        if y == 0:
            signY = 1
        if x == 0:
            signX = 1
        time.sleep(0.01)
        DeleteObject(brush)
        ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()

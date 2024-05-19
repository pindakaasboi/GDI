import random
import ctypes

while True:
    hdc = ctypes.windll.user32.GetDC(0)
    x = ctypes.windll.user32.GetSystemMetrics(0)
    y = ctypes.windll.user32.GetSystemMetrics(1)
    w = ctypes.windll.user32.GetSystemMetrics(0)
    h = ctypes.windll.user32.GetSystemMetrics(1)
    ctypes.windll.gdi32.BitBlt(hdc, random.randint(0, 665), random.randint(0, 665), w, h, hdc, random.randint(0, 665), random.randint(0, 665), 0x00990066)
    ctypes.windll.user32.ReleaseDC(0, hdc)
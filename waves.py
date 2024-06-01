import ctypes
import math
import time

gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

def draw_sine_wave():
    hdc = user32.GetDC(0)
    angle = 0
    while True:
        for i in range(width + height):
            a = int(math.sin(angle) * 20)
            gdi32.BitBlt(hdc, 0, i, width, 1, hdc, a, i, 0xCC0020)
            angle += math.pi / 40
        user32.ReleaseDC(0, hdc)
        time.sleep(0.1)

if __name__ == "__main__":
    draw_sine_wave()
    
    
'''
import ctypes
import math
import time

gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

def draw_sine_wave():
    hdc = user32.GetDC(0)
    angle1 = 0
    angle2 = 0
    while True:
        for i in range(width + height):
            a1 = int(math.sin(angle1) * 20)
            a2 = int(math.sin(angle2) * 20)
            gdi32.BitBlt(hdc, a1, i, width, 1, hdc, 0, i, 0xCC0020)
            gdi32.BitBlt(hdc, i, a2, 1, height, hdc, i, 0, 0xCC0020)
            angle1 += math.pi / 40
            angle2 += math.pi / 40
        user32.ReleaseDC(0, hdc)
        time.sleep(0.1)

if __name__ == "__main__":
    draw_sine_wave()
'''
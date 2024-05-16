from win32api import *
from win32gui import *
import time
import random

def main():
    texts = ["Hello World", "Hello World", "Hello World"]
    num_texts = len(texts)
    coords = [(0, 0), (100, 50), (200, 100)]  # Initial positions for each text
    signs = [(1, 1), (-1, 1), (1, -1)]
    incrementor = 30

    while True:
        for i in range(num_texts):
            x, y = coords[i]
            signX, signY = signs[i]
            w, h, hdc = GetSystemMetrics(0), GetSystemMetrics(1), GetDC(0)
            text = texts[i]
            color = random.randint(0, 255) | (random.randint(0, 255) << 8) | (random.randint(0, 255) << 16)
            SetTextColor(hdc, color)
            SetBkMode(hdc, 0)
            ExtTextOut(hdc, x, y, 0, None, text, None)
            x += incrementor * signX
            y += incrementor * signY
            if y >= h or y <= 0:
                signs[i] = (signs[i][0], -signs[i][1])
            if x >= w or x <= 0:
                signs[i] = (-signs[i][0], signs[i][1])
            coords[i] = (x, y)
            time.sleep(0.01)
            ReleaseDC(0, hdc)

main()

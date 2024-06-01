import ctypes
import random
import time

# Windows API fonksiyonlarını yükleyelim
user32 = ctypes.WinDLL('user32')
gdi32 = ctypes.WinDLL('gdi32')

# Windows API fonksiyonlarının prototiplerini tanımlayalım
GetSystemMetrics = user32.GetSystemMetrics
GetDC = user32.GetDC
ReleaseDC = user32.ReleaseDC
BitBlt = gdi32.BitBlt

# Ekran genişliği ve yüksekliği için sabitleri tanımlayalım
SM_CXSCREEN = 0
SM_CYSCREEN = 1

# BitBlt fonksiyonundaki sabitler
SRCAND = 0x008800C6

def main():
    while True:
        hdc = GetDC(0)
        w = GetSystemMetrics(SM_CXSCREEN)
        h = GetSystemMetrics(SM_CYSCREEN)
        BitBlt(hdc, random.randint(0, 1), random.randint(0, 1), w, h, hdc, random.randint(0, 1), random.randint(0, 1), SRCAND)
        ReleaseDC(0, hdc)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
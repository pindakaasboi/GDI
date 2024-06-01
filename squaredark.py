import ctypes
import random

# Windows API fonksiyonlarını yükleyelim
user32 = ctypes.WinDLL('user32')
gdi32 = ctypes.WinDLL('gdi32')

# Windows API fonksiyonlarının prototiplerini tanımlayalım
GetSystemMetrics = user32.GetSystemMetrics
GetDC = user32.GetDC
ReleaseDC = user32.ReleaseDC
CreateSolidBrush = gdi32.CreateSolidBrush
BitBlt = gdi32.BitBlt
DeleteObject = gdi32.DeleteObject
SelectObject = gdi32.SelectObject

# Ekran genişliği ve yüksekliği için sabitleri tanımlayalım
SM_CXSCREEN = 0
SM_CYSCREEN = 1

def main():
    w = GetSystemMetrics(SM_CXSCREEN)
    h = GetSystemMetrics(SM_CYSCREEN)
    while True:
        hdc = GetDC(0)
        for i in range(10):
            x = random.randint(0, w)
            y = random.randint(0, h)
            brush = CreateSolidBrush(((random.randint(0, 255) << 16) | (random.randint(0, 255) << 8) | random.randint(0, 255)))
            SelectObject(hdc, brush)
            BitBlt(hdc, x, y, 30, 30, hdc, x - 30, y - 30, 0x00C000CA)  # Raster Operation Code'u (ROP) buraya yazılmalı
            DeleteObject(brush)
        ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()
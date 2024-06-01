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

def main():
    while True:
        hdc = GetDC(0)
        w = GetSystemMetrics(SM_CXSCREEN)
        h = GetSystemMetrics(SM_CYSCREEN)
        x = random.randint(0, w)
        BitBlt(hdc, x, 1, 10, h, hdc, x, 0, 0x00330008)  # NOTSRCCOPY yerine kullanılan Raster Operation Code (ROP)
        time.sleep(0.002)  # 2 milisaniye bekletme
        ReleaseDC(0, hdc)

if __name__ == "__main__":
    main()

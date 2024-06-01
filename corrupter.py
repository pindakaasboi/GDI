import ctypes
import random
import time

# Windows API fonksiyonlarını yükleyelim
user32 = ctypes.WinDLL('user32')
gdi32 = ctypes.WinDLL('gdi32')

# Windows API fonksiyonlarının prototiplerini tanımlayalım
GetDC = user32.GetDC
GetSystemMetrics = user32.GetSystemMetrics
ReleaseDC = user32.ReleaseDC
BitBlt = gdi32.BitBlt

# Ekran genişliği ve yüksekliği için sabitleri tanımlayalım
SM_CXSCREEN = 0
SM_CYSCREEN = 1

def longtaskbar():
    while True:
        hdc = GetDC(0)
        w = GetSystemMetrics(SM_CXSCREEN)
        h = GetSystemMetrics(SM_CYSCREEN)
        BitBlt(hdc, random.randint(0, 222), random.randint(0, 222), w, h, hdc, random.randint(0, 222), random.randint(0, 222), 0x00330008)  # NOTSRCERASE yerine 0x00330008 kullanıyoruz
        ReleaseDC(0, hdc)
        time.sleep(0.01)
        
longtaskbar()
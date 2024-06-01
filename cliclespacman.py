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
CreateSolidBrush = gdi32.CreateSolidBrush
SelectObject = gdi32.SelectObject
Pie = gdi32.Pie
DeleteObject = gdi32.DeleteObject

# Ekran genişliği ve yüksekliği için sabitleri tanımlayalım
SM_CXSCREEN = 0
SM_CYSCREEN = 1

# RGB değeri oluşturmak için fonksiyon
def RGB(r, g, b):
    return r | (g << 8) | (b << 16)

def main():
    while True:
        hdc = GetDC(0)
        x = GetSystemMetrics(SM_CXSCREEN)
        y = GetSystemMetrics(SM_CYSCREEN)
        brush = CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        SelectObject(hdc, brush)
        Pie(hdc, random.randint(0, x), random.randint(0, y), random.randint(0, x), random.randint(0, y),
            random.randint(0, x), random.randint(0, y), random.randint(0, x), random.randint(0, y))
        DeleteObject(brush)
        ReleaseDC(None, hdc)
        time.sleep(0.01)

if __name__ == "__main__":
    main()

import win32gui
import win32con
import ctypes
import random

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


x = y = 0
while True:
    win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_WARNING)) # Change IDI_ERROR to something else to change the icon being displayed
    x = random.randint(0, 2000)
    if x >= w:
        y = random.randint(0, 2000)
        x = 0
    if y >= h:
        x = y = random.randint(0, 2000)
    win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_ERROR)) # Change IDI_ERROR to something else to change the icon being displayed
    x = random.randint(0, 2000)
    if x >= w:
        y = random.randint(0, 2000)
        x = 0
    if y >= h:
        x = y = random.randint(0, 2000)
    win32gui.DrawIcon(hdc, x , y , win32gui.LoadIcon(None, win32con.IDI_QUESTION)) # Change IDI_ERROR to something else to change the icon being displayed
    x = random.randint(0, 2000)
    if x >= w:
        y = random.randint(0, 2000)
        x = 0

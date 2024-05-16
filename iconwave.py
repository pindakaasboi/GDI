import win32gui
import win32con
import ctypes
import time
import math

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

# Wave parameters
amplitude = 50  # Height of the wave
frequency = 0.01  # Wave frequency

x = 0
while True:
    y = int((h // 2) + amplitude * math.sin(frequency * x))
    win32gui.DrawIcon(hdc, x, y, win32gui.LoadIcon(None, win32con.IDI_ERROR))
    
    x += 5  # Move to the right
    if x >= w:
        x = 0  # Reset to the left side of the screen
    
    time.sleep(0.05)  # Control the speed of the movement

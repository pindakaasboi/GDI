import win32gui
import win32con
import ctypes
import random
import time
from win32api import GetSystemMetrics

# Initialize and set DPI awareness
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

# Get device context for the entire screen
hdc = win32gui.GetDC(0)

# Get screen width and height
screen_width =  GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

while True:
    # Draw a warning icon at a random position
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    win32gui.DrawIcon(hdc, x, y, win32gui.LoadIcon(None, win32con.IDI_WARNING))
    time.sleep(0.1)  # Short delay

    # Draw an error icon at a random position
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    win32gui.DrawIcon(hdc, x, y, win32gui.LoadIcon(None, win32con.IDI_ERROR))
    time.sleep(0.1)  # Short delay

    # Draw a question icon at a random position
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    win32gui.DrawIcon(hdc, x, y, win32gui.LoadIcon(None, win32con.IDI_QUESTION))
    time.sleep(0.1)  # Short delay

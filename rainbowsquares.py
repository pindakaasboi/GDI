import win32gui
import win32con
import win32api
import random

def draw_square(hdc, x, y, size, color):
    left = x - size // 2
    top = y - size // 2
    right = x + size // 2
    bottom = y + size // 2

    brush_color = win32api.RGB(color[0], color[1], color[2])
    brush = win32gui.CreateSolidBrush(brush_color)
    win32gui.SelectObject(hdc, brush)
    win32gui.Rectangle(hdc, left, top, right, bottom)
    win32gui.DeleteObject(brush)

def main():
    while True:
        hwnd = win32gui.GetDesktopWindow()
        hdc = win32gui.GetWindowDC(hwnd)

        desktop_rect = win32gui.GetWindowRect(hwnd)
        desktop_width = desktop_rect[2] - desktop_rect[0]
        desktop_height = desktop_rect[3] - desktop_rect[1]

        x = random.randint(0, desktop_width)
        y = random.randint(0, desktop_height)
        size = random.randint(20, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw_square(hdc, x, y, size, color)

        win32gui.ReleaseDC(hwnd, hdc)

if __name__ == "__main__":
    main()

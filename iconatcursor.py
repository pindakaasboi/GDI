import ctypes
import win32gui
import win32con
import threading
import time

def showiconatc():
    while True:
        # Get the cursor position
        cpos = win32gui.GetCursorPos()

        # Get the device context for the entire screen
        hdc = win32gui.GetDC(0)

        # Load the icon (IDI_INFORMATION, for example)
        icon = win32gui.LoadIcon(None, win32con.IDI_WARNING)

        # Draw the icon at the cursor position
        win32gui.DrawIcon(hdc, cpos[0], cpos[1], icon)

        # Release the device context
        win32gui.ReleaseDC(0, hdc)


iconatc_thread = threading.Thread(target=showiconatc)
iconatc_thread.daemon = True  # Ensure the thread exits when the main program does
iconatc_thread.start()
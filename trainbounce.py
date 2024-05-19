from win32api import *  #type: ignore
from win32con import *  #type: ignore
from win32gui import *  #type: ignore
import math
from time import sleep

def calculate_position(t, initial_pos, initial_velocity, gravity):
    """
    Calculate the position of the "ball" at time t using projectile motion equations.
    """
    x0, y0 = initial_pos
    vx0, vy0 = initial_velocity
    x = x0 + vx0 * t
    y = y0 + vy0 * t - 0.5 * gravity * t**2
    return int(x), int(y)

def main():
    w, h = GetSystemMetrics(0), GetSystemMetrics(1)  # Screen width and height

    # Initial position and velocity
    initial_pos = (50, 50)
    initial_velocity = (20, -20)  # Initial horizontal and vertical velocities
    gravity = 9.8  # Acceleration due to gravity (m/s^2)

    try:            #type: ignore
        t = 0  # Initial time
        while True:
            hdc = GetDC(0)  # Get device context for the screen
            x, y = calculate_position(t, initial_pos, initial_velocity, gravity)
            if y < 0:  # If ball hits the top edge, reverse the vertical velocity
                initial_velocity = (initial_velocity[0], -initial_velocity[1])
                t = 0  # Reset time
            BitBlt(hdc, x, y, w, h, hdc, 0, 0, SRCCOPY)
            ReleaseDC(0, hdc)

            t += 0.2  # Increment time
            sleep(0.05)  # Small delay to control the speed of the animation

    except KeyboardInterrupt:
        pass

main()

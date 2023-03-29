import pyautogui
import random
import time

def random_move_and_click(interval=120):
    while True:
        # Get the screen size
        screen_width, screen_height = pyautogui.size()

        # Generate random x and y coordinates within the screen
        random_x = random.randint(0, screen_width - 1)
        random_y = random.randint(0, screen_height - 1)

        # Move the mouse to the random position
        pyautogui.moveTo(random_x, random_y, duration=0.5)

        # Click the left mouse button
        pyautogui.click()

        # Wait for the specified interval (in seconds) before the next action
        time.sleep(interval)

if __name__ == "__main__":
    # Set the interval to 2 minutes (120 seconds)
    interval = 120
    random_move_and_click(interval)

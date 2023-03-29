import pyautogui
import random
import time

def random_move_and_click(interval=120):
    while True:
        screen_width, screen_height = pyautogui.size()

        random_x = random.randint(0, screen_width - 1)
        random_y = random.randint(0, screen_height - 1)

        pyautogui.moveTo(random_x, random_y, duration=0.5)

        pyautogui.click()

        time.sleep(interval)

if __name__ == "__main__":
    interval = 120
    random_move_and_click(interval)

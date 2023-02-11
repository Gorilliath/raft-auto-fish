import keyboard
import pyautogui
import time
import win32api
import win32con


def left_click(release_delay=0):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    if release_delay > 0:
        time.sleep(release_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('esc') == False:
    time.sleep(1)
    if pyautogui.locateOnScreen('caught-1920-1080.png', grayscale=True, confidence=0.9) != None:
        left_click()
        time.sleep(1)
        left_click(release_delay=1)

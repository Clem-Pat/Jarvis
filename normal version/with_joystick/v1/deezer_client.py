import pygetwindow as gw
import keyboard
import time
import os

class Deezer_Client():
    def __init__(self, open=False):
        self.path = os.path.dirname(os.path.abspath(__file__))
        if open : self.open_deezer()

    def open_deezer(self):
        def press_and_release(s):
            keyboard.press(s)
            keyboard.release(s)

        def press_and_release_2(s1,s2):
            keyboard.press(s1)
            keyboard.press(s2)
            time.sleep(0.1)
            keyboard.release(s2)
            keyboard.release(s1)

        chrome_window_was_created = False
        windows_names = [w[-13:] for w in list(gw.getAllTitles())]
        if 'Google Chrome' not in windows_names:
            press_and_release_2('cmd', 's')
            time.sleep(0.2)
            press_and_release_2('c', 'h')
            press_and_release('enter')
            time.sleep(1)
            chrome_window_was_created = True
        n = 0
        while str(gw.getActiveWindow())[-15:-2] != 'Google Chrome' and not keyboard.is_pressed('ctrl') and n<10:
            press_and_release_2('alt', 'tab')
            n += 1
        n=0
        while str(gw.getActiveWindow())[-24:-2] != 'Deezer - Google Chrome' and not keyboard.is_pressed('ctrl') and n<10:
            press_and_release_2('ctrl', 'tab')
            n += 1
        if n == 10:
            if not chrome_window_was_created: press_and_release_2('ctrl', 't')
            time.sleep(0.01)
            press_and_release('d')
            time.sleep(0.5)
            press_and_release('e')
            time.sleep(0.5)
            press_and_release('enter')
        print('"Deezer - Google Chrome" is open')

    def play_pause(self):
        keyboard.press_and_release('space')

    def next_track(self):
        keyboard.press_and_release('maj+droite')

    def previous_track(self):
        keyboard.press_and_release('maj+gauche')

    def get_forward_in_track(self):
        keyboard.press_and_release('ctrl_l+droite')

    def get_backward_in_track(self):
        keyboard.press_and_release('ctrl_l+gauche')

import keyboard
import time
import os

class Deezer_Client():
    def __init__(self, open=False):
        self.path = os.path.dirname(os.path.abspath(__file__))
        if open : self.open_deezer()

    def open_deezer(self):
        os.system('start Chrome https://www.deezer.com/en/')
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

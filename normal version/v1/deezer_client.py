
import time
import os
import pandas as pd
import keyboard

class Deezer_Client():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        wallet = pd.read_csv(f'{self.path}/wallet.txt', sep='=', index_col=0, squeeze=True, header=None)
        self.username, self.pw = wallet['username'], wallet['pw']

    def open_and_login(self, login=False):
        pass

    def play_playlist(self, playlist='Rock Chill'):
        pass

    def play_pause(self):
        keyboard.press_and_release('space')

    def next_track(self):
        keyboard.press_and_release('maj+droite')

    def previous_track(self):
        keyboard.press_and_release('maj+gauche')

    def volume_up(self):
        keyboard.press_and_release('f8')

    def volume_down(self):
        keyboard.press_and_release('f7')

    def mute(self):
        keyboard.press_and_release('f6')

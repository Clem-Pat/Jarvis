
import time
import os
import pandas as pd
import keyboard

class Deezer_Client():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        wallet = pd.read_csv(f'{self.path}/secret.txt', sep='=', index_col=0, squeeze=True, header=None)
        self.username, self.pw = wallet['username'], wallet['pw']

    def open_and_login(self, login=False):
        pass

    def play_playlist(self, playlist='Rock Chill', shuffle=True):
        pass

    def next_track(self):
        pass

    def previous_track(self):
        pass

    def play_pause(self):
        pass

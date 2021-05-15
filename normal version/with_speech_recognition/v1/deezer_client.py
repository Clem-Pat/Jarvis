import time
import os
import pandas as pd
import keyboard
from pynput.keyboard import Key
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

class Deezer_Client():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        wallet = pd.read_csv(f'{self.path}/wallet.txt', sep='=', index_col=0, squeeze=True, header=None)
        self.username, self.pw = wallet['username'], wallet['pw']

    def open_and_login(self, login=False):
        pass

    def play_playlist(self, playlist='Rock Chill'):
        pass

    def play_pause(self, jarvis):
        keyboard.press_and_release('space')

    def next_track(self, jarvis):
        keyboard.press_and_release('maj+droite')

    def previous_track(self, jarvis):
        keyboard.press_and_release('maj+gauche')

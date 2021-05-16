import os
import keyboard

class Deezer_Client():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

    def play_pause(self, jarvis):
        keyboard.press_and_release('space')

    def next_track(self, jarvis):
        keyboard.press_and_release('maj+droite')

    def previous_track(self, jarvis):
        keyboard.press_and_release('maj+gauche')

import keyboard
import time
import os
import pygame
from pynput.keyboard import Key, Controller

# TODO : pygame cling

class Deezer_Client():
    def __init__(self, jarvis, open=False):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.jarvis = jarvis
        self.play = False
        pygame.init()
        self.cling_sound = pygame.mixer.Sound(f'{self.path[:-17]}/Ressources/cling.wav')
        self.cling_sound.set_volume(0.1)
        if open : self.open_deezer()

    def open_deezer(self):
        os.system('start Chrome https://www.deezer.com/en/')
        print('"Deezer - Google Chrome" is open')
        self.jarvis.log(text='"Deezer - Google Chrome" is open', type='warning')

    def play_pause(self):
        if os.environ['COMPUTERNAME'] == 'PC-DE-CLÉMENT': keyboard.send('f10')
        else: keyboard.send('space')
        if self.play: self.jarvis.log(text='J: Pause')
        else:
            self.jarvis.log(text='J: Play')
            # pygame.mixer.Sound.play(self.cling_sound)
            # self.cling_sound.set_volume(0.1)
        self.play = not self.play

    def next_track(self):
        if os.environ['COMPUTERNAME'] == 'PC-DE-CLÉMENT': keyboard.send('f11')
        else: keyboard.send('maj+droite')
        self.jarvis.log(text='J: Musique suivante')
        # pygame.mixer.Sound.play(self.cling_sound)
        # self.cling_sound.set_volume(0.1)

    def previous_track(self):
        if os.environ['COMPUTERNAME'] == 'PC-DE-CLÉMENT': keyboard.send('f9')
        else: keyboard.send('maj+gauche')
        self.jarvis.log(text='J: Musique précédente')
        # pygame.mixer.Sound.play(self.cling_sound)
        # self.cling_sound.set_volume(0.1)

    def get_forward_in_track(self):
        keyboard.press_and_release('ctrl_l+droite')
        self.jarvis.log(text='J: On avance un peu')

    def get_backward_in_track(self):
        keyboard.press_and_release('ctrl_l+gauche')
        self.jarvis.log(text='J: On recule un peu')

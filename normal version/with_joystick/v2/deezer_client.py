import keyboard
import time
import os
import pygame
import pygetwindow as gw


class Deezer_Client():
    def __init__(self, jarvis, open=False):
        #Coups de Coeur = https://www.deezer.com/en/profile/1952230322/loved
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.jarvis = jarvis
        self.play = False
        pygame.init()
        self.cling_sound = pygame.mixer.Sound(f'{self.path[:-17]}/Ressources/cling.wav')
        self.cling_sound.set_volume(0.1)
        self.playlist_id = 0
        self.playlists_code = [4437920742, 5171291864, 4541051964, 4437894482, 4543281204, 4437882342, 4437869642, 4437918842, 4437906002, 7857305562, 8712869722]
        self.playlists_name = ['Rock Chill', 'Rock*', 'Remember', 'Yep', 'Rap US', 'Chill', 'Sport', 'Nope', 'YUP', 'Rap FR', 'Disney']
        if open : self.open_window()

    def open_window(self):
        os.system(f'start Chrome /new-window https://www.deezer.com/en/playlist/{self.playlists_code[self.playlist_id]}')
        print('"Deezer - Google Chrome" is open')
        self.jarvis.log(text='Deezer est ouvert', type='warning')
        time.sleep(2)

    def play_pause(self):
        if os.environ['COMPUTERNAME'] == 'PC-DE-CLÉMENT':
            active_window = str(gw.getActiveWindow())
            if 'Deezer' in active_window: keyboard.send('maj+enter')
            else: keyboard.send('f10')
            if self.play: self.jarvis.log(text='J: Pause')
            else:
                self.jarvis.log(text='J: Play')
                # pygame.mixer.Sound.play(self.cling_sound)
                # self.cling_sound.set_volume(0.1)
            self.play = not self.play
        else:
            active_window = str(gw.getActiveWindow())
            if 'Deezer' in active_window or 'Spotify' in active_window:
                keyboard.send('space')
                if self.play: self.jarvis.log(text='J: Pause')
                else:
                    self.jarvis.log(text='J: Play')
                    # pygame.mixer.Sound.play(self.cling_sound)
                    # self.cling_sound.set_volume(0.1)
                self.play = not self.play
            else: self.jarvis.log(text='J: Restez sur une page Media', type='warning')

    def next_track(self):
        if os.environ['COMPUTERNAME'] == 'PC-DE-CLÉMENT':
            keyboard.send('f11')
            self.jarvis.log(text='J: Musique suivante')
            # pygame.mixer.Sound.play(self.cling_sound)
            # self.cling_sound.set_volume(0.1)
        else:
            active_window = str(gw.getActiveWindow())
            if 'Deezer' in active_window or 'Spotify' in active_window:
                if 'Deezer' in active_window: keyboard.send('maj+droite')
                if 'Spotify' in active_window: keyboard.send('alt+droite')
                self.jarvis.log(text='J: Musique suivante')
                # pygame.mixer.Sound.play(self.cling_sound)
                # self.cling_sound.set_volume(0.1)
            else: self.jarvis.log(text='J: Restez sur une page Media', type='warning')

    def previous_track(self):
        if os.environ['COMPUTERNAME'] == 'PC-DE-CLÉMENT':
            keyboard.send('f9')
            self.jarvis.log(text='J: Musique précédente')
            # pygame.mixer.Sound.play(self.cling_sound)
            # self.cling_sound.set_volume(0.1)
        else:
            active_window = str(gw.getActiveWindow())
            if 'Deezer' in active_window or 'Spotify' in active_window:
                if 'Deezer' in active_window: keyboard.send('maj+gauche')
                if 'Spotify' in active_window: keyboard.send('alt+gauche')
                self.jarvis.log(text='J: Musique précédente')
                # pygame.mixer.Sound.play(self.cling_sound)
                # self.cling_sound.set_volume(0.1)
            else: self.jarvis.log(text='J: Restez sur une page Media', type='warning')

    def get_forward_in_track(self):
        self.play = True
        active_window = str(gw.getActiveWindow())
        if 'Deezer' in active_window or 'Spotify' in active_window:
            if 'Deezer' in active_window: keyboard.send('ctrl+droite')
            if 'Spotify' in active_window: keyboard.send('ctrl+maj+droite')
            self.jarvis.log(text='J: On avance un peu')
        else: self.jarvis.log(text='J: Restez sur une page Media', type='warning')

    def get_backward_in_track(self):
        self.play = True
        active_window = str(gw.getActiveWindow())
        if 'Deezer' in active_window or 'Spotify' in active_window:
            if 'Deezer' in active_window: keyboard.send('ctrl+gauche')
            if 'Spotify' in active_window: keyboard.send('ctrl+maj+gauche')
            self.jarvis.log(text='J: On recule un peu')
        else: self.jarvis.log(text='J: Restez sur une page Media', type='warning')

    def change_playlist(self, command):
        if 'next' in command:
            if self.playlist_id == len(self.playlists_code) - 1: self.playlist_id = 0
            else: self.playlist_id += 1
        elif 'last' in command: self.playlist_id -= 1
        self.kill_window()
        self.jarvis.log(text=f'Je passe à {self.playlists_name[self.playlist_id]}')
        self.open_window()

    def kill_window(self):
        if self.play: self.play_pause()
        windows_names, titles_to_kill = list(gw.getAllTitles()), []
        for title in windows_names:
            if 'Deezer - Google Chrome' in title: titles_to_kill.append(title)
        for title in titles_to_kill:
            gw.getWindowsWithTitle(title)[0].close()
            time.sleep(0.2)
        if 'Deezer - Google Chrome' in str(gw.getActiveWindow()): keyboard.send('enter') #make sure to go to Deezer window before sending enter. (alt+tabs automatic)
        print('"Deezer - Google Chrome" is closed')

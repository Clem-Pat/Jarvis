import time
from volume_manager import Volume_manager
from arduino_board import Arduino_board
from console import Tkinter_window
from deezer_client import Deezer_Client
import os


class Jarvis():
    def __init__(self, auto_unfocus=False):
        self.console = Tkinter_window(self, auto_unfocus=auto_unfocus)
        self.arduinoboard = Arduino_board(self)
        self.deezer_client = Deezer_Client(jarvis=self, open=True)
        self.volume_manager = Volume_manager(self)
        self.command_wanted, self.last_loop_action, self.last_command = None, None, None
        self.start_play_asked, self.up_asked, self.down_asked, self.backward_asked, self.forward_asked = None, None, None, None, None

    def log(self, text, type='normal'):
        self.console.add_label(text=text, type=type)

    def listen(self):
        command = None
        if self.arduinoboard.arduinoboard != None:
            if self.arduinoboard.pin['A2'].read() == 0:  #si le bouton est pressé #TODO : ou le detecteur de mouvement renvoie True + ajouter le titre aux favoris
                if self.last_loop_action == None:
                    if self.command_wanted == None: self.command_wanted = ['mets play/pause', time.time()]
                    elif self.command_wanted[0] == 'mets play/pause': command, self.command_wanted = 'renvoie son actuel', None
                    self.last_loop_action = 'space'
                    self.start_play_asked = time.time()
                elif self.last_loop_action == 'space':
                    if time.time() - self.start_play_asked > 1: self.command_wanted, self.last_loop_action, command = None, 'kill Jarvis','kill Jarvis'

            elif self.arduinoboard.pin['A0'].read() < 0.2:
                if self.last_loop_action == None:
                    if self.command_wanted == None: self.command_wanted = ['monte le son', time.time()]
                    elif self.command_wanted[0] == 'monte le son': command, self.command_wanted = 'mets le son à 100%', None
                    self.last_loop_action = 'up'
                    self.up_asked = time.time()
                elif self.last_loop_action == 'up':
                    if time.time() - self.up_asked > 0.5: self.command_wanted, self.last_loop_action, command = None, 'monte le son', 'monte le son'

            elif self.arduinoboard.pin['A0'].read() > 0.8:
                if self.last_loop_action == None:
                    if self.command_wanted == None: self.command_wanted = ['baisse le son', time.time()]
                    elif self.command_wanted[0] == 'baisse le son': command, self.command_wanted = 'mets le son à 0%', None
                    self.last_loop_action = 'down'
                    self.down_asked = time.time()
                elif self.last_loop_action == 'down':
                    if time.time() - self.down_asked > 0.5: self.command_wanted, self.last_loop_action, command = None, 'baisse le son', 'baisse le son'

            elif self.arduinoboard.pin['A1'].read() < 0.2:
                if self.last_loop_action == None:
                    if self.command_wanted == None: self.command_wanted = ['avance un peu', time.time()]
                    elif self.command_wanted[0] == 'avance un peu': command, self.command_wanted = 'mets la suivante', None
                    self.last_loop_action = 'forward'
                    self.forward_asked = time.time()
                elif self.last_loop_action == 'forward':
                    if time.time() - self.forward_asked > 0.5: self.command_wanted, self.last_loop_action, command = None, 'next playlist', 'next playlist'

            elif self.arduinoboard.pin['A1'].read() > 0.8:
                if self.last_loop_action == None:
                    if self.command_wanted == None: self.command_wanted = ['recule un peu', time.time()]
                    elif self.command_wanted[0] == 'recule un peu': command, self.command_wanted = 'mets la precedente', None
                    self.last_loop_action = 'backward'
                    self.backward_asked = time.time()
                elif self.last_loop_action == 'backward':
                    if time.time() - self.backward_asked > 0.5: self.command_wanted, self.last_loop_action, command = None, 'last playlist', 'last playlist'
            else:
                self.last_loop_action = None
                if self.command_wanted != None:
                    if time.time() - self.command_wanted[1] > 0.25:
                        command = self.command_wanted[0]
                        self.command_wanted = None

        if command != None: self.call_the_right_command(command)

    def call_the_right_command(self, command):
        if 'playlist' in command : return self.deezer_client.change_playlist(command)
        elif 'pause' in command or 'play' in command : return self.deezer_client.play_pause()
        elif 'suivant' in command : return self.deezer_client.next_track()
        elif 'avance' in command : return self.deezer_client.get_forward_in_track()
        elif 'precedent' in command : return self.deezer_client.previous_track()
        elif 'recule' in command : return self.deezer_client.get_backward_in_track()
        elif 'arrete' in command or 'kill' in command : return self.kill()
        elif 'volume' in command or 'son'in command or 'tai' in command : return self.volume_manager.manage_volume(command)
        elif 'encore' in command : return self.call_the_right_command(self.last_command)
        else: pass
        self.last_command = command

    def kill(self, and_kill_music=True):
        if and_kill_music: self.deezer_client.kill_window()
        self.console.kill()
        print('Jarvis has been killed')
        os._exit(0)


# command = 'playlist suivante'
# jarvis = Jarvis()
# jarvis.call_the_right_command('deezer_client', command)

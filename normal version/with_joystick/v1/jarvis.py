import time
import keyboard
from win10toast import ToastNotifier
from volume_manager import Volume_manager
from arduino_board import Arduino_board
from console import Tkinter_window

class Jarvis():
    def __init__(self, auto_unfocus=False):
        self.console = Tkinter_window(auto_unfocus=auto_unfocus)
        self.arduinoboard = Arduino_board(self)
        self.volume_manager = Volume_manager(self)
        self.command_wanted, self.last_loop_action, self.start_play_asked = None, None, None
        self.last_command = None

    def notif(self, text):
        toast = ToastNotifier()
        toast.show_toast("Jarvis",text,duration=20,icon_path='normal version/Ressources/jarvis_icon.ico')
        while toast.notification_active(): time.sleep(0.1)

    def log(self, text, type='normal'):
        self.console.add_label(text=text, type=type)

    def listen(self):
        command = None
        if self.arduinoboard.arduinoboard != None:
            if self.arduinoboard.pin['A2'].read() == 0:  #si le bouton est pressé #TODO : ou le detecteur de mouvement renvoie True + ajouter le titre aux favoris
                if self.last_loop_action == None:
                    if self.command_wanted == None: self.command_wanted = ['mets play/pause', time.time()]
                    elif self.command_wanted[0] == 'mets play/pause': command, self.command_wanted = 'tais-toi', None
                    self.last_loop_action = 'space'
                    self.start_play_asked = time.time()
                elif self.last_loop_action == 'space':
                    if time.time() - self.start_play_asked > 0.5: self.command_wanted, self.last_loop_action, command = None, 'renvoie son actuel','renvoie son actuel'
            elif self.arduinoboard.pin['A0'].read() > 0.8:
                if self.last_loop_action == None: self.last_loop_action, command = 'something', 'monte le son'
            elif self.arduinoboard.pin['A0'].read() < 0.2:
                if self.last_loop_action == None: self.last_loop_action, command = 'something', 'baisse le son'
            elif self.arduinoboard.pin['A1'].read() > 0.8:
                if self.last_loop_action == None: self.last_loop_action, command = 'something', 'mets la suivante'
            elif self.arduinoboard.pin['A1'].read() < 0.2:
                if self.last_loop_action == None: self.last_loop_action, command = 'something', 'mets la precedente'
            else:
                self.last_loop_action = None
                if self.command_wanted != None:
                    if time.time() - self.command_wanted[1] > 0.3:
                        command = self.command_wanted[0]
                        self.command_wanted = None
        return command

    def call_the_right_command(self, deezer_client, command):
        if 'pause' in command or 'play' in command: deezer_client.play_pause()
        elif 'precedent' in command : deezer_client.previous_track()
        elif 'suivant' in command : deezer_client.next_track()
        elif 'arrete' in command or 'stop' in command : stop = True
        elif 'volume' in command or 'son'in command or 'tai' in command: self.volume_manager.manage_volume(command)
        elif 'encore' in command : self.call_the_right_command(deezer_client, self.last_command)
        self.last_command = command


# command = 'Coucou tais-toi'
# jarvis = Jarvis()
# jarvis.call_the_right_command('deezer_client', command)

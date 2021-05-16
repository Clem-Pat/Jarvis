from volume_manager import Volume_manager
from arduino_board import Arduino_board

class Jarvis():
    def __init__(self):
        self.arduinoboard = Arduino_board()
        self.volume_manager = Volume_manager()
        self.last_command, self.second_last_command = None, None

    def listen(self):
        command = None
        if self.arduinoboard.arduinoboard != None:
            if self.arduinoboard.pin['A3'].read() > 4:  #si le bouton est pressé
                #TODO : ou le detecteur de mouvement renvoie True
                #TODO : si le bouton est pressé longtemps : on renvoie le volume actuel
                #TODO : si le bouton est pressé deux fois rapidement : on se tait (volume=0)
                command = 'mets play/pause'
            elif self.arduinoboard.pin['A1'].read() > 4: command = 'monte le son'
            elif self.arduinoboard.pin['A1'].read() < 1: command = 'baisse le son'
            elif self.arduinoboard.pin['A2'].read() > 4: command = 'mets la suivante'
            elif self.arduinoboard.pin['A2'].read() < 1: command = 'mets la precedente'
        return command

    def call_the_right_command(self, deezer_client, command):
        print('I recognize the following command :', command)
        if 'pause' in command or 'play' in command: deezer_client.play_pause(self)
        elif 'precedent' in command : deezer_client.previous_track(self)
        elif 'suivant' in command : deezer_client.next_track(self)
        elif 'arrete' in command or 'stop' in command : stop = True
        elif 'volume' in command or 'son'in command or 'tai' in command: self.volume_manager.manage_volume(self, command)
        self.last_command = command


# command = 'Coucou quel est le son actuel ?'
# jarvis = Jarvis()
# jarvis.call_the_right_command('deezer_client', command)

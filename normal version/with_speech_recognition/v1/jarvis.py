import speech_recognition as sr
import unidecode
from volume_manager import Volume_manager


class Jarvis():
    def __init__(self):
        self.volume_manager = Volume_manager()
        self.last_action = None

    def listen(self):
        recognizer = sr.Recognizer()
        lang = "fr-FR"
        with sr.Microphone() as source:
            print('Calibrating the ambient noise')
            recognizer.adjust_for_ambient_noise(source)
            print('Talk...')
            audio = recognizer.listen(source)
            print("Done listening")
            try:
                command = recognizer.recognize_google(audio, language = lang).lower()
            except sr.UnknownValueError:
                command = None
                print("I didn't understand...")
            except sr.RequestError as e:
                command = None
                print("Error ; {0}".format(e))
        return command

    def call_the_right_command(self, deezer_client, command):
        stop = False
        command = unidecode.unidecode(command)
        print('I recognize the following command :', command)
        if 'pause' in command: deezer_client.play_pause(self)
        elif 'play' in command : deezer_client.play_pause(self)
        elif 'precedent' in command : deezer_client.previous_track(self)
        elif 'suivant' in command : deezer_client.next_track(self)
        elif 'arrete' in command or 'stop' in command : stop = True
        elif 'volume' in command or 'son'in command or 'tai' in command: self.volume_manager.manage_volume(self, command)
        return stop


# command = 'Coucou quel est le son actuel ?'
# jarvis = Jarvis()
# jarvis.call_the_right_command('deezer_client', command)

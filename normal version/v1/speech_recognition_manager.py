import speech_recognition as sr
import keyboard
import time
import unidecode

def listen():
    recognizer = sr.Recognizer()
    lang = "fr-FR"
    with sr.Microphone() as source:
        print('Setting the ambient noise')
        recognizer.adjust_for_ambient_noise(source)
        print('Talk...')
        audio = recognizer.listen(source)
        print("Done listening")
        try:
            command = recognizer.recognize_google(audio, language = lang).lower()
            print("You said :" + command)
        except sr.UnknownValueError:
            command = None
            print("I didn't understand...")
        except sr.RequestError as e:
            command = None
            print("Error ; {0}".format(e))
    return command

def call_the_right_command(deezer_client, command):
    command = unidecode.unidecode(command)
    print('I recognize the following command :', command)
    if 'pause' in command: deezer_client.play_pause()
    if 'play' in command : deezer_client.play_pause()
    if 'precedent' in command : deezer_client.previous_track()
    if 'suivant' in command : deezer_client.next_track()
    if 'monte' in command : deezer_client.volume_up()
    if 'desc' in command : deezer_client.volume_down()
    if 'news' in command : deezer_client.mute() #Google reconnait news comme étant mute... mdr


# command = listen()
#
# if command != None:
#     command = command.lower()
#     print('command lowercase', command)
#     if 'pause' in command:
#         keyboard.press_and_release('space')
#         print('pressed space')
#

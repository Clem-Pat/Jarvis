# -*- coding: utf-8 -*-
import os
import keyboard
from deezer_client import Deezer_Client
from speech_recognition_manager import listen, call_the_right_command

def main():
    deezer_client = Deezer_Client()
    while not keyboard.is_pressed('ctrl'):
        command = listen()
        if command != None:
            if 'jarvis' in command:
                command = command[command.find('jarvis'):]
                call_the_right_command(deezer_client, command)

if __name__ == '__main__':
    main()
    os._exit(0)

# -*- coding: utf-8 -*-
import os
import keyboard
from deezer_client import Deezer_Client
from jarvis import Jarvis

def main():
    deezer_client = Deezer_Client(open=True)
    jarvis = Jarvis()
    while not keyboard.is_pressed('delete'):
        command = jarvis.listen()
        if command != None: jarvis.call_the_right_command(deezer_client, command)

if __name__ == '__main__':
    main()
    os._exit(0)

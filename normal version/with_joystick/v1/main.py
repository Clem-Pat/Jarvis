import os
import keyboard
from deezer_client import Deezer_Client
from jarvis import Jarvis


def main():
    jarvis = Jarvis(auto_unfocus=False)
    deezer_client = Deezer_Client(jarvis=jarvis, open=False)
    while not keyboard.is_pressed('ctrl+maj+c'):
        command = jarvis.listen()
        if command != None: jarvis.call_the_right_command(deezer_client, command)
        jarvis.console.refresh()
    jarvis.console.kill_console()
    os._exit(0)
    
if __name__ == '__main__':
    main()

#TODO : know if there was an error (to display it on console)
#TODO

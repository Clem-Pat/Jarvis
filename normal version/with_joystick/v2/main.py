import os
import keyboard
from jarvis import Jarvis


def main():
    jarvis = Jarvis(auto_unfocus=True)
    jarvis.log("J'écoute")
    while not keyboard.is_pressed('ctrl+maj+c'):
        jarvis.listen()
        jarvis.console.refresh()
    jarvis.kill()


if __name__ == '__main__':
    main()

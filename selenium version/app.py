# -*- coding: utf-8 -*-
from deezer_client import Deezer_Client
import time
import os

def main():
    deezer = Deezer_Client()
    deezer.open_and_login()
    deezer.play_playlist('Chill')
    time.sleep(2)
    deezer.next_track()

    time.sleep(600)
    try: deezer.driver.close()
    except: pass

if __name__ == '__main__':
    main()
    os._exit(0)

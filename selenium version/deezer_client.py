from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import os
import pandas as pd
import keyboard

class Deezer_Client():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        wallet = pd.read_csv(f'{self.path}/secret.txt', sep='=', index_col=0, squeeze=True, header=None)
        self.username, self.pw = wallet['username'], wallet['pw']

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def open_and_login(self, login=False):
        self.driver.get("https://www.deezer.com/en/profile/1952230322/playlists")
        self.driver.find_element_by_xpath('//*[@id="dzr-app"]/div/div[5]/div/div[2]/button[1]').click()
        if login:
            self.driver.find_element_by_xpath('//*[@id="page_topbar"]/div[3]/a[2]').click()
            self.driver.find_element_by_xpath('//*[@id="login_mail"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//*[@id="login_password"]').send_keys(self.pw)
            self.driver.find_element_by_xpath('//*[@id="login_form_submit"]').click()
            while not keyboard.is_pressed('ctrl') or self.driver.current_url != 'https://www.deezer.com/en/profile/1952230322/playlists': pass #wait for the bot blocker to be solved manually
        time.sleep(1)

    def play_playlist(self, playlist='Rock Chill', shuffle=True):
        self.driver.get("https://www.deezer.com/en/profile/1952230322/playlists")
        y=0
        while not keyboard.is_pressed('ctrl'):
            if y<1080: y+=100
            self.driver.execute_script(f"window.scrollTo(0, {y});")
            try:
                self.driver.find_element_by_xpath(f'//*[@title="{playlist}"]').click()
                break
            except: pass
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="page_naboo_playlist"]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/button/span[2]/div[1]/span').click()
        time.sleep(2)
        if shuffle: self.driver.find_element_by_xpath('//*[@id="page_player"]/div/div[3]/ul/li[1]/ul/li[3]/button').click()

    def next_track(self):
        self.driver.find_element_by_xpath('//*[@id="page_player"]/div/div[1]/ul/li[5]/div/button').click()

    def previous_track(self):
        self.driver.find_element_by_xpath('//*[@id="page_player"]/div/div[1]/ul/li[1]/div/button').click()

    def play_pause(self):
        self.driver.find_element_by_xpath('//*[@id="page_player"]/div/div[1]/ul/li[3]/button').click()

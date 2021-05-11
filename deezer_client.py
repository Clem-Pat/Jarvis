from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import os

class Deezer_Client():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        wallet = pd.read_csv(f'{path}/wallet.txt', sep='=', index_col=0, squeeze=True, header=None)
        self.username, self.pw = wallet['username'], wallet['pw']

        self.driver = webdriver.Chrome()

        pass

    def open_and_login(self):

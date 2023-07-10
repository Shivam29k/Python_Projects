from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from os import getenv
from dotenv import load_dotenv
load_dotenv()

TWTR_USERNAME = getenv('t_username')
TWTR_PASS = getenv('pass')

class Tweetbot():
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://twitter.com/homes')
        sleep(5)
        self.login()

    def login(self):
        username = self.driver.find_element(By.CSS_SELECTOR, 'input')
        username.send_keys(TWTR_USERNAME,Keys.ENTER)
        sleep(1)
        password = self.driver.find_element(By.CSS_SELECTOR,'[name="password"]')
        password.send_keys(TWTR_PASS, Keys.ENTER)

    def tweet(self, down_speed, up_speed):
        sleep(5)
        textbox = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
        textbox.send_keys(f'I am getting {down_speed} Mb/sec and {up_speed} Mb/sec upload speed in my area on my Jio network.')
        sleep(2)
        try:
            send_tweet = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
            send_tweet.click()
            print("TWEET SENT")
            self.quit_window()
        except:
            print("TWEET NOT SENT")
            sleep(100)
    def quit_window(self):
        self.driver.quit()

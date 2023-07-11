from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

INTSA_USERNAME = os.getenv('insta_username')
INSTA_PASS = os.getenv('pass')
TARGERT_UID_LIST = ['swiggyindia', 'virat.kohli']

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
sleep(5)
username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
username.send_keys(INTSA_USERNAME)
sleep(2)
password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
password.send_keys(INSTA_PASS)
sleep(2)
password.send_keys(Keys.ENTER)
sleep(5)

class Follow():
    def __init__(self, driver, target_uid):
        self.driver = driver
        self.driver.get(f'https://www.instagram.com/{target_uid}/followers/')
        sleep(8)

    def start_following(self):

        while True:
            for _ in range (6):
                try:
                    follow = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-')
                    self.driver.execute_script('arguments[0].click()', follow)
                except NoSuchElementException:
                    print("NO one to follow")
                    break
                except ElementClickInterceptedException as exception:
                    print(exception)
                    pass
                sleep(2)
            follow.send_keys(Keys.PAGE_DOWN)

for target_uid in TARGERT_UID_LIST:
    follow = Follow(driver, target_uid)
    follow.start_following()
    print(target_uid, 'done.')
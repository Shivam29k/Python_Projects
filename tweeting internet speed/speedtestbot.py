from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



class Speedtestbot():
    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://www.speedtest.net/')
        sleep(5)

    def check_speed(self):
        try:
            acpt_cookies_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            acpt_cookies_btn.click()
        except:
            print('passed')
            pass
        start = self.driver.find_element(By.CLASS_NAME,"start-text")
        start.click()
        sleep(60)
        print('time passed')
        down = self.driver.find_element(By.CLASS_NAME,'download-speed')
        up = self.driver.find_element(By.CLASS_NAME,'upload-speed')
        download_speed = down.text
        upload_speed = up.text
        self.quit_window()
        return (download_speed, upload_speed)
    def quit_window(self):
        self.driver.quit()

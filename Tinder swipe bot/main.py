from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

FB_PHONE_NO = os.getenv('phone_no')
FB_PASSWORD = os.getenv('pass')

chrome_driver_path = "E:\Codes\dev_tool\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://tinder.com/")
sleep(5)
accept = driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept.click()
sleep(1)
signin = driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
signin.click()
sleep(2)
login_with_fb = driver.find_element(By.XPATH,'//*[@id="u-1238065328"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
login_with_fb.click()
sleep(3)

main_page = driver.current_window_handle
for handle in driver.window_handles:
    if handle!=main_page:
        login_page = handle
driver.switch_to.window(login_page)
phone_no = driver.find_element(By.XPATH,'//*[@id="email"]')
phone_no.send_keys(FB_PHONE_NO)
sleep(2)
password = driver.find_element(By.XPATH,'//*[@id="pass"]')
password.send_keys(FB_PASSWORD)
sleep(2)
login_btn = driver.find_element(By.CSS_SELECTOR,'[name="login"]')
login_btn.click()
driver.switch_to.window(main_page)
sleep(10)

allow_loc = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div/div[3]/button[1]/div[2]')
allow_loc.click()
sleep(2)
notificarion = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div/div[3]/button[2]/div[2]')
notificarion.click()
sleep(3)
for i in range(10):
    try:
        action = driver.find_element(By.CSS_SELECTOR,"body")
        # change LEFT --> RIGHT to like
        action.send_keys(Keys.LEFT)
    except:
        # code for additional pop ups, and if math found
        pass
    sleep(5)


sleep(100)
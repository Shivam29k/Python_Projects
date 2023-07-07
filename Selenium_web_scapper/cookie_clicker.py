from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "E:\Codes\dev_tool\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

start_time = time.time()
while True:
    cookie.click()
    if time.time() - start_time >= 5:
        money = int((driver.find_element(By.XPATH, '//*[@id="money"]')).text.replace(',',''))
        if money >= 123456789:
            time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
            time_machine.click()
        elif money>=1000000:
            portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
            portal.click()
        elif money>=50000:
            lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
            lab.click()
        elif money>=7000:
            shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
            shipment.click()
        elif money>=2000:
            mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
            mine.click()
        elif money>=500:
            factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
            factory.click()
        elif money>=111:
            grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
            grandma.click()
        elif money>=15:
            cusor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
            cusor.click()
        start_time = time.time()

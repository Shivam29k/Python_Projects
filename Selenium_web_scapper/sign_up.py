from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "E:\Codes\dev_tool\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
f_name.send_keys("Shivam")
time.sleep(0.5)

l_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
l_name.send_keys("Kumar")
time.sleep(0.5)

mail = driver.find_element(By.XPATH, '/html/body/form/input[3]')
mail.send_keys("example@mail.com")
time.sleep(0.5)

sign_up = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up.send_keys(Keys.ENTER)






time.sleep(10)
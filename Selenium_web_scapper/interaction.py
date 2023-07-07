from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "E:\Codes\dev_tool\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

noOfArticles = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]')
print(noOfArticles.text)
# noOfArticles.click()

all_portals = driver.find_element(By.LINK_TEXT, 'View history')
all_portals.click()

# search_btn = driver.find_element(By.CLASS_NAME,"mw-ui-icon-wikimedia-search")
# search_btn.click()

search_tab = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
search_tab.send_keys("Python", Keys.ENTER)

time.sleep(10) # wait for 3 seconds to load the results

# driver.quit()
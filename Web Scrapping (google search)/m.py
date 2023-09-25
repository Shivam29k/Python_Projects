from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

niche = input("Niche: ")
location = input("Location: ")
term = niche+' near '+location

# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
driver = webdriver.Firefox()
driver.implicitly_wait(10)
data = []
df = pd.DataFrame(data, columns=['Name', 'Phone Number', 'Website'])
df.to_csv('business_details.csv', index=False)

driver.get(f"https://www.google.com/maps/")
driver.implicitly_wait(5)
search = driver.find_element(By.CSS_SELECTOR,'input[id="searchboxinput"]')
search.send_keys(term + Keys.ENTER)
driver.implicitly_wait(10)


def getDetails():
    driver.implicitly_wait(5)
    # sleep(1)
    try:
        name = driver.find_element(By.CSS_SELECTOR, 'h1.DUwDvf.lfPIob').text
    except Exception as e:
        print(e)
        name = 'Not Available'
    print('Name:',name)

    try:
        website = driver.find_element(By.CSS_SELECTOR, 'a[data-tooltip="Open website"]').get_attribute('href')
    except:
        website = 'Not Available'
    print('Website:',website)

    try:
        phone_no = driver.find_element(By.CSS_SELECTOR, 'button[data-tooltip="Copy phone number"]').text
    except:
        phone_no = 'Not Available'
    print('phone no:',phone_no)

    # adding details to CSV
    data = []
    data.append([name, phone_no, website])
    df = pd.DataFrame(data, columns=['Name', 'Phone Number', 'Website'])
    df.to_csv('business_details.csv', mode='a', header=False, index=False)

i=3
while True:
    try:
        element = driver.find_element(By.CSS_SELECTOR, f'div.DxyBCb:nth-child(1) > div:nth-child({i})')
        element.click()
        # print(element.text)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.implicitly_wait(20)
        getDetails()
    except Exception as e:
        print(e)
        print('search finished')
        break
    i+=2

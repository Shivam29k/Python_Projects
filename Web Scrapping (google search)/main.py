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

def getDetails(element, interface):
    if interface ==1:
        try:
            details = element.find_element(By.CSS_SELECTOR, '.rllt__details')
            # getting name of the bussiness
            name = details.find_element(By.CSS_SELECTOR, '.OSrXXb').text
            print('name:', name)

            # getting phone number
            phone_no = details.find_element(By.CSS_SELECTOR, 'div:nth-child(4)').text[-13:].replace(' ', '')
            for char in phone_no:
                if not char.isdigit() or char=='+':
                    phone_no = phone_no.replace(char,'')
            if len(phone_no)<10:
                phone_no = 'Not Available'
            print('phone no:',phone_no)
            # trying to get website
            try:
                website = element.find_element(By.CSS_SELECTOR, '.L48Cpd').get_attribute('href')
            except:
                website = 'Not Available'
            print('website:',website)
        except:
            pass
    elif interface==2:
        try:
            name = element.find_element(By.CSS_SELECTOR, ".NwqBmc :first-child").text
            print(name)

            try:
                phone_no = element.find_element(By.CSS_SELECTOR, ".NwqBmc :nth-child(3) :nth-child(3)").text
            except:
                phone_no='Not Available'
            print(phone_no)

            website = element.find_element(By.CSS_SELECTOR, '.zuotBc').get_attribute('href').text
            print(website)
        except Exception as e:
            print(e)


    data = []
    data.append([name, phone_no, website])
    df = pd.DataFrame(data, columns=['Name', 'Phone Number', 'Website'])
    df.to_csv('business_details.csv', mode='a', header=False, index=False)

driver.get("http://www.google.com")
search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys(term, Keys.ENTER)
More_places = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.Z4Cazf')))
More_places.click()

while True:
    sleep(5)
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, '.VkpGBb')
        interface = 1
        if len(elements) == 0:
            elements = driver.find_elements(By.CSS_SELECTOR, 'div[data-test-id="organic-list-card"]')
            interface = 2
        if len(elements)==0:
            print('No results found')
            break

        print('interface:',interface)

        for element in elements:
            try:
                getDetails(element, interface)
            except Exception as e:
                print

        # if interface==1:
        #     driver.find_element(By.ID, 'pnnext').click()
    except:
        try:
            text = driver.find_element(By.ID, 'search').text
            if 'no results' in text:
                print(f'Search complete for {location}, go check the CSV file!!')
                break
        except Exception as e:
            print('Program terminated de to :\n',e)
    break
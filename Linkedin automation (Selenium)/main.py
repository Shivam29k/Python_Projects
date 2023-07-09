from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint
import time
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL=os.getenv('email')
PASSWORD=os.getenv('password')


chrome_driver_path = "E:\Codes\dev_tool\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3648054777&f_AL=true&geoId=102713980&keywords=python%20developer&location=India&refresh=true")
signin = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
signin.click()
# time.sleep(20)

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(PASSWORD)
signinButton = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
signinButton.click()
time.sleep(50)
print("50 sec done")

job_lists = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
pprint(job_lists)
time.sleep(5)

for job in job_lists:

    job.click()
    print("clicked")
    save = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    save.click()
    print("clicked 2")
    # time.sleep(2)
    # phone  = driver.find_element(By.CLASS_NAME,"artdeco-text-input--input")
    # phone.send_keys('1234567890')
    # print("clicked 3")
    # next = driver.find_element(By.CSS_SELECTOR, '[aria-label="Continue to next step"]')
    # next.click()
    # print("clicked 4")
    # next = driver.find_element(By.CSS_SELECTOR, '[aria-label="Continue to next step"]')
    # next.click()
    # print("clicked 5")

    time.sleep(2)




time.sleep(100)

import re
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

# driver = webdriver.Firefox()
# driver.get(wesite)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# page_source = driver.page_source

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
# html = driver.page_source


response = requests.get('https://thegym.nyc/')
html = BeautifulSoup(response.text, 'html.parser')
emails = re.findall(email_pattern, str(html))

# emails = find_mail(page_source)
print(emails)
# sleep(100)
# driver.quit()
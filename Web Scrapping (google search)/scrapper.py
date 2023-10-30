from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests

driver = webdriver.Firefox()

def startScraping(term):
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    driver.implicitly_wait(10)
    data = []
    df = pd.DataFrame(data, columns=['Name', 'Phone Number', 'Website', 'Address'])
    df.to_csv('business_details.csv', index=False)

    driver.get(f"https://www.google.com/maps/")
    driver.implicitly_wait(5)
    search = driver.find_element(By.CSS_SELECTOR,'input[id="searchboxinput"]')
    search.send_keys(term + Keys.ENTER)
    driver.implicitly_wait(10)


    def getDetails():
        driver.implicitly_wait(20)
        sleep(1)
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

        try:
            address = driver.find_element(By.CSS_SELECTOR, 'button[data-item-id="address"]').text
        except:
            address = 'Not Available'
        print('Address:',address)


        # adding details to CSV
        data = []
        data.append([name, phone_no, website, address])
        df = pd.DataFrame(data, columns=['Name', 'Phone Number', 'Website', 'Address'])
        df.to_csv('business_details.csv', mode='a', header=False, index=False)

    i=3
    while True:
        try:
            element = driver.find_element(By.CSS_SELECTOR, f'div.DxyBCb:nth-child(1) > div:nth-child({i})')
            element.click()
            # print(element.text)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.implicitly_wait(20)
            sleep(1)
            element = driver.find_element(By.CSS_SELECTOR, 'div[role="main"]')
            getDetails()
        except NoSuchElementException:
            print('search finished')
            break
        except Exception as e:
            print('Unknown Ending')
            print(e)
            print('search finished')
            break
        i+=2


# driver.quit()

def get_emails(deepdive):

    df = pd.read_csv('business_details.csv')
    websites = df['Website'].tolist()

    # websites = ['https://thegym.nyc/']
    print(websites)


    # for validating an Email
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
    def find_mail(html):
        emails = re.findall(email_pattern, html)
        return emails

    def deep_dive(soup):
        emails = []
        nav_links = soup.select('nav a')
        for nav_link in nav_links:
            try:
                response = requests.get(nav_link['href'])
                soup = BeautifulSoup(response.text, 'html.parser')
                emails.extend(find_mail(str(soup)))
            except:
                pass
        contact_pages = ['/contactus', '/contact', '/contact-us']
        for page in contact_pages:
            try:
                driver.get(website + page)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                emails.extend(find_mail(str(soup)))
                break
            except:
                pass
        return emails

    Emails =[]
    # loop through each website
    for website in websites:
        if website == 'Not Available':
            print('website not available')
            Emails.append(['Not Available'])
            continue
        emails = []
        try:
            driver.get(website)
            print(f"trying {website}")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            page_source = driver.page_source
            emails.extend(find_mail(page_source))
        except:
            if deepdive == 'auto' and len(emails) == 0:
                print(f"trying {website} with deep dive")
                deepdive = 'on'
        if deepdive == 'on':
            print(f"trying {website} with deep dive")
            emails.extend(deep_dive(soup))
        if len(emails) == 0:
            email = 'Not Available'
            emails.append(email)
            print('Email:', email)
        else:
            print('Emails:')
            for mail in emails:
                print(mail)
        emails = list(set(emails))
        Emails.append(emails)

    # save the updated DataFrame to a CSV file
    print(Emails)
    Emails = [','.join(Email) for Email in Emails]
    print(Emails)
    df['email'] = Emails
    df.to_csv('business_details_email.csv', index=False)

# startScraping('gym in nyc')
get_emails('on')
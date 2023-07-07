from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "E:\Codes\dev_tool\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# Interacting with web page
# element = driver.find_element(By.ID, "passwd-id")
# element = driver.find_element(By.NAME, "passwd")
# element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

# So, you’ve got an element. What can you do with it? First of all, you may want to enter some text into a text field:
# element.send_keys("some text")
# element.send_keys(" and some", Keys.ARROW_DOWN)  for simulating arrow keys



# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)

# docs = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs.text)

# USING XPATH
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# scarping upcoming events from pythondocs website
event_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul time')
event_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul a')

events = {}
i=0
for time, name in zip(event_time, event_name):
    events[i] = {
        "time" : time.text,
        "name" : name.text
    }
    i+=1
print(events)



# driver.close()  #to quit the tab
driver.quit()   # to quit the browser

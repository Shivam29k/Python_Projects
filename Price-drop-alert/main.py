import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

MY_MAIL = os.getenv("my_email")
MAIL_PASS = os.getenv("password")



PRODUCT_URL = "https://www.flipkart.com/campus-first-running-shoes-men/p/itm9659b1dfc927e?pid=SHOGFGMBHNDXZKDB&lid=LSTSHOGFGMBHNDXZKDB3LR8YX&marketplace=FLIPKART&q=sports+shoes+for+men+campus&store=osp%2Fcil%2F1cu&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_tQegkgjYOAo4zm-Spd9ylaMt0ltMlfo5z7Eu8Rb0pgmWPdrSzIy1qthTiYWR1x2iX-AVl5-0vmNHCY4qQfMfBg%3D%3D&ppt=sp&ppn=sp&ssid=bowl8psips0000001688724709242&qH=7fdd40d1c0ef70db"
response = requests.get(url=PRODUCT_URL)

soup = BeautifulSoup(response.text, "html.parser")

price = int(soup.find(name="div", class_="_30jeq3 _16Jk6d").getText().replace("₹", "").replace(",", ""))
print(price)
set_price = 1500

if price  <= set_price :

    shop_text = soup.find(class_="G6XhRU").getText()
    product_text = soup.find(class_="B_NuCI").getText()

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MAIL_PASS)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=MY_MAIL,
            msg=(f"Subject: Price Drop Alert !! \n\n{product_text} from {shop_text} is now for ₹{price}").encode("utf-8")
        )
        print("mail sent")

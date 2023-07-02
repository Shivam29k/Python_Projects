from twilio.rest import Client
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.getenv("account_sid")
TWILIO_AUTH_TOKEN = os.getenv("auth_token")
FROM_NO = os.getenv("from_phone_no")
TO_NO = os.getenv("to_phone_no")

MY_MAIL = os.getenv("my_email")
MAIL_PASS = os.getenv("password")

SHEETRY_GET_USERS = "https://api.sheety.co/7e5dc26de00c4f9595d05537d7febfae/flightDeals/users"
AUTH = os.getenv("sheety_authorization")

class NotificationManager:
    def send_mail(self, text, mail):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=MAIL_PASS)
            connection.sendmail(
                from_addr=MY_MAIL,
                to_addrs=mail,
                msg=(f"Subject: Price Alert !! \n\n{text}").encode("utf-8")
            )
        print("mail sent")

    def send_sms(self, text):
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            from_=FROM_NO,
            body=text,
            to=TO_NO
        )
        print("sms sent")

    def send_mails(self, text):
        head = {"Authorization": AUTH, "Content-Type": "application/json"}
        response = requests.get(url=SHEETRY_GET_USERS, headers=head)
        # print(response.json())
        for data in response.json()['users']:
            mail = data["email"]
            self.send_mail(text, mail)

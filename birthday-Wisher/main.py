import datetime as dt
import pandas as pd
import smtplib
from random import choice

my_email = "shivamkg29@gmail.com"
password = "vzhwkqekruvormqj"

data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()

def message(name):
    templates = ["letter_1", "letter_2", "letter_3"]
    with open(f"letter_templates/{choice(templates)}.txt", "r") as template_file:
        template = template_file.read()
    letter = template.replace("[NAME]", name)
    return letter


def send_mail(name, email):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject: HAPPY BIRTHDAY \n\n{message(name)}"
        )

for month, day, email, name in zip(data["month"], data["day"], data["email"], data["name"]):
    if month == now.month and day == now.day:
        send_mail(name, email)

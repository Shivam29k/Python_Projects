import requests
import datetime as dt
import smtplib
import time

my_email = "shivamkg29@gmail.com"
password = "vzhwkqekruvormqj"
to_mail = "21shubhamk2005@gmail.com"

MY_LATITUDE = 30.717499
MY_LONGITUDE = 76.761700


# ------------------------------------------- getiing ISS location --------------------------------------------
# ------------------------------------------- day or night  --------------------------------------------

def is_night():
    parameters =  {
        'lat' : MY_LATITUDE,
        'lng' : MY_LONGITUDE,
        'formatted' : 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    def ist(ISO):
        hr = int(ISO.split("T")[1].split(":")[0]) + 5
        min = int(ISO.split("T")[1].split(":")[1]) + 30
        if min>60:
            min -= 60
            hr += 1
        if hr>24:
            hr-=24
        time = (hr,min)
        return time
    sunrise = ist(data['results']['sunrise'])[0]
    sunset = ist(data['results']['sunset'])[0]
    now = dt.datetime.now()
    if now.hour < sunrise or now.hour >sunset:
        print("Night")
        return True
    else:
        print("Day")
        return False
    
def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_data = response.json()
    global iss_latitude, iss_logitude
    iss_logitude = float(iss_data['iss_position']['longitude'])
    iss_latitude = float(iss_data['iss_position']['latitude'])

    if (int(MY_LONGITUDE)+6 > int(iss_logitude) > int(MY_LONGITUDE)-6 ) and (int(MY_LATITUDE)+6 > int(iss_latitude) > int(MY_LATITUDE)-6):
        print("nearby")
        return True
    else:
        print("aint nearby")
        return False

def send_mail():
    print("Email SENT")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject: ISS APPROACHING\n\nISS is visible from your place tonight !!!!\ncurrent location of ISS is {iss_latitude}{iss_logitude}"
        )

while True:
    time.sleep(60)
    if is_night() and iss_nearby():
        print("sending mail")
        send_mail()

# print("exit")


# Different response code meanings:
# 1XX = Hold on
# 2XX = Here you go
# 3XX = GO Away (you dont have permission)
# 4XX = You screwed Up (Problem from user end)
# 5XX = Devloper Screwed Up
# -----> httpstatuses.com

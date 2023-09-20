import requests
from twilio.rest import Client


LATTITUDE = 30.73
LONGITUDE = 76.88
api_key = "fd5ee92b7e514e7e542e1f6413dfe5fc"
ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
account_sid = 'AC2d7a3f3a1772fc90bd2473904cf0d838'
auth_token = '173fa57db8f99c5d6c5090d15b847fb4'

weather_params = {
    "lat": LATTITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily", 
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()['hourly']

will_rain = True
for weather_info in data[:12]:
    description = weather_info['weather'][0]['description']
    main = weather_info['weather'][0]['main']
    id = weather_info['weather'][0]['id']
    if id < 700:
        will_rain = True  

    print(f"{main} : {description}")

if will_rain:
    # print("Bring Umbrela ☔")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+15416526582',
    body="TESTING",
    to='+919981840921'
    )

    print(message.sid)
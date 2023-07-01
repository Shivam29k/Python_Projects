import os
from dotenv import load_dotenv
import requests
from datetime import datetime

GENDER = 'male'
WEIGHT_KG = 69
HEIGHT_CM = 175
AGE = 19

load_dotenv()
NUTRITION_API = os.getenv("nutritionix_api")
NUTRITION_APPID = os.getenv("nutritionix_appid")
SHEETY_AUTH = os.getenv("Authorization")
print(SHEETY_AUTH)


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "X-app-id": NUTRITION_APPID,
    "x-app-key": NUTRITION_API,
    "Content-Type": "application/json",
}

exercise_params = {
    "query" : input("Tell me which exercise you did: "),
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

response = requests.post(url=nutritionix_endpoint,json=exercise_params, headers=headers)
response.raise_for_status()
result = response.json()['exercises']






# --------------------------------- upadating in google sheets -----------------------------------

sheety_post_endpoint = "https://api.sheety.co/7e5dc26de00c4f9595d05537d7febfae/workouts/workouts"

now = datetime.now()
date = now.strftime('%d/%m/%Y')
current_time = now.strftime("%X")

header = {
    'Authorization': SHEETY_AUTH,
    "Content-Type": "application/json"
}

for ex in result:
    exercise = ex['name']
    duration = ex['duration_min']
    calories = ex['nf_calories']
    workout_data = {
        'workout': {
            "date": date,
            "time": current_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=sheety_post_endpoint,json=workout_data,headers=header)
    # response.raise_for_status()
    print(response.text)
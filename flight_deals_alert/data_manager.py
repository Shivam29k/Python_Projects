import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from flight_search import FlightSearch
load_dotenv()  # take environment variables from.env

SHEETY_AUTH = os.getenv("sheety_authorization")
SHEETY_ENDPOINT = "https://api.sheety.co/7e5dc26de00c4f9595d05537d7febfae/flightDeals/prices"

fs = FlightSearch()

class DataManager:
    def __init__(self):
        self.headers = {
            'Authorization':SHEETY_AUTH,
            'Content-Type':'application/json'
        }
        response = requests.get(url=SHEETY_ENDPOINT,headers=self.headers )
        self.data = response.json()['prices']
        self.update_sheet_data()
        if self.change_made:
            response = requests.get(url=SHEETY_ENDPOINT,headers=self.headers )
            self.data = response.json()['prices']


    def update_sheet_data(self):
        self.change_made = False
        for airport_data in self.data:
            if len(airport_data['iataCode']) == 0:
                self.change_made = True
                city_name = airport_data['city']
                print(city_name)
                iata_code = fs.iata_code(city_name)
                pur_data = {
                    'price': {
                        'iataCode':iata_code
                    }
                }
                
                id = airport_data['id']
                requests.put(url=f'{SHEETY_ENDPOINT}/{id}',json=pur_data, headers=self.headers)
                
        # response = requests.get(url=SHEETY_ENDPOINT,headers=self.headers )
        # print(response.json())
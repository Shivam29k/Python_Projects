from dotenv import load_dotenv
import os
import requests
from pprint import pprint
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()
API_KEY = os.getenv("flight_search_api")
KIWI_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {
            "apikey":API_KEY,
        }
    def iata_code(self, city_name):
        params = {
            'term': city_name,
            'location_types': 'city',
            'limit': 1,
        }
        response = requests.get(url=f'{KIWI_ENDPOINT}/locations/query', headers=self.header, params=params)
        print(response.status_code)

        # Check response status code
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()

            # Extract city code from the response
            if 'locations' in data and len(data['locations']) > 0:
                city_code = data['locations'][0]['code']
                if city_code == None and len(data['locations'][0]['alternative_departure_points'])>0:
                    distance = 200
                    for nearby in data['locations'][0]['alternative_departure_points']:
                        if nearby['distance'] < distance:
                            distance = nearby['distance']
                            nearby_citycode = nearby['id']
                    return nearby_citycode
                elif city_code == None:
                    return "City not found"
                return city_code
            else:
                return "City not found"
        else:
            return f"Error occurd: {response.raise_for_status}"

    def find_flights(self, origin_city_code,destination_city_code):
        presentday = datetime.now()
        tomorrow_date = presentday + timedelta(1)
        tomorrow_date = (tomorrow_date).strftime('%d/%m/%Y')
        six_months_date = presentday + timedelta(180)
        six_months_date = (six_months_date).strftime('%d/%m/%Y')

        params={
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": tomorrow_date,
            "date_to": six_months_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        response = requests.get(url=f'{KIWI_ENDPOINT}/v2/search', headers=self.header,params=params)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],  #return city name
            origin_airport=data["route"][0]["flyFrom"], # return iata code of airport
            destination_city=data["route"][0]["cityTo"], #return city name
            destination_airport=data["route"][0]["flyTo"], # return iata code of airport
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ₹{flight_data.price}")
        return flight_data
        # print(f"{arrival_city}: {}")


#  url to update the member in flight club datasheet:-- https://replit.com/@ShivamKumar28/Shivam-Flight-Club

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

datamager = DataManager()
flightsearch = FlightSearch()
send_notification = NotificationManager()
ORIGIN_CITY_IATA = "LON"
for destination in datamager.data:
    flight = flightsearch.find_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
    )
    if flight is None: continue
    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only ₹{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        print(message)
        # send_notification.send_sms(message)
        # send_notification.send_mail(message)
        send_notification.send_mails(message)
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
import time
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] =="":
    
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(city_name= row["city"])
    pprint(f"Sheet Data:\n {sheet_data}")


data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=(6*30))

for destination in sheet_data:
    print(f"Checking Flights for {destination["city"]}...")
    flights = flight_search.check_flights(ORIGIN_CITY_IATA,
                                        destination["iataCode"],
                                        from_time=tomorrow,
                                        to_time=six_months_from_now)
    
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")

    time.sleep(2)
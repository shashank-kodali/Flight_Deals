import os 
from dotenv import load_dotenv
import requests

# headers = {"Authorization" : "Bearer RuYtTAWqRNpuUHjNRShEXGZXoI1K"}

load_dotenv()
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_ID"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self.get_new_token()


    def get_destination_code(self, city_name):
        headers = {"Authorization" : f"Bearer {self._token}"}
        query ={
            "keyword" : city_name,
            "max" : 2,
            "include" : "AIRPORTS"
        }

        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query )

        # print(f"Status Code : {response.status_code}. Airport IATA : {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: on airport code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError:on airport code found for {city_name} ")
            return "Not Found"
        
        return code


    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")

        return response.json()['access_token']

    def check_flights(self, origin_airport, destination,from_time, to_time, is_direct=True):
        headers = {"Authorization" : f"Bearer {self._token}"}
        query ={
            "originLocationCode" : origin_airport,
            "destinationLocationCode" : destination,
            "departureDate" : from_time.strftime("%Y-%m-%d"),
            "returnDate" : to_time.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "INR",
            "max" : "10"
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n")
            print("Response body:", response.text)
            return None

        return response.json()
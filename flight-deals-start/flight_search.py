from requests import *

# class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

APIKey = "NWscJE7fcjklZMIQhuQEvxCAXGtccNhw"
APISecret = "TpZlhpxUfvmNGvjW"
endpoint = "https://test.api.amadeus.com/reference-data/locations/cities"
"

headers = {
    "Authorization" : "Bearer RuYtTAWqRNpuUHjNRShEXGZXoI1K"
}

response = post(url=endpoint, data=payload, headers=headers)


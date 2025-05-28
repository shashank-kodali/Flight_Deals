class FlightData:

    def __init__(self, price, origin_airport, destination, out_data, return_data):
        self.price = price
        self.origin_airport = origin_airport
        self.destination = destination
        self.out_data = out_data
        self.return_data = return_data

def find_cheapest_flight(data):

    if data is None or not data["data"]:
        print("No Flight data")
        return FlightData("N/A","N/A","N/A","N/A","N/A")
    
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_data = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_data = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_data, return_data)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = flight["price"]["grandTotal"]
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_data = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_data = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_data, return_data)

    return cheapest_flight

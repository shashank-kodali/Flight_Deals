class FlightData:

    def __init__(self, price, origin_airport, destination, out_data, return_data, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination = destination
        self.out_data = out_data
        self.return_data = return_data
        self.stops = stops

def find_cheapest_flight(data):

    if data is None or not data["data"]:
        print("No Flight data")
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A"
        )
    
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_data = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_data = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_data, return_data, nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = flight["price"]["grandTotal"]
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_data = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_data = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_data, return_data, nr_stops)

    return cheapest_flight

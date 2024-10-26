class Company:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def flight_list(self):
        return [flight.flight_information() for flight in self.flights]


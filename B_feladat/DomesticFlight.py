from Flight import Flight

class DomesticFlight(Flight):
    def flight_information(self):
        return f"Belföldi járat -> Járatszám: {self.flight_number}, Célállomás: {self.destination}, Jegyár: {self.price} EUR"


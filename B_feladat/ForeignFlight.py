from Flight import Flight

class ForeignFlight(Flight):
    def flight_information(self):
        return f"Nemzetközi járat -> Járatszám: {self.flight_number}, Célállomás: {self.destination}, Jegyár: {self.price} EUR"

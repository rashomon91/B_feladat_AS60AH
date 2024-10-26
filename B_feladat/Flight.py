from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number, destination, price):
        self.flight_number = flight_number
        self.destination = destination
        self.price = price

    @abstractmethod

    def flight_information(self):
        pass


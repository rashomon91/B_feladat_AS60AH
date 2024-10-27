from Flight import Flight
from datetime import datetime

class Booking:
    def __init__(self, flight, passenger_name, date):
        self.flight = flight
        self.passenger_name = passenger_name
        self.date = date

    def book_information(self):
        return f"Foglalás -> Utas neve: {self.passenger_name}, Járat: {self.flight.flight_information()}, Dátum: {self.date}"

class BookingSystem:
    def __init__(self):
        self.books = []

    def book_ticket(self, flight, passenger_name, date):
        if not isinstance(flight, Flight):
            return "Nincs ilyen járat!"
        if not BookingSystem.valid_date(date):
            return "Érvénytelen dátum!"
        if not self.is_flight_available(flight, date):
            return "A járat nem elérhető a megadott időpontban!"
        book = Booking(flight, passenger_name, date)
        self.books.append(book)
        return flight.price

    def cancellation(self, passenger_name):
        for book in self.books:
            if book.passenger_name == passenger_name:
                self.books.remove(book)
                return f"Foglalás lemondva a következőnek: {passenger_name}"
        return "Nincs ilyen néven foglalás"

    def booking_list(self):
        return [book.book_information() for book in self.books]

    @staticmethod
    def valid_date(date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def is_flight_available(self, flight, date):
        pass



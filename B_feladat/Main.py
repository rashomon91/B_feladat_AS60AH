from DomesticFlight import DomesticFlight
from ForeignFlight import ForeignFlight
from Company import Company
from Booking import BookingSystem
from Booking import Booking

def basic_data(booking_system):
    company = Company("Turkish Airlines")

    flight1 = DomesticFlight("1234", "Győr", 2000)
    flight2 = DomesticFlight("4567", "Budapest", 25000)
    flight3 = ForeignFlight("8911", "Tokyo", 70000)

    company.add_flight(flight1)
    company.add_flight(flight2)
    company.add_flight(flight3)

    book1 = Booking(flight1, "Kiss Pista", "2024-10-22")
    book2 = Booking(flight2, "Nagy Margit", "2024-10-23")
    book3 = Booking(flight3, "Tóth Péter", "2024-09-22")
    book4 = Booking(flight1, "Szabó Anna", "2024-11-02")
    book5 = Booking(flight2, "Kovács Tihamér", "2024-12-22")
    book6 = Booking(flight3, "Lakatos Gáspár", "2024-12-31")

    booking_system.books.append(book1)
    booking_system.books.append(book2)
    booking_system.books.append(book3)
    booking_system.books.append(book4)
    booking_system.books.append(book5)
    booking_system.books.append(book6)

def menu():
    print("Repülőjegy Foglalási Rendszer")
    print("1 Jegy foglalás")
    print("2 Foglalás lemondása")
    print("3 Foglalások listázása")
    print("4 Kilépés")

book_system = BookingSystem()
basic_data(book_system)

while True:
    menu()
    choice = input("Válasszon egy lehetőséget: ")

    if choice == '1':
        flight_type = input("Járat típusa: belföldi/külföldi: ")
        flight_number = input("Járatszám: ")
        destination = input("Célállomás: ")
        price = input("Jegyár: ")
        passenger_name = input("Utas neve: ")
        date = input("Foglalás dátuma (ÉÉÉÉ-HH-NN): ")

        if flight_type == "belföldi":
            flight = DomesticFlight(flight_number, destination, price)
        elif flight_type == "külföldi":
            flight = ForeignFlight(flight_number, destination, price)
        else:
            print("Nincs ilyen járat típus!")
            continue

        fee = book_system.book_ticket(flight, passenger_name, date)
        print("Sikeres foglalás! Ár: {fee}")

    elif choice == '2':
        passenger_name = input("Utas neve a lemondáshoz: ")
        result = book_system.cancellation(passenger_name)
        print(result)

    elif choice == '3':
        books = book_system.booking_list()
        for book in books:
            print(book)

    elif choice == '4':
        print("Kilépés!")
        break

    else:
        print("Nem létezik, próbálja újra!")

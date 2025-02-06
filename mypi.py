class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if self.open_seats() == 0:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["harry", "leo", "john", "gina"]

for person in people:
    if flight.add_passenger(person):
        print(f"added {person} to the flight")
    else:
        print(f"No available seats for {person}")

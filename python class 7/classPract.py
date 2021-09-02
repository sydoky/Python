import random

class Passenger:
    def __init__(self, first_name, last_name, nationality, DOB):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.DOB = DOB

    def __str__(self):
        return self.first_name + ", " + self.last_name + ", " + self.nationality + ", " + self.DOB

class Flight:
    def __init__(self, flight_number, source, destination, date, aircraft):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.date = date
        self.aircraft = aircraft

    def __str__(self):
        return self.flight_number + " " + self.source + ", " + self.destination + ", " + self.date + ", " + self.aircraft.model

    '''def book(self, passenger):
        full_name = passenger.first_name + ", " + passenger.last_name
        seat = self.aircraft.seats[0] #0 will take first seat, we are taking a specific seat
        seat["taken"] = full_name '''
    def book(self, passenger):
        full_name = passenger.first_name + " " + passenger.last_name
        while True: #in order to book a seat and not overriding passengers we added while loop which include line 30,32 and 33
            random_seat_index = random.randint(0, len(self.aircraft.seats)-1) #first we added "import random" in line 1; -1 means it will go all the seats
            if self.aircraft.seats[random_seat_index] ["taken"] != "available":
                continue
            seat = self.aircraft.seats[random_seat_index] #0 will take first seat
            seat["taken"] = full_name
            break #we use break to stop the loop
    def window_seat(self, passenger):
        full_name = passenger.first_name + " " + passenger.last_name
        extra_fee = input("window_seat costs extra fee. Would you like to proceed? ")
        if extra_fee.lower() not in ["y", "yes"]:
            self.book(passenger)
            return
        while True:
            random_seat_index = random.randint(0, len(self.aircraft.seats) - 1)
            if self.aircraft.seats[random_seat_index]["taken"] != "available":
                continue
            seat = self.aircraft.seats[random_seat_index]["number"]
            if seat[1] != "A" and seat[1] != "F":
                continue
            seat = self.aircraft.seats[random_seat_index]
            seat["taken"] = full_name
            break
    def emergency_exit_row(self, passenger):
        full_name = passenger.first_name + " " + passenger.last_name
        best_seat = input("selected seats have extra space and cost additional fee. Type 'Yes' if you agree: ")
        if best_seat.lower() not in["yes", "y"]: #lower is a method
            self.book(passenger)
            return
        while True:
            random_seat_index = random.randint(0, len(self.aircraft.seats) - 1)
            if self.aircraft.seats[random_seat_index]["taken"] != "available":
                continue
            seat = self.aircraft.seats[random_seat_index]["number"]
            middle_row = self.aircraft.rows // 2 + 1 # because 5 / 2 = integer division gives 2 and we need 3 (mid row) +1
            if int(seat[0]) != middle_row:
                continue
            seat = self.aircraft.seats[random_seat_index]
            seat["taken"] = full_name
            break




    def cancel(self, passenger):
        full_name = passenger.first_name + " " + passenger.last_name
        for s in self.aircraft.seats:
            if s["taken"] == full_name:
                s["taken"] = "available"



class Plane:
    def __init__(self, model, rows, seat_per_row):
        self.model = model
        self.seats = []                # () is a tuple
        self.rows = rows

        list_of_seats = ("A", "B", "C", "D", "E", "F")

        for r in range(1, rows + 1): #range
            for s in list_of_seats[:seat_per_row]: #we fixed line 28 by adding [] and seat_per_row
                seat_number = {"number": str(r) + s, "taken": "available"}
                self.seats.append(seat_number)

    def __str__(self):
        sts = "" #empty string; "" inside the quotes nothing there
        for s in self.seats: #referes to line 17
            sts += s["number"] + " availability: " + s["taken"] + "\n"  #\n is enter inside of the string #number comes from dict line 23

        return self.model + "\n" + sts




plane1 =Plane("Boing777", 5, 6)
print(plane1)

flightToMiami = Flight("SU101", "Belgrade", "Miami", "01.01.2021", plane1)
print(flightToMiami)

passenger1 = Passenger("John", "Rambo", "USA", "01.01.1960")
print(passenger1)

flightToMiami.book(passenger1)

print(plane1)

passenger2 = Passenger("Sarah", "Rambo", "USA", "05.10.1987")
flightToMiami.book(passenger2)
print(plane1)

flightToMiami.cancel(passenger1)
print(plane1)

passenger3 = Passenger("Joshua", "Brown", "Spain", "12.12.1995")
flightToMiami.window_seat(passenger3)
print(plane1)

flightToMiami.emergency_exit_row(passenger1)
print(plane1)


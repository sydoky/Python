class Car:
    def __init__(self, brand, series, color, mileage, price):
        self.brand = brand
        self.series = series
        self.color = color
        self.mileage = mileage
        self.price = price
        self.additional_equipment = [] #when we put in (), we have to provide. otherwise it's optional

    def __str__(self):
        return self.brand.name + " " + self.series.series + ", " + str(self.series.year) + ", " + self.color + ", " \
    + str(self.mileage) + ", $" + str(self.price)


class Company:
    def __init__(self, name, country, founded):
        self.name = name
        self.country = country
        self.founded = founded

    def __str__(self):
        return self.name + ", " + self.country + ", " + str(self.founded)

class Model:
    def __init__(self, series, horse_power, year, engine):
        self.series = series
        self.horse_power = horse_power
        self.year = year
        self.engine = engine

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.storage = []

    def __str__(self):
        cars = "" #we want to see in our display a string method
        for c in self.storage:
            cars += str(c) + "\n" #we add \n for a new line
        return self.name + ", " + self.address + "\n" + cars

    def add_car(self, car):
        self.storage.append(car)  # if =, means assign smth different, changing  # we don't deal with real objects inside of class definitions





Your_Nazi_car = Store("Your Nazi car", "Miami")
print(Your_Nazi_car)
S500 = Model("S500", 302, 2020, 5)
Mercedes = Company("Mercedes Benz", "Germany", 1926)
car2 = Car(Mercedes, S500, "black", 30, 45000)
print(car2)
M5 = Model("M5", 282, 2020, 4.1)
BMW = Company("BMW", "Germany", 1916)
print(BMW)
car1 = Car(BMW, M5, "red", 50, 50000)
print(car1)
print("--------")
Your_Nazi_car.add_car(car1)
Your_Nazi_car.add_car(car2)
print(Your_Nazi_car)
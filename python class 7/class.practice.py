class VisitedCities:
    def __init__(self, city, number_of_visits):
        self.city = city
        self.number_of_visits = number_of_visits


    def __str__(self):
        return "city: " + self.city + ", number_of_visits: " + self.number_of_visits

    def __int__(self): #int method will return numbers
        return self.number_of_visits

    def __eq__(self, other):
        equal_names = False
        if self.city == other.city:
            equal_names = True
        number_of_visits = False
        if self.number_of_visits == other.number_of_visits:
            number_of_visits = True
        return equal_names and number_of_visits

    def __gt__(self, other): #gt - greater than
        comparing_visits = False
        if self.number_of_visits > other.number_of_visits:
            comparing_visits = True
        return comparing_visits

    def __ge__(self, other): # ge - greater or equal
        return self == other or self > other



city1 = VisitedCities("Belgrad", 16)

city2 = VisitedCities("Moscow", 35)

city3 = VisitedCities("Miami", 25)

print(city3 < city2)

print(city1 == city2)

print(city1 > city2)

print(city1 <= city2)

print(int(city3))

print(int(city1))


trip = {
    "country": "USA",
    "city": "Los Angeles",
    "number_of_days": 15
}
print(trip["city"])

trip["city"] = "New York"
print(trip)





name = "appleandbananas"

print(name[:-1])

my_range = range(1, 5, 3)
my_list = list(my_range)
print(my_list)









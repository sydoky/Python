class Coin:
    def __init__(self, denomination, year, mintage, material, origin, grade, grade_level, price):
        self.denomination = denomination
        self.year = year
        self.mintage = mintage
        self.material = material
        self.origin = origin
        self.grade = grade
        self.grade_level = grade_level
        self.price = price

    def __str__(self):
        return self.denomination + ", " + str(self.year) + ", " + str(self.mintage) + ", " + self.origin + ", " \
               + self.grade.abbreviation + str(self.grade_level) + " $" + str(self.price)
    def __gt__(self, other):
        return self.age() > other.age() #we put () because it's a method , line 18


    def age(self):
        today = 2020
        today = today - self.year
        return str(today) + " years old"

class Grade:
    def __init__(self, level_of_finest, abbreviation, scale, description):
        self.level_of_finest = level_of_finest
        self.abbreviation = abbreviation
        self.scale = scale
        self.description = description

    def __gt__(self, other): #self will always be in the left and "other" on the right with comparison
        grades_level = {
            "VF": 1,
            "XF": 2,
            "AU": 3,
            "MS": 4
        }
        return grades_level[self.abbreviation] > grades_level[other.abbreviation]


    def __str__(self):
        return self.abbreviation + ", " + str(self.scale)

class Grades:
    def __init__(self):
        self.vf = Grade("very fine", "VF", [20, 25, 30, 35], "Moderate wear")
        self.xf = Grade("extremely fine", "XF", [40, 45], "well defined")
        self.au = Grade("almost uncirculated", "AU", [50, 53, 55, 58], "high points")
        self.ms = Grade("mint state", "MS", list(range(60, 71)), "perfect")


class Collection:
    def __init__(self, name):
        self.name = name
        self.coins = []

    def add_coin(self, coin):
        self.coins.append(coin)

    def remove(self, coin):
        self.coins.remove(coin)  # whatever we are in class, things do not exsit, those are just variables.

    def value(self):
        dollar = 0
        for v in self.coins:
            dollar = dollar + v.price
        return dollar

    def __str__(self):
        coins = self.name + ": "
        for c in self.coins:
            coins += "\n" + str(c) #we added "\n" to move coins in lines seperately each/ to make new lines
        return coins

    def oldest(self):
        oldest_coin = None
        for c in self.coins:
            if oldest_coin is None:
                oldest_coin = c
            else:
                if c > oldest_coin:
                    oldest_coin = c
        return oldest_coin

    def best_grade(self):
        highest_quality = None
        for q in self.coins:
            if highest_quality is None:
                highest_quality = q.grade
            else:
                if q.grade > highest_quality:
                    highest_quality = q.grade
        return highest_quality

    def lowest_mintage(self):
        more_rare = None
        for r in self.coins:
            if more_rare is None:
                more_rare = r.mintage
            else:
                if r.mintage < more_rare:
                    more_rare = r.mintage
        return more_rare

    def rarest_coin(self):
        rc = None #rc is the object/ rarest coin/ real coin
        for c in self.coins: #I loop through all coins
            if rc is None: #
                rc = c
            else:
                if c.mintage < rc.mintage:
                    rc = c
        return rc

    def lowest_mintage2(self):
        rarest_coin = self.rarest_coin()
        return rarest_coin.mintage

    def lowest_mintage3(self):
        return self.rarest_coin().mintage

    def highest_grade(self):
        best_coin = None
        for c in self.coins:
            if best_coin is None:
                best_coin = c.grade_level
            else:
                if c.grade_level > best_coin:
                    best_coin = c.grade_level
        return best_coin












grades = Grades()
coin1 = Coin("rouble",1913, 2000000,"silver","Russia",grades.ms, grades.ms.scale[2], 100)
print(coin1)
coin2 = Coin("kopek", 1924, 5000, "Copper", "USSR", grades.au, grades.au.scale[2], 15)
print(coin2)

coin3 = Coin("rouble", 1899, 10000, "silver", "Russia", grades.xf, grades.xf.scale[0], 30)
print(coin3)

Mycollection = Collection("My collection")
Mycollection.add_coin(coin1)
Mycollection.add_coin(coin2)
Mycollection.add_coin(coin3)

#Mycollection.coins.append(coin1)
print(Mycollection)

print(Mycollection.value())

#Mycollection.remove(coin2)
print(Mycollection)
print(Mycollection.value())

print(coin1.age())
print(coin2.age())

Mycollection.oldest()
print(Mycollection.oldest())

print("-----------")

print(Mycollection.best_grade())


print(Mycollection.lowest_mintage())


print(Mycollection.rarest_coin())

print(Mycollection.lowest_mintage2())

print(Mycollection.highest_grade())

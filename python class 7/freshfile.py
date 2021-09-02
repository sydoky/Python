#name, age, append person, do you want to add more person
'''
List_of_people = []
while True:
    name = input("Enter person's name: ")
    age = input("Enter person's age: ")
    add_person = {
        "name": name,
        "age": age
    }
    List_of_people.append(add_person)
    repeat = input("Would you like add another person?")
    if repeat.lower() not in ["yes", "y"]:
        break

print(List_of_people)

def max_age():
    oldest_guy = None
    max_age = None
    for person in List_of_people:
        if max_age is None:
            max_age = person["age"]
        else:
            if person["age"] > max_age:
                max_age = person["age"]
    return max_age
#how to change code to return "oldest_guy" instead of max_age,
# create a similar thing dynamically go through list of ages, create a list of ages, will be a loop,

def give_the_oldest():
    oldest_guy = None
    max_age = None
    for person in List_of_people:
        if max_age is None:
            max_age = person["age"]
        else:
            if person["age"] > max_age:
                max_age = person["age"]
    return max_age


give_the_oldest()

new_list = [1, 2, 3]
maxx = None
for m in new_list:
    if maxx is None:
        maxx = m
    else:
        if m > maxx:
            maxx = m
'''


ages = [15, 23, 18, 25, 65, 32, 13, 19]
Jones = []
for a in ages:
    Jone = {
        "name": "Jone",
        "age": a
    }
    Jones.append(Jone)
print(Jones)


import random
James = []
for a in ages:
    Jame = {
        "name": "Jame",
        "dob": 2020 - a
    }
    James.append(Jame)
print(James)


names = ["Jone", "Adam", "Britt", "Vasya", "Dasha", "John", "William", "Fiona", "David", "Kate"]
last_names = ["Brown", "Black", "Roomy", "Donny", "Trump", "Putin", "Jones", "Gagarin", "Smith", "Anderson"]
Persons = []
for people in range(100): #we assign here to do that 100 times
    Person = {
        "name": names[random.randint(0, 9)],
        "last name": last_names[random.randint(0, 9)],
        "age": ages[random.randint(0, 7)]
    }

    Persons.append(Person)
for p in Persons:  # we created this loop to print a separate line for each guy
    print(p)



names = ["Jone", "Adam", "Britt", "Vasya", "Dasha", "John", "William", "Fiona", "David", "Kate"]
last_names = ["Brown", "Black", "Roomy", "Donny", "Trump", "Putin", "Jones", "Gagarin", "Smith", "Anderson"]
Persons = []
for people in range(100): #we assign here to do that 100 times
    Person = {
        "name": names[random.randint(0, 9)],
        "last name": last_names[random.randint(0, 9)],
        "age": random.randint(15, 65)
    }

    Persons.append(Person)
for p in Persons:  # we created this loop to print a separate line for each guy
    print(p)

    # for hw create a list of  10 countries, randomly assign which country I will visit 1-10 countries.


list_countries = ["Russia", "Serbia", "USA", "Brazil", "Spain", "Mexico", "Canada", "Japan", "Germany", "China"]
bucket_list = []
for c in range(10):
    while True:
        country = list_countries[random.randint(0, 9)]
        country_already_in_list = False
        for item in bucket_list:
            if country in item.values():
                country_already_in_list = True
        if not country_already_in_list:
            break
    while True:
        my_bucket_list_number = random.randint(1, 10)
        number_already_in_list = False
        for item in bucket_list:
            if my_bucket_list_number in item.values():
                number_already_in_list = True
        if not number_already_in_list:
            break

    countries = {
        "country": country,
        "bucket list number": my_bucket_list_number

    }

    bucket_list.append(countries)
print("-----------------")

for c in bucket_list:
    print(c)



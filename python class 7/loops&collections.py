#coffee machine selection, name, type, size, amount of sugar, amount of milk
'''
coffee_with_cream = {
    "name": "black coffee with cream",
    "type": "hot coffee",
    "size": 240,
    "amount of sugar": 0,
    "amount of cream": 3
}
'''

coffee_with_cream_version2 = {
    "name": "black coffee with cream",
    "type": "hot coffee",
    "size": {"amount": 240, "unit": "ml"},
    "ingredients": {"main ingredient": "roast coffee"},
    "ingredients2": {"main ingredient2": "water"},
    "amount of sugar": {"amount": 0, "unit": "Tspoons"},
    "amount of cream": {"amount": 0, "unit": "scoops"},
    "amount of milk": {"amount": 4, "unit": "ounces"},
    "amount of ice": {'"amount': 0, "unit": "cup"},
    "flavor": {"amount": 0, "unit": "ml"},
    "water": {"amount": 0, "unit": "liter"}
}
#"make 5 types of coffee, make a coffee machine (list)", brand, water capacity, \
# sugar storage/capacity, cream capacity and so on, prices, accepting coins, bills, price,
#amount of water, grams of ground coffee,

iced_coffee = {
    "name": "iced coffee with cream",
    "type": "cold coffee",
    "size": {"amount": 360, "unit": "ml"},
    "amount of espresso": {"amount": 20, "unit": "gram"},
    "ingredients2": {"main ingredient2": "water"},
    "amount of sugar": {"amount": 0, "unit": "Tspoons"},
    "amount of cream": {"amount": 0, "unit": "scoops"},
    "amount of ice": {"amount": 1/2, "unit": "cup"},
    "amount of milk": {"amount": 4, "unit": "ounces"},
    "flavor": {"amount": 0, "unit": "ml"},
    "water": {"amount": 0, "unit": "liter"},
    "amount of chocolate": {"amount": 500, "unit": "gram"}
}

latte = {
    "name": "latte",
    "type": "hot",
    "size": {"amount": 360, "unit": "ml"},
    "ingredients": {"main ingredient": "dark roast espresso coffee"},
    "amount of sugar": {"amount": 0, "unit": "Tspoons"},
    "amount of milk": {"amount": 1/3, "unit": "cup"},
    "flavor": {"amount": 0, "unit": "ml"},  # vanilla
    "amount of ice": {"amount": 0, "unit": "cup"},
    "water": {"amount": 0, "unit": "liter"}

}

cuban_espresso = {
    "name": "cafecito",
    "type": "espresso",
    "size": {"amount": 35, "unit": "ml"},
    "ingredients": {"main ingredient": "espresso ground coffee"},
    "ingredients2": {"main ingredient2": "water"},
    "amount of sugar": {"amount": 1/4, "unit": "cup"},
    "amount of ice": {'"amount': 0, "unit": "cup"},
    "amount of milk": {"amount": 0, "unit": "ounces"},
    "flavor": {"amount": 0, "unit": "ml"},
    "water": {"amount": 0, "unit": "liter"}
}

cappuccino = {
    "name": "cappucino",
    "type": "hot",
    "size": {"amount": 360, "unit": "ml"},
    "ingredients": {"main ingredient": "roast coffee"},
    "amount of sugar": {"amount": 0, "unit": "Tspoons"},
    "amount of milk": {"amount": 4, "unit": "ounces"},
    "flavor": {"amount": 0, "unit": "ml"},  # vanilla
    "amount of ice": {'"amount': 0, "unit": "cup"},
    "water": {"amount": 0, "unit": "liter"}
}

caffe_mocha = {
    "name": "caffe mocha",
    "type": "hot",
    "size": {"amount": 360, "unit": "ml"},
    "amount of espresso": {"amount": 30, "unit": "gram"},
    "amount of chocolate": {"amount": 30, "unit": "gram"},
    "amount of sugar": {"amount": 0, "unit": "Tspoons"},
    "amount of milk": {"amount": 4, "unit": "ounces"},
    "amount of ice": {'"amount': 0, "unit": "cup"},
    "flavor": {"amount": 0, "unit": "ml"},
    "water": {"amount": 0, "unit": "liter"}  # {} is value
}

chocolate = {
    "name": "chocolate",
    "type": "hot",
    "size": {"amount": 360, "unit": "ml"},
    "amount of espresso": {"amount": 0, "unit": "gram"},
    "amount of chocolate": {"amount": 100, "unit": "gram"},
    "amount of sugar": {"amount": 20, "unit": "Tspoons"},
    "amount of milk": {"amount": 4, "unit": "ounces"},
    "amount of ice": {'"amount': 0, "unit": "cup"},
    "flavor": {"amount": 0, "unit": "ml"},
    "water": {"amount": 0, "unit": "liter"}  # {} is value
}
#coffee machine - amount of water, amount of milk, amount of ground coffee, amount of cream,
#flavors - vanilla, hazelnut, cream,

coffee_machine = {
    "name": "fast ride",
    "amount of ground coffee": {"amount": 2000, "unit": "gram"},
    "amount of water": {"amount": 5, "unit": "liter"},
    "amount of milk": {"amount": 5, "unit": "liter"},
    "amount of cream": {"amount": 1, "unit": "liter"},
    "amount of chocolate": {"amount": 500, "unit": "gram"},
    "amount of ice": {"amount": 30, "unit": "cup"}
}
coffee_choice = caffe_mocha  # coffee_choice is my all my dictionaries, one at a time
coffee_choice = iced_coffee
water_check = False
espresso_check = False
chocolate_check = False
sugar_check = False
milk_check = False
ice_check = False
flavor_check = False

if coffee_choice["water"]["amount"] <= coffee_machine["amount of water"]["amount"]:
    water_check = True
if coffee_choice["amount of espresso"]["amount"] <= coffee_machine["amount of ground coffee"]["amount"]:
    espresso_check = True
if coffee_choice["amount of chocolate"]["amount"] <= coffee_machine["amount of chocolate"]["amount"]:
    chocolate_check = True
if coffee_choice["amount of sugar"]["amount"] <= coffee_machine["amount of chocolate"]["amount"]:
    sugar_check = True
if coffee_choice["amount of milk"]["amount"] <= coffee_machine["amount of milk"]["amount"]:
    milk_check = True
if coffee_choice["amount of ice"]["amount"] <= coffee_machine["amount of ice"]["amount"]:
    ice_check = True


if water_check and espresso_check:
    print("I am making " + coffee_choice["name"])

#coffee choice is my key






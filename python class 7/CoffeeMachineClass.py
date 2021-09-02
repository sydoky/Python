GROUND_COFFEE = "ground coffee"
class CoffeeMachine:  # class always name singular
    def __init__(self, name):
        self.name = name
        self.milk = Ingredient("milk", 0, "ml")
        self.milk_capacity = 5000
        self.ground_coffee = Ingredient(GROUND_COFFEE, 0, "grams")
        self.ground_coffee_capacity = 5000
        self.water = Ingredient("water", 0, "ml")
        self.water_capacity = 10000
        self.ice = Ingredient("ice", 0, "ml")
        self.ice_capacity = 10000
        self.chocolate = Ingredient("chocolate", 0, "ml")
        self.chocolate_capacity = 2000
        self.sugar = Ingredient("sugar", 0, "grams")
        self.sugar_capacity = 2000
        self.cream = Ingredient("cream", 0, "ml")
        self.cream_capacity = 1000
    def __str__(self):
        return self.name + ": milk=" + str(self.milk.amount) + ", coffee=" + str(self.ground_coffee.amount) + ", water=" + \
    str(self.water.amount) + ", ice=" + str(self.ice.amount) + ", chocolate=" + str(self.chocolate.amount) + ", sugar=" + \
    str(self.sugar.amount) + ", cream=" + str(self.cream.amount)


    def add_water(self, water):
        if water.amount + self.water.amount > self.water_capacity:
            print("The water capacity is filled up")
        else:
            self.water.amount += water.amount
            print("Added", water.amount, water.unit, "to the coffee machine")
    def add_sugar(self, sugar):
        if sugar.amount + self.sugar.amount > self.sugar_capacity:
            print("The sugar capacity is filled up")
        else:
            self.sugar.amount += sugar.amount
            print("Added", sugar.amount, sugar.unit, "to the coffee machine")

    def add_milk(self, milk):
        if milk.amount + self.milk.amount > self.milk_capacity:
            print("The milk capacity is filled up")
        else:
            self.milk.amount += milk.amount #  self.milk is a how much milk I had had before I added
            print("Added", milk.amount, milk.unit, "milk to the coffee machine")
    def add_ice(self, ice):
        if ice.amount + self.ice.amount > self.ice_capacity:
            print("The ice capacity is filled up")
        else:
            self.ice.amount += ice.amount
            print("Added", ice.amount, ice.unit, "ice to the coffee machine")
    def add_groundcoffee(self, ground_coffee):
        if ground_coffee.amount + self.ground_coffee.amount > self.ground_coffee_capacity:
            print("The ground coffee is filled up")
        else:
            self.ground_coffee.amount += ground_coffee.amount
            print("Added", ground_coffee.amount, ground_coffee.unit, "ground coffee to the coffee machine")
    def add_cream(self, cream):
        if cream.amount + self.cream.amount > self.cream_capacity:
            print("The cream capacity is filled up")
        else:
            self.cream.amount += cream.amount
            print("Added", cream.amount, cream.unit, "cream to the coffee machine")


    def make_coffee(self, kind, cup):
        ingredients = kind.ingredients()  # coffee is a kind, we want to make sure we have enough ingredients before we make coffee
        machine_ingredients = self.ingredients()
        enough_ingredients = True
        total_ingredients = 0
        for ingredient in ingredients:
            for machine_ingredient in machine_ingredients:
                if ingredient.name == machine_ingredient.name:
                    total_ingredients += ingredient.amount
                    if ingredient.amount > machine_ingredient.amount:
                        print("missing", ingredient.name)
                        enough_ingredients = False
        if not enough_ingredients:
            print("Sorry, we ran out of ingredients")
        cup_size = cup.size
        cup_large_enough = cup_size >= total_ingredients
        cup_state = cup.state
        if cup_state == "dirty":
            print("The cup is disgusting. Please wash it, you filthy animal")
        cup_empty = True
        if cup.liquid is not None:
            cup_empty = False
        if not cup_empty:
            print("Are you crazy? That cup is already full, mf")
        if enough_ingredients and cup_large_enough and cup_state == "clean" and cup_empty:
            cup.liquid = kind
            print("making a perfect", kind.name)
            for ingredient in ingredients:
                for machine_ingredient in machine_ingredients:
                    if ingredient.name == machine_ingredient.name:
                        machine_ingredient.amount -= ingredient.amount



    def ingredients(self):
        i = []
        if self.ground_coffee is not None:
            i.append(self.ground_coffee)
        if self.water is not None:
            i.append(self.water)
        if self.milk is not None:
            i.append(self.milk)
        if self.ice is not None:
            i.append(self.ice)
        if self.chocolate is not None:
            i.append(self.chocolate)
        if self.sugar is not None:
            i.append(self.sugar)
        if self.cream is not None:
            i.append(self.cream)
        return i





class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return self.name + " " + str(self.amount) + " " + self.unit

class Coffee:
    def __init__(self, name="", ground_coffee=None, water=None, sugar=None, milk=None, ice=None, chocolate=None, cream=None):
        self.name = name
        self.ground_coffee = ground_coffee
        self.water = water
        self.sugar = sugar
        self.milk = milk
        self.ice = ice
        self.chocolate = chocolate
        self.cream = cream

    def __str__(self):
        return self.name

    def ingredients(self):
        i = []
        if self.ground_coffee is not None:
            i.append(self.ground_coffee)
        if self.water is not None:
            i.append(self.water)
        if self.milk is not None:
            i.append(self.milk)
        if self.ice is not None:
            i.append(self.ice)
        if self.chocolate is not None:
            i.append(self.chocolate)
        if self.sugar is not None:
            i.append(self.sugar)
        if self.cream is not None:
            i.append(self.cream)
        return i

    def show_ingredients(self):
        #list_of_ingredients = [] #we create an empty list when we want to change the original one or smth like that
        for l in self.ingredients():
            print(l)
class Cup:
    def __init__(self, size):
        self.size = size
        self.liquid = None
        self.state = "clean"

    def __str__(self):
        liquid = ""
        state = self.state + " "
        if self.liquid is not None:
            liquid = " of " + self.liquid.name
            state = ""
        return "A " + state + str(self.size) + "ml sized cup" + liquid

    def empty_cup(self):
        self.liquid = None
        self.state = "dirty"

    def wash_the_cup(self):
        self.state = "clean"
        print("washing the cup")





milk = Ingredient("milk", 2000, "ml")
ground_coffee = Ingredient(GROUND_COFFEE, 2000, "grams")
water = Ingredient("water", 5000, "ml")
chocolate = Ingredient("chocolate", 500, "grams")
cream = Ingredient("cream", 500, "ml")
ice = Ingredient("ice", 100, "ml")
sugar = Ingredient("sugar", 1000, "grams")


coffee_machine = CoffeeMachine("Fast Ride")

coffee_machine.add_milk(milk)

coffee_machine.add_groundcoffee(ground_coffee)

coffee_machine.add_water(water)

coffee_machine.add_sugar(sugar)

coffee_machine.add_ice(ice)

coffee_machine.add_cream(cream)

ground_coffee_e = Ingredient(GROUND_COFFEE, 35, "grams")
water_e = Ingredient("water", 50, "ml")
sugar_e = Ingredient("sugar", 15, "grams")
espresso = Coffee("espresso", ground_coffee=ground_coffee_e, water=water_e, sugar=sugar_e)

#icedcoffee = Coffee(GROUND_COFFEE, "water", "ice", "cream", 360)
ground_coffee_i = Ingredient(GROUND_COFFEE, 30, "grams")
water_i = Ingredient("water", 200, "ml")
ice_i = Ingredient("ice", 100, "ml")
cream_i = Ingredient("cream", 30, "ml")
iced_coffee = Coffee("iced coffee", ground_coffee=ground_coffee_i, water=water_i, ice=ice_i, cream=cream_i)
espresso.show_ingredients()

iced_coffee.show_ingredients()

print("----------------------------")


espresso.show_ingredients()

cup_of_drink = Cup(500)
print(cup_of_drink)

coffee_machine.make_coffee(espresso, cup_of_drink)
print(coffee_machine)

print(cup_of_drink)

cup_of_drink.empty_cup()
print(cup_of_drink)

coffee_machine.make_coffee(espresso, cup_of_drink)

cup_of_drink.wash_the_cup()
print(cup_of_drink)

coffee_machine.make_coffee(espresso, cup_of_drink)
print(cup_of_drink)

coffee_machine.make_coffee(iced_coffee, cup_of_drink)

coffee_machine.add_ice(ice)

coffee_machine.make_coffee(iced_coffee, cup_of_drink)









#create a drink method that will empty the cup and run/print "drinking X" (where the x will be the actual name of the drink)


'''

class Apple:
    def __init__(self):
        stock = []  # we are making list here.


class Iphone:
    def __init__(self, model, color, memory, memory_unit):
        self.model = model
        self.color = color
        self.memory = memory
        self.memory_unit = memory_unit


    def __str__(self):
        return self.model + " " + self.color + " " + str(self.memory) + "" + self.memory_unit

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_memory(self):
        return self.memory

    def get_memory_unit(self):
        return self.memory_unit


class Stock:
    def __init__(self):
        self.items = []
        self.size = 0  # how many items I have

    def add_item(self, item):
        self.items.append(StockItem(item))  # we want to make sure that if item exists in this line
        self.size += 1

    def item_exists(self, item):
        pass



class StockItem:
    def __init__(self, item, quantity=1, price_per_item=None, discount=0):
        self.item = item
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.discount = discount

    def add_item(self, item, quantity=1):  # by default we add an iphone
        self.item = item
        self.quantity = quantity

    def set_price_per_item(self, price_per_item):
        self.price_per_item = price_per_item

    def set_discount(self, discount):
        self.discount = discount












iphone12 = Iphone("Iphone 12", "gold", 256, "GB")

print(iphone12)



'''
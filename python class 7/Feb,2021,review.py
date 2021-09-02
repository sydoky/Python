class Soda:
    def __init__(self, type, flavor, amount, sugar_free, decaf, price):
        self.type = type
        self.flavor = flavor
        self.amount = amount
        self.sugar_free = sugar_free
        self.decaf = decaf
        self.price = price

    def get_type(self):
        return self.type

    def get_flavor(self):
        return self.flavor

    def get_amount(self):
        return self.amount

    def get_sugar_free(self):
        return self.sugar_free

    def get_decaf(self):
        return self.decaf

    def get_price(self):
        return self.price

    def __eq__(self, other):
        equal = self.get_type() == other.get_type()
        equal = equal and self.get_flavor() == other.get_flavor()
        equal = equal and self.get_amount() == other.get_amount()
        equal = equal and self.get_sugar_free() == other.get_sugar_free()
        equal = equal and self.get_decaf() == other.get_decaf()
        return equal

    # def __str__(self):
    #     return self.type + " " + self.flavor + " " + str(self.amount) + " " + str(self.sugar_free) + " " + \
    #            str(self.decaf) + " " + str(self.price)

    def __str__(self):
        sugar_free = ""
        if self.sugar_free:
            sugar_free = "sugar free,"
        decaf = ""
        if self.decaf:
            decaf = "decaf,"
        return "{}, {}, {}, {} {} ${}".format(self.type, self.flavor, self.amount, sugar_free, decaf, self.price)


class Amount:
    def __init__(self, amount, units):
        self.amount = amount
        self.units = units

    def __str__(self):
        return "{} {}".format(self.amount, self.units)

    def get_amount(self):
        return self.amount

    def get_units(self):
        return self.units

    def __eq__(self, other):
        return self.get_amount() == other.get_amount() and self.get_units() == other.get_units()

class Pack:
    def __init__(self, item, items_per_pack, pack_discount):
        self.type = item.get_type()
        self.items_per_pack = items_per_pack
        self.flavor = item.get_flavor()
        self.amount = item.get_amount()
        self.sugar_free = item.get_sugar_free()
        self.decaf = item.get_decaf()
        self.price = (item.get_price() * items_per_pack) - (item.get_price() * items_per_pack) * (pack_discount / 100)
        self.items = []
        self.filled_pack()

    def get_type(self):
        return self.type

    def get_flavor(self):
        return self.flavor

    def get_amount(self):
        return self.amount

    def get_sugar_free(self):
        return self.sugar_free

    def get_decaf(self):
        return self.decaf

    def get_price(self):
        return self.price

    def __str__(self):
        sugar_free = ""
        if self.sugar_free:
            sugar_free = "sugar free,"
        decaf = ""
        if self.decaf:
            decaf = "decaf coke,"

        return "{}, {} pack, {}, {}, {} {} ${}".format(self.type, self.items_per_pack, self.flavor, self.amount,
                                                       sugar_free, decaf, self.price)

    def filled_pack(self):
        for item in range(self.items_per_pack):
            soda = Soda(self.type, self.flavor, self.amount, self.sugar_free, self.decaf,
                        self.price / self.items_per_pack)
            self.items.append(soda)

    def show(self):
        for item in self.items:
            print(item)

    def remove_item(self):
        return self.items.pop()

    def add_item(self, soda):
        if self.pack_not_full():
            self.items.append(soda)
            print("Adding {} to the pack".format(soda))
        else:
            print("The pack is already full")

    def add_items(self, sodas):
        for soda in sodas:
            self.add_item(soda)

    def pack_not_full(self): #we detect if the pack is full
        return self.items_per_pack > len(self.items)

    def move_items(self, pack):
        if self == pack:
            for item in range(len(self.items)):
                if pack.pack_not_full(): #first we check the space in the pack
                    soda = self.remove_item()
                    pack.add_item(soda)

    def __eq__(self, other): #eq = equal
        equal = self.get_type() == other.get_type() #other will be "soda can"
        equal = equal and self.get_flavor() == other.get_flavor()
        equal = equal and self.get_amount() == other.get_amount()
        equal = equal and self.get_sugar_free() == other.get_sugar_free()
        equal = equal and self.get_decaf() == other.get_decaf()
        return equal

# create more packs in the real world and play with moving
class Storage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.items = []

    def __str__(self):
        return "{}, {}/{}".format(self.name, len(self.items), self.capacity)

    def add(self, pack):
        if self.capacity > len(self.items):
            self.items.append(pack)
            print("Adding {} to the storage".format(pack))
        else:
            print("Storage is full")

    def remove(self):
        if len(self.items) > 0:
            print("Removing a pack from the storage")
            return self.items.pop()
        print("You cannot remove an item from an empty storage")

    def pack_exist(self, item):
        for i in self.items:
            if i == item:
                return True
        return False

    def find(self, item):
        for it in self.items:
            if it == item:
                return it

    def pack_count(self, item):
        counter = 0
        for ite in self.items:
            if ite == item:
                counter += 1
        return counter



coke = Soda("regular", "no flavor", Amount(0.5, "Liter"), False, False, 2.00)
decaf_coke = Soda("decaf", "no flavor", Amount(0.33, "Liter"), False, True, 2.00)
fanta = Soda("diet", "orange", Amount(1, "Liter"), True, False, 1.5)
sprite = Soda("regular", "cranberry", Amount(0.33, "Liter"), False, False, 1.15)

print(coke)
print(decaf_coke)
print(fanta)
coke_six_pack = Pack(coke, 6, 15)
fanta_six_pack = Pack(fanta, 6, 17)
sprite_six_pack = Pack(sprite, 6, 10)
print(coke_six_pack.price)
print(coke_six_pack)
coke_six_pack.show()
fanta_six_pack.show()
sprite_six_pack.show()

storage1 = Storage("Great Value", 2)
storage1.add(coke_six_pack)
storage1.add(fanta_six_pack)
storage1.add(sprite_six_pack)
print("--------------------")
fanta_can = fanta_six_pack.remove_item()
print(fanta_can)
print("--------------------")
fanta_six_pack.show()
print("--------------------")
fanta_can = fanta_six_pack.remove_item()
print(fanta_can)
print("--------------------")
fanta_six_pack.show()

print("--------------------")
fanta_six_pack.add_item(fanta_can)
fanta_six_pack.show()

print("--------------------")
print("--------------------")
fanta1 = Soda("diet", "orange", Amount(1, "Liter"), True, False, 1.5)
fanta2 = Soda("diet", "orange", Amount(1, "Liter"), True, False, 1.5)
fanta3 = Soda("diet", "orange", Amount(1, "Liter"), True, False, 1.5)

coke1 = Soda("diet", "vanilla", Amount(2, "Liter"), True, False, 2.0)
coke2 = Soda("diet", "vanilla", Amount(2, "Liter"), True, False, 2.0)
coke3 = Soda("diet", "vanilla", Amount(2, "Liter"), True, False, 2.0)

sprite1 = Soda("regular", "lemon", Amount(0.33, "Liter"), False, False, 1.2)
sprite2 = Soda("regular", "lemon", Amount(0.33, "Liter"), False, False, 1.2)
sprite3 = Soda("regular", "lemon", Amount(0.33, "Liter"), False, False, 1.2)



fantas = [fanta1, fanta2, fanta3]
fanta_six_pack.add_items(fantas)
print(fantas)

print("%%%%%%%%%%%")

fanta_six_pack.remove_item()
fanta_six_pack.remove_item()
fanta_six_pack.remove_item()
fanta_six_pack.show()

print("%%%%%%%%%%%")
coke_six_pack.move_items(fanta_six_pack)
print("%%%%%%%%%%%")
fanta_six_pack.show()

print("((((((((((((((((((((((((((((((")
print(fanta_six_pack == fanta1)

print(storage1)
print("fanta exists", storage1.pack_exist(fanta1))
print(storage1.find(fanta1))
print(storage1.pack_count(fanta1))
print(storage1.pack_count(sprite1))
print(storage1.pack_count(coke))
print(storage1.items[0])
print(storage1.items[1])
storage1.remove()
print(storage1)

storage1.remove()
print(storage1)

storage1.remove()
print(storage1)

print("fanta exists: ", storage1.pack_exist(fanta1))

print(storage1.find(fanta1))




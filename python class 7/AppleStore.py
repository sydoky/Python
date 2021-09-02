class Apple:
    def __init__(self):
        self.stock = Stock()  # we are making list here.
        self.shopping_cart = []

    def __str__(self):
        return str(self.stock)

    def add_to_stock(self, item, quantity=1):
        self.stock.add_item(item, quantity)

    def create_shopping_cart(self):  # online shopping
        self.shopping_cart.append(ShoppingCart())
        return self.shopping_cart[-1]  # add -1 cause Shoppingcart is end of the list and we want to return the last one

    def buy(self, shopping_cart, item):
        if self.stock.item_exists(item):
            item = self.stock.get_stock_item(item)
            if item.get_price_per_item() is not None:
                shopping_cart.add_item(item)
            else:
                print("Price is not set yet for", str(item))
        else:
            print("Out of stock")
    def set_price(self, item, price):
        if self.stock.item_exists(item):
            item = self.stock.get_stock_item(item)
            item.set_price_per_item(price)
        else:
            print("The price cannot be set. Item is not available.")


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

    def __str__(self):
        string = "stock:\n"  # \n is a new line
        for stock_item in self.items:
            string += str(stock_item) + "\n"
        return string

    def add_item(self, item, quantity=1):
        if self.item_exists(item):
            self.get_stock_item(item).add_item(item, quantity)
        else:
            self.items.append(StockItem(item))  # we want to make sure that if item exists in this line
            self.size += 1

    def item_exists(self, item):
        for stock_item in self.items:  # line above init
            if stock_item.get_item(item).model == item.model:
                return True
        return False

    def get_stock_item(self, item):
        for stock_item in self.items:
            if stock_item.get_item(item).model == item.model:
                return stock_item


class StockItem:
    def __init__(self, item, quantity=1, price_per_item=None, discount=0):
        self.item = item
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.tax = 0.07
        self.discount = discount
        self.available_colors = [item.get_color()]

    def __str__(self):
        string = ""
        for i in self.available_colors:
            string += i + ", "
        return str(self.item.get_model()) + " " + str(self.quantity) + " available in colors: " \
               + string

    def add_item(self, item, quantity=1):  # by default we add an iphone
        self.increase_quantity(quantity)
        print(item.get_color())
        if not self.color_exists(item.get_color()):
            self.available_colors.append(item.get_color())

    def color_exists(self, color):
        return color in self.available_colors

    def get_price_per_item(self):
        return self.price_per_item

    def set_price_per_item(self, price_per_item):
        self.price_per_item = price_per_item

    def set_discount(self, discount):
        self.discount = discount

    def increase_quantity(self, quantity=1):
        self.quantity += quantity

    def get_item(self, item):
        return self.item

    def get_tax(self):
        return self.tax


class ShoppingCart:
    def __init__(self):
        self.shopping_items = []  # we created another self.shopping_cart in apple class after this one
        self.pretax_total = 0
        self.total = 0

    def __str__(self):
        string = "shopping cart:\n"
        for shopping_cart in self.shopping_items:
            string += str(shopping_cart) + "\n"
        string += "pre tax total: $" + str(self.pretax_total) + "\n"
        string += "total: $" + str(self.total) + "\n"
        return string  # we never ever put return inside of for without condition

        #return str(self.shopping_items)  # every time when you want to use a string method to return a list, you must loop thru it

    def add_item(self, item):
        self.shopping_items.append(item)  # we are connecting this line to Apple class
        price = item.get_price_per_item()
        self.add_price_to_total(price)
        self.update_total(price + price * item.get_tax())

    def add_items2(self, items):
        for item in items:
            self.add_item(item)

    def add_items(self, *items):
        for item in items:
            self.add_item(item)

    def checking_shopping_cart(self, item):
        for c in self.shopping_items:
            if item == c:
                return True
        return False

    def remove_item(self, item):
        if self.checking_shopping_cart(item):
            self.shopping_items.remove(item)

    def add_price_to_total(self, price):
        self.pretax_total += price

    def update_total(self, price):
        self.total += price



store = Apple()

iphone12pro = Iphone("Iphone 12 pro", "pacific blue", 512, "GB")
iphone12 = Iphone("Iphone 12", "gold", 256, "GB")
store.add_to_stock(iphone12)
iphone11pro = Iphone("Iphone 11 pro", "silver", 128, "GB")
ipad = Iphone("Ipad Pro", "black", 256, "GB")
iphone12 = Iphone("Iphone 12", "silver", 256, "GB")
store.add_to_stock(iphone12)
iphone12 = Iphone("Iphone 12", "silver", 256, "GB")



print(iphone12)


#  print(store.stock.items[0].item.model)
store.add_to_stock(iphone12)
store.add_to_stock(iphone12pro)
store.add_to_stock(iphone11pro)
store.add_to_stock(ipad)
ipad = Iphone("Ipad Pro", "black", 256, "GB")
store.add_to_stock(ipad)
iphone12 = Iphone("Iphone 12", "white", 256, "GB")
store.add_to_stock(iphone12)
ipad = Iphone("Ipad Pro", "red", 256, "GB")
store.add_to_stock(ipad)
print(store)

My_shopping_cart = store.create_shopping_cart()
'''My_shopping_cart.add_item(ipad)
print(My_shopping_cart)

My_shopping_cart.add_items(ipad, iphone12, iphone11pro, iphone12pro)
My_shopping_cart.add_items2([iphone12pro, ipad, iphone11pro])
print(My_shopping_cart)

My_shopping_cart.remove_item(ipad)
print(My_shopping_cart)

My_shopping_cart.remove_item(ipad)
print(My_shopping_cart)

My_shopping_cart.remove_item(ipad)
print(My_shopping_cart)

My_shopping_cart.remove_item(ipad)
print(My_shopping_cart)'''

store.buy(My_shopping_cart, ipad)
print(My_shopping_cart)
store.set_price(ipad, 1000)
store.buy(My_shopping_cart, ipad)
print(My_shopping_cart)
store.set_price(iphone12, 1250)
store.buy(My_shopping_cart, iphone12)
print(My_shopping_cart)


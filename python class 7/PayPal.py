class PayPal:
    def __init__(self, id, email, name, balance):
        self.id = id
        self.email = email
        self.name = name
        self.balance = balance
        self.is_active = False
        self.items = []

    def buyitem(self, item_name, seller):
        item = None
        amount = None
        for product in seller.items:
            if item_name in product:
                amount = product[item_name]
        if amount == None:
            print("seller does not have that item")
            return
        if self.sendmoney(amount, seller):
            for product in seller.items:
                if item_name in product:
                    item = product
                    item["owner"] = self.name
                    seller.items.remove(product)
                    self.items.append(item)
                    print("Sending", item_name, "from ", seller.name, "to ", self.name)

    def borrowitem(self, item_name, item_owner):
        item = None
        for product in item_owner.items:
            if item_name in product:
                item = product
        if item == None:
            print("borrower does not have that item")
            return
        for product in item_owner.items:
            if item_name in product:
                item = product
                item_owner.items.remove(product)
                self.items.append(item)
                print("Borrowing", item_name, "from ", item_owner.name, "to ", self.name)

    def returnitem(self, item_name):
        item = None
        for product in self.items:
            if item_name in product:
                item = product
        if item == None:
            print(self.name, "does not have that item")
            return
        for product in self.items:
            if item_name in product:
                item = product
                owner = None
                for user in paypal_users:
                    if user.name == item["owner"]:
                        owner = user
                self.items.remove(product)
                owner.items.append(item)
                print("Returning borrowed item", item_name, "from ", self.name, "to ", item["owner"])







    def additem(self, item):
        item["owner"] = self.name
        self.items.append(item)
        print(item, "has been added to", self.name, "'s list of items")


    def info(self):
        active = "inactive"
        if self.is_active:
            active = "active"
        print("id:", self.id, ", name:", self.name, ", email:", self.email, ", balance: $", self.balance, ", is active:", active, ", list of items", self.items)

    def activate(self):
        if self.is_active:
            print("Error404. The account is already activated ")
        else:
            print("activated account", self.id)
            self.is_active = True

    def deactivate(self):
        if self.is_active == False:
            print("This account is already deactivated")
        else:
            print("The deactivated account", self.id)
            self.is_active = False

    def sendmoney(self, amount, receiver):
        if amount <= 0:
            print("gotcha mr.robot")
            return
        if self.is_active == False:
            print("error404! sender's account is not active")
            return
        if receiver.is_active == False:
            print("error404! receiver's account is not active")
            return

        if self.balance >= amount:
            if receiver != None:
                self.balance -= amount
                receiver.balance += amount
                print("Sum of $", amount, "has been transferred from ", self.name, " to ", receiver.name)
                return True
        else:
            print("Not enough balance")
            return


    def addmoney(self, amount):
        self.balance += amount
        print("The amount of ", amount, " has been added to ", self.name)






account1 = PayPal(1, "email@mail.ru", "Vasya", 200.20)
account1.info()

account2 = PayPal(2, "cat@gmail.com", "Bill Gates", 5.05)
account2.info()

account3 = PayPal(3, "notvasya@notgmail.com", "Marko", 500)

paypal_users = [account1, account2, account3]

account2.activate()
account2.info()

account1.deactivate()

account1.activate()
account1.info()

account1.deactivate()
account1.info()



account2.sendmoney(10, account1)

account1.sendmoney(10, account2)

account2.info()

account1.info()

account2.sendmoney(-190, account1)

account2.info()
account1.info()

account1.activate()
account1.sendmoney(10, account2)


item1 = {
    "book": 50,
    "owner": ""
}

item2 = {
    "magazine": 14.99,
    "owner": ""
}

item3 = {
    "coffee": 2.99,
    "owner": ""
}

item4 = {
    "puzzle game": 20,
    "owner": ""
}

item5 = {
    "pen": 0.99,
    "owner": ""
}

item6 = {
    "eraser": 1.99,
    "owner": ""

}

item7 = {
    "poster": 15.00,
    "owner": ""
}

item8 = {
    "whiteout": 7.00,
    "owner": ""
}

account1.additem(item1)
account1.info()

account1.additem(item3)
account1.info()


account2.additem(item6)
account2.info()

account2.additem(item4)
account2.info()

account1.buyitem("eraser", account2)
account1.info()
account2.info()

account1.buyitem("book", account2)

account2.buyitem("book", account1)
account2.info()
account1.info()


account2.buyitem("book", account1)
account2.info()


account2.addmoney(35)
account2.info()

account2.buyitem("book", account1)
account2.info()

account1.info()

account1.buyitem("book", account2)
account1.info()

account1.deactivate()
account2.buyitem("coffee", account1)

account3.additem(item8)
account3.info()

account3.activate()
account3.info()

account3.additem(item7)
account3.info()


account3.buyitem("book", account1)
account3.info()

account1.activate()
account1.info()

account3.buyitem("book", account1)
account3.info()
account1.info()


account1.borrowitem("book", account3)

account1.info()

account1.returnitem("book")

account1.info()
account3.info()
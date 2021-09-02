class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle" + ", " + str(self.width) + ", " + str(self.height)

    def surface(self):
        return self.width * self.height

    def __eq__(self, other):
        if self.surface() == other.surface(): #you cannot put anything inside the () because we define everything in line 9
            return True
        else:
            return False
    def __gt__(self, other):
        if self.surface() > other.surface():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.surface() < other.surface():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.surface() >= other.surface():
            return True
        else:
            return False

    def __le__(self, other):
        if self.surface() <= other.surface():
            return True
        else:
            return False




        #for hw less, greater than equal and less than equal


rec1 = Rectangle(16, 20)
print(rec1)
rec2 = Rectangle(20, 15)
print(rec2)

multiplication = rec1.surface()
print(multiplication)

multiplication = rec2.surface()
print(multiplication)

print(rec1 == rec2)

print(rec1 > rec2)

print(rec1 < rec2)

print(rec1 >= rec2)

print(rec1 <= rec2)










































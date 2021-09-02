class A:
    def __init__(self):
        self.name = "A"
        self.nested_object = None

    def __str__(self):
        return self.name


class B:
    def __init__(self):
        self.name = "B"
        self.nested_object = None

    def __str__(self):
        return self.name


class C:
    def __init__(self):
        self.name = "C"
        self.nested_object = None

    def __str__(self):
        return self.name

Ob1 = A()
Ob2 = B()
Ob3 = C()
Ob4 = A()
Ob5 = C()


Ob1.nested_object = Ob2
Ob2.nested_object = Ob3
print(Ob1.nested_object.nested_object)

Ob3.nested_object = Ob4
Ob4.nested_object = Ob5
print(Ob2.nested_object.nested_object.nested_object)

class TransportVehicle:
    def __init__(self, color, v_type, number_of_wheels, fuel_type):
        self.color = color.title()
        self.v_type = v_type
        self.number_of_wheels = number_of_wheels
        self.fuel_type = fuel_type
        self.started = False

    def __str__(self):
        return "{} {} with {} wheels, runs on {}".format(self.color, self.v_type, self.number_of_wheels, self.fuel_type)

    def paint(self, color):
        print("Painting {} {} into {}".format(self.color, self.v_type, color))
        self.color = color.title()

    def start(self):
        if not self.started:
            print("Starting {} {}".format(self.color, self.v_type))
            self.started = True
        else:
            print("Cannot start {} {} because it is already running".format(self.color, self.v_type))

    def drive(self):
        if self.started:
            print("Driving {} {}".format(self.color, self.v_type))
        else:
            print("{} {} is not running yet".format(self.color, self.v_type))

    def stop(self):
        if self.started:
            print("Stopping {} {}".format(self.color, self.v_type))
            self.started = False
        else:
            print("Cannot stop {} {} because it is already stopped".format(self.color, self.v_type))


class Motorcycle(TransportVehicle):
    def __init__(self, color, number_of_wheels, fuel_type, required_license):
        super().__init__(color, "motorcycle", number_of_wheels, fuel_type)
        self.required_license = required_license

    def __str__(self):
        return "{}, the license is {}".format(super().__str__(), "required" if self.required_license else "not required")


class Car(TransportVehicle):
    def __init__(self, color, number_of_wheels, fuel_type, number_of_doors):
        super().__init__(color, "car", number_of_wheels, fuel_type)
        self.number_of_doors = number_of_doors

    def __str__(self):
        return "{}, it has {} door/s".format(super().__str__(), self.number_of_doors)


car1 = Car("blue", 4, "gas", 4)
print(car1)
motorcycle1 = Motorcycle("black", 2, "gas", False)
print(motorcycle1)
car1.paint("orange")
print(car1)
motorcycle1.paint("pink")
print(motorcycle1)

car1.drive()

car1.start()
car1.drive()
car1.stop()
car1.drive()
car1.start()
car1.drive()
car1.start()



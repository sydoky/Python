from abc import abstractmethod, ABC


class TransportVehicle(ABC):
    def __init__(self, color, v_type, number_of_wheels, fuel_type, tire_type):
        self.color = color.title()
        self.v_type = v_type
        self.number_of_wheels = number_of_wheels
        self.fuel_type = fuel_type
        self.tire_type = tire_type
        self.started = False
        self.locked = True

    def __str__(self):
        return "{} {} with {} wheels, runs on {}".format(self.color, self.v_type, self.number_of_wheels, self.fuel_type)

    @abstractmethod
    def change_tire(self, tire):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def refill_gas(self, gas):
        pass

    @abstractmethod
    def lock(self, key):
        pass

    @abstractmethod
    def unlock(self, key):
        pass

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
    def __init__(self, color, number_of_wheels, fuel_type, required_license, tire_type):
        super().__init__(color, "motorcycle", number_of_wheels, fuel_type, tire_type)
        self.required_license = required_license

    def __str__(self):
        return "{}, the license is {}".format(super().__str__(), "required" if self.required_license else "not required")

    def change_tire(self, tire):
        if tire.tire_type == self.tire_type:
            print("Changing the motorcycle tire")
        else:
            print("You have to use only a motorcycle tire")

    def register(self):
        print("The motorcycle is now registered.")

    def refill_gas(self, gas):
        if gas.type_of_gas == self.fuel_type:
            print("Motorcycle tank is full now")
        else:
            print("You cannot use {} in the motorcycle which runs on {}".format(gas.type_of_gas, self.fuel_type))

    def lock(self, key):
        if isinstance(key, MotorKey):  # we don't want to use the car key to lock the motorcycle
            if self.locked:
                print("The motorcycle is already locked")
            else:
                key.use()
                print("The motorcycle is now locked")
        else:
            print("You need a motorcycle key for locking the motorcycle")

    def unlock(self, key):
        if isinstance(key, MotorKey):
            if not self.locked:
                print("The motorcycle is unlocked")
            else:
                key.use()
                print("The motorcycle is now unlocked")
        else:
            print("You need a motorcycle key to open the motorcycle")


class Car(TransportVehicle):
    def __init__(self, color, number_of_wheels, fuel_type, number_of_doors, tire_type):
        super().__init__(color, "car", number_of_wheels, fuel_type, tire_type)
        self.number_of_doors = number_of_doors

    def __str__(self):
        return "{}, it has {} door/s".format(super().__str__(), self.number_of_doors)

    def change_tire(self, tire):
        if tire.tire_type == self.tire_type:
            print("Changing the car tire")
        else:
            print("You have to use a car tire only")

    def register(self):
        print('The car is now registered.')

    def refill_gas(self, gas):
        if gas.type_of_gas == self.fuel_type:
            print("Car tank is full now")
        else:
            print("You cannot use {} in the car that runs {}".format(gas.type_of_gas, self.fuel_type))

    def lock(self, key):
        if isinstance(key, CarKey):
            if self.locked:
                print("The car is already locked")
            else:
                key.use()
                print("The car is now locked")
        else:
            print("You need a car key for locking the car")

    def unlock(self, key):
        if isinstance(key, CarKey):
            if not self.locked:
                print("The car is unlocked")
            else:
                key.use()
                print("The car is now unlocked")
        else:
            print("You need a car key to open the car")


class Key(ABC):
    def __init__(self, type_of_key):
        self.type_of_key = type_of_key

    @abstractmethod
    def use(self):
        pass

class MotorKey(Key):
    def __init__(self):
        super().__init__("motor key")

    def use(self):
        print("Using the motor key")


class CarKey(Key):
    def __init__(self):
        super().__init__("car key")

    def use(self):
        print("Using the car key")

class Gas(ABC):
    def __init__(self, type_of_gas):
        self.type_of_gas = type_of_gas

    @abstractmethod
    def pumping_gas(self):
        pass

class Diesel(Gas):
    def __init__(self):
        super().__init__("diesel")

    def pumping_gas(self):
        print("Pumping diesel gas")

class Unleaded(Gas):
    def __init__(self):
        super().__init__("unleaded gas")

    def pumping_gas(self):
        print("Pumping unleaded gas")

class Tire(ABC):
    def __init__(self, tire_type):
        self.tire_type = tire_type

    @abstractmethod
    def change_tire(self):
        pass

class CarTire(Tire):
    def __init__(self):
        super().__init__("car tire")

    def change_tire(self):
        print("Changing the car tire")

class MotorcycleTire(Tire):
    def __init__(self):
        super().__init__("motorcycle tire")

    def change_tire(self):
        print("Changing the motorcycle tire")


car1 = Car("blue", 4, "diesel", 4, "car tire")
print(car1)
motorcycle1 = Motorcycle("black", 2, "unleaded gas", False, "motorcycle tire")
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

#car1.change_tire()

car1.stop()

print('-----------------------')


def start_vehicle(vehicle):  # this is a polymorphic function
    vehicle.register()

def refill_vehicle(vehicle, gas):
    vehicle.refill_gas(gas)

def changing_tire_vechicle(vehicle, tire):
    vehicle.change_tire(tire)

start_vehicle(motorcycle1)
start_vehicle(car1)

#car1.refill_gas() this is not a polyomorphic way
diesel = Diesel()
unleaded = Unleaded()
refill_vehicle(motorcycle1, unleaded)
refill_vehicle(car1, unleaded)
refill_vehicle(motorcycle1, diesel)
refill_vehicle(motorcycle1, unleaded)

tire_m = MotorcycleTire()
tire_c = CarTire()

car_key = CarKey()
motorcycle_key = MotorKey()

car1.lock(car_key)
car1.unlock(motorcycle_key)

changing_tire_vechicle(car1, tire_c)
changing_tire_vechicle(motorcycle1, tire_m)
changing_tire_vechicle(car1, tire_m)
changing_tire_vechicle(motorcycle1, tire_c)







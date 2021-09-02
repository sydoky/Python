class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.name + str(self.damage)


class Creature:
    def __init__(self, name, speed, x, y, weapon):
        self.name = name
        self.speed = speed
        self.initial_x_position = x
        self.initial_y_position = y
        self.x = x
        self.y = y
        self.weapon = weapon


    def swap_weapon(self, creature):
        temp_weapon = self.weapon
        self.weapon = creature.weapon
        creature.weapon = temp_weapon
        print("Swapping the weapons of", self.name, "and", creature.name)

    def __str__(self):
        return "name: " + self.name + ", speed: " + str(self.speed) + " x: " + str(self.x) + " y: " + str(self.y) + " weapon: " + str(self.weapon)

    def move(self, x, y):
        print("Moving", self.name, "from coordinates: (", str(self.x), ",", str(self.y), ") to coordinates: (", str(x),
              ",", str(y), ")")
        self.x = x
        self.y = y


    def reset_position(self):
        self.x = self.initial_x_position
        self.y = self.initial_y_position

    def set_speed(self, speed):
        self.speed = speed

    def change_name(self, new_name):
        self.name = new_name



bat = Weapon("Bat", 5)
lazer_gun = Weapon("Lazer Gun", 15)

zombie_c = Creature("zombie", 3, 0, 0, lazer_gun)
ghost_c = Creature("ghost",5, 400, 200, bat)
blue_g = Creature("blue ghost", 5, 0, 0, Weapon("Lazer Gun", 25))
print("---------------")
print(zombie_c)
print(ghost_c)
print("----BEFORE SWAP----")
print(zombie_c)
print(blue_g)
zombie_c.swap_weapon(blue_g)
print("----AFTER SWAP----")
print(zombie_c)
print(blue_g)
#blue_g.swap_weapon(zombie_c)

print("---------------")
zombie_c.move(150,50)
zombie_c.set_speed(9)
print(zombie_c)

ghost_c.reset_position()

zombie_c.reset_position()
zombie_c.change_name("Cool Zombie")
print()
print(zombie_c)
blue_g.change_name("Azure Ghost")
print(blue_g)


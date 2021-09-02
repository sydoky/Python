class Door:
    def __init__(self, color):
        self.color = color
        self.is_open = False
    def open(self):
        self.is_open = True #this is how I open the door
    def close(self):
        self.is_open = False #this is how I close the door
    def check_if_it_is_open(self):
        if self.is_open:
            print(self.color, " door is open")
        else:
            print(self.color, " door is closed")

red_door = Door("Red") #it refers to line 2 color
blue_door = Door("Blue")
red_door.check_if_it_is_open()
red_door.open()
red_door.check_if_it_is_open()
blue_door.check_if_it_is_open()
blue_door.open()
blue_door.check_if_it_is_open()

red_door.check_if_it_is_open()
red_door.close()

blue_door.check_if_it_is_open()
blue_door.close()

blue_door.check_if_it_is_open()
red_door.check_if_it_is_open()
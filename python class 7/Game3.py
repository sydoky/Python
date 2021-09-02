import pygame
pygame.init()
import random


display_width = 1200
display_height = 900
col_num = display_width//100
row_num = display_height//100
BLACK = (0, 0, 0) #rgb (red, green, black) is a code,  background color
WHITE = (255, 255, 255) #intensity of color up to 255
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
display_background_color =(BLACK) # variable that we use
game_display = pygame.display.set_mode((display_width, display_height))     # tuple inside the ()
pygame.display.set_caption("Misha's game")
clock = pygame.time.Clock()
game_speed = 60
robot_speed = 7
counter = 0     # counter start with 0 sec. at the end check
robot_image = pygame.image.load("robot-icon-7.png")
ghost_image = None
heart_image = pygame.image.load("heart.png")
gray_ghost_image = None
blue_ghost_image = None
zombie_image = None
robot_width = 64
robot_height = 64
heart_width = 24
heart_height = 24
robot_image = pygame.transform.scale(robot_image,(robot_width, robot_height))   # to create the size of robot more flexible
heart_image = pygame.transform.scale(heart_image,(heart_width, heart_height))
creatures = [] #making a list
def create_creatures(name, speed, x, y, width, height, image): # making dictionary
    creature = {}
    creature["name"] = name
    creature["speed"] = speed
    creature["initial x"] = x
    creature["initial y"] = y
    creature["x"] = x
    creature["y"] = y
    creature["move"] = (0, 0)
    creature["width"] = width
    creature["height"] = height
    creature["image"] = pygame.image.load(image)
    creature["image"] = pygame.transform.scale(creature["image"], (width, height))
    creatures.append(creature)

create_creatures(
    "zombie",
    1,  # speed
    (display_width//12)*5 + (display_width//12 - 64)//2,      # zombie x, 64 is the width!
    (display_height//9)*5 + (display_height//9 - 64)//2,     # zombie y 64 is the height!
    64,  # width
    64,  # height
    "zombie.png"
)
create_creatures(
    "white ghost",
    2,  # speed
    display_width,  # ghost_x
    0,  # ghost_y
    24,  # ghost_width
    24, # ghost_height
    "white-ghost.png"
)

create_creatures(
    "blue ghost",
    1,  # speed
    0,  # blue ghost x
    0,  # blue ghost y
    24,  # blue ghost width
    24,   # blue ghost height
    "blue.png"
)
create_creatures(
    "gray ghost",
    2,  # speed
    0,  # gray ghost x
    display_height - 24,  # gray ghost y, 24 is the ghost's height
    24,  # gray ghost width
    24,   # gray ghost height
    "gray.png"
)


def heart_position(x, y):
    game_display.blit(heart_image,(x, y))
lives_number = 3
def robot_position(x, y):
    game_display.blit(robot_image,(x, y)) #blit
def ghost_position(x, y):
    creature = None
    for c in creatures:
        if "white ghost" in c.values():
            creature = c
    game_display.blit(creature["image"], (x, y))
def gray_ghost_position(x, y):
    creature = None
    for c in creatures:
        if "gray ghost" in c.values():
            creature = c
    game_display.blit(creature["image"], (x, y))
def zombie_position(x, y):
    creature = None
    for c in creatures:
        if "zombie" in c.values():
            creature = c
    game_display.blit(creature["image"], (x, y))
zombie_direction = None
zombie_origin = None
def set_zombie_direction():
    available_directions = []
    zombie = None
    for creature in creatures:
        if "zombie" in creature.values():
            zombie = creature
    zombie_col = (zombie["x"] + zombie["width"]//2) // (display_width // 12) + 1
    zombie_row = (zombie["y"] + zombie["height"]//2) // (display_height // 9) + 1
    zombie_col_off_set = (zombie["x"] + zombie["width"]//2) % (display_width // 12) #this is where we fixed the zombie with movement
    zombie_row_off_set = (zombie["y"] + zombie["height"]//2) % (display_height // 9)
    zombie_at_the_square_center = False
    if zombie_col_off_set == 50 and zombie_row_off_set == 50:
        zombie_at_the_square_center = True
    for square in squares:
        if zombie_at_the_square_center and zombie_col == square["x"] and zombie_row == square ["y"]: #[] dictionary, "" - is a key
            for direction, avalability in square.items():
                if square[direction] == True:
                    available_directions.append(direction)
    num_of_directions = len(available_directions)
    if num_of_directions > 0:
        global zombie_direction, zombie_origin
        direction = zombie_origin
        while direction == zombie_origin:
            direction_index = random.randint(0, num_of_directions - 1)
            direction = available_directions[direction_index]
            if num_of_directions == 1: #we are fixing the bug, let the zombie turn around
                zombie_origin = zombie_direction
                break
        if num_of_directions > 1:
            if direction == "UP":
                zombie_origin = "DOWN"
            if direction == "DOWN":
                zombie_origin = "UP"
            if direction == "RIGHT":
                zombie_origin = "LEFT"
            if direction == "LEFT":
                zombie_origin = "RIGHT"
        if direction != zombie_origin:
            zombie_direction = direction
        print(zombie_direction, zombie_origin, available_directions)
def zombie_move():
    zombie = None
    for creature in creatures:
        if "zombie" in creature.values():
            zombie = creature
    if zombie_direction == "UP":
        zombie["y"] = zombie["y"] - zombie["speed"]
    if zombie_direction == "DOWN":
        zombie["y"] = zombie["y"] + zombie["speed"]
    if zombie_direction == "LEFT":
        zombie["x"] = zombie["x"] - zombie["speed"]
    if zombie_direction == "RIGHT":
        zombie["x"] = zombie["x"] + zombie["speed"]

def blue_ghost_position(x, y):
    creature = None
    for c in creatures:
        if "blue ghost" in c.values():
            creature = c
    game_display.blit(creature["image"],(x, y))
x = 18
y = 700+24
x_move = 0 #lefft & right
y_move = 0 #up & down
ghost_x_move = 0
ghost_y_move = 0
def ghost_out_of_screen():
    ghost = None
    for creature in creatures:
        if "white ghost" in creature.values():
            ghost = creature
    if (ghost["x"] >= display_width or ghost["x"] <= 0 - ghost["width"]) or (ghost["y"] >= display_height or ghost["y"] <= 0 - ghost["height"]):
        return True #if the ghost outside the screen, it will detect
    return False #if the ghost is inside the screen, then it'no gonna do anything
def ghost_direction():
    ghost = None
    for creature in creatures:
        if "white ghost" in creature.values():
            ghost = creature
    x_distance = ghost["x"] - x #the 2nd x is the coordinator of the robot. #how much the ghost move to the left, right, up and down.
    y_distance = ghost["y"] - y
    x_sign = 1
    if x_distance > 0: #here we are testing;    if x_distance great than 0, that means ghost is right to the robot
        x_sign = -1 #-1 means ghost should go to the left to catch the robot
    y_sign = 1

    if y_distance > 0:
        y_sign = -1
    x_distance = abs(x_distance)
    y_distance = abs(y_distance)

    max_distance = max(x_distance, y_distance)  #testing the distance, is the robot distance from the ghost horizontal or vertical larger
    if max_distance == x_distance: #abs -absolute value
        ghost_x_move = ghost["speed"]*x_sign
        ghost_y_move = ghost["speed"]*y_sign*(y_distance/x_distance)
    else:
        ghost_y_move = ghost["speed"]*y_sign
        ghost_x_move = ghost["speed"]*x_sign*(x_distance/y_distance)

    return (int(ghost_x_move//1), int(ghost_y_move//1))
ghost_move = ghost_direction()

def blue_ghost_direction():
    ghost = None
    for creature in creatures:
        if "blue ghost" in creature.values():
            ghost = creature
    x_distance = ghost["x"] - x #the 2nd x is the coordinator of the robot. #how much the ghost move to the left, right, up and down.
    y_distance = ghost["y"] - y
    x_sign = 1
    if x_distance > 0: #here we are testing;    if x_distance great than 0, that means ghost is right to the robot
        x_sign = -1 #-1 means ghost should go to the left to catch the robot
    y_sign = 1

    if y_distance > 0:
        y_sign = -1
    x_distance = abs(x_distance)
    y_distance = abs(y_distance)

    if x_distance == 0:
        x_distance = 1
    if y_distance == 0:
        y_distance = 1

    max_distance = max(x_distance, y_distance)  #testing the distance, is the robot distance from the ghost horizontal or vertical larger
    if max_distance == x_distance: #abs -absolute value
        blue_ghost_x_move = ghost["speed"]*x_sign
        blue_ghost_y_move = ghost["speed"]*y_sign*(y_distance/x_distance)
    else:
        blue_ghost_y_move = ghost["speed"]*y_sign
        blue_ghost_x_move = ghost["speed"]*x_sign*(x_distance/y_distance)

    return (int(blue_ghost_x_move//1), int(blue_ghost_y_move//1))
blue_ghost_move = blue_ghost_direction()

def gray_ghost_direction():
    ghost = None
    for creature in creatures:
        if "gray ghost" in creature.values():
            ghost = creature
    x_distance = ghost["x"] - x #the 2nd x is the coordinator of the robot. #how much the ghost move to the left, right, up and down.
    y_distance = ghost["y"] - y
    x_sign = 1
    if x_distance > 0: #here we are testing;    if x_distance great than 0, that means ghost is right to the robot
        x_sign = -1 #-1 means ghost should go to the left to catch the robot
    y_sign = 1

    if y_distance > 0:
        y_sign = -1
    x_distance = abs(x_distance)
    y_distance = abs(y_distance)
    if x_distance == 0:
        x_distance = 1
    if y_distance == 0:
        y_distance = 1

    max_distance = max(x_distance, y_distance)  #testing the distance, is the robot distance from the ghost horizontal or vertical larger
    if max_distance == x_distance: #abs -absolute value
        gray_ghost_x_move = ghost["speed"]*x_sign
        gray_ghost_y_move = ghost["speed"]*y_sign*(y_distance/x_distance)
    else:
        gray_ghost_y_move = ghost["speed"]*y_sign
        gray_ghost_x_move = ghost["speed"]*x_sign*(x_distance/y_distance)


    return (int(gray_ghost_x_move//1), int(gray_ghost_y_move//1))





walls = []
doors = []
opened_doors = []
keys = []
keylist = []
inventory = []
lasers = []
def draw_element(x, y, w, h, c): #w stands for width, h height, c color
    pygame.draw.rect(game_display, c, [x, y, w, h]) #rectangle shape

def draw_wall(col, row, orientation, length):
    x = col*100-4
    y = row*100-4
    w = 0
    h = 0
    if orientation == "h":
        w = length*100+8 #8 is the thickness of the wall
        h = 8
    else: #in case it's not a horizontal
        w = 8
        h = length*100+8
    draw_element(x, y, w, h, WHITE) #line 35 , white is color
    wall = {"xl": x, "xr": x+w, "yt": y, "yb": y+h} #making wall detection l left, r right, t top, b bottom
    walls.append(wall)

def draw_door(col, row, orientation, length, colorcode, color):
    x = col*100-4
    y = row*100-4
    w = 0
    h = 0
    if orientation == "h":
        w = length*100+8
        h = 8
    else:
        w = 8
        h = length*100+8
    draw_element(x, y, w, h, colorcode)
    door = {"xl": x, "xr": x+w, "yt": y, "yb": y+h, "color": color, "type": "door"} #making wall detection l left, r right, t top, b bottom
    doors.append(door)

def draw_key(col, row, w, h, colorcode, color):
    x = col*100-55
    y = row*100-55

    draw_element(x, y, w, h, colorcode)
    key = {"xl": x, "xr": x+w, "yt": y, "yb": y+h, "color": color, "type": "key"}
    keys.append(key)


def draw_laser(col, row, orientation, length, colorcode, color, speed):
    x = col*100-1
    y = row*100-1
    w = 0
    h = 0
    if orientation == "h":
        w = length*100+2
        h = 2
    else:
        w = 2
        h = length*100+2
    draw_element(x, y, w, h, colorcode)
    laser = {"xl": x, "xr": x+w, "yt": y, "yb": y+h, "color": color, "type": "laser", "speed": speed}
    lasers.append(laser)

def detectwall(x, y): #wall detection
    for wall in walls:
        x_breach = False #fixing the wall detection problem. robot does not move
        y_breach = False
        if x > wall["xl"] - robot_width and x < wall["xr"]:
            x_breach = True
        if y > wall["yt"] - robot_height and y < wall["yb"]: #t top, b bottom
            y_breach = True
        if x_breach and y_breach:
            return None #it means the position is none

    return (x, y) #potential move

def detectdoor(x, y):
    for door in doors:
        x_breach = False #fixing the door detection problem. robot does not move
        y_breach = False
        if x > door["xl"] - robot_width and x < door["xr"]:
            x_breach = True
        if y > door["yt"] - robot_height and y < door["yb"]: #t top, b bottom
            y_breach = True
        if x_breach and y_breach: #checking if the robot is trying to go through the door.
            if door["color"] in keylist:
                opened_doors.append(door)
                return (x, y)
            return None #it means the position is none

    return (x, y) #potential move

def deteckey(x, y):
    for key in keys:
        x_breach = False #fixing the wall detection problem. robot does not move
        y_breach = False
        if x > key["xl"] - robot_width and x < key["xr"]:
            x_breach = True
        if y > key["yt"] - robot_height and y < key["yb"]: #t top, b bottom
            y_breach = True
        if x_breach and y_breach:
            inventory.append(key)
            keys.remove(key)

            #we don't have any return because we don't care about robot's move. Do not care about movements  All we care about the robot getting the key.

def detectlaser(x, y):
    for laser in lasers:
        x_breach = False
        y_breach = False
        if x > laser["xl"] - robot_width and x < laser["xr"]:
            x_breach = True
        if y > laser["yt"] - robot_height and y < laser["yb"]:
            y_breach = True
        if x_breach and y_breach:
            print("ouch, suka")
            loselife()

            #here we only care about touching the laser, no movements.

def detect_ghost():
    ghost = None
    for creature in creatures:
        if "white ghost" in creature.values():
            ghost = creature
    x_breach = False
    y_breach = False
    if x > ghost["x"] - robot_width and x < ghost["x"] + ghost["width"]:
        x_breach = True
    if y > ghost["y"] - robot_height and y < ghost["y"] + ghost["height"]:
        y_breach = True
    if x_breach and y_breach:
        print("ouch, suka")
        loselife()

def detect_zombie():
    zombie = None
    for creature in creatures:
        if "zombie" in creature.values():
            zombie = creature
    x_breach = False
    y_breach = False
    if x > zombie["x"] - zombie["width"] and x < zombie["x"] + zombie["width"]:
        x_breach = True
    if y > zombie["y"] - zombie["height"] and y < zombie["y"] + zombie["height"]:
        y_breach = True
    if x_breach and y_breach:
        print("oh, no")
        loselife()
def detect_blue_ghost():
    ghost = None
    for creature in creatures:
        if "blue ghost" in creature.values():
            ghost = creature
    x_breach = False
    y_breach = False
    if x + robot_width > ghost["x"] and x < ghost["x"] + ghost["width"]:
        x_breach = True
    if y + robot_height > ghost["y"] and y < ghost["y"] + ghost["height"]:
        y_breach = True
    if x_breach and y_breach:
        print("yeap")
        loselife()
def detect_gray_ghost():
    ghost = None
    for creature in creatures:
        if "gray ghost" in creature.values():
            ghost = creature
    x_breach = False
    y_breach = False
    if x + robot_width > ghost["x"] and x < ghost["x"] + ghost["width"]:
        x_breach = True
    if y + robot_height > ghost["y"] and y < ghost["y"] + ghost["height"]:
        y_breach = True
    if x_breach and y_breach:
        print("yeap")
        loselife()

def levelcomplete():

    opened_doors.clear()
    keylist.clear()
    inventory.clear()
    game_display.fill(display_background_color)
    font = pygame.font.Font(pygame.font.get_default_font(), 92)
    text = font.render("Level 1 Completed!", True, WHITE, RED)
    text_rect = text.get_rect()
    text_rect.center = (display_width // 2, display_height // 2)
    game_display.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)

def restart_game():
    global lives_number
    lives_number = 3
    opened_doors.clear() #here we reset the game if you die in the game
    keylist.clear()
    inventory.clear()
    game_display.fill(display_background_color)
    font = pygame.font.Font(pygame.font.get_default_font(), 92) #font is the style of the letters
    text = font.render("Game Over", True, WHITE, RED)
    text_rect = text.get_rect() #rect - rectangle
    text_rect.center = (display_width//2, display_height//2)
    game_display.blit(text, text_rect) #line 216 to 220 creating a game over function
    pygame.display.update()  # line 215-216 is the restart function lines, the screen goes black
    pygame.time.wait(3000) #1000 means one second

def loselife():
    for c in creatures:
        c["x"] = c["initial x"]
        c["y"] = c["initial y"]
        c["move"] = (0, 0)
    global x, y, lives_number  # global means we are connecting x, y outside/globally
    x = 18
    y = 700 + 24
    lives_number -= 1
    if lives_number == 0:
        restart_game()
def is_there_a_path(cords):
    x_out_of_screen = False
    y_out_of_screen = False
    if cords[0] - 50 < 0 or cords[0] + 50 > display_width:
        x_out_of_screen = True
    if cords[1] - 50 < 0 or cords[1] + 50 > display_height:
        y_out_of_screen = True
    for wall in walls:
        x_breach = False
        y_breach = False
        if cords[0] > wall["xl"] and cords[0] < wall["xr"]: #we are making tuples
            x_breach = True
        if cords[1] > wall["yt"] and cords[1] < wall["yb"]:
            y_breach = True
        if (x_breach and y_breach) or x_out_of_screen or y_out_of_screen:
            return False
    return True

squares = [] #
def create_path():
    for col in range(1, col_num + 1):
        for row in range(1, row_num + 1):
            center_x = col * 100 - 50
            center_y = row * 100 - 50
            right = (center_x + 50, center_y)
            left = (center_x - 50, center_y)
            up = (center_x, center_y - 50)
            down = (center_x, center_y + 50)
            square = {'x': col, 'y': row}
            square['RIGHT'] = is_there_a_path(right)
            square['LEFT'] = is_there_a_path(left)
            square['UP'] = is_there_a_path(up)
            square['DOWN'] = is_there_a_path(down)
            squares.append(square)



path_set = False

game_over = False #most important thing in any game is loop. we don't create anything. we just set up
while not game_over: #we measure while the game is not over
    counter += 1 #we are countrolling lasers on this line
    for event in pygame.event.get(): #pygame init; event is "press A", event makes everything what you touch
        if event.type == pygame.QUIT: #is user clicks exit (x)
            game_over = True #if user click exit, then the game is over
        if event.type == pygame.KEYDOWN: #keydown means pressed key on a keaboard
            if event.key == pygame.K_LEFT: #left arrow
                x_move = - robot_speed #move to the left. 3 is speed
            if event.key == pygame.K_RIGHT: #event.key specific key was pressed (you pressed x, y, w, etc)
                x_move = robot_speed
            if event.key == pygame.K_DOWN:
                y_move = robot_speed
            if event.key == pygame.K_UP:
                y_move = -robot_speed
        if event.type == pygame.KEYUP: #MAKE A STOP if you don't press any key it will make robot stop
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_move = 0 #it means the difference between the current position of the robot and new one
                y_move = 0 #it means the difference between the current position of the robot and new one
    game_display.fill(display_background_color) #display the black color of screen
    walls.clear() #it's a must to set .clear otherwise python will struggle
    draw_wall(1, 1, "h", 10) #100, 100 are coodrinations, 8, 8 are size of the cube/dimensetion
    draw_wall(1, 1, "v", 6)
    draw_wall(1, 8, "h", 10) #1 is collon, 8 is row, 10 is length
    draw_wall(2, 2, "v", 6)
    draw_wall(3, 2, "h", 7)
    draw_wall(11, 2, "v", 6)
    draw_wall(10, 1, "v", 1) #v - vertical
    draw_wall(2, 3, "h", 3) #h - horizontal
    draw_wall(6, 2, "v", 2)
    draw_wall(5, 3, "v", 1)
    draw_wall(4, 5, "h", 3)
    draw_wall(4, 4, "v", 1)
    draw_wall(3, 4, "h", 1)
    draw_wall(2, 5, "h", 1)
    draw_wall(3, 6, "h", 2)
    draw_wall(3, 6, "v", 1)
    draw_wall(4, 7, "v", 1)
    draw_wall(5, 6, "v", 1)
    draw_wall(6, 5, "v", 1)
    draw_wall(7, 3, "v", 2)
    draw_wall(5, 7, "h", 2)
    draw_wall(7, 6, "v", 1)
    draw_wall(7, 3, "h", 1)
    draw_wall(7, 6, "h", 2)
    draw_wall(8, 4, "v", 2)
    draw_wall(8, 7, "v", 1)
    draw_wall(8, 4, "h", 2)
    draw_wall(9, 2, "v", 2)
    draw_wall(10, 3, "h", 1)
    draw_wall(9, 5, "h", 2)
    draw_wall(9, 6, "v", 1)
    draw_wall(9, 7, "h", 1)
    draw_wall(10, 6, "v", 1)
    draw_wall(6, 0, "v", 1)
    draw_wall(6, 8, "v", 1)
    doors.clear()
    opened_doorslist = []
    for door in opened_doors:
        opened_doorslist.append(door["color"])
    if "BLUE" not in opened_doorslist:
        draw_door(11, 1, "v", 1, BLUE, "BLUE")
    if "GREEN" not in opened_doorslist:
        draw_door(1, 7, "v", 1, GREEN, "GREEN")
    keys.clear()
    keylist.clear()
    for item in inventory:
        if "key" in item.values():
            keylist.append(item["color"])
    if "GREEN" not in keylist:
        draw_key(6, 9, 10, 10, GREEN, "GREEN")
    if "BLUE" not in keylist:
        draw_key(10, 2, 10, 10, BLUE, "BLUE")
    #print(inventory, "***", keys)
    lasers.clear()
    if counter < game_speed//4:
        draw_laser(9, 1, "v", 1, RED, "RED", 2)
        draw_laser(7, 1, "v", 1, RED, "RED", 2)
        draw_laser(5, 8, "v", 1, RED, "RED", 2)
        draw_laser(3, 8, "v", 1, RED, "RED", 2)
    if counter > 60 and counter < 75:
        draw_laser(8, 1, "v", 1, RED, "RED", 2)
        draw_laser(6, 1, "v", 1, RED, "RED", 2)
        draw_laser(4, 8, "v", 1, RED, "RED", 2)
        draw_laser(2, 8, "v", 1, RED, "RED", 2)

    if not path_set:
        create_path()
        path_set = True
        print(squares)


    movethroughdoor = detectdoor(x + x_move, y + y_move)


    move = detectwall(x + x_move, y + y_move) #wall detection, testing position in wall
    if move != None and movethroughdoor != None:
        x += x_move #this will change the current position of the robot
        y += y_move

    if x > display_width - robot_width: #we make bounderies here
        x = display_width - robot_width
    if x < 0:
        x = 0 #we complete bounderies to the left
    if y > display_height - robot_height:
        y = display_height - robot_height
    if y < 0:
        y = 0
    robot_position(x, y) #here we move robot's image in a new position
    if x > display_width - 100:
        levelcomplete()
    if ghost_out_of_screen():
        ghost_move = ghost_direction()

    creature = None
    for c in creatures:
        if "blue ghost" in c.values():
            creature = c

    blue_ghost_move = blue_ghost_direction()
    creature["x"] += blue_ghost_move[0]
    creature["y"] += blue_ghost_move[1]
    blue_ghost_position(creature["x"], creature["y"])


    creature = None
    for c in creatures:
        if "gray ghost" in c.values():
            creature = c
            if "BLUE" in keylist:
                c["move"] = gray_ghost_direction()
    creature["x"] += c["move"][0]
    creature["y"] += c["move"][1]
    gray_ghost_position(creature["x"], creature["y"])
    creature = None
    for c in creatures:
        if "white ghost" in c.values():
            creature = c
    creature["x"] += ghost_move[0]
    creature["y"] += ghost_move[1]
    ghost_position(creature["x"], creature["y"])
    creature = None
    for c in creatures:
        if "zombie" in c.values():
            creature = c
    zombie_position(creature["x"], creature["y"])
    set_zombie_direction()
    zombie_move()

    ctr = 0
    while ctr < lives_number:
        heart_y = 26
        heart_x = 1000+ctr*50
        ctr += 1
        heart_position(heart_x, heart_y)
    detect_ghost()
    detect_zombie()
    detect_blue_ghost()
    detect_gray_ghost()
    deteckey(x, y) #to see if he touches the key
    detectlaser(x, y) #to see if he touches the laser
    pygame.display.update() #in this line we draw the game what we have
    clock.tick(game_speed) #set the speed
    if counter >= game_speed*2:
        counter = 0
pygame.quit() #this will stop the background of proccessing of pygame.
quit() #close the game window




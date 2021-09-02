import pygame
pygame.init() #


display_width = 1200
display_height = 900
BLACK = (0, 0, 0) #rgb (red, green, black) is a code,  background color
WHITE = (255, 255, 255) #intensity of color up to 255
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
display_background_color =(BLACK) #variable that we use
game_display = pygame.display.set_mode((display_width, display_height)) #tupil inside the ()
pygame.display.set_caption("Misha's game")
clock = pygame.time.Clock()
game_speed = 60
robot_speed = 7
counter = 0 #counter start with 0 sec. at the end check
robot_image = pygame.image.load("robot-icon-7.png")
ghost_image = pygame.image.load("white-ghost.png")
heart_image = pygame.image.load("heart.png")
robot_width = 64
robot_height = 64
heart_width = 24
heart_height = 24
robot_image = pygame.transform.scale(robot_image,(robot_width, robot_height)) #to create the size of robot more flexible
heart_image = pygame.transform.scale(heart_image,(heart_width, heart_height))
ghost_width = 24
ghost_height = 24
ghost_image = pygame.transform.scale(ghost_image,(ghost_width, ghost_height))
def heart_position(x, y):
    game_display.blit(heart_image,(x, y))
lives_number = 3
def robot_position(x, y):
    game_display.blit(robot_image,(x, y)) #blit
def ghost_position(x, y):
    game_display.blit(ghost_image,(x, y)) #blit
x = 18
y = 700+24
x_move = 0 #lefft & right
y_move = 0 #up & down
ghost_x = display_width #it will leave the ghost outside the screen but it's there
ghost_y = 0
ghost_x_move = 0
ghost_y_move = 0
def ghost_out_of_screen():
    if (ghost_x >= display_width or ghost_x <= 0 - ghost_width) or (ghost_y >= display_height or ghost_y <= 0 - ghost_height):
        return True #if the ghost outside the screen, it will detect
    return False #if the ghost is inside the screen, then it'no gonna do anything
ghost_speed = 2 #number 1 we are making the speed of the ghost
def ghost_direction():
    x_distance = ghost_x - x #the 2nd x is the coordinator of the robot. #how much the ghost move to the left, right, up and down.
    y_distance = ghost_y - y
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
        ghost_x_move = ghost_speed*x_sign
        ghost_y_move = ghost_speed*y_sign*(y_distance/x_distance)
    else:
        ghost_y_move = ghost_speed*y_sign
        ghost_x_move = ghost_speed*x_sign*(x_distance/y_distance)

    return (int(ghost_x_move//1), int(ghost_y_move//1))
ghost_move = ghost_direction()


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
    x_breach = False
    y_breach = False
    if x > ghost_x - robot_width and x < ghost_x + ghost_width:
        x_breach = True
    if y > ghost_y - robot_height and y < ghost_y + ghost_height:
        y_breach = True
    if x_breach and y_breach:
        print("ouch, suka")
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
    global lives_number, ghost_x, ghost_y
    lives_number = 3
    ghost_x = display_width
    ghost_y = 0
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
    global x, y, lives_number  # global means we are connecting x, y outside/globally
    x = 18
    y = 700 + 24
    lives_number -= 1
    if lives_number == 0:
        restart_game()



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
    ghost_x += ghost_move[0]
    ghost_y += ghost_move[1]
    ghost_position(ghost_x, ghost_y)
    ctr = 0
    while ctr < lives_number:
        heart_y = 26
        heart_x = 1000+ctr*50
        ctr += 1
        heart_position(heart_x, heart_y)
    detect_ghost()
    deteckey(x, y) #to see if he touches the key
    detectlaser(x, y) #to see if he touches the laser
    pygame.display.update() #in this line we draw the game what we have
    clock.tick(game_speed) #set the speed
    if counter >= game_speed*2:
        counter = 0
pygame.quit() #this will stop the background of proccessing of pygame.
quit() #close the game window




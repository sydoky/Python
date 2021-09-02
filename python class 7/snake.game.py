import random
import pygame
pygame.init()
display_width = 1300
display_height = 900
snake_split_width = 25
snake_split_height = 25
snake_head_x = 0
snake_head_y = 0
snake_body = [[1, 0]]
apples = []
eaten_apples = 0
high_score = 0
lives = 3
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 128, 0)
RED = (255, 0, 0)
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game v.1.0')
clock = pygame.time.Clock()
SNAKE_SPEED = 7
game_speed = SNAKE_SPEED

def draw_rectangle(x, y, w, h, c):
    pygame.draw.rect(game_display, c, [x, y, w, h])


def spawn_apples(number):
    apples.clear()
    for apple in range(number):
        apple_x = random.randint(1, display_width // snake_split_width - 2) * snake_split_width
        apple_y = random.randint(1, display_height // snake_split_height - 2) * snake_split_height

        apples.append([apple_x, apple_y])

def draw_apples():
    for apple in apples:
        draw_rectangle(apple[0],apple[1], snake_split_width, snake_split_height, RED)

def spawn_snake():
    global snake_head_x, snake_head_y, snake_body
    snake_head_x = random.randint(1, display_width//snake_split_width-2)*snake_split_width
    snake_head_y = random.randint(1, display_height//snake_split_height-2)*snake_split_height
    snake_body = [snake_body[0]]

def draw_snake():
    colour = GREEN
    draw_rectangle(snake_head_x, snake_head_y, snake_split_width, snake_split_height, colour)
    split_x = snake_head_x
    split_y = snake_head_y
    index = 0
    for snake_split in snake_body:
        split_x += snake_split[0] * snake_split_width
        split_y += snake_split[1] * snake_split_height
        if index % 2 == 0:
            colour = LIGHT_GREEN
        else:
            colour = GREEN
        index += 1
        draw_rectangle(split_x, split_y, snake_split_width, snake_split_height, colour)

def move_body(x, y):
    for snake_split in snake_body:
        current_x = snake_split[0]
        current_y = snake_split[1]
        snake_split[0] = -x
        snake_split[1] = -y
        x = -current_x
        y = -current_y


def detect_apple():
    global game_speed, eaten_apples
    index = 0
    bite = None
    for apple in apples:
        if apple[0] == snake_head_x and apple[1] == snake_head_y:
            print('yummy')
            eaten_apples += 1
            print('apples eaten:', eaten_apples)
            bite = index
            tale = snake_body[-1].copy()
            snake_body.append(tale)
            if len(snake_body)%4 == 0:
                game_speed += 3
        index += 1
    if bite is not None:
        apples.pop(bite)
        spawn_apples(1)



def detect_body():#
    split_x = snake_head_x
    split_y = snake_head_y
    index = 0
    for snake_split in snake_body:
        split_x += snake_split[0] * snake_split_width
        split_y += snake_split[1] * snake_split_height
        index += 1
        if snake_head_x == split_x and snake_head_y == split_y:
            die()
def die():
    global game_speed, lives, eaten_apples, high_score
    print('die')
    spawn_snake()
    spawn_apples(1)
    game_speed = SNAKE_SPEED
    lives -= 1
    print('lives left:', lives)
    if lives == 0:
        lives = 3
        print('GAME OVER')
        if eaten_apples>high_score:
            print('well done! this is your new high score', eaten_apples)
            high_score = eaten_apples
        eaten_apples = 0


spawn_apples(1)
spawn_snake()
game_over = False
while not game_over:
    first_split = snake_body[0]
    snake_head_x += - snake_split_width * first_split[0]
    snake_head_y += - snake_split_height * first_split[1]
    if snake_head_x + snake_split_width > display_width:
        print('ouch_right')
        die()
    if snake_head_y + snake_split_height < 0:
        print('ouch_up')
        die()
    if snake_head_y + snake_split_height > display_height:
        print('ouch_down')
        die()
    if snake_head_x + snake_split_width < 0:
        print('ouch_left')
        die()
    move_body(- first_split[0], - first_split[1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        if snake_head_x - snake_split_width < 0:
            print('ouch_left')
            spawn_snake()
            spawn_apples(1)
        else:
            snake_head_x -= snake_split_width
            move_body(-1, 0)
    if pressed_keys[pygame.K_d]:
        if snake_head_x + snake_split_width > display_width - snake_split_width:
            print('ouch_right')
            spawn_snake()
            spawn_apples(1)
        else:
            snake_head_x += snake_split_width
            move_body(1, 0)
    if pressed_keys[pygame.K_w]:
        if snake_head_y - snake_split_height < 0:
            print('ouch_up')
            spawn_snake()
            spawn_apples(1)
        else:
            snake_head_y -= snake_split_height
            move_body(0, -1)
    if pressed_keys[pygame.K_s]:
        if snake_head_y + snake_split_height >display_height -snake_split_height:
            print('ouch_down')
            spawn_snake()
            spawn_apples(1)
        else:
            snake_head_y += snake_split_height
            move_body(0, 1)
    game_display.fill((BLACK))
    draw_apples()
    draw_snake()
    detect_apple()
    detect_body()
    pygame.display.update()
    clock.tick(game_speed)
pygame.quit()
quit()





from random import randint
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

move_list = [1,2,3,4]
display_list = []

score = 0
current_move = 0
count = 4
dance_length = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor("dancer-start")
dancer.pos = CENTRE_X + 5, CENTRE_Y - 40

up = Actor("up")
up.pos = CENTRE_X, CENTRE_Y + 110
right = Actor("right")
right.pos = CENTRE_X + 60, CENTRE_Y + 170
down = Actor("down")
down.pos = CENTRE_X, CENTRE_Y + 230
left = Actor("left")
left.pos = CENTRE_X - 60, CENTRE_Y + 170

def draw():
    global game_over, score, say_dance
    global count, show_countdown
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
        if say_dance:
            screen.draw.text("DANCE!!!!", color="black", fontsize=60, topleft=(CENTRE_X - 65, 150))
        if show_countdown:
            screen.draw.text(str(count), color="black", fontsize=60, topleft=(CENTRE_X -8, 150))
    else:
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
        screen.draw.text("GAME OVER", color="black", fontsize=60, topleft=(CENTRE_X - 130, 220))

def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        down.image = "down"
        right.image = "right"
        left.image = "left"

def update_dancer(move):
    global game_over
    if not game_over:
        if move == 0:
            up.image = "up-lit"
            dancer.image = "dancer-up"
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer, 0.5)
        elif move == 3:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer, 0.5)

def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown
    if display_list:
        d = display_list.pop(0)
        update_dancer(d)
        clock.schedule(display_moves, 1)
    else:
        say_dance = True
        show_countdown = False

def generate_moves():
    global move_list, count, show_countdown, say_dance
    count = 4
    move_list = []
    say_dance = False
    show_countdown = True
    for move in range(0, dance_length):
        rand_move = randint(0, 3)
        display_list.append(rand_move)
        move_list.append(rand_move)
    countdown()
        
def countdown():
    global count, show_countdown
    if count > 1:
        count -= 1
        clock.schedule(countdown, 1 )
    else:
        show_countdown = False
        display_moves()

def next_move():
    global current_move, moves_complete
    if current_move < dance_length - 1:
        current_move += 1
    else:
        moves_complete = True

def on_key_up(key):
    if not say_dance or game_over:
        return
    if key == keys.UP:
        update_dancer(0)
        check_game_status(0)
    elif key == keys.RIGHT:
        update_dancer(1)
        check_game_status(1)
    elif key == keys.DOWN:
        update_dancer(2)
        check_game_status(2)
    elif key == keys.LEFT:
        update_dancer(3)
        check_game_status(3)

def update():
    global current_move, moves_complete
    if not game_over:
        if moves_complete:
            generate_moves()
            current_move = 0
            moves_complete = False

def check_game_status(move):
    global game_over, score
    if move_list[current_move] == move:
        score += 1
        next_move()
    else:
        game_over = True

music.play("vanishing-horizon")

generate_moves()
from random import randint
import time
from os import environ

environ['SDL_VIDEO_CENTERED'] = '1'
WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH / 2
CENTRE_Y = HEIGHT / 2

game_over = False
finalised = False
garden_happy = True
fangflower_collision = False

time_elapsed = 0
start_time = time.time()

cow = Actor("cow")
cow.pos = 100, 500

flower_list = []
wilted_list = []
fangflower_list = []
fangflower_vy_list = []
fangflower_vx_list = []

def draw():
    global game_over, time_elapsed, finalised
    if not game_over:
        screen.clear()
        screen.blit("garden", (0,0))
        cow.draw()
        for flower in flower_list:
            flower.draw()
        for fangflower in fangflower_list:
            fangflower.draw()
        time_elapsed = int(time.time() - start_time)
        screen.draw.text(
            "Garden happy for: " +
            str(time_elapsed) + " seconds", 
            topleft=(10,10), color="black"
        )
    else:
        #show_game_over()
        if not finalised:
            cow.draw()
            screen.draw.text(
            "Garden happy for: " + str(time_elapsed) + " seconds", 
            topleft=(10, 10), color="black"
        )
        if not garden_happy:
            screen.draw.text("GARDEN UNHAPPY - GAME OVER!", color="black", topleft=(10, 50))
            finalised = True
        else:
            screen.draw.text("FANGFLOWER ATTACK - GAME OVER!", color="black", topleft=(10,50))
            finalised=True

def new_flower():
    global flower_list, wilted_list
    flower_new = Actor("flower")
    flower_new.pos = randint(50, WIDTH - 50), randint(150, HEIGHT - 100)
    flower_list.append(flower_new)
    wilted_list.append("happy")

def add_flower():
    if not game_over:
        new_flower()
        clock.schedule(add_flower, 4)

def check_wilt_times():
    global game_over, garden_happy
    for wilted_since in wilted_list:
        if wilted_since == "happy": continue
        time_wilted = int(time.time()- wilted_since)
        if time_wilted > 10.0:
            garden_happy = False
            game_over = True
            break

def wilt_flower():
    if not game_over and flower_list:
        rand_flower_index = randint(0, len(flower_list) - 1)
        rand_flower = flower_list[rand_flower_index]
        if (rand_flower.image == 'flower'):
            rand_flower.image = 'flower-wilt'
            wilted_list[rand_flower_index] = time.time()
        clock.schedule(wilt_flower, 3) 

def check_flower_collison():
    global wilted_list
    index = 0
    for flower in flower_list:
        if flower.colliderect(cow)  and flower.image == "flower-wilt":
            flower.image = "flower"
            wilted_list[index] = "happy"
            break
        index += 1

def check_fangflower_collision():
    global cow, fangflower_list, fangflower_collision, game_over
    for fangflower in fangflower_list:
        if fangflower.colliderect(cow):
            cow.image = "zap"
            sounds.electric_zap.play()
            game_over = True
            break       

def velocity():
    random_dir = randint(0,1)
    random_velocity = randint(2,3)
    if random_dir == 0:
        return -random_velocity
    else:
        return random_velocity

def mutate():
    global flower_list, fangflower_list, fangflower_vx_list
    global fangflower_vy_list, game_over
    if not game_over and flower_list:
        rand_flower = randint(0, len(flower_list) -1)
        fangflower_pos_x = flower_list[rand_flower].y
        fangflower_pos_y = flower_list[rand_flower].x
        del flower_list[rand_flower]
        fangflower= Actor("fangflower")
        fangflower.pos = fangflower_pos_x, fangflower_pos_y
        fangflower_vx = velocity()
        fangflower_vy = velocity()
        fangflower=fangflower_list.append(fangflower)
        fangflower_vx_list.append(fangflower_vx)
        fangflower_vy_list.append(fangflower_vy)
        clock.schedule(mutate, 20)
        
def update_fangflower():
    global fangflower_list, game_over
    if not game_over:
        index = 0
        for fangflower in fangflower_list:
            fangflower_vx = fangflower_vx_list[index]
            fangflower_vy = fangflower_vy_list[index]
            fangflower.x = fangflower.x + fangflower_vx
            fangflower.y = fangflower.y + fangflower_vy
            if fangflower.left < 0:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.right > WIDTH:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.top < 150:
                fangflower_vy_list[index] = -fangflower_vy
            if fangflower.bottom > HEIGHT:
                fangflower_vy_list[index] = -fangflower_vy
            index += 1

def reset_cow():
    if not game_over:
        cow.image = "cow"

def update():
    global score, game_over, fangflower_collision
    global flower_list, fangflower_list, time_elapsed
    fangflower_collision = check_fangflower_collision()
    check_wilt_times()
    if not game_over:
        if keyboard.left and cow.x > 0:
            cow.x -= 5
        elif keyboard.right and cow.x < WIDTH:
            cow.x += 5
        elif keyboard.up and cow.y > 150:
            cow.y -= 5
        elif keyboard.down and cow.y < HEIGHT:
            cow.y += 5
        if time_elapsed > 15 and not fangflower_list:
            mutate()
        update_fangflower()
        if keyboard.space:
            cow.image = "cow-water"
            clock.schedule(reset_cow, 0.5)
            check_flower_collison() 

def show_game_over():
    global finalised
    if not finalised:
        cow.draw()
        screen.draw.text(
            "Garden happy for: " + str(time_elapsed) + " seconds", 
            topleft=(10, 10), color="black"
        )
        if not garden_happy:
            screen.draw.text("GARDEN UNHAPPY - GAME OVER!", color="black", topleft=(10, 50))
            finalised = True

add_flower()
wilt_flower()
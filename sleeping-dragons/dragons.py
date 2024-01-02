import math
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH/2
CENYER_Y = HEIGHT/2
CENTER = (CENTER_X, CENYER_Y)
FONT_COLOR = (0, 0, 0)
EGG_TARGET = 20
HERO_START = (200,300)
ATTACK_DISTANCE = 200
DRAGON_WAKE_TIME = 2
EGG_HIDE_TIME = 2
MOVE_DISTANCE = 5

lives = 3
egg_collected = 0
game_over = False
game_completed = False
reset_required = False

easy_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 100)), 
    "eggs": Actor("one-egg", pos=(400 ,100)),
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 10,
    "sleep_counter": 0,
    "wake_counter": 0,
}

medium_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 300)), 
    "eggs": Actor("two-eggs", pos=(400 ,300)),
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 7,
    "sleep_counter": 0,
    "wake_counter": 0,
}

hard_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 500)), 
    "eggs": Actor("three-eggs", pos=(400 ,500)),
    "egg_count": 3,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 4,
    "sleep_counter": 0,
    "wake_counter": 0,
}

lairs = [easy_lair, medium_lair, hard_lair]

hero=Actor("hero", pos=HERO_START)

def draw():
    screen.clear()
    screen.blit("dungeon", (0,0))
    if game_over:
        screen.draw.text("GAME OVER!",fontsize=(60), color=FONT_COLOR, center=CENTER )
    elif game_completed:
        screen.draw.text("YOU WON! 🎉",fontsize=(60), color=FONT_COLOR, center=CENTER )
    else:
        hero.draw()
        draw_lairs(lairs)
        draw_counters(egg_collected, lives)

# TODO: Check why we need this argument
def draw_lairs(lairs):
    for lair in lairs:
        lair["dragon"].draw()
        if not lair["egg_hidden"]:
            lair["eggs"].draw()

def draw_counters(egg_collected, lives):
    screen.blit("egg-count", (0, HEIGHT- 30))
    screen.blit("life-count", (60, HEIGHT- 30))
    screen.draw.text(str(egg_collected), fontsize=40, pos=(30,HEIGHT- 30), color=FONT_COLOR)
    screen.draw.text(str(lives), fontsize=40, pos=(90,HEIGHT- 30), color=FONT_COLOR)

def update():
    if keyboard.right and hero.x < WIDTH- 35:
        hero.x += MOVE_DISTANCE
    elif keyboard.left and hero.x > 35:
        hero.x -= MOVE_DISTANCE
    elif keyboard.up and hero.y > 50:
        hero.y -= MOVE_DISTANCE
    elif keyboard.down and hero.y < HEIGHT - 50:
        hero.y += MOVE_DISTANCE
    check_for_collisions()

def check_for_collisions():
    global lairs, egg_collected, lives, reset_required, game_completed
    for lair in lairs:
        if lair["egg_hidden"] is False:
            check_for_egg_collision(lair)
        if lair["dragon"].image == "dragon-awake" and reset_required is False:
            check_for_dragon_collision(lair)

def update_lairs():
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_waking_dragon(lair)
        update_egg(lair)

clock.schedule_interval(update_lairs, 1)

def update_sleeping_dragon(lair):
    if lair["sleep_counter"] >= lair["sleep_length"]:
        if random.choice([True, False]):
            lair["dragon"].image = "dragon-awake"
            lair["sleep_counter"] = 0
    else:
        lair["sleep_counter"] += 1

def update_waking_dragon(lair):
    if lair["wake_counter"] >= DRAGON_WAKE_TIME:
        lair["dragon"].image = "dragon-asleep"
        lair["wake_counter"] = 0
    else:
        lair["wake_counter"] += 1

def update_egg(lair):
    if lair["egg_hidden"] is True :
        if lair["egg_hide_counter"] >= EGG_HIDE_TIME:
            lair["egg_hidden"] = False
            lair["egg_hide-counter"] = 0
        else:
            lair["egg_hide_counter"] += 1

def check_for_dragon_collision(lair):
    x_distance  = hero.x - lair["dragon"].x
    y_distance  = hero.y - lair["dragon"].y
    distance = math.hypot(x_distance, y_distance)
    if distance < ATTACK_DISTANCE:
        handle_dragon_collision()

def handle_dragon_collision():
    global reset_required
    reset_required = True
    animate(hero, pos=HERO_START, on_finished=subtract_life)    

def check_for_egg_collision(lair):
    global egg_collected, game_completed
    if hero.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        egg_collected += lair["egg_count"]
        if egg_collected >= EGG_TARGET:
            game_completed = True
    
def subtract_life():
    global lives, reset_required, game_over
    lives -= 1
    if lives == 0:
        game_over = True
    reset_required = False




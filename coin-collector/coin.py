from random import randint
import os

WIDTH = 500
HEIGHT = 500
score = 0
game_over = False
os.environ['SDL_VIDEO_CENTERED'] = '1'

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200



def start():
   sounds.starting.play() 

def play_sound():
    sounds.coin_sound.play()

def draw():
    screen.fill("blue")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("red")
        screen.draw.text("Final Score: " + str(score), topleft=(60, HEIGHT / 2), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score 

    if keyboard.left:
        fox.x = fox.x - 3
    if keyboard.right:
        fox.x = fox.x + 3
    if keyboard.up:
        fox.y = fox.y - 3
    if keyboard.down:
        fox.y = fox.y + 3
    
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        play_sound()
        place_coin()

clock.schedule(time_up, 7.9999999999999999)
place_coin()
start()


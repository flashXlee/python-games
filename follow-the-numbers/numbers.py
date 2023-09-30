from random import randint
from os import environ

environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 700
HEIGHT = 600

dots = []
lines = []

lives = 3
next_dot = 0

for dot in range(0,10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    screen.fill("black")
    number = 1
    screen.draw.text("Live = "+str(lives) + " out of 3" ,topleft=(10,10))
    for dot in dots:
        screen.draw.text(str(number), (dot.x+8,dot.y+8))
        dot.draw()
        number = number +1
    for line in lines:
        screen.draw.line(line[0],line[1],(0,139,139))
    if lives == 0:
        screen.fill("red")
        screen.draw.text("Game Over",topleft=(250,HEIGHT/2),fontsize=60)

def on_mouse_down(pos):
    global next_dot
    global lines
    global lives

    if lives == 0: return
    
    if dots[next_dot].collidepoint(pos):
        if next_dot:
           lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
        next_dot = next_dot +1
    else:
        lines=[]
        next_dot = 0
        lives = lives - 1
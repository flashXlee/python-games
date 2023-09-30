from random import randint
apple = Actor("apple")
score = 0

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Score " + str(score), topleft=(10,10))

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    
def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("whoa! Good shot")
        score = score +1
        place_apple()
    else:
        print("UnLuCkLy You missed")
        quit()

place_apple()


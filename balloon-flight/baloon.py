from random import randint
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400, 300

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

house = Actor("house")
house.pos = randint(800, 1600),460

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10,200)

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
scores = []

def draw():
    screen.blit("background",(0, 0))
    if not game_over:
        tree.draw()
        balloon.draw()
        house.draw()
        bird.draw()
        screen.draw.text("Score: " + str(score), (700,5), color="black")
    else:
        dispaly_high_scores()

def on_mouse_down():
    global up
    up = True
    balloon.y -= 50

def on_mouse_up():
    global up
    up = False

def flap():
    global bird_up
    if bird_up:
        bird.image="bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

def update():
    global game_over
    if not game_over:
        if not up:
            balloon.y+=1
        if balloon.y < -10 or balloon.bottom > 560:
            game_over = True
            update_high_scores()
        
        if balloon.collidepoint(bird.pos) or \
           balloon.collidepoint(tree.pos) or \
           balloon.collidepoint(house.pos):
            game_over = True
            update_high_scores() 
        move_bird()
        move_house()
        move_tree()

def move_bird():
    global number_of_updates, score
    if bird.x > -45:
        bird.x-=3
        if number_of_updates == 9:
            flap()
            number_of_updates=0
        else:
            number_of_updates+=1
    else:
        bird.pos = randint(800, 1600), randint(10,200)
        score +=1
        number_of_updates =0

def move_house():
    global score
    if house.x > -45:
        house.x -= 2
    else:
        house.pos = randint(800, 1600),460
        score+=1          

def move_tree():
    global score
    if tree.x > -45:
        tree.x-= 2
    else:
        tree.pos = randint(800, 1600), 450
        score +=1

def update_high_scores():
    global scores
    local_score = score
    filename = r"/Users/sami/code/python-games/balloon-flight/top_legendery_scores.txt"
    scores=[]
    with open(filename, "r") as file:
        line = file.readline()
        highscores=line.split()
        for top_score in highscores:
            if local_score > int(top_score):
                scores.append(str(local_score) + " ")
                local_score = int(top_score)
            else:
                scores.append(str(top_score) + " ")
        
    with open(filename, "w") as file:
        for write_score in scores:
            file.write(write_score)

def dispaly_high_scores():
    screen.draw.text("Your Score is " + str(score), (350, 150), color="maroon")
    screen.draw.text("HIGH SCORES", (350, 200), color="black")
    y = 225
    position = 1
    for high_score in scores:
        screen.draw.text(str(position)+ ") " + high_score, (350, y), color="black")
        y += 25
        position += 1

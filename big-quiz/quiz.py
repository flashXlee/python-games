import os

WIDTH = 1280
HEIGHT = 720
os.environ['SDL_VIDEO_CENTERED'] = '1'

main_box =  Rect(50, 40, 820, 240)
timer_box = Rect(990, 40, 240, 240)
answer_box1 = Rect(50, 358, 495, 165)
answer_box2 = Rect(735, 358, 495, 165)
answer_box3 = Rect(50, 538, 495, 165)
answer_box4 = Rect(735, 538, 495, 165)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]  

score = 0
time_left = 10

q1 = ["What is the capital of France"
      ,"Rome", "Paris", "London", "Berlin", 2]

q2 = ["What is 12 x 7"
      , "84", "96", "72", "88", 1]

q3 = ["What is the ninth month of the year"
      ,"October", "Setember", "November", "Augest", 2]

q4 = ["Which planet is closet to the sun"
      , "Mars", "Venus", "A random star", "Mercury", 4]

q5 = ["Who is the last Pharaoh of Egypt"
      ,"Tutankhamun", "Ramsis", "Cleaopatra", "Khufu", 3]

questions = [q1, q2, q3, q4, q5 ]
question = questions.pop(0)

def draw():
    screen.fill("slate grey")
    screen.draw.filled_rect(main_box, "cyan")
    screen.draw.filled_rect(timer_box, "deep sky blue")
    
    for box in answer_boxes:
        screen.draw.filled_rect(box, "sandy brown")

    screen.draw.textbox(str(time_left), timer_box, color="black")
    screen.draw.textbox(question[0], main_box, color="black")

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index],box, color="black")
        index += 1   

def game_over():
    global question, time_left
    time_left = 0
    message = "Game Over. You got %s questions correct" % str(score)
    question = [message, " ", " ", " ", " ", 5]

def correct_answer():
    global question, score, time_left
    score += 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions devolper")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("You clicked on answer " + str(index))
            if index == question[5]:
                correct_answer()
            else:
                game_over()
        index += 1

def update_time_left():
    global time_left

    if time_left:
        time_left -=1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1 ) 
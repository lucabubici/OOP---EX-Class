# cold = False
# if cold == True:
#     print("Outside is cold, today.")
# else:
#     print("Outside is not cold, today.")

# is_cold = input("Is it cold outside?")
# if answer == True:
#     print("Outside is cold.")
#     temperature_minor_10 = input("Is it the temperature below 10 celsius.")
#     if temperature_minor_10 == True:
#         print("Temperature is below 10 degrees celsius.")
#         have_coat = input("do you have a coat?")
#         while have_coat == True:
#             print("Great! See you soon.")
#         elif have_coat == False:
#             print("I have ordered one for you on Amazon! It will get there tomorrow.")
#         else: 
#             print("You are allowed to enter only 'True' or 'False'")
#     else:
#         print("Just wear a jumper")
# else:
#     print("There will be good weather today!")

# password_input = input("Insert you password") 
# password = "3D4%"

# if password_input == password:
#     print("Access granted")
# else:
#     print("Access denied. The password is incorrect.")
    
# score = 80 
# if score >= 85:
#     print("Grade is HD")
# elif score >= 80:
#     print("Grade is D")
# else:
#     print("Needs improvements")


# score = int(input("Enter grade..."))

# if score >= 90:
#     print("Your grade is A.")
# elif score >= 80:
#     print("Your grade is B")
# elif score >= 70:
#     print("Your grade is C")
# elif score >= 60:
#     print("Your grade is D")
# else:
#     print("Your grade is F")


# import turtle
# turtle.showturtle
# turtle.bgcolor('blue')
# turtle.forward(50)
# turtle.setheading(60)
# turtle.forward(50)
# turtle.done()

#SNAKE GAME
import turtle



# CANVAS
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

screen.tracer(0)

# PLAYER
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)

segments = []

#MOVEMENT
head.direction = "stop"

#MOVEMENT FUNCTIONS
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
    
# MOVEMENT
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# KEYBOARD CONTROLS
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

screen.onkey(go_up, 'Up')
screen.onkey(go_down, "Down")
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')



# ADD FOOD
import random

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# GAME LOOP
import time

while True:
    screen.update()

    # MOVE BODY SEGMENTS (BACK TO FRONT)
    for i in range(len(segments)-1, 0 , -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    # MOVE FIRST SEGMENT TO HEAD
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()

    # Collision Detection
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # BORDER COLLISION 
    boundary = 290
    margin = 10

    if (head.xcor() > boundary + margin and head.direction == "right") \
        or (head.xcor() < -boundary + margin and head.direction == "left") \
        or head.ycor() > boundary + margin and head.direction == "up" \
        or head.ycor() < -boundary + margin and head.direction == "down":

        head.goto(0, 0)
        head.direction = "stop"

        # HIDE SEGMENTS
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
    
    time.sleep(0.1)

turtle.done()


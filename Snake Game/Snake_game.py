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
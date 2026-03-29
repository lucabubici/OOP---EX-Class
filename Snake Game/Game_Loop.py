import Snake_game

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
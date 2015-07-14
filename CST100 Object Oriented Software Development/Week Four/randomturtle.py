## Random turtles

import turtle
import random

wn = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def isInScreen(w, t):
    leftBound = -(wn.window_width()/2)
    rightBound = wn.window_width()/2
    topBound = wn.window_height()/2
    bottomBound = -(wn.window_height()/2)

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

numberOfMoves = 0

while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:       ## Heads
        t.left(90)
    else:               ## Tails
        t.right(90)

    t.forward(50)

    numberOfMoves = numberOfMoves + 1

print(numberOfMoves)

wn.exitonclick()


    

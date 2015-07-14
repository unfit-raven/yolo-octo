import turtle               ## Import turtle module

wn = turtle.Screen()        ## Create a graphics window
wn.bgcolor("blue")          ## Sets background color of window
tom = turtle.Turtle()       ## Create a turtle named tom
tom.speed(0)                ## Set tom's speed
## tom.hideturtle()            ## Hide tom from view

## -------------------
## - Define functions
## -------------------

def repositionTurtle(t, x, y):
    """Make turtle t move to x, y coordinates"""
    t.up()
    t.goto(x, y)
    t.down()

def drawCircle(t, x, y, z):
    """Make turtle t draw circle with range x, forward y, left z and fill"""
    t.color("white")
    t.begin_fill()
    for i in range(x):
        t.forward(y)
        t.left(z)
    t.end_fill()
    t.color("black")
    for i in range(x):
        t.forward(y)
        t.left(z)
    

## ---------------
## - Draw snowman
## ---------------
        
repositionTurtle(tom, 0, -250)      ## For bottom circle
    
drawCircle(tom, 313, 2, 1.15)       ## Bottom circle



repositionTurtle(tom, 0, -50)       ## For middle circle

drawCircle(tom, 313, 1.5, 1.15)     ## Middle circle



repositionTurtle(tom, 0, 100)       ## For top circle

drawCircle(tom, 313, 1.1, 1.15)     ## Top circle





wn.exitonclick()

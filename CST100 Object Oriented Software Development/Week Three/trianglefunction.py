import turtle               ## Import turtle module

wn = turtle.Screen()        ## Create a graphics window
wn.bgcolor("blue")          ## Sets background color of window
tom = turtle.Turtle()       ## Create a turtle named tom
tom.speed(1)                ## Set tom's speed
## tom.hideturtle()            ## Hide tom from view

## -------------------
## - Define functions
## -------------------

def repositionTurtle(t, x, y):
    """Make turtle t move to x, y coordinates"""
    t.up()
    t.goto(x, y)
    t.down()
    

def drawTriangle(t, color, x, y):
    """Make turtle t draw triangle in c color, forward x"""
 ##   t.color(color)
 ##   t.begin_fill()
    for i in range(3):
        t.forward(x)
        t.right(y)
 ##   t.end_fill()

repositionTurtle(tom, -15, 160)         ## Move for nose
drawTriangle(tom, "orange", 30, 120)         ## Draw nose

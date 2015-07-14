import turtle           ## Import turtle module

wn = turtle.Screen()    ## Create a graphics window
wn.bgcolor("green")     ## Set background color of window
tom = turtle.Turtle()   ## Create a turtle named tom
tom.pensize(3)          ## Sets tom's pensize
tom.color("pink")       ## Sets tom's color
tom.speed(0)

## ----------------
## Define functions
## ----------------

def repositionTurtle(t, x, y):
    """Make turtle t move to x, y coordinates"""
    t.up()
    t.goto(x, y)
    t.down()


def drawSquare(t, sz):
    """Make turtle draw a square with 20 units for each side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

## ---------------------------------------------
## Draw 4 squares and reposition turtle for each
## ---------------------------------------------

for i in range(5):
    drawSquare(tom, 20)
    tom.up()
    tom.forward(40)
    tom.down()

## ---------------------------
## Draw squares within squares
## ---------------------------

repositionTurtle(tom, 0, 100)



wn.exitonclick()




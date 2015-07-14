import turtle       ## Import turtle module

wn = turtle.Screen()        ## Create window
wn.bgcolor("lightgreen")    ## Set background color
tom = turtle.Turtle()       ## Create turtle named tom
tom.pensize(2)              ## Set tom's pensize
tom.color("blue")           ## set tom's color
tom.speed(9)

## Define functions
def drawSquare(t, size):
    """Draw square with "t" turtle and "size" sides as paramters"""
    for i in range(4):
        t.forward(size)
        t.left(90)

## Reposition tom
##tom.up()
##tom.goto(-100, 0)
##tom.down()

## Draw square
for i in range(36):
    drawSquare(tom, 100)
    tom.right(10)

wn.exitonclick()

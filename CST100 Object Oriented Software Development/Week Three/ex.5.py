import turtle       ## Import turtle module

wn = turtle.Screen()    ## Create window
wn.bgcolor("lightgreen") ## Set background color of window
tom = turtle.Turtle()   ## Create turtle named tom
tom.pensize(2)          ## Set tom's pensize
tom.color("blue")       ## Set tom's color
tom.speed(0)            ## Set tom's speed

tom.up()
tom.goto(-150, 0)
tom.down()

tom.left(90)
tom.forward(2)
tom.backward(2)
tom.left(90)

## Functions

def drawSpiral(t, size):
    """Draw spiral with "t" turtle and "size" unit sides"""
    for i in range(2):
        t.forward(size)
        t.right(90)

## Draw spirals
size = 5
for i in range(45):
    drawSpiral(tom, size)
    size = size + 5

tom.up()
tom.goto(100,0)
tom.down()

size = 5
for i in range(45):
    drawSpiral(tom, size)
    size = size + 5
    tom.left(2)
    
wn.exitonclick()

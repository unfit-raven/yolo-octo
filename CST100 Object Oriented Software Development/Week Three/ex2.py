import turtle            ## Import turtle module

wn = turtle.Screen()     ## Make a window
wn.bgcolor("lightgreen") ## Set background color of window
tom = turtle.Turtle()    ## Make a turtle named tom
tom.pensize(3)           ## Set pensize
tom.color("hotpink")     ## Set color

## Function definitions
def drawSquare(t, sz):
    """Draw a square with t turtle, sides sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

## Draw squares
size = 20                ## size of smallest square
for i in range(5):
    drawSquare(tom, size)
    size = size + 20
    tom.up()
    tom.backward(10)
    tom.right(90)
    tom.forward(10)
    tom.setheading(0)
    tom.down()
   
wn.exitonclick()
    

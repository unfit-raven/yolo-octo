import turtle

## Create function to draw squre
def drawSquare(t, sz):
    ## Make turtle t draw a square with side sz

    for i in range(4):
        t.forward(sz)
        t.left(90)

## Create function to draw triangle
def drawTriangle(t, sz):
    ## Make turtle t draw a triangle with side sz
    for i in range(3):
        t.forward(sz)
        t.left(120)

## Create a function to draw an octogon
def drawOctogon(t, sz):
    ## Make turtle t draw an octogon with side sz
    for i in range(8):
        t.forward(sz)
        t.left(45)

## Create window and turtle
wn = turtle.Screen()
alex = turtle.Turtle()

## Call function to draw square, passing actual turtle and side size
drawSquare(alex, 25)

## Call function to draw triangle, passing actual turtle and side size
drawTriangle(alex, 25)

## Call function to draw square, passing actual turtle and side size
drawSquare(alex, 50)

## Call function to draw triangle, passing actual turtle and side size
drawTriangle(alex, 50)

## Call funtion to draw larger square
drawSquare(alex, 100)

## Call funtion to draw larger triangle
drawTriangle(alex, 100)

## Call funtion to draw octogon, passing actual turtle and side size
drawOctogon(alex, 100)

wn.exitonclick()    ## Exit program on mouse click within window




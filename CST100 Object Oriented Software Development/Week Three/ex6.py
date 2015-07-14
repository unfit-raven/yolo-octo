import turtle       ## Import turtle module

wn = turtle.Screen()    ## Create window
tom = turtle.Turtle()   ## Create a turtle named tom

## Poly function
def drawPoly(someturtle, somesides, somesize):
    """Draw shape with "t" turtle, "sides" and "size"""""
    for i in range(somesides):
        tom.forward(somesize)
        tom.left(360/somesides)

## Triangle function that calls poly function
def drawEquitriangle(someturtle, somesides, somesize):
    """Use drawPoly to create triangle"""
    drawPoly(someturtle, somesides, somesize)

#### Call drawPoly function to draw triangle
##drawPoly(tom, 3, 100)
##
#### move tom
##tom.up()
##tom.goto(100, 0)
##tom.down()

drawEquitriangle(tom, 3, 10)



wn.exitonclick()

import turtle       ## Import turtle module

wn = turtle.Screen()    ## Create window
wn.bgcolor("lightgreen") ## Set background color of window
tom = turtle.Turtle()   ## Create turtle named tom
tom.pensize(3)          ## Set tom's pensize
tom.color("hotpink")    ## Set tom's color

## Make polygon
for i in range(8):
    tom.forward(50)
    tom.left(45)

## Move tom away from first polygon
tom.up()
tom.goto(-100, -100)
tom.down()

## Make polygon function
def drawPoly(t, sides, size):
    """Draw a poly gone with number of sides and size passed as parameters"""
    for i in range(sides): ## Pass number of sides(8)
        tom.forward(size)   ## Pass size in units
        tom.left(360/sides) ## Divide 360 by sides (8) for angle of 45 degrees

## Call polygon function
drawPoly(tom, 8, 50)
        
wn.exitonclick()

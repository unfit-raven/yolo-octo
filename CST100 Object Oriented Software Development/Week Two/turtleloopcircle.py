import turtle       ## Import turtle library

wn = turtle.Screen()## Create graphics window
wn.bgcolor("blue")  ## Set window background color to blue

frank = turtle.Turtle()
frank.hideturtle()  ## Turn off turtle animation
frank.speed(0)      ## Animation as fast as possible

## Bottom circle of snowman
frank.color("white")
frank.begin_fill()
for i in range(72):
    frank.right(5)
    frank.forward(13)
frank.end_fill()
 
## Move turtle up to top of next circle
frank.up()          ## Put tail up
frank.left(90)
frank.forward(208)
frank.right(90)
frank.down()        ## Put tail down

## Middle circle of snowman
frank.color("white")
frank.begin_fill()
for i in range(60):
    frank.right(6)
    frank.forward(11)
frank.end_fill()

## Move turtle up to top of next circle
frank.up()          ## Put tail up
frank.left(90)
frank.forward(140)
frank.right(90)
frank.down()        ## Put tail down

## Top circle of snowman
frank.color("white")
frank.begin_fill()
for i in range(40):
    frank.right(9)
    frank.forward(11)
frank.end_fill()

wn.exitonclick()    ## Close window on mouse click

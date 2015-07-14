import turtle               ## Import turtle module

wn = turtle.Screen()        ## Create a graphics window
wn.bgcolor("blue")          ## Sets background color of window
tom = turtle.Turtle()       ## Create a turtle named tom
tom.speed(8)                ## Set tom's speed
tom.hideturtle()

## Reposition tom
tom.up()    
tom.goto(0,-250)
tom.down()

## Bottom circle loop and color fill
tom.color("white")
tom.begin_fill()
for i in range(313):
    tom.forward(2)
    tom.left(1.15)
tom.end_fill()

## Black outline loop
tom.color("black")
for i in range(313):
    tom.forward(2)
    tom.left(1.15)

## Reposition tom
tom.up()
tom.goto(0,-50)
tom.down()

## Middle circle loop and color fill
tom.color("white")
tom.begin_fill()
for i in range(313):
    tom.forward(1.5)
    tom.left(1.15)
tom.end_fill()

## Black outline loop
tom.color("black")
for i in range(313):
    tom.forward(1.5)
    tom.left(1.15)

## Reposition tom
tom.up()
tom.goto(0,100)
tom.down()

## Top circle loop and color fill
tom.color("white")
tom.begin_fill()
for i in range(313):
    tom.forward(1.1)
    tom.left(1.15)
tom.end_fill()

## Black outline loop
tom.color("black")
for i in range(313):
    tom.forward(1.1)
    tom.left(1.15)

## Reposition tom, starting at left eye
tom.up()
tom.goto(-24, 170)

## Draw eyes
tom.color("black")
tom.dot(17)
tom.goto(24,170)
tom.dot(17)

## Reposition tom for nose
tom.goto(-15, 160)

## Draw nose
tom.color("orange")
tom.begin_fill()
for i in [0,1,2]:
    tom.forward(30)
    tom.right(120)
tom.end_fill()

## Reposition tom for buttons
tom.goto(0,60)

## Draw buttons
tom.color("red")
tom.dot(17)
tom.goto(0,40)
tom.dot(17)
tom.goto(0,20)
tom.dot(17)
tom.goto(0,0)
tom.dot(17)

## Draw left arm
tom.goto(-75,30)
tom.color("black")
tom.pensize(6)
tom.down()
tom.right(180)
tom.forward(100)
tom.pensize(3)
tom.left(45)
tom.forward(15)
tom.backward(15)
tom.right(90)
tom.forward(15)
tom.up()

## Draw right arm
tom.setheading(0)
tom.goto(75,30)
tom.pensize(6)
tom.down()
tom.forward(100)
tom.pensize(3)
tom.left(45)
tom.forward(15)
tom.backward(15)
tom.right(90)
tom.forward(15)

## Draw top hat
tom.up()
tom.setheading(0)
tom.goto(-60,200)
tom.down()
tom.pensize(7)
tom.color("black")
tom.begin_fill()
tom.forward(120)
tom.left(90)
tom.forward(10)
tom.left(90)
tom.forward(30)
tom.right(90)
tom.forward(40)
tom.left(90)
tom.forward(60)
tom.left(90)
tom.forward(40)
tom.right(90)
tom.forward(30)
tom.left(90)
tom.forward(10)
tom.end_fill()



















import turtle               ## Import turtle module

wn = turtle.Screen()        ## Create a graphics window
wn.bgcolor("blue")          ## Sets background color of window
tom = turtle.Turtle()       ## Create a turtle named tom
tom.speed(0)                ## Set tom's speed
tom.hideturtle()            ## Hide tom from view

## -------------------
## - Define functions
## -------------------

def repositionTurtle(t, x, y):
    """Make turtle t move to x, y coordinates"""
    t.up()
    t.goto(x, y)
    t.down()

def drawFilledCircle(t, y):
    """Make turtle t draw circle with forward y, left z and fill"""
    t.color("white")
    t.begin_fill()
    for i in range(313):  ## White, filled circle
        t.forward(y)
        t.left(1.15)
    t.end_fill()
   
    t.color("black")
    for i in range(313):  ## Black outline
        t.forward(y)
        t.left(1.15)

def drawDot(t, color, size):
    """Make turtle t draw dot in c color, s pen size"""
    t.color(color)
    t.dot(size)

def drawTriangle(t, color, x, y):
    """Make turtle t draw triangle in c color, forward x"""
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.forward(x)
        t.right(y)
    t.end_fill()

def drawSquare(t, color, x):
    """Make turtle t draw square in c color, forward x"""
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(x)
        t.right(90)
    t.end_fill()

def drawArm(t, x):
    """Make turtle t draw arm, turning x degrees"""
    t.color("black")
    t.pensize(6)
    t.setheading(x)   ## Needed to angle arms correctly, 180 is left, 0 right
    t.forward(100)
    t.pensize(3)
    t.left(45)
    t.forward(15)
    t.backward(15)
    t.right(90)
    t.forward(15)

## ---------------
## - Draw snowman
## ---------------
        
repositionTurtle(tom, 0, -250)      ## For bottom circle   
drawFilledCircle(tom, 2)            ## Bottom circle

repositionTurtle(tom, 0, -50)       ## For middle circle
drawFilledCircle(tom, 1.5)          ## Middle circle

repositionTurtle(tom, 0, 100)       ## For top circle
drawFilledCircle(tom, 1.1)          ## Top circle

repositionTurtle(tom, -24, 170)     ## Move for left eye
drawDot(tom, "black", 17)           ## Dot left eye

repositionTurtle(tom, 24, 170)      ## Move for right eye
drawDot(tom, "black", 17)           ## Dot right eye

repositionTurtle(tom, 0, 60)        ## Move for first button
drawDot(tom, "red", 17)             ## Dot button

repositionTurtle(tom, 0, 40)        ## Move for second button
drawDot(tom, "red", 17)             ## Dot button

repositionTurtle(tom, 0, 20)        ## Move for third button
drawDot(tom, "red", 17)             ## Dot button

repositionTurtle(tom, 0, 0)         ## Move for fourth button
drawDot(tom, "red", 17)             ## Dot button

repositionTurtle(tom, -15, 160)     ## Move for nose
drawTriangle(tom, "orange", 30, 120)## Draw nose

repositionTurtle(tom, -75, 30)      ## Move for left arm
drawArm(tom, 180)                   ## Draw left arm, turning 180 degrees

repositionTurtle(tom, 75, 30)       ## Move for right arm
drawArm(tom, 0)                     ## Draw right arm, at 0 degrees

tom.setheading(0)                   ## Reset tom's position to default

repositionTurtle(tom, -220, -135)   ## Move for tree trunk
drawSquare(tom, "brown", 35)        ## Draw square for tree trunk

## Draw body of tree
tom.color("Green")
tom.backward(35)
tom.begin_fill()
for i in [0,1,2]:
    tom.forward(105)
    tom.left(120)
tom.end_fill()

repositionTurtle(tom, -60, 200)

## Draw top hat
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
tom.up()

wn.exitonclick()

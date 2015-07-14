import turtle 

wn = turtle.Screen()   # creates a graphic window

alex = turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)

tina = turtle.Turtle()
tina.left(180)
tina.forward(150)
tina.right(90)
tina.forward(75)
tina.right(90)
tina.forward(150)
tina.right(90)
tina.forward(75)

alex.forward(75)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(225)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)

tina.forward(75)
tina.right(90)
tina.forward(150)
tina.right(90)
tina.forward(225)
tina.right(90)
tina.forward(150)
tina.right(90)
tina.forward(150)

wn.exitonclick()

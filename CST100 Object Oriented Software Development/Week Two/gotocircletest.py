import turtle           ## import turtle library/module

wn = turtle.Screen()    ## Create a graphics window from turtle
wn.bgcolor("blue")


tom = turtle.Turtle()   ## Create a Turtle named tom from turtle
tom.speed(0)

tom.up()                ## Tail up
tom.goto(0,-50)         ## Move tom
tom.down()              ## Tail down

tom.color("white")      ## Set color of turtle to white
tom.begin_fill()        ## Begin filling circle with color
for i in range(72):     ## Loop to draw bottom circle
    tom.right(5)
    tom.forward(10)
tom.end_fill()          ## End filling circle with color


## Loop to make black outline
tom.color("black")
for i in range(72):     
    tom.right(5)
    tom.forward(10)
    

tom.up()                ## Tail up
tom.goto(0,98)          ## Move tom
tom.setheading(0)
tom.down()              ## Tail down

tom.color("white")      ## Set color of turtle to white
tom.begin_fill()        ## Begin filling circle with color
for i in range(52):     ## Loop to draw middle circle
    tom.right(7)    
    tom.forward(9)
tom.end_fill()          ## End filling circle with color


## Loop to make black outline
tom.color("black")
for i in range(52):     
    tom.right(7)    
    tom.forward(9)
    

tom.up()                ## Tail up
tom.goto(0,200)        ## Move tom
tom.setheading(0)
tom.down()              ## Tail down

tom.color("white")      ## Set color of turtle to white
tom.begin_fill()        ## Begin filling circle with color
for i in range(40):     ## Loop to draw top circle
    tom.right(9)
    tom.forward(8)
tom.end_fill()          ## End filling circle with color


## Loop to make black outline
tom.color("black")
for i in range(40):     
    tom.right(9)
    tom.forward(8)

## Set eyes
tom.up()
tom.goto(13,170)
tom.dot(17, "black")
tom.goto(-33,170)
tom.dot(17,"black")


## Set nose
tom.goto(-20,158)
tom.setheading(0)
tom.down()
tom.color("orange")
tom.begin_fill()
for i in [0,1,2]:
    tom.forward(20)
    tom.right(120)
tom.end_fill()

## Set buttons
tom.up()
tom.goto(0,70)
tom.dot(17,"red")
tom.goto(0,50)
tom.dot(17,"red")
tom.goto(0,30)
tom.dot(17,"red")
tom.goto(0,10)
tom.dot(17,"red")

wn.exitonclick()        ## Close window on mouse click  

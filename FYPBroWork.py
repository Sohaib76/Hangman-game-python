import turtle

myTurtle = turtle.Turtle()

#For Rectangle
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(50)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(50)
myTurtle.left(90)

myTurtle.clear()

#For Circle
myTurtle.circle(50)

myTurtle.clear()

#For Triangle
myTurtle.forward(100) # draw base
myTurtle.left(120)
myTurtle.forward(100)
myTurtle.left(120)
myTurtle.forward(100)

myTurtle.clear()
myTurtle.reset()

#For Square
myTurtle.color("red")
myTurtle.begin_fill()
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.end_fill()



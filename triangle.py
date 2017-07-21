from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
t.penup()
setup(500,300)
x_pos = -0
y_pos = -0
t.setposition(x_pos, y_pos)

### Write your code below:
t.pendown()
t.pencolor("black")
t.fillcolor("hot pink")
t.begin_fill()
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward (100)
t.right(120)
t.forward(100)
t.end_fill()
# Close window on click.
exitonclick()

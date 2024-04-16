# In this we will create a Simple Square shape using python turtle
import turtle
pointer = turtle.Turtle()
pointer.color("white")
wn = turtle.Screen()
wn.bgcolor("black")
pointer.begin_fill()
pointer.fillcolor("blue")
for i in range(4):
    pointer.forward(100)
    pointer.left(90)
pointer.end_fill()
pointer.hideturtle()
turtle.done()


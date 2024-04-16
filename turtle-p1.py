# Basic of turtle
import turtle
# by using import turtle . we can import turtle libray.
pointer = turtle.Turtle()
#  "pointer" is the name of the variable . you can use any name like a , b , c . Here "turtle" is the module name and "TURTLE" is the class.
pointer.shape("turtle")
#By using .shape() we change the shape of the pointer. There are few pr-define shapes.
wn = turtle.Screen()
# wn is a variable name which we are using for calling turtle screen
wn.bgcolor("black")
#By using .bgcolor() we can chnage the color of the background of the screen.
pointer.color('green','white')
# one is the line color and other is the pointer color.
pointer.forward(100)
#forward is use to move the pointer forward direction and by giving value , it move the number of blocks.
pointer.backward(100)

pointer.setheading(180)
#By using .setheading('angle_name') we can change the face/head of the pointer . Understand it as , it is present in a graph and you can change the face by giving the angle
pointer.backward(100)

pointer.right(20)
#It will turn the pointer to the 20degree right. you can use left / right . it work same as forward / backward .

turtle.done()
# it is use to stop the screen from closing.
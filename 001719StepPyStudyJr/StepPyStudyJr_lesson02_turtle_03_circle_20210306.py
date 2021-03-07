import turtle
# import random

window = turtle.Screen()
turtle.reset()

turtle.shape("classic")
turtle.bgcolor("yellow")
turtle.color("red")

turtle.speed(3)
turtle.pensize(2)

turtle.circle(80)
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.circle(80)
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.circle(80)

window.exitonclick()

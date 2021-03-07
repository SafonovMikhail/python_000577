import turtle

window = turtle.Screen()
turtle.reset()

turtle.shape("classic")
turtle.bgcolor("dark slate gray")
turtle.color("alice blue")

turtle.speed(4)
turtle.pensize(2)

for i in range(12):
# for i in range(24):
    turtle.left(30)
    # turtle.left(15)
    turtle.forward(40)
    # turtle.forward(140)
    turtle.left(90)
    # turtle.left(15)
    turtle.forward(40)
    # turtle.forward(140)
    turtle.left(90)
    # turtle.left(15)
    turtle.forward(40)
    # turtle.forward(140)
    turtle.left(90)
    turtle.forward(40)
    # turtle.forward(140)
    turtle.left(90)

window.exitonclick()

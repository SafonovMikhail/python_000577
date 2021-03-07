import turtle

window = turtle.Screen()
turtle.reset()

turtle.shape("classic")
turtle.bgcolor("dark slate gray")
turtle.color("alice blue")
turtle.speed(4)
turtle.pensize(2)

for i in 1, 2, 3, 4, 5, 6:
    turtle.left(30)

    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)

window.exitonclick()

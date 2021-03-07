import turtle

window = turtle.Screen()
turtle.reset()

turtle.shape("turtle")
turtle.bgcolor("black")
turtle.pencolor("yellow")

turtle.speed(100)
turtle.pensize(2)

for i in range(360):
    turtle.pensize(int(i / 100) + 1)
    turtle.forward(i)
    turtle.left(59)
    # turtle.left(35)

window.exitonclick()

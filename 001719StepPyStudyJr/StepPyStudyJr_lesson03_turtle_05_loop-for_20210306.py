import turtle

window = turtle.Screen()
turtle.reset()

turtle.shape("classic")
turtle.bgcolor("black")
turtle.pencolor("purple")

turtle.speed(100)
turtle.pensize(2)

# for i in range(30):
for i in range(30):
    turtle.circle(5 * i)
    # turtle.circle(-5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)

window.exitonclick()

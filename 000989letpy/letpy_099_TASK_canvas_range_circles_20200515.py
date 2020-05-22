import canvas
import time

rad = 180
for i in range(7, rad, 7):
    canvas.circle(175, 175, i)
    if i % 2 == 0:
        canvas.set_color("Red")
    else:
        canvas.set_color("Grey")
    canvas.draw()

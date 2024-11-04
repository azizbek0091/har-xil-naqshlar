import turtle as t
from colorsys import *
t.speed(0)
t.bgcolor("black")
y = 0
for i in range(90):
    c = hsv_to_rgb(y,1,0.9)
    y += 0.014
    t.pencolor(c)
    for j in range(5):
        t.forward(i - 3)
        t.right(9 * 5)
        t.left(8)
    t.right(115)
    t.hideturtle()
t.done()
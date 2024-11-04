from turtle import *
from colorsys import *
speed(0)
bgcolor('black')
y = 0
for i in range(120):
    c = hsv_to_rgb(y,1,0.8)
    y += 0.002
    color(c)
    lt(7.5)
    fd(60)
    rt(175)
    for j in range(4):
        fd(i * -1)
        lt(6)
    hideturtle()
done()
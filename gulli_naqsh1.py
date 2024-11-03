import os; os.system("cls")
import turtle as r
import colorsys  

r.tracer(2)
r.bgcolor("black")
r.pensize(2)
n = 100
h = 0

# 25 marta aylantirish
for i in range(40):
    for j in range(4):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 1/n
        r.color(c)
        r.circle(49 + i * 5, 90)
        r.left(90)
    r.right(10)  # Har bir to'rtburchakdan keyin 10 daraja o'ngga aylantirish

r.done()
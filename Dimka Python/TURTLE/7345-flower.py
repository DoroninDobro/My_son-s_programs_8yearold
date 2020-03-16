#
import turtle
t = turtle.Pen()
for x in range(1000000):
    for y in range(4):
        t.circle(x)
        t.left(90)
        t.forward(x/2)

# SquareSpirall.py - Рисование квадратной спирали
import turtle
import time
colors = ['red','yellow','blue','green','black','green','white','purple','pink','orange',]
t = turtle.Pen()
for x in range(0,100000,10):
        for r in range(10):
                t.pencolor(colors[x%7])
                t.forward(x)
                t.right(36)

# SquareSpirall.py - Рисование квадратной спирали
import turtle
import time
t = turtle.Pen()
for x in range(100000):
    for r in range(6):
        t.backward(x)
#time.sleep(0.2)
        t.right(60)

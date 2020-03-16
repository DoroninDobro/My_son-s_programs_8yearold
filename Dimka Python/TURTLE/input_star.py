# SquareSpirall.py - Рисование квадратной спирали
import turtle
import time
u = eval(input("Введите количество сторон"))
t = turtle.Pen()
for x in range(100000):
    for r in range(6):
        t.forward(x)
#time.sleep(0.2)
        t.right(360/u)

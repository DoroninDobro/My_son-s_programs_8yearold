# HexSpiralBeta.py

import turtle
colors=['black', 'orange', 'yellow', 'green', 'blue', 'white']
t=turtle.Pen()
turtle.bgcolor('red')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+2)
    t.forward(x)
    t.left(24)

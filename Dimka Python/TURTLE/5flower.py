# 
import turtle
t = turtle.Pen()
#r = turtle()
colors = ['pink', 'purple']
for x in range(1000000):
    t.pencolor(colors[x%2])
    for y in range(5):
        turtle.bgcolor("green")
        t.circle(x)
        t.left(72)
        
        
        

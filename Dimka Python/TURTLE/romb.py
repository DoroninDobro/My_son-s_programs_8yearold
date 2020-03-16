#
import turtle
t = turtle.Pen()
#r = turtle()
colors = ["red","blue","green","yellow",]
for x in range(1000000):
    t.pencolor(colors[x%4])
    for y in range(5):
        #turtle.bgcolor("")
        t.forward(x)
        t.left(78)
        t.forward(x)
        t.left(108)
       

        

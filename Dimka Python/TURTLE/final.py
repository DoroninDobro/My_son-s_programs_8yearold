import turtle
t = turtle.Pen()
#r = turtle()
colors = ["red","blue","green","yellow",]
t.width(8)
for x in range(7,1000000):
    t.pencolor(colors[x%4])
    turtle.bgcolor("black")
    t.circle(x)
    t.left(120)

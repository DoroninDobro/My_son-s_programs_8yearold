import turtle
t = turtle.Pen()
turtle.bgcolor("pink")
for x in range(1000000):
    t.pencolor('red')
    t.forward(x)
    t.left(64)

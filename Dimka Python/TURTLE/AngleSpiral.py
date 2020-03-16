import turtle
t = turtle.Pen()
for x in range(33,1000000):
    for u in range(x-30):
        t.forward(x*2)
        t.left(360/(x-30))

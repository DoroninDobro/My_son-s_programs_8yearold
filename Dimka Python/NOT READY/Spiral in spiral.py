import turtle
t=turtle.Pen()
t.pencolor('blue')
#t.bgcolor('grey')
for h in range(5000):
    pozi = t.position()
    head = t.heading()
    t.left(64)
    t.forward(h)
    setx(pozi[0])
    sety(pozi[1])
    for x in range(60):
        t.forward(x)
        t.left(60)
        if  (h / 6)%1 == 0:
            pozi = t.position()
            head = t.heading()

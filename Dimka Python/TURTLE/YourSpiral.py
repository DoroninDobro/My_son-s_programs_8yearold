
import turtle
z = input('circle, name or line ')
x = eval(input('angle '))
color = input('PenColor ')
BGcolor = input('BgColor ')
dfg = eval(input('number angle '))
t=turtle.Pen()
t.pencolor(color)
turtle.bgcolor(BGcolor)
if    z == 'name':
    c = turtle.textinput('name','name')
for u in range(360000):
    for r in range(dfg):
        if    z == 'line':
            t.forward(u)
        if  z == 'name' :  
            t.penup()
            t.forward(u*4)
            t.pendown()
            t.write(c, font = ("Arial", int((u+4)/4), "bold"))
        if  z == 'circle':
            t.circle(u*4)
        t.left(x)


import turtle
t=turtle.Pen()
t.pencolor('blue')
#t.bgcolor('grey')
Name = turtle.textinput('what name','name')
for x in range(360):
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(Name, font = ('Arial', int((x + 4) / 4), 'bold'))
    t.left(61)

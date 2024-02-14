import turtle
s = turtle.Screen()#langas
t = turtle.Turtle()#veikejas

colors = ['Aqua', 'Beige', 'Bisque', 'Tomato', 'Violet', 'Olive', 'MediumSpringGreen', 'Lime', 'Red']
s.bgcolor('Black')
s.title('Pirmas kartas')
t.pencolor('yellow')
t.speed(10) 
t.penup()
t.goto(0, -350)
t.pendown()

for i in range(3, 15):
    t.pencolor(colors[(i-3)%len(colors)])
    t.fillcolor(colors[i%len(colors)])
    t.begin_fill()
    for j in range (i):

        t.fd(100)
        t.lt(360/1)








s.exitonclick()
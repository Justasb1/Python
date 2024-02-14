import turtle
s = turtle.Screen()#langas
t = turtle.Turtle()#veikejas

colors = ['Aqua', 'Beige', 'Bisque', 'Tomato', 'Violet', 'Olive', 'MediumSpringGreen', 'Lime', 'Red']
s.bgcolor('Black')
s.title('Pirmas kartas')
#******************************************
def kvadratas():
    for i in range(4):
        t.pencolor(colors[i])
        t.fd(100)
        t.lt(90)
t.speed(10) 
t.penup()
t.goto(-350, 0)
t.pendown()
for j in range(5):
    for i in range (5):
    kvadratas()
    t.penupen()
    t.fd(200)
    t.pendown()








s.exitonclick()
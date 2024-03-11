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
skaitliukas = 0
for i in range(3, 15):
    t.pencolor(colors[skaitliukas])
    if skaitliukas< len(colors)-1:
        skaitliukas += 1
    else :
        skaitliukas = 0
    for j in range (i):

        t.fd(100)
        t.lt(360/1)








s.exitonclick()
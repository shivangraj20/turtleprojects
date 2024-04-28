import turtle
turtle.bgcolor("black")
colors=['red','purple','orange','green','blue','yellow']
turtle.speed(10)
for i in range(200):
    turtle.pencolor(colors[i%6])
    turtle.pensize(i/88 +1)
    turtle.forward(i)
    turtle.left(59)
turtle.done()
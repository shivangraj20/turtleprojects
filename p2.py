import turtle
import math

# Function to draw a smooth curve with Bézier splines for better shape control
def draw_bezier_curve(t, control_points, steps):
  x_points, y_points = zip(*control_points)  # Unpack coordinates separately
  t.penup()
  t.goto(x_points[0], y_points[0])
  t.pendown()
  for i in range(1, steps + 1):
    t.setpos(
        sum(a * b**i for a, b in zip(x_points, range(steps + 1 - i, 0, -1))),
        sum(a * b**i for a, b in zip(y_points, range(steps + 1 - i, 0, -1)))
    )

# Function to draw the left ventricle with a more accurate shape
def draw_left_ventricle(t, radius):
  control_points = [(-radius, 0), (-radius * 0.8, radius * 0.6), (-radius * 0.3, radius * 1.2), (0, radius)]
  draw_bezier_curve(t, control_points, 100)  # Adjust steps for smoothness

# Function to draw the right ventricle with a proportional size
def draw_right_ventricle(t, radius):
  control_points = [(radius * 0.4, 0), (radius * 0.6, radius * 0.4), (radius, radius * 0.8), (radius * 0.7, radius)]
  draw_bezier_curve(t, control_points, 80)  # Adjust steps for smoothness

# Function to draw the aorta and pulmonary artery with proper positioning
def draw_arteries(t, radius):
  t.penup()
  t.goto(0, radius * 0.8)
  t.pendown()
  t.setheading(0)
  t.forward(radius * 0.15)
  t.left(90)
  t.forward(radius * 0.08)

  t.penup()
  t.goto(radius * 0.45, radius * 0.7)
  t.pendown()
  t.setheading(0)
  t.forward(radius * 0.15)
  t.left(90)
  t.forward(radius * 0.08)

# Main program
t = turtle.Turtle()
t.speed(0)  # Set drawing speed to fastest
screen = turtle.Screen()
screen.bgcolor("lightblue")

t.pensize(3)
t.pencolor("red")

draw_left_ventricle(t, 50)
draw_right_ventricle(t, 50)
draw_arteries(t, 50)

t.hideturtle()
screen.exitonclick()
t.goto(0 ,radius * 0.7)
t.pendown()
t.setheading(0)
t.forward(radius * 0.2)
t.left(90)
t.forward(radius * 0.1)

t.penup()
t.goto(radius * 0.3, radius * 0.6)
t.pendown()
t.setheading(0)
t.forward(radius * 0.2)
t.left(90)
t.forward(radius * 0.1)

# Main program
t = turtle.Turtle()
t.speed(0)  # Set drawing speed to fastest
screen = turtle.Screen()
screen.bgcolor("lightblue")

t.pensize(3)
t.pencolor("red")

draw_left_ventricle(t, 50)
draw_right_ventricle(t, 50)
draw_arteries(t, 50)

t.hideturtle()
screen.exitonclick()

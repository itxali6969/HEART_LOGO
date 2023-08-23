import turtle

turtle.speed(1)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.bgcolor("black")

turtle.left(140)
turtle.forward(224)
for _ in range(200):
    turtle.right(1)
    turtle.forward(2)
turtle.left(120)
for _ in range(200):
    turtle.right(1)
    turtle.forward(2)
turtle.forward(224)

turtle.end_fill()

turtle.hideturtle()
turtle.done()
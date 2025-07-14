from turtle import Turtle, Screen

tim_the_turtle = Turtle()

for i in range(15):
    tim_the_turtle.forward(10)
    tim_the_turtle.color('White')
    tim_the_turtle.forward(10)
    tim_the_turtle.color('black')

# for _ in range(15):
#     tim_the_turtle.forward(10)
#     tim_the_turtle.penup()
#     tim_the_turtle.forward(10)
#     tim_the_turtle.penup()


screen = Screen()
screen.exitonclick()
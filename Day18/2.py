from turtle import Turtle, Screen

tim_the_turtle = Turtle()
tim_the_turtle.shape('turtle')
tim_the_turtle.color('Green')
for i in range(4):
    tim_the_turtle.right(90)
    tim_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()
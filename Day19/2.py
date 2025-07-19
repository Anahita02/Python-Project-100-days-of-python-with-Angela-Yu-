from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def Forwards():
    tim.forward(10)

def Backwards():
    tim.backward(10)

def Counter_Clockwise():
    tim.left(10)
    # new_heading = tim.setheading() + 10
    # tim.setheading(new_heading)

def Clockwise():
    tim.right(10)
    # new_heading = tim.setheading() - 10
    # tim.setheading(new_heading)


def Clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=Forwards)
screen.onkey(key="s", fun=Backwards)
screen.onkey(key="a", fun=Counter_Clockwise)
screen.onkey(key="d", fun=Clockwise)
screen.onkey(key="c", fun=Clear_drawing)



screen.exitonclick()
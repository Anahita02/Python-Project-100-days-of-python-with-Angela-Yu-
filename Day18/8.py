import turtle as t
from turtle import Turtle, Screen
import random

t.Turtle()
# t.pensize(10)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(00, 255)
    random_colors = (r, g, b)
    return random_colors

t.speed('fastest')

# for _ in range(35):
#     t.circle(50)
#     t.left(10)
#     t.color(random_color())

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
import turtle as t
from turtle import Turtle, Screen
import random

tim = t.Turtle()
tim.pensize(10)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(00, 255)
    random_color = (r, g, b)
    return random_color

tim.speed('fast')

moves = [0, 90, 180, 270]


for _ in range(100):
    tim.forward(10)
    tim.setheading(random.choice(moves))
    tim.color(random_color())

screen = Screen()
screen.exitonclick()
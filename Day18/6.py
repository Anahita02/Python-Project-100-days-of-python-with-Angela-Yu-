from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(10)
tim.speed('fast')

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
moves = [0, 90, 180, 270]


for _ in range(100):
    tim.forward(10)
    tim.setheading(random.choice(moves))
    tim.color(random.choice(colors))

screen = Screen()
screen.exitonclick()
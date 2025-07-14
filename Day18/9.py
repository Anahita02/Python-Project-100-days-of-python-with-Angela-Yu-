import turtle as t
from turtle import Turtle, Screen
import random
import colorgram
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

t.colormode(255)
t.speed('fastest')
t.penup()
t.hideturtle()

color_list = [(236, 223, 202), (203, 158, 111), (214, 216, 225), (233, 213, 223), (167, 77, 41), (226, 208, 121), (142, 146, 162), (97, 105, 134), (191, 150, 170), (183, 152, 42), (222, 231, 224), (15, 21, 55), (102, 116, 168), (173, 23, 5), (33, 32, 15), (221, 172, 194), (15, 29, 15), (199, 95, 73), (231, 175, 163), (121, 95, 105), (151, 161, 154), (90, 102, 91), (182, 184, 216), (42, 52, 104), (167, 103, 117), (37, 22, 35), (230, 206, 13), (75, 75, 37), (154, 25, 36), (183, 197, 185)]

t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 101


for dot_count in range(1, number_of_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = Screen()
screen.exitonclick()
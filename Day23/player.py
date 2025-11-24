from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Green")
        self.setheading(90)
        self.penup()
        self.reset_place()

    def Go_Up(self):
        self.forward(MOVE_DISTANCE)

    def reset_place(self):
        self.penup()
        self.goto(STARTING_POSITION)
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self. score_player_left = 0
        self.score_player_right = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_player_left, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.score_player_right, align=ALIGNMENT, font=FONT)

    def left_player_point(self):
        self.score_player_left += 1
        self.update_scoreboard()

    def right_player_point(self):
        self.score_player_right += 1
        self.update_scoreboard()
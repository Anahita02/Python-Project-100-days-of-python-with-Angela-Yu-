from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  
        with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day20\data.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 267)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day20\data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.update_scoreboard()
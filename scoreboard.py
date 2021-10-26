from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-220, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(POSITION)
        self.write(f"level: {self.level}", move=False, align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.goto(POSITION)
        self.write(f"level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"game over", move=False, align="center", font=FONT)
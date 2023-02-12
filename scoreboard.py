from turtle import Turtle

FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(240, 270)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(220, 270)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.lscore=0
        self.rscore=0
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 500)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 500)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def lpoint(self):
        self.lscore+=1
        self.update_scoreboard()

    def rpoint(self):
        self.rscore+=1
        self.update_scoreboard()

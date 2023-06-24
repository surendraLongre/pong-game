from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x_c, y_c):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.penup()
        self.speed("fast")
        self.goto(x_c,y_c)

    def move_up(self):
        if self.ycor()< 500:
            self.goto(self.xcor(), self.ycor()+40)

    def move_down(self):
        if self.ycor()> -500:
            self.goto(self.xcor(), self.ycor()-40)



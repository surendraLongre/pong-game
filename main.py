from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

#initialize constants
screen=Screen()
screen.bgcolor("black")
screen.setup(width=1600,height=1200)
screen.title("Pong")
#screen.trace(0)

#create paddles
paddle=Paddle(780,0)
paddle2=Paddle(-780,0)
top_paddle=Paddle(0, 450)


#create ball
ball=Ball()
ball.right(45)

#create scoreboard
score=ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=paddle.move_up)
screen.onkey(key="Down", fun=paddle.move_down)
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)

while True:
    if ball.xcor()>850:
        score.lpoint()
        ball.reset_position()
    if ball.xcor()< -850:
        score.rpoint()
        ball.reset_position()
    if (ball.distance(paddle)<100 and ball.xcor() > 580) or (ball.distance(paddle2) <100 and abs(ball.xcor())>580) or (ball.distance(top_paddle)<70):
        ball.paddle_bounce()
    ball.bounce()
    ball.move()





screen.exitonclick()

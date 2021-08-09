from turtle import Screen, ycor
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(x=350)
l_paddle = Paddle(x=-350)
ball = Ball()
score_board = Scoreboard()





screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall


    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        

   #Detect collision with the paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
       ball.bounce_x()

    #Detects the ball out of bounds and at the edge of the screen

    if ball.xcor() > 380:
       ball.reset_position()
       score_board.l_point()
       

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()
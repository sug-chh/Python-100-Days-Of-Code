from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


segments = []

screen = Screen()
food = Food()
score_board = ScoreBoard()




screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.123)
    snake.move_snake()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.jump_screen()
        snake.extend()
        score_board.increase_score()

    # Detect collision With Wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()
        
    # Detect collision With Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
screen.exitonclick()

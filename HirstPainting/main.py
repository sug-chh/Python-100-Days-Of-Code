from turtle import Turtle, Screen
import turtle

import random

timmy_the_turtle = Turtle()
turtle.colormode(255)
timmy_the_turtle.shape()
timmy_the_turtle.speed("fastest")

color_list = [(210, 150, 102), (118, 161, 195),
              (229, 216, 111), (139, 96, 74), (200, 94, 78), (81, 90, 145), (130, 182, 134), (198, 135, 153),
              (94, 114, 186), (133, 92, 117), (182, 96, 125), (167, 158, 51), (146, 217, 195), (227, 168, 183),
              (172, 183, 222), (94, 116, 91), (107, 149, 96), (59, 51, 123), (228, 173, 164), (153, 208, 220),
              (240, 234, 4), (87, 155, 161), (57, 42, 80), (69, 52, 84), (63, 51, 71), (75, 58, 46)]
timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
timmy_the_turtle.hideturtle()


def make_dots():
    for i in range(10):
        timmy_the_turtle.dot(10, random.choice(color_list))
        timmy_the_turtle.forward(50)


def make_direction():
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(180)
    timmy_the_turtle.forward(500)
    timmy_the_turtle.setheading(0)


for n in range(10):
    make_dots()
    make_direction()

screen = Screen()
screen.exitonclick()

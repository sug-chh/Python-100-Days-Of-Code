from turtle import Turtle, Screen
import random

"""Etch a sketch"""

# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.speed('fastest')


# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_right():
#     tim.right(10)
#
#
# def turn_left():
#     tim.left(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen = Screen()
# screen.listen()
# screen.onkey(key='Up', fun=move_forwards)
# screen.onkey(key='Down', fun=move_backwards)
# screen.onkey(key='Right', fun=turn_right)
# screen.onkey(key='Left', fun=turn_left)
# screen.onkey(key='c', fun=clear)
# screen.exitonclick()


"""Turtle Racing"""

screen = Screen()
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color.")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [120, 80, 40, 0, -40, -80]

screen.setup(500, 400)

all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)
print(all_turtles)

is_on = False

if user_bet:
    is_on = True

winning_turtle_color = ""

while is_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 230:
            winning_turtle_color = (turtle.pencolor())
            is_on = False
if user_bet == winning_turtle_color:
    print(f"The winner is {winning_turtle_color} turtle. You won!")
else:
    print(f"The winner is {winning_turtle_color}. You lost!")
screen.exitonclick()

# My Logic
# It has finding cooridnate code as well....Review the lecture for that


# from os import stat
# import turtle
# from typing import SupportsComplex
# import pandas
# ALIGNMENT = 'center'
# FONT = ("Courier", 8, "normal")

# screen = turtle.Screen()
# screen.title("U.S. State Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# screen.setup(width=735, height=495)
# turtle.shape(image)
# t2 = turtle.Turtle()
# t2.penup()
# t2.hideturtle()


# guessed_counter = 0
# game_is_on = True
# while game_is_on:
#     answer_state = screen.textinput(title=f"{guessed_counter}/50 States Correct", prompt="What's another state's name.......?                        ")

#     data = pandas.read_csv('50_states.csv')


#     for state in data.state:
#         if answer_state.lower() == state.lower() :
#             guessed_counter += 1
#             filtered_state = data[data.state == state]

#             t2.goto(int(filtered_state.x), int(filtered_state.y))

#             t2.write(f"{state}", align=ALIGNMENT, font=FONT )

#     if answer_state == 'exit':
#         game_is_on = False

#     elif guessed_counter == len(data):
#         game_is_on = False


# screen.exitonclick()


# Angela's way of solving it


import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=735, height=495)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = []
guessed_state = []


while len(guessed_state) < len(data):
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(data)} States Correct",
                                    prompt="What's another state's name.......?                        ").title()

    if answer_state == "Exit":
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)

        missing_state = [
            state for state in all_states if state not in guessed_state]

        states_to_learn = pandas.DataFrame(missing_state)
        states_to_learn.to_csv('states_to_learn.csv')

        break

    all_states = data.state.to_list()

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

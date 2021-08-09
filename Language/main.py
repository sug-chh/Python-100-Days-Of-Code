from tkinter import *

import pandas
from pandas.core.frame import DataFrame
import random

BACKGROUND_COLOR = "#B1DDC6"
FONTFAMILY = "Ariel"

current_card = None

#-----Functionality-----

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

# My way a bold way
# data_list = [{row.French: row.English} for (key, row) in data.iterrows()]
data_dict = DataFrame.to_dict(data, orient="records")


def is_known():

    data_dict.remove(current_card)

    new_data_frame = pandas.DataFrame(data_dict)
    new_data_frame.to_csv("data/words_to_learn.csv", index=False)

    next_item()


def flip():
    global current_card

    canvas.itemconfig(canvas_img, image=new_img)

    canvas.itemconfig(card_title, text="English", fill="white")

    canvas.itemconfig(card_text, text=current_card["English"], fill="white")


def next_item():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(data_dict)

    canvas.itemconfig(canvas_img, image=old_img)

    canvas.itemconfig(card_title, text="French", fill="black")

    canvas.itemconfig(card_text, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip)


#--------UI--------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(height=526,
                width=800,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)
old_img = PhotoImage(file="images/card_front.png")

new_img = PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(400, 263, image=old_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400,
                                150,
                                text="French",
                                font=(FONTFAMILY, 40, "italic"))

card_text = canvas.create_text(400,
                               263,
                               text="Word",
                               font=(FONTFAMILY, 60, "bold"))

# Button Xcross

button_cross_img = PhotoImage(file="images/wrong.png")

button_cross = Button(image=button_cross_img,
                      padx=50,
                      pady=50,
                      highlightthickness=0,
                      command=next_item)
button_cross.grid(row=1, column=0)

# Button Check mark

button_check_img = PhotoImage(file="images/right.png")
button_right = Button(image=button_check_img,
                      padx=50,
                      pady=50,
                      highlightthickness=0,
                      command=is_known)
button_right.grid(row=1, column=1)

flip_timer = window.after(3000, flip)
next_item()
window.mainloop()

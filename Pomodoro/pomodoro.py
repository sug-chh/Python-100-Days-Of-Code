from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(countdown_text, text="00:00")
    timer_text.config(text="Timer")
    check_list.config(text="")
    global reps
    reps = 0
    button_start.config(state="active")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    button_start.config(state="disabled")
    window.state(newstate="normal")

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_second)
        timer_text.config(text="Short Break", fg=PINK)

    else:
        count_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    if count >= 0:
        global timer
        canvas.itemconfig(
            countdown_text, text=f"{count_min} : {count_seconds}")
        timer = window.after(1000, count_down, count - 1)

    else:

        start_timer()

        marks = ""
        # My way:
        # for n in range(1, reps + 1):
        #     if n % 2 == 0:
        #         marks += "✔"
        # check_list.config(text=marks)

        # Angela's Way:

        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_list.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

countdown_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer
timer_text = Label(text="Timer", font=(
    FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(row=0, column=1)


# Button

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)


button_end = Button(text="Reset", command=reset_timer)
button_end.grid(row=2, column=2)


# Checklist

check_list = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
check_list.grid(row=3, column=1)


window.mainloop()

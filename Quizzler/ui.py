from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white")

        self.score_text = Label(text="Score : 0", bg=THEME_COLOR, fg="white")

        self.score_text.grid(row=0, column=1)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.quiz_text = self.canvas.create_text(150, 125, text="Hi this is me", font=(
            "Arial", 20, "italic"), fill=THEME_COLOR, width=300)

        self.button_correct_img = PhotoImage(file="images/true.png")
        self.button_correct = Button(
            image=self.button_correct_img, command=self.button_right_pressed)

        self.button_correct.grid(row=2, column=0)

        self.button_wrong_img = PhotoImage(file="images/false.png")
        self.button_wrong = Button(
            image=self.button_wrong_img, command=self.button_wrong_pressed)

        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.score_text.config(text=f"Score : {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question_text)

        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the Quiz !")
            self.button_correct.config(state="disable")
            self.button_wrong.config(state="disabled")

    def button_right_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def button_wrong_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

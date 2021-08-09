from turtle import Turtle, mode

ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")

with open("data.txt") as data:
    high_score_data = int(data.read())

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = high_score_data
        print(self.high_score)
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
        
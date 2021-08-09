from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score : {self.l_score} || {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()


    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
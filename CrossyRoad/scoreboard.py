from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)
        
       
    def increment_score(self):
        self.clear()
        self.level = self.level + 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
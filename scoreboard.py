from turtle import Turtle

class Scoreboard(Turtle): # scoreboard design
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self): # updates scoreboard to stop drawing overlap
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 40, "normal"))

    def r_score_point(self): # adds point to L
        self.l_score += 1
        self.update_scoreboard()

    def l_score_point(self): # adds point to R
        self.r_score += 1
        self.update_scoreboard()
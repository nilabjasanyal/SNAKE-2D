from turtle import Turtle

class PointBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point=0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=("Arial", 40, "normal"))

    def update_scoreboard(self):
        self.write(f"score: {self.point}", align='center', font=("Arial", 20, "normal"))

    def show_score(self):
        self.clear()
        self.point += 1
        self.update_scoreboard()




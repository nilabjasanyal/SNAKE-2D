from turtle import Turtle
import random as r
# import snake as s
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.speed('fastest')
    def refresh(self):
        x=r.randint(-280,280)
        y=r.randint(-280,280)
        self.goto(x,y)








import turtle as t
move_distance=20
RIGHT=0
UP=90
DOWN=270
LEFT=180
class Snake():
    def __init__(self):
        self.position_list=[]
        self.segment_list = []
        self.create_snake()
        self.head=self.segment_list[0]
    def create_snake(self):
        x = 0
        for a in range(3):
            timmy_main = t.Turtle('square')
            timmy_main.penup()
            timmy_main.goto(x=x, y=0)
            x -= 20
            self.segment_list += [timmy_main]

    def extend(self):
        self.extended_segment=self.segment_list[-1]
        tommy=t.Turtle('square')
        tommy.penup()
        tommy.goto(self.extended_segment.position())
        self.segment_list+=[tommy]


    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


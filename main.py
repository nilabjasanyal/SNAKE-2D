from turtle import Screen
import time
import snake as s
from snakefood import Food
from scoreboard import PointBoard
points=0
my_screen = Screen()
my_screen.setup(height=600, width=600)
my_screen.bgcolor('navy blue')
my_screen.title('SNAKE GAME')
my_screen.tracer(0)
cobra = s.Snake()
food = Food()
score_board=PointBoard()


should_continue = True

while should_continue:
    my_screen.update()
    time.sleep(0.08)
    cobra.move()
    my_screen.listen()
    my_screen.onkey(cobra.up, "w")
    my_screen.onkey(cobra.down, "s")
    my_screen.onkey(cobra.left, "a")
    my_screen.onkey(cobra.right, "d")

    if cobra.head.distance(food)<15:
        print("nom nom nom")
        points += 1
        score_board.show_score()
        food.refresh()
        cobra.extend()

#DETECT COLLISION WITH THE WALL

    if cobra.head.xcor()>300 or cobra.head.xcor()<-300 or cobra.head.ycor()>300 or cobra.head.ycor()<-300:
        score_board.game_over()
        should_continue=False
    for segment in cobra.segment_list[1:]:
        if cobra.head.distance(segment)<=10:
            score_board.game_over()
            should_continue=False






my_screen.exitonclick()
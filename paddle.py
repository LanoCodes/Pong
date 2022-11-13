from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, coord):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coord)


    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

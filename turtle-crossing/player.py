from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.at_finish_line = False

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() == 280:
            self.at_finish_line = True

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake_segment = Turtle("square")
            new_snake_segment.color("white")
            new_snake_segment.penup()
            new_snake_segment.goto(position)
            self.snake_segments.append(new_snake_segment)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

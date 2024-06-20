from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")


screen.exitonclick()

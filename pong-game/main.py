from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

while game_is_on:
    screen.update()
    screen.listen()
    ball.move()
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")

    #Detect collision with wall.
    if ball.ycor() > 290 or ball.ycor() <= -290:
        ball.bounce_y()

    #Detect collision with paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() > -380:
        ball.bounce_x()


screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    screen.listen()
    ball.move()
    scoreboard.update_scoreboard()
    screen.onkey(right_paddle.move_up, "Up")
    screen.onkey(right_paddle.move_down, "Down")
    screen.onkey(left_paddle.move_up, "w")
    screen.onkey(left_paddle.move_down, "s")

    #Detect collision with wall.
    if ball.ycor() > 290 or ball.ycor() <= -290:
        ball.bounce_y()

    #Detect collision with paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() > -330:
        ball.bounce_x()

    #Detect ball out of bounds right.
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_score += 1
        scoreboard.update_scoreboard()
        if scoreboard.left_score >= 3:
            scoreboard.end_game("Right player")
            game_is_on = False

    #Detect ball out of bounds left.
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_score += 1
        scoreboard.update_scoreboard()
        if scoreboard.right_score >= 3:
            scoreboard.end_game("Left player")
            game_is_on = False

screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
protagonist = Player()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(protagonist.move, "Up")

    #Detect when at finish line.
    if protagonist.at_finish_line:
        print("You made it!")
        game_is_on = False


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
protagonist = Player()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(protagonist.move, "Up")
    car_manager.create_car()
    car_manager.move_cars()

    #Detect when at finish line.
    if protagonist.at_finish_line():
        protagonist.go_to_start_position()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

    #Detect collision with car.
    for car in car_manager.car_list:
        if car.distance(protagonist) < 20:
            scoreboard.game_over_text()
            game_is_on = False

screen.exitonclick()

from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Car_manager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Road Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = Car_manager()

cars = []

screen.listen()
screen.onkeypress(player.move, " ")


game_is_on = True
while game_is_on:


    car.create_car(scoreboard.level)
    car.move_car()
    # send player to start after road crossed and increse the level too.
    if player.ycor() > 260:
        print("-----------")
        player.start()
        scoreboard.level_inc()
        car.inc_car_speed()

    for i in car.all_cars:
        if i.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()




    time.sleep(0.1)
    screen.update()



screen.exitonclick()
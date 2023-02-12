import time
from turtle import Screen
from player import Turtoise
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtoise = Turtoise()
car_spawn_timer = 0
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtoise.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    car_spawn_timer += 1

    if car_spawn_timer % 10 == 0:
        car_manager.spawn_car()
    car_manager.move_car()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtoise) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtoise.is_at_finish_line():
        turtoise.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()

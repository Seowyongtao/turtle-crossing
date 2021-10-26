import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = []
speed = 0.1

screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(speed)
    random_int = random.randint(1, 10)
    if random_int < 3:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:

        car.move()

        # DETECT COLLISION WITH THE WALL
        if player.ycor() > 280:
            player.back_to_starting()
            scoreboard.update_score()
            speed *= 0.5

        # DETECT COLLISION WITH THE CAR
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
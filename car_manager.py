from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.moving_distance = STARTING_MOVE_DISTANCE
        self.random_color = random.choice(COLORS)
        self.color(self.random_color)
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.random_y = random.randint(-240, 240)
        self.goto(300, self.random_y)

    def move(self):
        self.forward(self.moving_distance)



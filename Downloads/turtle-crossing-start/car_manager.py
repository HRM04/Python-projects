from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        if random.randint(1,6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_pos = random.randint(-260, 280)
            x_pos = 300
            car.setpos(x_pos, y_pos)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.bk(self.speed)


    def level_up(self):
        self.speed += MOVE_INCREMENT
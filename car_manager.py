from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 40


class CarManager:

    def __init__(self):
        self.cars_moving_list = []
        self.cars_idle_list = []
        self.generate_cars()

    def generate_cars(self):
        for _ in range(0, NUMBER_OF_CARS):
            new_car = Turtle(shape="square")
            new_car.hideturtle()
            new_car.up()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            self.cars_idle_list.append(new_car)

    def turn_car_on(self):
        if random.randint(1, 100) > 85 and len(self.cars_idle_list) >= 1:
            self.cars_moving_list.append(self.cars_idle_list[0])
            self.cars_idle_list.pop(0)
            y_cord = random.randint(-250, 260)
            self.cars_moving_list[-1].goto(300, y_cord)
            self.cars_moving_list[-1].showturtle()

    def turn_car_off(self, car):
        car.hideturtle()
        self.cars_idle_list.append(car)
        self.cars_moving_list.remove(car)

    def move_cars(self):
        for car in self.cars_moving_list:
            x_cord = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(x_cord, car.ycor())
            if car.xcor() <= -320:
                self.turn_car_off(car)

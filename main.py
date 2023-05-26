import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SPEED_MULTIPLIER = 0.8
current_speed = 0.06
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(current_speed)
    screen.update()

    cars.turn_car_on()
    cars.move_cars()

    # Check if player collides with car
    for car in cars.cars_moving_list:
        if player.top_of_player > car.ycor() - 12 and player.bot_of_player < car.ycor() + 12 and player.left_of_player < car.xcor() + 18 and player.right_of_player > car.xcor() - 18:
            scoreboard.lose_screen()
            game_is_on = False

    if player.reached_finish():
        player.reset_player()
        scoreboard.next_level()
        current_speed *= SPEED_MULTIPLIER

screen.exitonclick()
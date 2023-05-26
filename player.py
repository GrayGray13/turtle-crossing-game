from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.top_of_player = self.ycor() + 10
        self.bot_of_player = self.ycor() - 10
        self.left_of_player = -10
        self.right_of_player = 10

    def move(self):
        self.forward(MOVE_DISTANCE)
        self.top_of_player += MOVE_DISTANCE
        self.bot_of_player += MOVE_DISTANCE

    def reached_finish(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset_player(self):
        self.goto(STARTING_POSITION)
        self.top_of_player = self.ycor() + 10
        self.bot_of_player = self.ycor() - 10

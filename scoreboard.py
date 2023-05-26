from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.up()
        self.goto(-215, 250)
        self.update_scoreboard()

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def lose_screen(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=("Courier", 24, "bold"))

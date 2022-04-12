from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 260)
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_update(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)


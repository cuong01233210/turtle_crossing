from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def show_end(self):
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

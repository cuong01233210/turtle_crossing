from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.finish_a_turn()
        self.final_line_y = FINISH_LINE_Y


    def move_left(self):
        self.xpos -= MOVE_DISTANCE
        self.goto(self.xpos, self.ypos)

    def move_right(self):
        self.xpos += MOVE_DISTANCE
        self.goto(self.xpos, self.ypos)

    def move_straight(self):
        self.ypos += MOVE_DISTANCE
        self.goto(self.xpos, self.ypos)

    def finish_a_turn(self):
        self.goto(STARTING_POSITION)
        self.xpos = STARTING_POSITION[0]
        self.ypos = STARTING_POSITION[1]
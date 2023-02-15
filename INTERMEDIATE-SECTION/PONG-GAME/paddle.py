from turtle import Turtle

MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.goto(pos)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)
        self.shape('square')
        self.penup()
        self.color('white')

        # Not Turtle related
        self.score = 0

    def move_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

    def score_point(self):
        self.score += 1

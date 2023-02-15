from turtle import Turtle


MOVE_SPEED = 0.09

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        print(self.move_speed)
        self.x_move *= -1
        self.move_speed *= 0.9

    def score(self):
        self.home()
        self.move_speed = MOVE_SPEED
        self.hit()

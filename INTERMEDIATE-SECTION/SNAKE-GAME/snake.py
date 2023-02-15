import time
from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    """
    The class represents the Snake as a whole, the snake consists of small squared pieces growing by one each time
    the snake eats the food display in the map, these squares are grouped in a list representing the snake's size
    """

    def __init__(self):
        self.segments = []
        self.create_snake(POSITIONS)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self, positions):
        """
        Called in the "snake's creation", setting the initial size of 3 little squares grouped together and appending
        them to the list 'segments' that represents the snake's size
        :return: None
        """

        for position in positions:
            body = Turtle('square')
            body.color('white')
            body.penup()
            body.goto(position)
            self.segments.append(body)

    def go_up(self):
        if abs(self.segments[0].heading() - UP) == 180:
            return
        self.head.setheading(UP)

    def go_down(self):
        if abs(self.segments[0].heading() - DOWN) == 180:
            return
        self.head.setheading(DOWN)

    def go_left(self):
        if abs(self.segments[0].heading() - LEFT) == 180:
            return
        self.head.setheading(LEFT)

    def go_right(self):
        if abs(self.segments[0].heading() - RIGHT) == 180:
            return
        self.head.setheading(RIGHT)

    def move(self, screen):
        """

        :param screen:
        :return:
        """

        head = self.head.heading()
        x_limit = screen.window_width() - 8
        y_limit = screen.window_height() - 8

        for seg_pos in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_pos - 1].xcor()
            new_y = self.segments[seg_pos - 1].ycor()
            self.segments[seg_pos].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def grow(self):
        coord_tail = [tuple(self.tail.position())]
        self.create_snake(coord_tail)


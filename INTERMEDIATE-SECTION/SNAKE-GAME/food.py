from collections import namedtuple
from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.get_random_color())
        self.speed('fastest')
        self.refresh()
        self.screen = screen

    def get_random_color(self):
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        new_color = r, g, b

        return new_color

    def refresh(self):
        reserved = [0, -20, -40]

        max_width, max_height = self.screen.screensize()

        # Setting the map's limits
        Limits = namedtuple('Limits', ['positive_x', 'negative_x', 'positive_y', 'negative_y'])
        limits = Limits(max_width/2 - 20, -max_width/2 + 20, max_height/2 - 20, -max_height/2 + 20)

        while True:
            x_coord = randint(limits.negative_x, limits.positive_x)
            y_coord = randint(limits.negative_y, limits.positive_y)
            if (x_coord % 20 == 0 and y_coord % 20 == 0) or x_coord in reserved:
                break
            else:
                continue

        self.goto(x_coord, y_coord)

    # Destructor
    def __del__(self):
        return
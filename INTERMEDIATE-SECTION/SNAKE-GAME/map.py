from turtle import Screen


class Map:

    def __init__(self):
        self.screen = Screen()
        self.create_map()

    def create_map(self):
        self.screen.setup(width=608, height=608)
        width, height = self.screen.window_width(), self.screen.window_height()
        self.screen.screensize(canvwidth=width-8, canvheight=height-8)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.title('Snake Game')
        self.screen.colormode(255)

    def limits(self):
        x, y = self.screen.screensize()
        x_limit = x / 2
        y_limit = y / 2

        return x_limit, y_limit

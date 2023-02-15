from turtle import Turtle

ALIGN = 'center'
STYLE = 'Courier', 50, 'bold'


def draw_line():
    """
    Draw a line in the middle of the screen to
    :return:
    """

    line = Turtle()
    line.penup()
    line.color('white')
    line.goto(0, 300)
    line.setheading(270)
    line.hideturtle()

    for i in range(60):
        if i % 2 == 0:
            line.pendown()
            line.forward(10)
        else:
            line.penup()
            line.forward(10)


class ScoreBoard(Turtle):

    def __init__(self, player, place):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(place)
        self.player = player
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.player.score}", align=ALIGN, font=STYLE)

    def increase_score(self):
        self.clear()
        self.update_score()

    def restart(self):
        pass


import turtle
from turtle import Turtle

ALIGN = 'center'
STYLE = 'Courier', 16, 'bold'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('yellow')
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f'Score: {self.score}', align=ALIGN, font=STYLE)

    def game_over(self):
        self.home()
        self.write(arg=f'GAME OVER\nScore: {self.score}', align=ALIGN, font=STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def draw_line(self):
        line = Turtle()
        line.color('white')
        line.goto(300)

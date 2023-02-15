import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from gamesettings import ScoreBoard
from gamesettings import draw_line

if __name__ == "__main__":
    # Screen settings
    screen = Screen()
    screen.setup(width=1000, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    # Line
    draw_line()

    # Borders
    y_axis = screen.window_height() / 2
    x_axis = screen.window_width() / 2

    # Paddle settings
    paddle = Paddle((450, 0))
    p1_scoreboard = ScoreBoard(paddle, (50, 210))

    paddle2 = Paddle((-450, 0))
    p2_scoreboard = ScoreBoard(paddle2,  (-50, 210))

    # Ball
    ball = Ball()

    # Movements settings
    screen.listen()
    screen.onkeypress(paddle.move_down, 'Down')
    screen.onkeypress(paddle.move_up, 'Up')
    screen.onkeypress(paddle2.move_down, 's')
    screen.onkeypress(paddle2.move_up, 'w')

    # Gameplay

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Scoring
        if ball.xcor() > 480:
            paddle2.score += 1
            p2_scoreboard.increase_score()
            ball.score()

        elif ball.xcor() < -480:
            paddle.score += 1
            p1_scoreboard.increase_score()
            ball.score()

        # Bouncing
        if ball.ycor() >= 285:
            ball.bounce()
        elif ball.ycor() <= -280:
            ball.bounce()

        # Hitting right player
        if ball.xcor() >= 425 and ball.distance(paddle.position()) <= 65:
            ball.hit()

        # Hitting left player
        if ball.xcor() <= -425 and ball.distance(paddle2.position()) <= 65:
            ball.hit()

    # Exit the game
    screen.exitonclick()


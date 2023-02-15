import time
from map import Map
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def play():
    score = 0

    # Screen settings
    game_map = Map()
    screen = game_map.screen
    x_wall, y_wall = game_map.limits()

    # Snake
    snake = Snake()
    food = Food(screen)
    score_board = ScoreBoard()

    # Gameplay
    screen.listen()
    screen.onkeypress(snake.go_up, "Up")
    screen.onkeypress(snake.go_down, "Down")
    screen.onkeypress(snake.go_left, "Left")
    screen.onkeypress(snake.go_right, "Right")

    alive = True
    while alive:
        screen.update()
        time.sleep(0.1)
        snake.move(screen)

        # Eating the food
        if snake.head.distance(food) < 15:
            snake.grow()
            food.refresh()
            score_board.increase_score()

        # Hitting the wall
        if snake.head.xcor() > x_wall - 10 or snake.head.xcor() < -x_wall + 10:
            alive = False
            score_board.game_over()

        elif snake.head.ycor() > y_wall - 10 or snake.head.ycor() < -y_wall + 10:
            alive = False
            score_board.game_over()

        # Hitting itself
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                alive = False
                score_board.game_over()

    # Exit Game
    screen.exitonclick()


if __name__ == "__main__":
    play()

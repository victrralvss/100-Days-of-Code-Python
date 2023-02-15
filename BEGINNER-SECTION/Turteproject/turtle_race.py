import random
import heroes
from turtle import Turtle
from turtle import Screen


def race():
    # Screens settings
    screen = Screen()
    screen.screensize(canvwidth=600, canvheight=600)
    screen.colormode(255)
    print(screen.screensize())
    print(screen.window_height(), screen.window_height())

    def get_random_color():
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        new_color = r, g, b

        return new_color

    def get_names(competitors):
        names = []
        while True:
            if len(names) == competitors:
                return names
            else:
                name = heroes.gen()
                if name in names:
                    continue
                else:
                    names.append(name)

    def get_turtles(competitors):
        turtles = {}
        names = get_names(competitors)
        y_axis = 125

        for turtle in range(competitors):
            name = names[turtle]
            racer = name
            racer = Turtle()
            racer.shape('turtle')
            racer.color(get_random_color())
            racer.shapesize(2)
            racer.penup()
            racer.speed(2)

            racer.goto(-280, y_axis)
            if competitors == 3:
                y_axis -= 125
            elif competitors == 4:
                y_axis -= 90
            elif competitors == 5:
                y_axis -= 70
            else:
                y_axis -= 50
            turtles.update({name: racer})

        return turtles

    def start_race(turtles):
        while True:
            positions = []
            for racer in turtles.items():
                turtle_name, turtle = racer
                turtle.forward(random.randint(5, 15))
                ran, useless = turtle.position()
                positions.append(ran)
                if ran >= 260:
                    return turtle_name

    num_racers = int(screen.numinput("COMPETITORS", "How many racers will be?\n(MIN: 3 | MAX: 6)", minval=3, maxval=6))
    racers = get_turtles(num_racers)
    winner = start_race(racers)
    print(f"The {winner} won!")
    screen.exitonclick()


if __name__ == "__main__":
    race()
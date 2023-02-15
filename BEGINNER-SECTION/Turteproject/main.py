import random
import turtle
import colorgram
from turtle import Turtle
from turtle import Screen


colors = colorgram.extract("space_pallet.jpg", 30)
color = [color.rgb for color in colors]


def create_palette():
    all_colors = []
    for _ in color:
        r, g, b = random.choice(color)
        new_color = (r, g, b)
        all_colors.append(new_color)

    return all_colors


def painting_art():
    cursor.speed('fastest')
    cursor.hideturtle()
    cursor.setheading(220)
    cursor.penup()
    cursor.forward(300)
    cursor.setheading(0)


    for i in range(1, 1001):
        cursor.dot(5, random.choice(color_palette))
        cursor.forward(10)

        if i % 100 == 0 and i > 0:
            cursor.dot(5, random.choice(color_palette))
            cursor.setheading(90)
            cursor.forward(10)
            if (i/100) % 2 == 0:
                cursor.setheading(0)
            else:
                cursor.setheading(180)


color_palette = create_palette()

# Turtle settings
turtle.colormode(255)

# Screen settings
screen = Screen()
screen.bgcolor("beige")


# Cursor settings
cursor = Turtle()
painting_art()
screen.exitonclick()

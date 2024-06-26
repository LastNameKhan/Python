import turtle
import random

import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('hirst.PNG', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)


color_list = [(250, 248, 245), (251, 246, 249), (242, 249, 246), (241, 246, 250),
 (234, 227, 82), (237, 50, 131), (204, 72, 11), (105, 182, 222),
 (19, 26, 171), (191, 169, 9), (216, 157, 108), (231, 224, 6),
 (22, 101, 166), (197, 5, 69), (214, 130, 184), (9, 189, 215),
 (27, 193, 116), (10, 43, 24), (15, 22, 65), (205, 29, 149),
 (231, 169, 197), (128, 186, 166), (56, 13, 29), (235, 73, 36),
 (114, 101, 203), (189, 15, 3), (121, 216, 234), (156, 215, 200),
 (66, 109, 97), (10, 96, 69)]

turtle.colormode(255)
timmy = Turtle()
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
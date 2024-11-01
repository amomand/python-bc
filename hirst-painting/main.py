import turtle
import colorgram
import random
from turtle import Turtle, Screen

color_list = colorgram.extract("image.jpg", 20)
color_palette = []
tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("dark green")
turtle.colormode(255)
tim.penup()

for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)


def draw_line_of_dots(number_of_dots):
    for i in range(number_of_dots):
        tim.dot(20, random.choice(color_palette))
        tim.penup()
        tim.forward(50)
    tim.back(50*number_of_dots)


def new_line():
    tim.left(90)
    tim.forward(50)
    tim.right(90)


for line in range(10):
    draw_line_of_dots(10)
    new_line()



screen.exitonclick()
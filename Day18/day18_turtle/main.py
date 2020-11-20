from turtle import Turtle, Screen
from random import randint, choice
import turtle
#color_list = ["aliceblue", "slategray", "wheat", "indianred", "pink", "gold", "green", "plum", "blue1", "blue2", "blue3"]
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = [r, g, b]
    return rgb


tim = Turtle()
tim.shape("turtle")
tim.color("black", "DarkSeaGreen4")
# # different shapes
# shape = 3
# while shape < 10:
#     angle = 360 / shape
#     for _ in range(shape):
#         tim.fd(100)
#         tim.rt(angle)
#     shape += 1
#     tim.home()
#     pencolor = choice(color_list)
#     tim.pencolor(pencolor)


# # random walk
# heading_list = [0, 90, 180, 270]
# tim.speed("fastest")
# tim.pensize(15)
#
#
# def random_walk(steps):
#     for i in range(steps):
#         heading = choice(heading_list)
#         tim.setheading(heading)
#         tim.fd(20)
#         tim.pencolor(random_color())
#
#
# random_walk(200)


# spirograph
def spirograph(n):
    for i in range(n+1):
        tim.speed(0)
        tim.circle(120)
        tim.pencolor(random_color())
        tim.tilt(360/n)
        tim.left(360/n)


spirograph(100)
screen = Screen()
screen.exitonclick()

import random
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)
# import colorgram

# # extract colors from Hirst painting
# rgb_colors = []
# colors = colorgram.extract("hirstSpot.jpg", 100)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(234, 225, 206), (215, 216, 223), (207, 157, 109), (108, 110, 127), (139, 142, 157), (235, 211, 224),
              (223, 213, 116), (173, 75, 39), (217, 233, 221), (203, 144, 173), (105, 111, 170), (179, 159, 39),
              (17, 19, 62), (227, 168, 195), (196, 13, 3), (217, 83, 60), (16, 37, 19), (33, 33, 14), (153, 168, 157),
              (234, 171, 161), (199, 9, 21), (142, 77, 91), (88, 106, 91), (208, 75, 93), (43, 45, 118),
              (180, 180, 218), (222, 209, 15), (40, 19, 42), (73, 79, 37), (181, 203, 178), (114, 137, 118),
              (47, 77, 48), (251, 7, 11), (115, 132, 137), (171, 198, 206), (247, 14, 11), (44, 71, 83)]
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed(0)


def hirst(height, width):
    tim.hideturtle()
    for j in range(height + 1):
        for i in range(width + 1):
            pencolor = random.choice(color_list)
            tim.dot(20, pencolor)
            tim.pu()
            tim.fd(40)
        tim.home()
        tim.lt(90)
        tim.fd(40 * j)
        tim.rt(90)



hirst(10, 10)

screen = Screen()
screen.exitonclick()

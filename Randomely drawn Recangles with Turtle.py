# This code draws 200 rectangles using Turtle.
# The rectangles have random side length, color, pen size and coordinates

# importing turtle and random library
from turtle import *
import random

# setting pen speed
TURTLE_SPEED = 50

#setting the number of rectangles to be drawn
RECTANGLES = 200

#setting the maximum thickness of the pen
MAX_PENSIZE = 15


def int_to_hex(random_int):

    return str(hex(random_int))


def rectangle(pen_size, pen_color, travel, angle=90):
# This Function takes the inputs and draws the rectangles.
# Every loop draws a single side of the rectangle. So with 4 repeats 
# The whole rectangles is drawn
    for i in range(4):
        pensize(pen_size)
        color(pen_color)
        forward(travel)
        right(angle)


def movement(x, y):
# raises the pen up and puts it in the new coordinate
    penup()
    goto(x, y)
    pendown()

speed(TURTLE_SPEED)

for i in range(RECTANGLES):
# This function chooses all the random factors of the code.

    # The next 3 lines randomely choose an integer between
    # 0 and 2 to the power of 24, then turn it to a hex
    # and put a "#" sign in front of it to make a color code
    random_color = random.randrange(0, 2 ** 24)
    hex_color = hex(random_color)
    std_color = "#" + hex_color[2:5]
    
    # Random pensize, Color and side length
    rectangle(random.randrange(1, MAX_PENSIZE),
              std_color,
              random.randrange(10, 200))
              
    # Choosing a coordination on the page randomely
    movement(random.randrange(-400, 250), random.randrange(-250, 400))

done()



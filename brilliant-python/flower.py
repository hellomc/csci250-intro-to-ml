# Based on brilliant.org coursework

from turtle import *

hideturtle()
color('black', 'magenta')

def left_turn():
    for i in range(10):
        forward(15)
        left(9)

# Creates one petal with black outline and magenta fill.
def petal():
    begin_fill()
    left_turn()
    left(90)
    left_turn()
    end_fill()
    left(90)

# Creates a flower with 5 petals.
def flower():
    for i in range(5):
        petal()
        right(360/5)

flower()
bye()

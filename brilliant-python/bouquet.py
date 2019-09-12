# Now draw a bouquet of flowers

from turtle import *

hideturtle()
color('black', 'magenta')

def left_turn():
    for i in range(10):
        forward(15)
        left(9)
        
def petal():
    begin_fill()
    left_turn()
    left(90)
    left_turn()
    end_fill()
    left(90)

def flower():
    for i in range(5):
        petal()
        right(360/5)

penup()
back(200)
pendown()

# Create a bouquet of flowers that will be some integer number.
def bouquet(flowers):
    for i in range(flowers):
        flower()
        penup()
        forward(250)
        pendown()

bouquet(3)
bye()

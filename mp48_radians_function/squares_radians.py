import turtle as t
import math

# Set window size and drawing speed.
t.screensize(700, 550)
t.speed(10)

# Use radians for all angle measurements.
t.radians()

def draw_square(size):
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(math.pi/2)
    t.penup()

# Make a pattern of squares.
num_squares = 10
for _ in range(num_squares):
    draw_square(250)
    # Turn an amount that will use all the squares
    #   to complete one full revolution around
    #   the center point.
    t.left((2*math.pi)/num_squares)

# Keep the drawing window open.
t.done()
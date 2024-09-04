import turtle as t

LENGTH=500

def regular_star(n,m):
    """Draws a regular star polygon (not a degenerate one)
       n = number of pointies
       m = number of points to skip
    """

    angle = 360*m/n 

    for count in range(n):
       t.forward(LENGTH)
       t.right(angle)


t.hideturtle()
t.pensize(2)
t.color("green")

regular_star(103,51)

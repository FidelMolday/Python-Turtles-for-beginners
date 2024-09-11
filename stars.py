#!/usr/bin/python3
import turtle

def main():
    count = 1
    while count <= 3:
        turtle.forward(300)
        turtle.right(120)
        count = count + 1
        print(count)

    turtle.penup()
    turtle.goto( turtle.pos() + (0,-160) )
    turtle.pendown()

    count = 1
    while count <= 3:
        turtle.forward(300)
        turtle.right(-120)
        count = count + 1
        print(count)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
#!/usr/bin/python3
# https://pythonprogramminglanguage.com
import turtle
import time

turtle.setworldcoordinates(-250, -250, 640, 480)
turtle.width(20)

turtle.circle(60)
turtle.penup()
turtle.forward(140)
turtle.pendown()
turtle.color("red")
turtle.circle(60)
turtle.penup()
turtle.forward(140)
turtle.pendown()
turtle.color("yellow")
turtle.circle(60)
turtle.penup()
turtle.goto(210, -50)  
turtle.pendown()
turtle.color("blue")
turtle.circle(60)
turtle.penup()
turtle.goto(60, -50)
turtle.pendown()
turtle.color("green")
turtle.circle(60)

time.sleep(5)

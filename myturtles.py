#! /usr/bin/env python

import turtle

color = input("Enter background  color: ")
wn = turtle.Screen()
wn.bgcolor(color)

alex = turtle.Turtle()
alex.pensize(3)
alex.color("white")
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.left(125)
alex.forward(200)

wn.exitonclick()

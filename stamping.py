#! /usr/bin/env python

import turtle

wind = turtle.Screen()
wind.bgcolor("lightblue")

tess = turtle.Turtle()
tess.color("red")
tess.shape("turtle")
tess.speed(1)
tess.up()

for step in range(5, 60, 2):
	tess.stamp()
	tess.forward(step)
	tess.left(24)

tess.color("green")
	
wind.exitonclick()



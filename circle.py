#! /usr/bin/env python

import turtle

wn = turtle.Screen()
wn.bgcolor("lightpink")

clin = turtle.Turtle()
clin.shape("turtle")
clin.pensize(5)
clin.color("white")
clin.up()
for angle in range(0, 360, 20):
	clin.color("yellow")
	clin.forward(100)
	clin.stamp()
	clin.color("green")
	clin.forward(-100)
	clin.left(20)

clin.color("green")

wn.exitonclick()

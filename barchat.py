#! /usr/bin/env python

import turtle

def main():
	numbers = [48, 117, 200, 240, 160, 260, 220]
	sumres = sum(numbers)
	wn = turtle.Screen()
	wn.bgcolor("lightgreen")
	
	bon = turtle.Turtle()
	bon.shape("turtle")
	bon.pensize(2)
	bon.color("white")
	bon.speed(1)
	drawxaxis(bon, (60 * len(numbers)) + 60)
	drawyaxis(bon, (60 * len(numbers)) + 60)
	chart(bon, numbers)
	wn.exitonclick()
	

def chart(t, num):
	t.up()
	for ind in num:
		t.color("white")
		t.forward(30)
		t.down()
		t.left(90)
		t.color("yellow")
		t.forward(ind)
		t.right(90)
		t.forward(10)
		t.color("white")
		t.write(str(ind))
		t.color("yellow")
		t.forward(20)
		t.right(90)
		t.forward(ind)
		t.left(90)
		t.up()
		
def drawxaxis(t, l):
	t.up()
	t.goto(-250,-250)
	t.down()
	t.forward(l)
	t.shape("arrow")
	t.stamp()
	t.shape("turtle")
	t.goto(-250, -250)
	
	
def drawyaxis(t, l):
	t.up()
	t.goto(-250,-250)
	t.left(90)
	t.down()
	t.forward(l)
	t.shape("arrow")
	t.stamp()
	t.shape("turtle")
	t.goto(-250, -250)
	t.right(90)
	
main()

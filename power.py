#! /usr/bin/env python

def square(x):
	total = 0
	for i in range(x):
		total = total + x
	return total

def anypower(x, y):
	total = 0
	for i in range(y):
		for j in range(x):
			total = total + x
	return total

a = int (input(" number:  "))
print("answer:  ", square(a))
b = int (input(" power:  "))
print("answer:  ", anypower(a, b))

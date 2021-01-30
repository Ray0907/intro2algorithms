#!/usr/bin/python3
# -*- coding: utf-8 -*-

from scipy import misc

def newtonsMethod(f, x, tolerance=0.000001):
	while True:
		x1 = x - f(x) / misc.derivative(f, x)
		t = abs(x1 -x)
		if t < tolerance:
			break
		x = x1
	return x1

def f(x):
	return (1.0/4.0)*x**3+(3.0/4.0)*x**2-(3.0/2.0)*x-2

if __name__ == '__main__':
	x = 4
	x0 = newtonsMethod(f, x)
	print('x: ', x)
	print('x0: ', x0)
	print("f(x0) = ", ((1.0/4.0)*x0**3+(3.0/4.0)*x0**2-(3.0/2.0)*x0-2 ))
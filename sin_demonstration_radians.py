# approximation for sin function: sin x = x − x3/3! + x5/5! − x7/7! + ...

import math

def sinpy(x):
	return math.sin(x)

def sin1(x):
	return x
	
def sin2(x):
	return x - (x**3/math.factorial(3))
	
def sin3(x):
	return x - (x**3/math.factorial(3)) + (x**5/math.factorial(5))
	
def sin4(x):
	return x - (x**3/math.factorial(3)) + (x**5/math.factorial(5)) - (x**7/math.factorial(7))
	
def sin5(x):
	return x - (x**3/math.factorial(3)) + (x**5/math.factorial(5)) - (x**7/math.factorial(7)) + (x**9/math.factorial(9))




"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.axis.YAxis as YAx


x = np.linspace((-2*math.pi), (2*math.pi))

line, = plt.plot(x/math.pi, np.sin(x), '--', linewidth=2)
dashes = [10, 1, 100, 1] # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)


line, = plt.plot(x/math.pi, sin1(x), '--', linewidth=2)
dashes = [10, 5, 10, 5] # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

line, = plt.plot(x/math.pi, sin2(x), '--', linewidth=2)
dashes = [20, 5, 10, 5] # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

line, = plt.plot(x/math.pi, sin3(x), '--', linewidth=2)
dashes = [30, 5, 10, 5] # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

line, = plt.plot(x/math.pi, sin4(x), '--', linewidth=2)
dashes = [40, 5, 10, 5] # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

line, = plt.plot(x/math.pi, sin5(x), '--', linewidth=2)
dashes = [50, 5, 10, 5] # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

#YAx.set_data_interval(-10,10)

plt.ylim(-10,10)
#plt.xticks(30)
#plt.yticks(int(1))
plt.grid(True)

plt.show()

# approximation for sin function: sin x = x − x3/3! + x5/5! − x7/7! + ...
# x is in radians

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
	
def sinCalc(i,x):
	'''this is a more general calculation method'''
	'''this should estimate the sin of x (in radians) using i terms'''
	'''the expression is sin x = x**1/1! − x**3/3! + x**5/5! − x**7/7! + ...'''
	'''generalizes to sin x = sum from 1 - i of (x**(2i-1)/(2i-1)!)*(((i%2)*2)-1)'''
	'''the (((i%2)*2)-1) term determines the plu or minus signage of each element of the sum'''
	
	def signage(i):
		'''returns positive signage for odd integers and negative signage for evens'''
		return (((i%2)*2)-1)
	
	def iFactor(i):
		'''returns the exponentiating factor and factorial divisor for the i-th term'''
		return (2*i-1)
		

	estSinX = 0	#initialize value for calculated sin of x
	
	for i in range(1,(i+1)):
		'''the first 'i' is for the for loop'''
		'''the second'i' is number of terms, which was passed to sinCalc function'''
		estSinX = estSinX + signage(i)*(x**iFactor(i))/(iFactor(i))

	return estSinX

"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.axis.YAxis as YAx


x = np.linspace((-2*math.pi), (2*math.pi)) #plots from -2*pi to +2*pi

#plot the 'true'sin function, at least ast numpy sees it
line, = plt.plot(x/math.pi, np.sin(x), '--', linewidth=2)
dashes = [100, 5, 100, 5] # 100 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

#plot the estimate using 1 term
# the following line was commented out, replaced with more general calc below
#line, = plt.plot(x/math.pi, sin1(x), '--', linewidth=2)
line, = plt.plot(x/math.pi, sinCalc(1,x), '--', linewidth=2)
dashes = [10, 5, 10, 5] # 10 points on, 5 off, 10 points on, 5 off
line.set_dashes(dashes)

#plot the estimate using 2 terms
line, = plt.plot(x/math.pi, sin2(x), '--', linewidth=2)
dashes = [20, 5, 10, 5] # 20 points on, 5 off, 10 on, 5 off
line.set_dashes(dashes)

#plot the estimate using 3 terms
line, = plt.plot(x/math.pi, sin3(x), '--', linewidth=2)
dashes = [30, 5, 10, 5] # 30 points on, 5 off, 10 on, 5 off
line.set_dashes(dashes)

#plot the estimate using 4 terms
line, = plt.plot(x/math.pi, sin4(x), '--', linewidth=2)
dashes = [40, 5, 10, 5] # 40 points on, 5 off, 10 on, 5 off
line.set_dashes(dashes)

#plot the estimate using 5 terms
line, = plt.plot(x/math.pi, sin5(x), '--', linewidth=2)
dashes = [50, 5, 10, 5] # 50 points on, 5 off, 10 on, 5 off
line.set_dashes(dashes)

#YAx.set_data_interval(-5,5)
plt.ylim(-5,5)
#plt.xticks(30)
#plt.yticks(int(1))
plt.grid(True)

plt.show()

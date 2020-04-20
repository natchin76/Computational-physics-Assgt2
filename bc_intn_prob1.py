#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:52:54 2020
prob1: backward intergration
@author: chintan
"""
#Part 1:
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import newton
def f(y):
    return(-9*y)
a=0
b=1
n=25
h=(b-a)/(n-1)
y0=np.exp(1)
x=np.linspace(a,b,n)
y=np.zeros(n)
y[0]=y0
for i in range(n-1):
    def g(z):
        return(z-y[i]-h*f(z))
    y[i+1]=newton(g,y[i])
y_ext=np.exp(-9*x+1)
plt.plot(x,y_ext,label='exact soln')
plt.scatter(x,y,label='backward intgn')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
    

#Part 2:    
def f(x,y):
    return(-20*(y-x)**2 + 2*x)
a=0
b=1
n=25
h=(b-a)/(n-1)
y0=1/3
x=np.linspace(a,b,n)
y=np.zeros(n)
y[0]=y0
for i in range(n-1):
    def g(z):
        return(z-y[i]-h*f(x[i+1],z))
    y[i+1]=newton(g,y[i])

plt.scatter(x,y,label='backward intgn')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show() 
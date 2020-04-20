#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:16:02 2020
Prob13: Euler method to solve 2nd order diff eqn
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
a=1
b=2
h=0.001
n=int((b-a)/h+1)
def f(t,y):
    return(np.array([y[1],t*np.log(t)-2*y[0]/t**2+2*y[1]/t]))
t=np.linspace(a,b,n)
y=np.zeros([2,n])
y[:,0]=[1,0]
for i in range(n-1):
    y[:,i+1]=y[:,i]+h*f(t[i],y[:,i])
y_ext=7*t/4 + t**3/2*np.log(t)-3/4*t**3 
plt.plot(t,y[0,:],label='Euler method')
plt.plot(t,y_ext,label='Exact soln')
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()   
    
        

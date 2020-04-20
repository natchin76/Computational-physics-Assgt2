#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:38:07 2020
prob 2: Euler method
@author: chintan
"""
from matplotlib import pyplot as plt
import numpy as np
def f(y,t):
    return(y/t-(y/t)**2)
a=1
b=2
h=0.1
n=(b-a)/h +1
y0=1
t=np.linspace(a,b,n)
y=np.zeros(len(t))
y[0]=y0
for i in range(len(t)-1):
    y[i+1]=y[i]+h*f(y[i],t[i])
y_ext=t/(1+np.log(t))
plt.plot(t,y_ext,label='Exact solution')
plt.scatter(t,y,label='Euler method')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid()
plt.show()    
err=abs(y_ext-y)
rel=abs((y_ext-y)/y_ext)
print('absolute error:',err)
print('relative error:',rel)
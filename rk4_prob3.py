#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:26:42 2020
4th order RK method
@author: chintan
"""
from RK4_fun import RK4
import numpy as np
from matplotlib import pyplot as plt
x0=0
xf=1
y0=[0,0]
n=20
def f(x,y):
    return(np.array([y[1],2*y[1] -y[0] + x*np.exp(x) - x]))
y=RK4(x0,xf,y0,f,n)
x=np.linspace(x0,xf,n)
plt.scatter(x,y[0],label='y(x)')
plt.scatter(x,y[1],label='y\'(x)')
plt.legend()
plt.xlabel('x')
plt.grid()
plt.show()        
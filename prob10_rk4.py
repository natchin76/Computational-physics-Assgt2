#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:30:25 2020
Prob10:RK4 to solve 1st order ode
@author: chintan
"""
#since the domain of t is infinite, instead of solving for t, I solve for arctan(t) as
#the independent variable.
from RK4_fun import RK4
import numpy as np
from matplotlib import pyplot as plt
a=0
b=np.pi/2
x0=[1]
n=1000
def f(u,x):
    return(1/((x**2+np.tan(u)**2)*np.cos(u)**2))
x=RK4(a,b,x0,f,n)
u=np.linspace(a,b,n)
t=np.tan(u)
plt.semilogx(t,x[0])
plt.title('x(t) vs t')
plt.grid()
t1=3.5*1e6
u1=np.arctan(t1)
i=np.argmin(abs(u-u1))
plt.scatter(t1,x[0][i])
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()
print('x(3.5*1e-6)=',x[0][i])

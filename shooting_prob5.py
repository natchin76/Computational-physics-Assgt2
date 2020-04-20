#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:45:33 2020
Prob5: Shooting method
@author: chintan
"""
# I'll use Euler method to solve the ode
import numpy as np
from matplotlib import pyplot as plt
n1=50
n2=100
g=10
t=np.linspace(0,10,n1)
h=10/(n1-1)
x=np.zeros((2,n1,n2))
vi=np.linspace(35,60,n2)
xf=[]
for j in range(n2-1):
    x[:,0,j]=[0,vi[j]]
    for i in range(n1-1):
        x[0,i+1,j]=x[0,i,j]+h*x[1,i,j]
        x[1,i+1,j]=x[1,i,j]-h*g
    xf.append(abs(x[0,n1-1,j]))
j1=np.argmin(xf)
plt.scatter(t,x[0,:,j1],label='v0=%.3f(solution)' %vi[j1])
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.legend()
for i in range(5):
    plt.plot(t,x[0,:,int(n2/5)*i],label='v0=%.3f' %vi[int(n2/5)*i])
    plt.legend()
plt.show()    
print('Solution:\nx=',x[0,:,j1])
    
        
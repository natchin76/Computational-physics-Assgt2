#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:49:06 2020
Prob11:RK4 to solve system of 3 1st order simultaneous ode
@author: chintan
"""
import numpy as np
from RK4_fun import RK4
from matplotlib import pyplot as plt
t0=0
tf=1
n=50
u0=[3,-1,1]
def f(t,u):
    return(np.array([u[0]+2*u[1]-2*u[2]+np.exp(-t),u[1]+u[2]-2*np.exp(-t),u[0]+2*u[1]+np.exp(-t)]))
t=np.linspace(t0,tf,n)
u=RK4(t0,tf,u0,f,n)
for i in range(3):
    plt.plot(t,u[i,:],label='u%d' %i)
plt.legend()    
plt.grid()
plt.xlabel('t')
plt.show()

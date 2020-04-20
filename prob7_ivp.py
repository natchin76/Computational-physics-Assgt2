#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:25:48 2020
Prob 7:solve using scipy_integrate
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp
#1
def f(t,y):
    return(t*np.exp(3*t)-2*y)
y=solve_ivp(f,[0,1],[0],t_eval=np.linspace(0,1,30))
y_ext=1/25*np.exp(-2*y.t)*(1-np.exp(5*y.t)+5*y.t*np.exp(5*y.t))
plt.title('Eqn1')
plt.scatter(y.t,y.y[0],label='Using solve_ivp')
plt.plot(y.t,y_ext,label='Exact soln')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.show()

#2
def f(t,y):
    return(1-(t-y)**2)
y=solve_ivp(f,[2,3],[1],t_eval=np.linspace(2,3,30))
y_ext=(1-3*y.t+y.t**2)/(-3+y.t)
plt.title('Eqn2')
plt.scatter(y.t,y.y[0],label='Using solve_ivp')
plt.plot(y.t,y_ext,label='Exact soln')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.show()

#3
def f(t,y):
    return(1+y/t)    
y=solve_ivp(f,[1,2],[2],t_eval=np.linspace(1,2,30))
y_ext=2*y.t+y.t*np.log(y.t)
plt.title('Eqn3')
plt.scatter(y.t,y.y[0],label='Using solve_ivp')
plt.plot(y.t,y_ext,label='Exact soln')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.show()

#4
def f(t,y):
    return(np.cos(2*t)+np.sin(3*t))  
y=solve_ivp(f,[0,1],[1],t_eval=np.linspace(0,1,30))
y_ext=(8-2*np.cos(3*y.t)+3*np.sin(2*y.t))/6
plt.title('Eqn4')
plt.scatter(y.t,y.y[0],label='Using solve_ivp')
plt.plot(y.t,y_ext,label='Exact soln')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid()
plt.show()
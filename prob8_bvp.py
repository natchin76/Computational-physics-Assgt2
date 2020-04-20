#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:37:47 2020
BV problems using scipy function
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
from bvp_fun import sol_bvp
from scipy.integrate import solve_bvp
#1

def f(x,y):
    return(np.vstack((y[1],-np.exp(-2*y[0]))))
xa=1
xb=2
ya=0
yb=np.log(2)
x=np.linspace(xa,xb,50)
y=sol_bvp(f,xa,xb,ya,yb,x)
plt.title('eqn1')
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()

#2
def f(x,y):
    return(np.vstack((y[1],1/2-y[1]**2/2-y[0]*np.sin(x/2))))
n=10
xa=0
xb=np.pi/2
ya=1
yb=np.exp(1)
x=np.linspace(xa,xb,n)
y=np.zeros((2,n))+.1
def bc(y1,y2):
    return(y1[0]-ya,y2[0]-yb)
soln=solve_bvp(f,bc,x,y)
x1=np.linspace(xa,xb,50)      
y1=soln.sol(x1)[0]
plt.title('eqn2')
plt.plot(x1,y1)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()

#3
def f(x,y):
    return(np.vstack((y[1],-(1/np.cos(x))*(2*y[1]**3+y[0]**2*y[1]))))
xa=np.pi/4
xb=np.pi/3
ya=2**(-1/4)
yb=12**(1/4)/2
x=np.linspace(xa,xb,50)
y=sol_bvp(f,xa,xb,ya,yb,x)
plt.title('eqn3')
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()

#4
def f(x,y):
    return(np.vstack((y[1],1/2-y[1]**2/2-y[0]*np.sin(x/2))))
xa=0
xb=np.pi
ya=2
yb=2
x=np.linspace(xa,xb,50)
y=sol_bvp(f,xa,xb,ya,yb,x)
plt.title('eqn4')
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()

    

 
    


    



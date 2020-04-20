#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:58:35 2020
Adaptive step size control RK4
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
a=1
b=3
h=.1
y0=-2
err=.5*1e-4
def f(t,y):
    return((y**2 + y)/t)
t=[1]
y=[y0]
i=0
while t[i]<b:
    K1=h*f(t[i],y[i])
    K2=h*f(t[i]+h/2,y[i]+K1/2)
    K3=h*f(t[i]+h/2,y[i]+K2/2)
    K4=h*f(t[i]+h,y[i]+K3)
    yint=(y[i]+ K1/6 + K2/3 + K3/3 + K4/6)
    
    K1=h*f(t[i]+h,yint)
    K2=h*f(t[i]+3*h/2,yint+K1/2)
    K3=h*f(t[i]+3*h/2,yint+K2/2)
    K4=h*f(t[i]+2*h,yint+K3)
    y1=(yint+ K1/6 + K2/3 + K3/3 + K4/6)
    
    h2=2*h
    K1=h2*f(t[i],y[i])
    K2=h2*f(t[i]+h2/2,y[i]+K1/2)
    K3=h2*f(t[i]+h2/2,y[i]+K2/2)
    K4=h2*f(t[i]+h2,y[i]+K3)
    y2=(y[i]+ K1/6 + K2/3 + K3/3 + K4/6)
    
    h=h*(30*err/abs(y1-y2))**.2
    t.append(t[i]+h)
    if t[i+1]>3:
        t[i+1]=3
        h=t[i+1]-t[i]
    
    K1=h*f(t[i],y[i])
    K2=h*f(t[i]+h/2,y[i]+K1/2)
    K3=h*f(t[i]+h/2,y[i]+K2/2)
    K4=h*f(t[i]+h,y[i]+K3)
    y.append(y[i]+ K1/6 + K2/3 + K3/3 + K4/6)
    i+=1
t=np.array(t)
t1=np.linspace(a,b,50)
y_ext=2*t/(1-2*t)    
y_ext1=2*t1/(1-2*t1) 
er=abs(y-y_ext) 
plt.scatter(t,y,label='approx soln')
plt.plot(t1,y_ext1,label='exact soln')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('y(t) vs t')
plt.grid()
plt.legend()

plt.show()
plt.scatter(t,er)
plt.ylim(-2*max(er),2*max(er))
plt.title('error(t) vs t')
plt.xlabel('t')
plt.ylabel('Absolute Error')
plt.grid()
plt.show()

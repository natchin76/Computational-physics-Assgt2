#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:40:56 2020

@author: chintan
"""
import numpy as np
def RK4(x0,xf,y0,f,n):
    order=len(y0)
    x=np.linspace(x0,xf,n)
    h=(xf-x0)/(n-1)
    y=np.zeros([order,n])
    y[:,0]=y0
    for i in range(n-1):
        K1=h*f(x[i],y[:,i])
        K2=h*f(x[i]+h/2,y[:,i]+K1/2)
        K3=h*f(x[i]+h/2,y[:,i]+K2/2)
        K4=h*f(x[i]+h,y[:,i]+K3)
        y[:,i+1]=y[:,i]+ K1/6 + K2/3 + K3/3 + K4/6
    return(y)
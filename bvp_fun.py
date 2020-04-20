#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:09:57 2020
Function to solve bvp
@author: chintan
"""
""" f=RHS of ode
xa=initial x value
xf=final x value
ya=value at x=xa
yb=value at x=xb
x1=input vector for which soln will be given as output"""
import numpy as np
from scipy.integrate import solve_bvp
def sol_bvp(f,xa,xb,ya,yb,x1):  
    n=10
    x=np.linspace(xa,xb,n)
    y=np.zeros((2,n))
    def bc(y1,y2):
        return(y1[0]-ya,y2[0]-yb)
    soln=solve_bvp(f,bc,x,y)      
    y1=soln.sol(x1)[0]
    return(y1) 
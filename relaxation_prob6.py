    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:04:43 2020
Relaxation method
@author: chintan
"""
from gsiedel import g_siedel
import numpy as np
from matplotlib import pyplot as plt
g=10
n=30    
h=10/(n-1)
t=np.linspace(0,10,n)
A=np.zeros((n-2,n-2))
A[0,0:2]=[-2,1]
A[n-3,n-4:n-2]=[1,-2]
for i in range(1,n-3):
    A[i,i-1:i+2]=[1,-2,1]
b=[]
for i in range(n-2):
    b.append(-g*h**2)
x=np.zeros([n,5])
k=g_siedel(A,b)[1]
x[1:n-1,0]=g_siedel(A,b)[0][int(k/5)]
x[1:n-1,1]=g_siedel(A,b)[0][int(2*k/5)]
x[1:n-1,2]=g_siedel(A,b)[0][int(3*k/5)]
x[1:n-1,3]=g_siedel(A,b)[0][int(4*k/5)]
x[1:n-1,4]=g_siedel(A,b)[0][k]
plt.scatter(t,x[:,4],label='solution')
for i in range(4):
    plt.plot(t,x[:,i])
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.show()    
print('Solution:\nx=',x[:,4])    

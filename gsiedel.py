#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:33:56 2020
Gauss Siedel function file
@author: chintan
"""
import numpy as np
def g_siedel(A,b):
    x0=np.zeros(len(b))
    X=[x0]
    k=0
    while max(abs(np.dot(A,X[k])-b))>.01:
        k+=1
        x=np.zeros(len(b))
        for i in range(len(b)):
            x[i]=X[k-1][i]
        for j in range(len(b)):
            s=0
            for l in range(len(b)):
                if j!=l:
                    s+=A[j][l]*x[l]
                x[j]=(b[j]-s)/A[j][j]
        X.append(x)
    return(X,k)
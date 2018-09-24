#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:53:26 2018

@author: 
Chung Yang 31732286
Yi-Pei Chen 31739156
Hao Cheng Cheam 31749564
Wenting Wang 31930946

# Coding question 3.32

"""

import numpy as np
from q3_17_powersvd import powersvd # our own SVD implementation using power iteration

# Generate data      
def create_sheath(n=100):
    data = np.zeros((3, 100))
    for i in range(1, n+1):
        x = np.sin((np.pi / 100) * i)
        y = np.sqrt(1 - x**2)
        z = 0.003 * i
        data[:, i-1] = np.vstack([x,y,z]).reshape(3,)
        
    distance = np.zeros((3, 10))
    for i in range(1, 6): 
        distance[:,i-1] = data[:, i-1] - data[:, 5];
        distance[:,i+5-1] = data[:, i+5] - data[:, 5]
    return data, distance

data, distance = create_sheath(n=100)

# perform SVD on distance matrix
# should get approx rank 2 
u,s,vt = powersvd(distance, 3, epsilon = 1e-5)

# The 3 singular values are [3.30032787e-01 2.17985474e-02 3.86625081e-05]

# verification of SVD
# u_actual, s_actual, vt_actual = np.linalg.svd(distance)
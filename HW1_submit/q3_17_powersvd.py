#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:15:05 2018

@author: 
Chung Yang 31732286
Yi-Pei Chen 31739156
Hao Cheng Cheam 31749564
Wenting Wang 31930946

# Coding question 3.17

"""
import numpy as np
from numpy.linalg import norm
import itertools
from scipy.linalg import orth

# Part 1 & 2
# power method on specific dimensionS
def powersvd(A, dimension, epsilon=1e-6):
    """
    :param A: input matrix
    :param dimension: number of singular vectors of a matrix A to find
    :param epsilon: the threshold to determine whether the approximation is good enough
    :return currentU: the first left singular vector
            sigma: The principle singular value
            currentV: transpose of the first right singular vector
    """
    # prepare
    n, m = A.shape
    if m < dimension:
        raise ValueError("Column number of matrix must be no less than dimensions.")

        

    # initialize a unit vector
    InitV = np.random.random((m, dimension))
    currentV = InitV/norm(InitV)
    LastV = 1

    # build a symmetric matrix
    B = np.dot(A.T, A)
    
    # power iteration
    iter_num = 0
    while norm(LastV - currentV) > epsilon:
        iter_num += 1
        LastV = currentV
        currentV_unorth = np.dot(B, currentV) # unorthonormal vectors        
        currentV = orth(currentV_unorth)
    
    product = A.dot(currentV)
    sigma = norm(product, axis=0)
    currentU = product/sigma
    print('Find the first', str(dimension), 'singular vectors after', str(iter_num), 'iterations')
    print('The first', str(dimension), 'left singular vectors:')
    print(currentU)
    print('The first', str(dimension), 'singular values:')
    print(sigma)
    print('The transpose of first', str(dimension), 'right singular vectors:')
    print(currentV.T)
    
    return currentU, sigma, currentV.T

if __name__ == "__main__":
    np.random.seed(0)
    # generate A
    A = np.zeros((10,10))
    for i, j in itertools.product(range(10), range(10)):
        if i + j < 10:
            A[i,j] = i+j+1
    
    # Power SVD on A to find the v1
    u1, s1, v1t = powersvd(A, 1)
    print(' ')
    
    # Power SVD on A to find the v1,v2,v3,v4
    U,S,VT = powersvd(A, 4)


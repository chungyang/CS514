import numpy as np
A = np.array([
        [0,1,1,0,0,0,0,0,0], # A to B,C
        [1,0,1,0,0,0,0,1,0], # B to A,C,H
        [1,1,0,1,0,0,0,0,0], # C to A,B,D
        [0,0,1,0,1,1,0,0,0], # D to C,E,F
        [0,0,0,1,0,1,1,0,0], # E to D,F,G
        [0,0,0,1,1,0,0,0,0], # F to D,E
        [0,0,0,0,1,0,0,1,1], # G to E,H,I
        [0,1,0,0,0,0,1,0,1], # H to B,G,I
        [0,0,0,0,0,0,1,1,0]  # I to G,H
    ])
D = np.diag([2,3,3,3,3,2,3,3,2])
L = D - A
result = np.linalg.eig(L)
idx = np.argsort(result[0])
# second-smallest eigenvalue and its eigenvector
print('second-smallest eigenvalue: ', np.sort(result[0])[1]) # ASC
print('corresponding vector: ', result[1][idx[1]])

# third-smallest eigenvalue and its eigenvector
print('third-smallest eigenvalue: ', np.sort(result[0])[2]) # ASC
print('corresponding vector: ', result[1][idx[2]])

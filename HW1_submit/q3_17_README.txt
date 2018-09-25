Homework 1 - q3_17_README.txt
Program: Solution to 3.17

=== Files Includes For This Program ===

    q3_17_README.txt
    q3_17_powersvd.py

=== How Do The Programs Work ===

    This program contains a function (powersvd) that calculates the Singular Vector Decomposition on an arbitrary matrix. Given the matrix, a specific number of dimension and an epsilon (1e-6 as default), it returns the first specific number of left singular vectors U, corresponding singular values S and the transpose of right singular vectors V.T 

    For the question 3.17 part I, given the matrix A and dimension as one, the function returns the first singular value, left and right ﬁrst singular vector of matrix A.

    For the question 3.17 part II, given the matrix A and dimension as four, the function returns the first four singular values, left and right ﬁrst four singular vectors of matrix A.

    Explain the powersvd() function:

        Step 1: Check the input values, the column number of matrix A must be no less than the dimension number, since the reconstructed space cannot have higher dimension than the original one.

        Step 2: Initialize a orthogonal vectors (n rows, dimension columns) as the first specific number (dimension) of left sigular vectors V. Obtain a symmetric matrix B as inner product of A.T and A. Since A is assumed as inner product of U,S and V.T, B is inner product of V, sqaure of S and V.T. The V of A equals to the V of B. The Initialized V for A is also for B.

        Step 3: Calculate the inner product of B and V, orthonormalize the result to get the new V, replace the V with new V. Iteratively calculate the inner product of B and V and orthonormalize the result, untill new V does not change so much (the norm of V and new V is less than the set epsilon).

        Step 4: Given the final V from the last step, calculate the inner product of A and V, normalize the result along each column to get the S. Then obtain the U by calculating the inner product over S.

    Explain the __main__ part:

        Generate the matrix A. Use powersvd(A, 1) to get the first left singular vector, the first singular value and the transpose of first right singular vector. Use powersvd(A, 4) to get the first left four singular vector, the first four singular value and the transpose of first four right singular vector. 

=== Pseudocode ===
    
    Data: matrix, dimension, epsilon (1e-6 as default)
    Result: U, S, V.T

    check input;
    initialization V;
    B := inner product of A.T and A;
    WHILE change of V larger than eplison DO
        V := inner product of B and V;
        V := orthonormalize V;
    obtain S from A and V;
    obtain U from A and V and S;
    END

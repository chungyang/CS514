Homework 1 - q3_17_README.txt

Program: Solution to 3.17

Mon 24 Sep. 2018

=== Team members ===

    Chung Yang 31732286
    Yi-Pei Chen 31739156
    Hao Cheng Cheam 31749564
    Wenting Wang 31930946


=== How To Run This Program ===

    In terminal or command shell. Go to the submitted homework folder 'HW1_submit'.
    Run 'python3 q3_17_powersvd.py' to get the result of question 3.17.


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


=== Program Results ===

    Part I:

        Find the first 1 singular vectors after 12 iterations

        The first 1 left singular vectors:
        [[0.31975064]
         [0.36962506]
         [0.39811311]
         [0.40391891]
         [0.38728042]
         [0.34995868]
         [0.29512622]
         [0.22716235]
         [0.15136861]
         [0.07362361]]

        The first 1 singular values:
        [43.43043275]

        The transpose of first 1 right singular vectors:
        [[0.31975052 0.36962496 0.39811304 0.40391889 0.38728045 0.34995875
          0.29512632 0.22716245 0.15136869 0.07362366]]

    Part II:

        Find the first 4 singular vectors after 29 iterations

        The first 4 left singular vectors:
        [[-0.3197506  -0.45784552 -0.42415456 -0.39363343]
         [-0.36962502 -0.3936509  -0.24288284 -0.02849202]
         [-0.39811309 -0.25497036  0.07043602  0.36152052]
         [-0.4039189  -0.06980555  0.33936334  0.38322642]
         [-0.38728043  0.12450888  0.41233765  0.01440651]
         [-0.3499587   0.2887672   0.24775341 -0.37382104]
         [-0.29512626  0.38972804 -0.06268814 -0.39083236]
         [-0.22716239  0.40675711 -0.34546459 -0.0199787 ]
         [-0.15136864  0.33594883 -0.44265159  0.36463826]
         [-0.07362363  0.19090282 -0.30058613  0.37499533]]

        The first 4 singular values:
        [43.43043275 23.98317214 14.11091604 10.49704858]

        The transpose of first 4 right singular vectors:
        [[-0.3197506  -0.36962502 -0.39811309 -0.4039189  -0.38728043 -0.3499587
          -0.29512626 -0.22716239 -0.15136864 -0.07362363]
         [ 0.45784552  0.3936509   0.25497036  0.06980555 -0.12450888 -0.2887672
          -0.38972804 -0.40675711 -0.33594883 -0.19090282]
         [-0.42415456 -0.24288284  0.07043602  0.33936334  0.41233765  0.24775341
          -0.06268814 -0.34546459 -0.44265159 -0.30058613]
         [ 0.39363441  0.02849158 -0.36152169 -0.38322646 -0.01440535  0.3738216
           0.39083145  0.01997777 -0.36463773 -0.37499415]]


  
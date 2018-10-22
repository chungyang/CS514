This is Readme for Exercise 7.4

To run the program and see the results, simply open "7_4.ipynb" using jupyter notebook based on python 3.6.

Kmeans Algorithm:
    1. Initialize centroids:
        In this exercise, we did not use kmeans++, just simply used random initialization.
    2. Compute distance and assign each data point to nearest cluster.
    3. Update centroids of each cluster by the mean point of intra-class points.
    4. Repeat 2. and 3. until converge:
        We determined convergence by if the distances between new and old centroids small enough.
    5. Compute the sum of square errors(SSE) and return labels and SSE.

pseudocode:
    Input:
      X -- Data matrix
    Output:
      SSE -- sum of square errors
      labels -- label vector for X

    Code:
    Init_centroids <-- K random choices from X
    While not converge:
        for each centroids C_i:
            distance_vec <-- l2 distances between each data point to C_i

        distance_matrix <-- all distance_vec stack together

        for each datapoint X_i:
            labels[i] <-- index of col giving the min distance in i-th row in distance_matrix

        new_centroids <-- mean of datapoints in each cluster
    
    SSE <-- sum of distances for each point to its cluster's centroid
    Return SSE, labels

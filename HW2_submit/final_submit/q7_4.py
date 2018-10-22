import numpy as np
from scipy.linalg import block_diag
import matplotlib.pyplot as plt


def KMeans_fit(X, epsilon=0, n_clusters=1, random_state=None):
    """
        A simple impelementation of KMeans methods,
        using random initialization and do not re-
        initialize centroids.
        Input:
          X -- input array
          epsilon -- a very small number used to identify convergence
          n_clusters -- number of clusters, integer
          random_state -- random seed, integer
        Output:
          inertia -- sum of square errors
          labels -- a array contains labels for data
    """
    # delta is the difference between previous centroids and new centroids
    delta = 1.0
    # distance matrix, with shape N x k, N is the num of samples, k is n_clusters
    distance = np.zeros((X.shape[0],n_clusters))
    # labels, an 1-D array with shape (N,), storing the cluster number data fell into.
    labels = np.zeros(X.shape[0])
    # initialize centroids
    if random_state is not None:
        np.random.seed(random_state)
    indices = np.random.randint(150, size=n_clusters)
    centroids = X[indices]
    
    while(delta > epsilon):
        # compute distance matrix
        for i, centroid in enumerate(centroids):
            distance[:,i] = np.linalg.norm(X - centroid, axis=1)
        # assign each point to nearest cluster
        labels = np.argsort(distance,axis=1)[:,0]
        # update centroids by the means of each cluster
        new_centroids = np.zeros_like(centroids)
        for i in range(n_clusters):
            mean = np.mean(X[labels == i], axis=0)
            new_centroids[i] = mean
        # delta equals the sum of l2 distances between new and old centroids
        delta = np.sum(np.linalg.norm(new_centroids - centroids,axis=1))
        # update
        centroids = new_centroids
    
    # compute sum of square errors
    inertia = np.sum(distance.min(axis=1))
    
    return inertia, labels


# construct A
a = np.ones((50,50))
A = block_diag(a,a,a)
A = A * 0.4 + 0.3
print(' Matrix A ')
print(A)

# generate B, for convenience of reproduction, fix random seed
np.random.seed(86)
B = np.random.random(A.shape)
print(' Matrix B ')
print(B)
# replace B's values 
ones = B >= A
B_replaced = ones * 1
print(' Matrix B_replaced ')
print(B_replaced)


np.set_printoptions(threshold=150)
# random permutation
np.random.seed(86)
permutation = np.random.permutation(A.shape[0])
# shuffle rows
A_shuffled = A[permutation]
# shuffle cols
A_shuffled = A_shuffled[:,permutation]
inertia, labels = KMeans_fit(A_shuffled, n_clusters=3, random_state=86)
# print clustering result to check if the clusters match natural clusters in A
# each cluster should correspond to a block in A,
# e.g. block1: row 0 to row 49, block2: row 50 to row 99
for k in range(3):
    # get indices of datapoints fell into cluster k in shuffled A 
    indices = labels == k
    # print original indices of those datapoints in A
    print('Cluster %d indices' %k)
    print(permutation[indices])


# plot SSE vs k
errors = []
ks = np.arange(1,11)
for k in ks:
    sse, _ = KMeans_fit(A_shuffled, n_clusters=k, random_state=86)
    errors.append(sse)

plt.plot(ks, errors)
plt.xlabel('k')
plt.xticks(ks)
plt.ylabel('SSE')
plt.title('KMeans k-SSE plot')
plt.show()

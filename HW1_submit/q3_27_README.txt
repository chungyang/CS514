The program basically works as following.

Import the image

For each percentage:

    1. Calculate SVD of the image

    2. Calculate min(n,m) * percentage. Here denoted as N

    3. Reconstruct the image with the first N singular values and N singular vectors

    4. Calculate the norm of reconstructed image and divide it by norm of original

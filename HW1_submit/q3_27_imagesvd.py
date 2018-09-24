#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:32:20 2018

@author: 
Chung Yang 31732286
Yi-Pei Chen 31739156
Hao Cheng Cheam 31749564
Wenting Wang 31930946

# Coding question 3.27

"""

from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from numpy.linalg import svd
from q3_17_powersvd import powersvd # own svd function

# Show input image
def showImg(image):
    print('Input image:')
    plt.imshow(image, cmap='gray')
    plt.title("The input image")
    plt.draw()
    print(' ')

# Perform SVD, then reconstruct image in several levels and show it
def reconImg(image, pct, figure_n):
    plt.figure(figure_n)
    # SVD
    n, m = image.shape
    u, s, vh = svd(image, full_matrices=True)
#    u, s, vh = powersvd(image, m) # very slow
    
    # Reconstruct
    idx = int(min(n,m) * pct)
    print(idx)
    img_recon = u[:, :idx].dot(np.diag(s[:idx])).dot(vh[:idx,:])
    print('Use Top {:.0%} of the singular values.'.format(pct), '\n')

    # Percentage of Frobenius norm
    fb_norm_pct = norm(s[:idx])/norm(s)
    print('{:.5%} percent of the Forbenius norm is captured.'.format(fb_norm_pct))
    
    # Show image
    plt.imshow(img_recon, cmap='gray')
    plt.title('Top {:.0%} of the singular values.'.format(pct) + '\n' + \
              '{:.5%} percent of the Forbenius norm is captured.'.format(fb_norm_pct))
    plt.draw()


if __name__ == "__main__":
    # Read Image
    # (put the image file to the folder os.getcwd())
    img = misc.imread('image.jpg', 1)
    showImg(img) # show the input image
    
    percentages = [0.05, 0.10, 0.25, 0.50]
    figure_n = 1
    for pct in percentages:
        reconImg(img, pct, figure_n) # show the reconstructed image
        figure_n += 1
    plt.show()

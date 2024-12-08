#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    # Calculate the dot product of corresponding rows in X and Y
    dot_product = np.einsum('ij,ij->i', X, Y)
    dot_product = np.sum(X*Y, axis = 1)
    print(dot_product)
    # Calculate the norms (magnitudes) of the vectors in X and Y
    norm_X = np.sqrt(np.sum(X ** 2, axis = 1))
    norm_Y = np.sqrt(np.sum(Y ** 2, axis = 1))
    print(norm_X)
    # Compute the cosine of the angle using dot product and norms
    cos_angles = dot_product / (norm_X * norm_Y)
    
    # Clip the values to be in the range [-1, 1] to avoid issues with numerical precision
    cos_angles = np.clip(cos_angles, -1.0, 1.0)
    
    # Compute the angles in radians and convert to degrees
    angles = np.degrees(np.arccos(cos_angles))
    
    return angles

def main():
    np.random.seed(0)
    x = np.random.randint(0, 10, (2, 2))
    y = np.random.randint(0, 10, (2, 2))
    print(vector_angles(x, y))
    np.array([])

if __name__ == "__main__":
    main()

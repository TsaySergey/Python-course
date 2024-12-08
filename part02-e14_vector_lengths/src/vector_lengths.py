#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    norm = np.sqrt(np.sum(a**2, axis=1))
    return norm

def main():
    np.random.seed(0)
    arr = np.random.randint(0,10, (4, 4))
    print(vector_lengths(arr))

    pass

if __name__ == "__main__":
    main()

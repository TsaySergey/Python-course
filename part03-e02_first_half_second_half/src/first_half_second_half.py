#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m = a.shape[1] // 2
    first_half = np.sum(a[:, :m], axis = 1)
    second_half = np.sum(a[:, m:], axis = 1)
    print(first_half)
    print(second_half)
    return a[first_half > second_half]

def main(): 
    a = np.array([[1, 3, 4, 2],
                  [2, 2, 1, 2]])
    result = first_half_second_half(a)
    print(result)
    pass


if __name__ == "__main__":
    main()

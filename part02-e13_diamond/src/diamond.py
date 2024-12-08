#!/usr/bin/env python3

import numpy as np

def diamond(n):
    top = np.eye(n, dtype = int)
    bottom = top[:-1][::-1]
    half = np.concatenate((top, bottom), axis = 0)
    full_diamond = np.concatenate((half[:, ::-1], half[:, 1:]), axis = 1)
    print(full_diamond)
    return full_diamond

def main():
    print(diamond(3))

    pass

if __name__ == "__main__":
    main()
